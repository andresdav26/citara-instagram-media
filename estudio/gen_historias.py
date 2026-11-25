"""Historias de las destacadas (1080x1920). Zona segura: 250 px arriba y 350 px abajo.

Cómo funciona (3) · Para quién (2) · Prueba gratis (2). El texto sale del sitio:
components/Businesses.tsx (con qué se configura), lib/examples.ts (los negocios de ejemplo),
app/page.tsx (la FAQ) y app/prueba/page.tsx (los pasos de la prueba).
"""
from pathlib import Path

OUT = Path(__file__).parent / "src" / "historias"
OUT.mkdir(parents=True, exist_ok=True)
A = "../../assets"
HEAD = """<!doctype html><html><head><meta charset="utf-8"><meta name="size" content="1080x1920">
<link rel="stylesheet" href="../base.css"><style>:root{{--w:1080px;--h:1920px}}
.msg{{font-size:40px;max-width:86%}}
.top{{position:absolute;left:90px;right:90px;top:250px;display:flex;justify-content:space-between;align-items:center}}
.bar{{display:flex;gap:10px}} .bar i{{display:block;width:44px;height:8px;border-radius:4px;background:currentColor;opacity:.25}} .bar i.on{{opacity:1}}
.row{{display:flex;gap:28px;align-items:flex-start;padding:30px 0;border-top:1px solid rgba(46,64,82,.14)}}
.n{{flex:none;width:76px;height:76px;border-radius:50%;background:var(--pizarra);color:var(--bv);display:grid;place-items:center;font-family:Unbounded;font-weight:700;font-size:34px}}
.chip{{display:inline-block;background:#fff;border:1px solid rgba(46,64,82,.12);border-radius:40px;padding:18px 30px;font-size:38px;font-weight:500;margin:0 12px 16px 0}}
</style></head><body><div class="canvas {cls}" style="{style}">{body}</div></body></html>"""


def page(name, body, cls="", style=""):
    (OUT / f"{name}.html").write_text(HEAD.format(body=body, cls=cls, style=style), encoding="utf-8")


def top(label, i, n, symbol="citara-simbolo-oscuro.svg", color="var(--salvia)"):
    bars = "".join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(n))
    return f"""<div class="top"><div><div class="eyebrow" style="color:{color}">{label}</div><div class="bar" style="color:{color};margin-top:18px">{bars}</div></div>
      {f'<img src="{A}/{symbol}" style="width:90px">' if symbol else '<span style="font-weight:600;font-size:28px;color:var(--pizarra)">citara.com.co</span>'}</div>"""


PHONE = """<div class="phone"><div class="chat-head"><div class="avatar" style="width:66px;height:66px;font-size:24px">TN</div><div><div class="chat-title" style="font-size:31px">Tu negocio · WhatsApp</div><div class="chat-sub" style="font-size:22px">Atendido por Citara</div></div></div>
  <div class="chat-body" style="gap:22px;padding:34px 28px">{msgs}</div></div>"""
NOTE = '<div class="note" style="position:absolute;left:90px;bottom:300px;font-size:24px;{c}">Vista ilustrativa · datos de ejemplo</div>'

# ---------- Cómo funciona ----------
page("cf-1", top("Cómo funciona", 0, 3) + f"""
<div class="h1" style="position:absolute;left:90px;right:90px;top:430px;font-size:88px">Tu cliente escribe <b>como siempre.</b></div>
<div style="position:absolute;left:80px;right:80px;top:760px">{PHONE.format(msgs='<div class="msg out">Hola, ¿tienen cita el viernes?</div>')}</div>
<div class="body" style="position:absolute;left:90px;right:90px;top:1180px;font-size:40px;color:var(--salvia)">A tu WhatsApp de siempre, a cualquier hora.</div>
{NOTE.format(c='color:var(--salvia)')}""", cls="dark")

page("cf-2", top("Cómo funciona", 1, 3) + f"""
<div class="h1" style="position:absolute;left:90px;right:90px;top:430px;font-size:88px">Citara le ofrece <b>lo que está libre.</b></div>
<div style="position:absolute;left:80px;right:80px;top:760px">{PHONE.format(msgs='<div class="msg out">Hola, ¿tienen cita el viernes?</div><div class="msg in">¡Hola! El viernes tengo <b>10:00&nbsp;a.&nbsp;m.</b> o <b>3:00&nbsp;p.&nbsp;m.</b> ¿Cuál te sirve?</div><div class="msg out">La de las 10 👌</div>')}</div>
<div class="body" style="position:absolute;left:90px;right:90px;top:1400px;font-size:38px;color:var(--salvia)">Solo los espacios que de verdad están libres en tu agenda.</div>
{NOTE.format(c='color:var(--salvia)')}""", cls="dark")

page("cf-3", top("Cómo funciona", 2, 3) + f"""
<div class="h1" style="position:absolute;left:90px;right:90px;top:430px;font-size:88px">Y la cita queda <b>en tu panel.</b></div>
<div class="phone" style="position:absolute;left:80px;right:80px;top:770px;color:var(--pizarra)">
  <div style="display:flex;justify-content:space-between;align-items:center;padding:28px 32px;border-bottom:1px solid rgba(46,64,82,.1)">
    <img src="{A}/citara-claro.svg" style="width:170px"><span style="font-size:26px;opacity:.7">Tu agenda</span></div>
  <div style="padding:26px 32px 10px;font-size:22px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;opacity:.55">Viernes</div>
  <div style="padding:0 32px;font-size:40px;font-weight:600">27 de noviembre</div>
  <div style="padding:26px 32px 34px;display:flex;flex-direction:column;gap:16px">
    <div style="display:flex;gap:22px;align-items:stretch"><span style="width:110px;font-size:26px;opacity:.6;padding-top:12px">9:00</span><div style="flex:1;border-top:1px solid rgba(46,64,82,.1)"></div></div>
    <div style="display:flex;gap:22px;align-items:stretch"><span style="width:110px;font-size:26px;opacity:.6;padding-top:12px">10:00</span>
      <div style="flex:1;background:#FDE7D0;border-left:8px solid var(--naranja);border-radius:12px;padding:18px 22px"><div style="font-size:24px;opacity:.75">10:00 – 11:00</div><div style="font-size:32px;font-weight:600">Nueva cita</div><div style="font-size:24px;opacity:.75">Agendada por Citara</div></div></div>
    <div style="display:flex;gap:22px;align-items:stretch"><span style="width:110px;font-size:26px;opacity:.6;padding-top:12px">11:00</span><div style="flex:1;border-top:1px solid rgba(46,64,82,.1)"></div></div>
  </div></div>
<div class="body" style="position:absolute;left:90px;right:90px;top:1390px;font-size:38px;color:var(--salvia)">Tu equipo ve todo y toma la conversación cuando hace falta.</div>
{NOTE.format(c='color:var(--salvia)')}""", cls="dark")

# ---------- Para quién ----------
chips = "".join(f'<span class="chip">{t}</span>' for t in [
    "Consulta", "Corte de cabello", "Clase de pilates", "Asesoría contable",
    "Masaje relajante", "Limpieza dental", "Sesión de fisioterapia"])
page("pq-1", top("Para quién", 0, 2, "citara-simbolo-claro.svg", "var(--petroleo)") + f"""
<div class="h1" style="position:absolute;left:90px;right:90px;top:430px;font-size:96px">¿Trabajas con <b>cita previa?</b></div>
<div style="position:absolute;left:90px;right:70px;top:780px">{chips}</div>
<div class="h1" style="position:absolute;left:90px;right:90px;top:1310px;font-size:64px">Entonces Citara <b>es para ti.</b></div>
""")

rows = "".join(f'<div class="row"{" style=\"border-bottom:1px solid rgba(46,64,82,.14)\"" if i == 4 else ""}><div class="n">{i}</div><div><div style="font-family:Unbounded;font-weight:600;font-size:42px;letter-spacing:-.02em">{t}</div><div style="font-size:31px;line-height:1.36;opacity:.75;margin-top:8px">{d}</div></div></div>'
               for i, (t, d) in enumerate([
                   ("Tus servicios", "Cada uno con su nombre y su duración."),
                   ("Tu equipo y tus espacios", "Quién atiende y dónde: profesionales, salas, cabinas o consultorios."),
                   ("Tus horarios", "Solo ofrece los espacios que de verdad están libres."),
                   ("Tu criterio", "Lo que necesita a una persona pasa a tu equipo."),
               ], start=1))
page("pq-2", top("Para quién", 1, 2, "citara-simbolo-claro.svg", "var(--petroleo)") + f"""
<div class="h1" style="position:absolute;left:90px;right:90px;top:430px;font-size:84px">Se configura <b>con tu negocio.</b></div>
<div style="position:absolute;left:90px;right:90px;top:740px">{rows}</div>
""")

# ---------- Prueba gratis (con espacio para el sticker de enlace) ----------
BUBBLE = "M161.26,0H0c7.9,8.65,29.35,38.79,29.35,38.79v68.21h0c0,59.09,47.91,107,107,107h24.91c59.09,0,107-47.91,107-107h0C268.26,47.91,220.35,0,161.26,0Z"
STICKER = ''  # espacio vacío (y 1380–1530) para el sticker de enlace que Andrés pone al publicar
page("pg-1", top("Prueba gratis", 0, 2, None, "var(--pizarra)") + f"""
<div style="position:absolute;left:90px;top:400px;width:620px;height:540px">
  <svg viewBox="-12 -20 292 254" width="620" height="540" style="position:absolute;inset:0"><path d="{BUBBLE}" fill="var(--pizarra)"/></svg>
  <div style="position:absolute;inset:0;display:grid;place-items:center;padding:40px 0 0 70px;font-family:Unbounded;font-weight:700;font-size:150px;line-height:.92;letter-spacing:-.04em;color:var(--bv);text-align:center">7<br>días</div></div>
<div class="h1" style="position:absolute;left:90px;right:90px;top:1010px;font-size:80px;color:var(--pizarra)">Pruébalo gratis.</div>
<div class="body" style="position:absolute;left:90px;right:90px;top:1130px;font-size:40px;color:var(--pizarra)">Sin tarjeta. En el WhatsApp de tu negocio, con el ritmo real de tu agenda.</div>
{STICKER}""", style="background:var(--naranja)")

steps = "".join(f'<div class="row"><div class="n">{i}</div><div style="font-size:36px;line-height:1.36;padding-top:10px">{t}</div></div>' for i, t in enumerate([
    "Creas la cuenta de tu negocio en el panel.",
    "Configuras tus servicios, tu equipo y tus horarios con una guía.",
    "Conectas tu WhatsApp en unos minutos, y lo <b>sigues usando en tu teléfono.</b>",
], start=1))
page("pg-2", top("Prueba gratis", 1, 2, "citara-simbolo-claro.svg", "var(--petroleo)") + f"""
<div class="h1" style="position:absolute;left:90px;right:90px;top:430px;font-size:84px">Empiezas en <b>3 pasos.</b></div>
<div style="position:absolute;left:90px;right:90px;top:700px">{steps}</div>
<div style="position:absolute;left:90px;right:90px;top:1250px;font-size:32px;font-weight:600;color:var(--petroleo)">Los 7 días empiezan el día que lo conectas.</div>
{STICKER}""")
print("ok")
