#!/usr/bin/env python3
"""Singles Life post renderer.

Usage: python3 render.py spec.json OUTDIR
Renders each slide in spec["slides"] to OUTDIR/<slug>-NN.jpg (JPEG, which Instagram requires) at 1080x1350 (4:5, works for
Instagram feed/carousel and Facebook). Fonts load from ./fonts next to this script.

Slide types (all fields are plain text; keep them short):
  cover     {title, sub?, kicker?}                 first slide of a carousel
  point     {n?, title, body}                      one idea per slide
  checklist {title, items:[...], note?}           3-6 short items
  statement {text, attribution?}                   single-image post, one strong line
  cta       {title?, body?}                        closing slide (save / share / app)
Spec may set "footer" (default "singles-life.app") and "label" (header text on single images).
Each slide may set theme: pine | chalk | highlight (default alternates sensibly).
"""
import json, sys, pathlib, html, base64
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
def font_b64(name):
    return base64.b64encode((HERE / "fonts" / name).read_bytes()).decode()

THEMES = {
    "pine":      {"bg": "#1F3B37", "fg": "#F4F3EE", "muted": "#A9BDB6", "mark": "#F2D64B", "rule": "#2F524C", "hl": "rgba(242,214,75,.42)"},
    "chalk":     {"bg": "#F4F3EE", "fg": "#14201E", "muted": "#5B6B66", "mark": "#1F3B37", "rule": "#DAD9D1", "hl": "#F2D64B"},
    "highlight": {"bg": "#F2D64B", "fg": "#14201E", "muted": "#5A4F17", "mark": "#1F3B37", "rule": "#E0C43A", "hl": "rgba(255,255,255,.7)"},
}

CSS = """
@font-face{font-family:Brico;src:url(data:font/ttf;base64,%(brico)s) format('truetype');font-weight:200 800;font-stretch:75%% 100%%}
@font-face{font-family:Fig;src:url(data:font/ttf;base64,%(fig)s) format('truetype');font-weight:300 900}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{background:var(--bg);color:var(--fg);font-family:Fig,sans-serif;position:relative;overflow:hidden}
.frame{position:absolute;inset:0;padding:84px 88px 0;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;font:600 26px/1 Fig;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.brand{display:flex;align-items:center;gap:14px;color:var(--fg)}
.box{width:30px;height:30px;border:4px solid var(--mark);border-radius:6px;position:relative}
.box:after{content:"";position:absolute;left:6px;top:0px;width:9px;height:16px;border:solid var(--mark);border-width:0 4px 4px 0;transform:rotate(45deg)}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px;padding-bottom:40px}
.foot{height:120px;border-top:3px solid var(--rule);display:flex;align-items:center;justify-content:space-between;font:600 28px/1 Fig;color:var(--muted)}
.foot b{color:var(--fg);font-weight:700}
h1{font-family:Brico;font-weight:800;font-stretch:85%%;font-size:124px;line-height:.98;letter-spacing:-.02em;text-wrap:balance}
h2{font-family:Brico;font-weight:800;font-stretch:85%%;font-size:92px;line-height:1.02;letter-spacing:-.015em;text-wrap:balance}
.kicker{display:inline-block;align-self:flex-start;background:var(--mark);color:var(--bg);font:800 28px/1 Fig;letter-spacing:.12em;text-transform:uppercase;padding:14px 20px;border-radius:6px}
.sub{font:500 44px/1.32 Fig;color:var(--muted);max-width:860px;text-wrap:pretty}
.p{font:500 46px/1.36 Fig;max-width:880px;text-wrap:pretty}
.num{font-family:Brico;font-weight:800;font-size:220px;line-height:.8;color:var(--mark);font-stretch:75%%}
ul{list-style:none;display:flex;flex-direction:column;gap:30px}
li{display:grid;grid-template-columns:62px 1fr;gap:26px;align-items:start;font:600 46px/1.25 Fig}
li .box{width:52px;height:52px;border-width:5px;border-radius:9px;margin-top:2px}
li .box:after{left:13px;top:3px;width:14px;height:26px;border-width:0 6px 6px 0}
.note{font:500 34px/1.35 Fig;color:var(--muted)}
.stmt{font-family:Brico;font-weight:700;font-stretch:90%%;font-size:104px;line-height:1.05;letter-spacing:-.015em;text-wrap:balance}
mark{color:inherit;background:linear-gradient(transparent 58%%, var(--hl) 58%%, var(--hl) 92%%, transparent 92%%)}
.attr{font:600 32px/1 Fig;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.swipe{font:700 32px/1 Fig;color:var(--fg)}
"""

def esc(s):
    s = html.escape(str(s or ""))
    # *word* -> highlighted word
    out, on = "", False
    for part in s.split("*"):
        out += (("<mark>" + part + "</mark>") if on else part)
        on = not on
    return out

def slide_html(sl, i, total, slug_label, footer="singles-life.app"):
    t = THEMES.get(sl.get("theme"), THEMES["pine"])
    var = ";".join(f"--{k}:{v}" for k, v in t.items())
    kind = sl.get("type", "point")
    count = f"{i+1:02d} / {total:02d}" if total > 1 else slug_label
    if kind == "cover":
        inner = (f'<span class="kicker">{esc(sl.get("kicker","Solo living"))}</span>'
                 f'<h1>{esc(sl["title"])}</h1>' + (f'<p class="sub">{esc(sl.get("sub"))}</p>' if sl.get("sub") else ""))
    elif kind == "checklist":
        items = "".join(f'<li><span class="box"></span><span>{esc(x)}</span></li>' for x in sl["items"])
        inner = f'<h2>{esc(sl["title"])}</h2><ul>{items}</ul>' + (f'<p class="note">{esc(sl.get("note"))}</p>' if sl.get("note") else "")
    elif kind == "statement":
        inner = f'<p class="stmt">{esc(sl["text"])}</p>' + (f'<p class="attr">{esc(sl.get("attribution"))}</p>' if sl.get("attribution") else "")
    elif kind == "cta":
        inner = (f'<h2>{esc(sl.get("title","Save this for later."))}</h2>'
                 f'<p class="p">{esc(sl.get("body","Share it with someone running a household on their own. More practical tools at singles-life.app"))}</p>')
    else:
        n = sl.get("n")
        inner = (f'<div class="num">{esc(n)}</div>' if n else "") + f'<h2>{esc(sl["title"])}</h2><p class="p">{esc(sl["body"])}</p>'
    right = '<span class="swipe">Swipe →</span>' if (total > 1 and i < total - 1) else "<span>Single life, made simple.</span>"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS % FONTS}</style></head>
<body style="{var}"><div class="frame">
<div class="top"><span class="brand"><span class="box"></span>Singles Life</span><span>{count}</span></div>
<div class="body">{inner}</div>
<div class="foot"><b>{esc(footer)}</b>{right}</div>
</div></body></html>"""

FONTS = {}
def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
    FONTS.update(brico=font_b64("BricolageGrotesque.ttf"), fig=font_b64("Figtree.ttf"))
    slides = spec["slides"]; total = len(slides)
    files = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, sl in enumerate(slides):
            pg.set_content(slide_html(sl, i, total, spec.get("label", "Tip of the day"), spec.get("footer", "singles-life.app")), wait_until="load")
            pg.evaluate("document.fonts.ready")
            f = out / f"{spec['slug']}-{i+1:02d}.jpg"
            pg.screenshot(path=str(f), type="jpeg", quality=92)
            files.append(str(f))
        b.close()
    print("\n".join(files))

if __name__ == "__main__":
    main()
