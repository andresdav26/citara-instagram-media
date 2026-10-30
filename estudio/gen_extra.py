"""Semana 1 · post tipográfico, plantilla con persona y portadas de destacadas."""
from pathlib import Path
import sys

ROOT = Path(__file__).parent / "src"
A = "../../assets"
HEAD = """<!doctype html><html><head><meta charset="utf-8"><meta name="size" content="{w}x{h}">
<link rel="stylesheet" href="../base.css"><style>:root{{--w:{w}px;--h:{h}px}} {css}</style></head>
<body><div class="canvas {cls}">{body}</div></body></html>"""

def page(folder, name, body, w=1080, h=1350, cls="", css=""):
    d = ROOT / folder; d.mkdir(parents=True, exist_ok=True)
    (d / f"{name}.html").write_text(HEAD.format(w=w, h=h, body=body, cls=cls, css=css), encoding="utf-8")

# ---------- Post tipográfico: bandeja de WhatsApp ----------
rows = [
    ("LA", "Laura", "¿Tienen cita hoy en la tarde?", "3:12 p. m."),
    ("AN", "Andrea", "¿Puedo cambiar mi hora?", "3:14 p. m."),
    ("PA", "Paula", "¿Cuánto dura la sesión?", "3:17 p. m."),
    ("SO", "Sofía", "¿Atienden el sábado?", "3:19 p. m."),
    ("CA", "Camilo", "Hola, ¿hay espacio mañana?", "3:22 p. m."),
]
row_html = "".join(f"""
<div style="display:flex;align-items:center;gap:22px;padding:18px 30px;border-top:1px solid rgba(46,64,82,.08)">
  <div class="avatar" style="width:62px;height:62px;flex:none">{ini}</div>
  <div style="flex:1;min-width:0">
    <div style="display:flex;justify-content:space-between;align-items:baseline">
      <span style="font-weight:600;font-size:29px">{name}</span>
      <span style="font-size:21px;color:var(--petroleo);font-weight:600">{hora}</span>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-top:4px">
      <span style="font-size:27px;opacity:.72;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{msg}</span>
      <span style="width:16px;height:16px;border-radius:50%;background:var(--petroleo);flex:none;margin-left:16px"></span>
    </div>
  </div>
</div>""" for ini, name, msg, hora in rows)

page("w1-post", "bandeja", f"""
<div style="position:absolute;left:90px;right:90px;top:92px;display:flex;justify-content:space-between;align-items:center">
  <div class="eyebrow">Entre una cita y otra</div>
  <img src="{A}/citara-simbolo-claro.svg" style="width:78px">
</div>
<div class="h1" style="position:absolute;left:90px;right:90px;top:180px;font-size:66px">Mientras atiendes,<br><b>WhatsApp no para.</b></div>
<div class="phone" style="position:absolute;left:90px;right:90px;top:370px">
  <div style="display:flex;justify-content:space-between;align-items:center;padding:24px 30px;background:#F6FAF8">
    <span style="font-weight:600;font-size:28px">WhatsApp del negocio</span>
    <span style="background:var(--naranja);color:var(--pizarra);font-weight:700;font-size:22px;padding:8px 18px;border-radius:30px">12 sin leer</span>
  </div>
  {row_html}
</div>
<div style="position:absolute;left:90px;right:90px;bottom:96px;display:flex;justify-content:space-between;align-items:flex-end">
  <div style="font-size:30px;line-height:1.35;max-width:600px"><b style="font-weight:600">¿Te suena?</b> Citara atiende las citas por WhatsApp, en el mismo chat.</div>
  <div style="text-align:right">
    <img src="{A}/citara-claro.svg" style="width:190px;display:block;margin-left:auto">
    <div class="url" style="margin-top:10px;font-size:24px;color:var(--petroleo)">citara.com.co</div>
  </div>
</div>
""")

# ---------- Plantilla con persona (serie foto) ----------
photo = sys.argv[1] if len(sys.argv) > 1 else None
photo_css = (f"background:url('{photo}') center/cover no-repeat" if photo else
             "background:repeating-linear-gradient(45deg,#C0D8D1 0 20px,#E2EDE9 20px 40px)")
page("w1-foto", "silla-vacia", f"""
<div style="position:absolute;left:0;right:0;top:0;height:640px;background:var(--bv)">
  <img src="{A}/citara-claro.svg" style="position:absolute;left:90px;top:84px;width:220px">
  <div class="eyebrow" style="position:absolute;left:90px;top:218px">Cada cita cuenta</div>
  <div class="h1" style="position:absolute;left:90px;right:90px;top:268px;font-size:76px">Una silla vacía.<br><b>Una hora perdida.</b></div>
  <div class="body" style="position:absolute;left:90px;right:90px;top:478px;font-size:32px;opacity:.85">Citara recuerda cada cita un día antes y, si alguien cancela, el espacio vuelve a tu agenda.</div>
</div>
<div style="position:absolute;left:0;right:0;top:640px;bottom:0;{photo_css}">
  {'<div style="position:absolute;left:0;right:0;bottom:0;height:260px;background:linear-gradient(to top,rgba(46,64,82,.55),rgba(46,64,82,0))"></div>' if photo else '<div style="position:absolute;inset:0;display:grid;place-items:center;font-family:Unbounded;font-size:44px;color:var(--pizarra);opacity:.6">FOTO 16:9</div>'}
</div>
<div style="position:absolute;left:90px;right:90px;bottom:80px;display:flex;justify-content:space-between;align-items:center">
  <span class="pill" style="background:var(--petroleo);color:var(--bv);border-radius:40px;padding:16px 32px;font-size:28px">Conoce Citara</span>
  <span class="url" style="color:#fff;font-size:28px;text-shadow:0 2px 12px rgba(0,0,0,.45)">citara.com.co</span>
</div>
""")

# ---------- Portadas de destacadas (1080x1920) ----------
ICONS = {
    "como-funciona": '<svg width="300" height="300" viewBox="0 0 24 24" fill="none" stroke="#2E4052" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5h16v10H9l-5 4z"/><path d="M8.5 10.5l2.3 2.3 4.7-4.6"/></svg>',
    "para-quien": '<svg width="300" height="300" viewBox="0 0 24 24" fill="none" stroke="#2E4052" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 9.5h17M8 3v4M16 3v4"/><path d="M8 13.5h3M13 13.5h3M8 16.5h3"/></svg>',
    "prueba-gratis": '<div style="text-align:center;color:#2E4052;line-height:.9"><div style="font-family:Unbounded;font-weight:700;font-size:250px;letter-spacing:-.04em">7</div><div style="font-family:Jost;font-weight:700;font-size:58px;letter-spacing:.14em">DÍAS</div></div>',
}
for name, icon in ICONS.items():
    page("destacadas", name, f"""
<div style="position:absolute;left:50%;top:50%;width:620px;height:620px;margin:-310px 0 0 -310px;border-radius:50%;background:var(--naranja);display:grid;place-items:center">{icon}</div>
""", w=1080, h=1920, cls="dark")
print("ok")
