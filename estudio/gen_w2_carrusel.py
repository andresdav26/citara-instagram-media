"""Semana 2 · Carrusel: Diciembre se viene lleno. ¿Tu agenda está lista?

Cada consejo corresponde a algo que el panel de Citara ya hace (citara/admin-ui/src/pages/settings):
festivos (HolidaysSection), horario con fechas de validez (SchedulesSection), bloqueos (BlackoutsSection)
y recordatorio un día antes (M6).
"""
from pathlib import Path

OUT = Path(__file__).parent / "src" / "w2-carrusel"
OUT.mkdir(parents=True, exist_ok=True)
A = "../../assets"
N = 6

HEAD = """<!doctype html><html><head><meta charset="utf-8"><meta name="size" content="1080x1350">
<link rel="stylesheet" href="../base.css">
<style>:root{{--w:1080px;--h:1350px}}
.card{{background:#fff;border-radius:28px;box-shadow:0 24px 70px rgba(46,64,82,.14);border:1px solid rgba(46,64,82,.07);overflow:hidden}}
.card-h{{padding:24px 30px;background:#F6FAF8;border-bottom:1px solid rgba(46,64,82,.08);display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:27px}}
.row{{display:flex;justify-content:space-between;align-items:center;padding:20px 30px;border-top:1px solid rgba(46,64,82,.07);font-size:28px}}
.row:first-of-type{{border-top:none}}
.chip{{display:inline-block;font-weight:600;font-size:22px;padding:8px 18px;border-radius:30px;background:var(--salvia-2);color:var(--petroleo)}}
.chip.on{{background:var(--petroleo);color:var(--bv)}}
.muted{{opacity:.6}}
</style></head><body><div class="canvas {cls}">{body}</div></body></html>"""


def page(name, body, cls=""):
    (OUT / f"{name}.html").write_text(HEAD.format(body=body, cls=cls), encoding="utf-8")


def dots(i, dark=False):
    on = "var(--naranja)" if dark else "var(--petroleo)"
    off = "rgba(251,254,249,.3)" if dark else "rgba(46,64,82,.18)"
    return "".join(f'<span style="display:inline-block;height:10px;border-radius:5px;margin-left:10px;width:{40 if k == i else 10}px;background:{on if k == i else off}"></span>' for k in range(N))


# ---------- Portada ----------
page("01", f"""
<img class="logo" src="{A}/citara-oscuro.svg" style="position:absolute;left:90px;top:96px;width:250px">
<div style="position:absolute;left:90px;right:90px;top:330px">
  <div class="eyebrow">Temporada de fin de año</div>
  <div class="h1" style="font-size:90px;margin-top:34px">Diciembre se viene lleno. <b>¿Tu agenda está lista?</b></div>
  <div class="body" style="margin-top:44px;color:var(--salvia);max-width:860px">4 cosas para dejar listas esta semana, antes de que lleguen los mensajes.</div>
</div>
<div style="position:absolute;left:90px;bottom:96px;font-weight:600;font-size:28px;color:var(--naranja)">Desliza →</div>
<div style="position:absolute;right:90px;bottom:106px">{dots(0, True)}</div>
""", cls="dark")

# ---------- Consejos ----------
festivos = "".join(f'<div class="row"><span>{d}</span><span class="muted" style="font-size:24px">{n}</span></div>' for d, n in [
    ("Martes 8 de diciembre", "Inmaculada Concepción"),
    ("Viernes 25 de diciembre", "Navidad"),
    ("Viernes 1 de enero", "Año Nuevo"),
    ("Lunes 11 de enero", "Reyes Magos"),
])
MOCKS = {
    1: f"""<div class="card"><div class="card-h"><span>¿Abres los festivos?</span><span><span class="chip">Cerrado</span> <span class="chip on">Abierto 9:00 a. m. – 2:00 p. m.</span></span></div>
          <div style="padding:16px 30px 4px;font-size:21px;font-weight:600;letter-spacing:.12em;text-transform:uppercase" class="muted">Los próximos festivos</div>{festivos}</div>""",
    2: """<div class="card"><div class="card-h"><span>Horario de temporada</span><span class="chip on">Activo</span></div>
          <div class="row"><span>Lunes a sábado</span><b style="font-weight:600">8:00 a. m. – 8:00 p. m.</b></div>
          <div class="row"><span class="muted">Válido desde</span><span>1 de diciembre</span></div>
          <div class="row"><span class="muted">Válido hasta</span><span>31 de diciembre</span></div></div>""",
    3: """<div class="card"><div class="card-h"><span>Nuevo bloqueo</span><span class="chip">Todo el equipo</span></div>
          <div class="row"><span class="muted">Desde el día</span><span>28 de diciembre</span></div>
          <div class="row"><span class="muted">Hasta el día</span><span>2 de enero</span></div>
          <div class="row"><span class="muted">Motivo</span><span>Vacaciones</span></div></div>""",
    4: """<div class="phone"><div class="chat-head"><div class="avatar">TN</div><div><div class="chat-title">Tu negocio · WhatsApp</div><div class="chat-sub">Atendido por Citara</div></div></div>
          <div class="chat-body" style="gap:18px">
            <div class="msg in" style="font-size:29px">Hola, Laura. Te recordamos tu cita mañana a las <b>4:00&nbsp;p.&nbsp;m.</b> ¿Nos confirmas?</div>
            <div class="msg out" style="font-size:29px">Uy, mañana no puedo. ¿Me la pasas para el viernes?</div>
          </div></div>""",
}
TIPS = [
    ("Los festivos.", "Decide si abres y en qué horario, antes de que alguien te pida cita para el 8.",
     "Respondes “¿Abres los festivos?” en el panel, y Citara solo ofrece las horas en que de verdad atiendes."),
    ("El horario de temporada.", "Si vas a atender más horas en diciembre, déjalo definido desde ya.",
     "Agregas un horario con fecha de inicio y de fin, y los nuevos espacios se ofrecen solos."),
    ("Tus días libres.", "Vacaciones, cierres o capacitaciones: bloquéalos antes de que se llenen.",
     "Creas un bloqueo de un día a otro y nadie puede agendar ahí. Si ya había citas, el panel te avisa."),
    ("Los recordatorios.", "En temporada alta, una cita olvidada es un espacio que otra persona quería.",
     "Cada cita recibe un recordatorio un día antes, y quien no puede ir reprograma en el mismo chat."),
]
for i, (title, hoy, citara) in enumerate(TIPS, start=1):
    page(f"{i + 1:02d}", f"""
<div style="position:absolute;left:90px;right:90px;top:92px;display:flex;justify-content:space-between;align-items:center">
  <div class="eyebrow">Diciembre · {i:02d} <span style="opacity:.45">/ 04</span></div>
  <img src="{A}/citara-simbolo-claro.svg" style="width:78px">
</div>
<div style="position:absolute;left:90px;right:90px;top:180px;bottom:170px;display:flex;flex-direction:column;justify-content:space-between">
  <div class="h1" style="font-size:72px">{title}</div>
  <div>{MOCKS[i]}</div>
  <div>
    <div style="font-size:33px;line-height:1.38;opacity:.85;padding:0 6px">{hoy}</div>
    <div style="margin-top:26px;background:var(--salvia-3);border-left:8px solid var(--petroleo);border-radius:0 20px 20px 0;padding:28px 32px;display:flex;gap:26px;align-items:flex-start">
      <div style="flex:0 0 138px;font-weight:700;font-size:23px;letter-spacing:.12em;text-transform:uppercase;color:var(--petroleo);padding-top:8px">Con Citara</div>
      <div style="font-size:33px;line-height:1.34;font-weight:500">{citara}</div>
    </div>
  </div>
</div>
<div class="note" style="position:absolute;left:90px;bottom:100px">Vista ilustrativa · datos de ejemplo</div>
<div style="position:absolute;right:90px;bottom:106px">{dots(i)}</div>
""")

# ---------- Cierre ----------
page(f"{N:02d}", f"""
<div style="position:absolute;left:90px;right:90px;top:300px">
  <div class="eyebrow">Lo dejas listo una vez</div>
  <div class="h1" style="font-size:96px;margin-top:34px">Diciembre,<br><b>sin enredos.</b></div>
  <div class="body" style="margin-top:44px;color:var(--salvia);max-width:860px">Prueba Citara 7 días gratis, sin tarjeta. Creas tu cuenta y configuras tu agenda con una guía.</div>
  <div style="margin-top:56px;display:flex;align-items:center;gap:34px">
    <span class="pill">Prueba gratis 7 días <span style="font-size:34px">→</span></span>
    <span class="url" style="color:var(--bv)">citara.com.co</span>
  </div>
</div>
<div style="position:absolute;left:90px;bottom:210px;font-size:28px;color:var(--salvia)">📌 Guárdalo para revisarlo con tu equipo.</div>
<img class="logo" src="{A}/citara-oscuro.svg" style="position:absolute;left:90px;bottom:96px;width:210px">
<div style="position:absolute;right:90px;bottom:106px">{dots(N - 1, True)}</div>
""", cls="dark")
print("ok")
