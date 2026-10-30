# Estudio de piezas de Citara

Plantillas HTML que se renderizan a PNG o MP4 con Playwright (Chromium). Fuentes (Unbounded y Jost, licencia OFL) y logos en `assets/`.

- Carrusel: `python3 gen_carrusel.py && node render.js out/w1-carrusel src/w1-carrusel/*.html`
- Post, plantilla con foto y destacadas: `python3 gen_extra.py [ruta-foto]` y luego `node render.js <salida> <html...>`
- Reel: `node render_video.js src/w1-reel/reel.html out/frames 15 30` y después ffmpeg (H.264, yuv420p, 30 fps, con pista de audio silenciosa).

Los medios finales van en `semana-XX/` y Metricool los toma desde `raw.githubusercontent.com`.
