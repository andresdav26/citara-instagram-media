"""Portadas de destacadas, tres direcciones (sin íconos).

A · Conversación: una burbuja con la forma del logo y dos palabras.
B · Fotos: recortes de las fotos de la campaña, con un aro naranja.
C · Marca: la burbuja del logo en grande, recortada, en tres combinaciones de la paleta.

Cada portada es una historia de 1080x1920: Instagram recorta un círculo del centro.
"""
from pathlib import Path

OUT = Path(__file__).parent / "src" / "destacadas-v2"
OUT.mkdir(parents=True, exist_ok=True)
A = "../../assets"
HEAD = """<!doctype html><html><head><meta charset="utf-8"><meta name="size" content="1080x1920">
<link rel="stylesheet" href="../base.css"><style>:root{{--w:1080px;--h:1920px}}
.c{{position:absolute;left:50%;top:50%;width:760px;height:760px;margin:-380px 0 0 -380px;border-radius:50%;overflow:hidden;display:grid;place-items:center}}
</style></head><body><div class="canvas" style="background:{bg}">{body}</div></body></html>"""

# La burbuja del logo (primer path de citara-simbolo), como forma.
BUBBLE = "M161.26,0H0c7.9,8.65,29.35,38.79,29.35,38.79v68.21h0c0,59.09,47.91,107,107,107h24.91c59.09,0,107-47.91,107-107h0C268.26,47.91,220.35,0,161.26,0Z"
STAR = "M136.99,145.06c-1.74-8.21-2.97-16.72-6.86-23.81-6.07-11.07-18.97-12.59-30.31-15.29,9.26-2.18,20.31-3.78,26.93-10.67,6.57-6.83,8.21-18.77,10.24-28.58,2.07,10.12,3.7,22.99,11.47,29.79,6.75,5.9,16.96,7.39,25.74,9.46-9.32,2.16-20.83,3.82-27.37,11.04-6.24,6.89-7.9,18.55-9.84,28.06Z"

HL = ["como-funciona", "para-quien", "prueba-gratis"]

# A · Conversación
A_SET = [("var(--pizarra)", "var(--naranja)", "var(--pizarra)", "¿Tienen<br>cita?"),
         ("var(--petroleo)", "var(--bv)", "var(--pizarra)", "Para<br>ti"),
         ("var(--naranja)", "var(--pizarra)", "var(--bv)", "7<br>días")]
for name, (bg, bub, ink, txt) in zip(HL, A_SET):
    body = f"""<div class="c"><svg viewBox="-12 -20 292 254" width="700" height="609" style="position:absolute">
      <path d="{BUBBLE}" fill="{bub}"/></svg>
      <div style="position:relative;margin:40px 0 0 70px;font-family:Unbounded;font-weight:700;font-size:104px;line-height:.98;letter-spacing:-.04em;color:{ink};text-align:center">{txt}</div></div>"""
    (OUT / f"A-{name}.html").write_text(HEAD.format(bg=bg, body=body), encoding="utf-8")

# B · Fotos (posición del recorte en %, zoom)
B_SET = [("foto-af874636.jpg", "72% 45%", 300),   # barbero con el celular
         ("foto-f98ecd5c.jpg", "36% 62%", 210),   # el salón, sillas y equipo
         ("foto-5fb562bc.jpg", "70% 38%", 300)]   # estilista con el celular
for name, (img, pos, zoom) in zip(HL, B_SET):
    body = f"""<div class="c" style="background:url('{A}/{img}') {pos}/{zoom}% auto no-repeat;box-shadow:inset 0 0 0 22px var(--naranja)"></div>"""
    (OUT / f"B-{name}.html").write_text(HEAD.format(bg="var(--pizarra)", body=body), encoding="utf-8")

# C · Marca: la burbuja enorme y recortada, con la estrella
C_SET = [("var(--naranja)", "var(--pizarra)", "var(--naranja)", "-40 -10 210 170"),
         ("var(--salvia)", "var(--petroleo)", "var(--bv)", "60 40 210 170"),
         ("var(--pizarra)", "var(--naranja)", "var(--pizarra)", "20 70 200 160")]
for name, (bg, bub, star, vb) in zip(HL, C_SET):
    body = f"""<div class="c" style="background:{bg}"><svg viewBox="{vb}" width="760" height="760" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0">
      <path d="{BUBBLE}" fill="{bub}"/><path d="{STAR}" fill="{star}"/></svg></div>"""
    (OUT / f"C-{name}.html").write_text(HEAD.format(bg=bg, body=body), encoding="utf-8")
print("ok")
