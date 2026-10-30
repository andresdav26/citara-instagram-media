"""Semana 1 · Carrusel: 5 mensajes que tu equipo responde todos los días."""
from pathlib import Path

OUT = Path(__file__).parent / "src" / "w1-carrusel"
OUT.mkdir(parents=True, exist_ok=True)
A = "../../assets"

HEAD = """<!doctype html><html><head><meta charset="utf-8"><meta name="size" content="1080x1350">
<link rel="stylesheet" href="../base.css">
<style>:root{{--w:1080px;--h:1350px}} {css}</style></head><body><div class="canvas {cls}">{body}</div></body></html>"""

def page(name, body, cls="", css=""):
    (OUT / f"{name}.html").write_text(HEAD.format(body=body, cls=cls, css=css), encoding="utf-8")

def dots(i, n=7, dark=False):
    c_on = "var(--naranja)" if dark else "var(--petroleo)"
    c_off = "rgba(251,254,249,.3)" if dark else "rgba(46,64,82,.18)"
    return "".join(
        f'<span style="display:inline-block;height:10px;border-radius:5px;margin-left:10px;'
        f'width:{40 if k == i else 10}px;background:{c_on if k == i else c_off}"></span>'
        for k in range(n))

# ---------- 1. Portada ----------
page("01", f"""
<img class="logo" src="{A}/citara-oscuro.svg" style="position:absolute;left:90px;top:96px;width:250px">
<div style="position:absolute;left:90px;right:90px;top:300px">
  <div class="eyebrow">Hoy, en tu negocio</div>
  <div class="h1" style="font-size:88px;margin-top:34px">5 mensajes que tu equipo responde <b>todos los días.</b></div>
  <div class="body" style="margin-top:40px;color:var(--salvia);max-width:820px">Y cómo se resuelven sin que nadie suelte lo que está haciendo.</div>
</div>
<div style="position:absolute;left:90px;right:90px;bottom:200px;display:flex;flex-direction:column;gap:18px;align-items:flex-end">
  <div class="msg out" style="font-size:28px;transform:rotate(-1.5deg)">¿Tienen cita el viernes?</div>
  <div class="msg out" style="font-size:28px;margin-right:60px;transform:rotate(1deg)">¿Puedo cambiar mi cita?</div>
  <div class="msg out" style="font-size:28px;margin-right:10px;transform:rotate(-.5deg)">Ya no voy a poder ir 😕</div>
</div>
<div style="position:absolute;left:90px;bottom:96px;font-weight:600;font-size:28px;color:var(--naranja)">Desliza →</div>
<div style="position:absolute;right:90px;bottom:106px">{dots(0, dark=True)}</div>
""", cls="dark")

# ---------- 2-6. Mensajes ----------
ITEMS = [
    ("Agenda",
     [("out", "Hola, ¿tienen cita el viernes?")],
     "Alguien deja lo que está haciendo, revisa la agenda y responde. Si escriben de noche, la respuesta llega al otro día.",
     "Ofrece solo los horarios que de verdad están libres y deja la cita en tu panel."),
    ("Confirma",
     [("in", "Hola, Ana. Te recordamos tu cita mañana a las <b>3:00&nbsp;p.&nbsp;m.</b> ¿Nos confirmas?"),
      ("out", "Sí, ahí estaré 👍")],
     "Alguien escribe, una por una, a todas las personas que tienen cita al día siguiente.",
     "Envía el recordatorio un día antes y la confirmación queda registrada en tu agenda."),
    ("Reprograma",
     [("out", "¿Puedo cambiar mi cita para el jueves?")],
     "Hay que buscar otro espacio, mover la cita y acordarse de liberar la anterior.",
     "Reprograma en el mismo chat y el horario anterior vuelve a quedar libre."),
    ("Cancela",
     [("out", "Ya no voy a poder ir mañana 😕")],
     "El mensaje se pierde entre otros y el espacio se queda vacío.",
     "Cancela la cita y el espacio vuelve a quedar disponible en tu agenda."),
    ("Pasa al equipo",
     [("out", "Antes de agendar, tengo una duda sobre el tratamiento")],
     "Las preguntas que necesitan a una persona se mezclan con las de horarios.",
     "Lo que necesita criterio humano pasa a tu equipo, en la misma conversación."),
]

for idx, (tag, msgs, hoy, citara) in enumerate(ITEMS, start=1):
    bubbles = "".join(f'<div class="msg {d}" style="font-size:32px">{t}</div>' for d, t in msgs)
    page(f"{idx + 1:02d}", f"""
<div style="position:absolute;left:90px;right:90px;top:92px;display:flex;justify-content:space-between;align-items:center">
  <div class="eyebrow">Mensaje {idx:02d} <span style="opacity:.45">/ 05</span></div>
  <img src="{A}/citara-simbolo-claro.svg" style="width:78px">
</div>
<div style="position:absolute;left:90px;right:90px;top:190px;bottom:170px;display:flex;flex-direction:column;justify-content:space-between">
  <div class="h1" style="font-size:80px">{tag}<span style="color:var(--naranja)">.</span></div>
  <div class="phone">
    <div class="chat-head"><div class="avatar">TN</div><div><div class="chat-title">Tu negocio · WhatsApp</div><div class="chat-sub">Atendido por Citara</div></div></div>
    <div class="chat-body" style="min-height:250px;justify-content:center;gap:20px">{bubbles}</div>
  </div>
  <div>
    <div style="display:flex;gap:28px;align-items:flex-start;padding:0 34px 0 42px">
      <div style="flex:0 0 142px;font-weight:600;font-size:24px;letter-spacing:.12em;text-transform:uppercase;opacity:.5;padding-top:8px">Hoy</div>
      <div style="font-size:33px;line-height:1.38;opacity:.8">{hoy}</div>
    </div>
    <div style="margin-top:30px;background:var(--salvia-3);border-left:8px solid var(--petroleo);border-radius:0 20px 20px 0;padding:32px 34px;display:flex;gap:28px;align-items:flex-start">
      <div style="flex:0 0 142px;font-weight:700;font-size:24px;letter-spacing:.12em;text-transform:uppercase;color:var(--petroleo);padding-top:8px">Con Citara</div>
      <div style="font-size:36px;line-height:1.34;font-weight:500">{citara}</div>
    </div>
  </div>
</div>
<div class="note" style="position:absolute;left:90px;bottom:100px">Vista ilustrativa · datos de ejemplo</div>
<div style="position:absolute;right:90px;bottom:106px">{dots(idx)}</div>
""")

# ---------- 7. Cierre ----------
page("07", f"""
<div style="position:absolute;left:90px;right:90px;top:330px">
  <div class="eyebrow">Los cinco, en un solo chat</div>
  <div class="h1" style="font-size:84px;margin-top:34px">Tu agenda fluye.<br>Tu equipo <b>respira.</b></div>
  <div class="body" style="margin-top:44px;color:var(--salvia);max-width:840px">Pruébalo 7 días en el WhatsApp de tu negocio. Sin tarjeta y con acompañamiento.</div>
  <div style="margin-top:56px;display:flex;align-items:center;gap:34px">
    <span class="pill">Prueba gratis 7 días <span style="font-size:34px">→</span></span>
    <span class="url" style="color:var(--bv)">citara.com.co</span>
  </div>
</div>
<div style="position:absolute;left:90px;bottom:210px;font-size:28px;color:var(--salvia)">📌 Guarda este post y compártelo con tu equipo.</div>
<img class="logo" src="{A}/citara-oscuro.svg" style="position:absolute;left:90px;bottom:96px;width:210px">
<div style="position:absolute;right:90px;bottom:106px">{dots(6, dark=True)}</div>
""", cls="dark")
print("ok")
