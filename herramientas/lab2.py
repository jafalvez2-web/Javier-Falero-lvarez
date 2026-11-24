"""Dibujos de laboratorio con material de verdad (SVG), estilo «pizarra limpia».

Piezas (cada función devuelve SVG y se coloca con coordenadas):
  balanza(x, y, lectura, sustancia)       balanza digital con vidrio de reloj y polvo
  erlenmeyer(x, y, w, h, liquido, ...)    matraz Erlenmeyer con líquido, burbujas, sólido, iones
  bureta(x, y_top, y_tip, texto)          bureta con graduaciones, llave y gota, en su soporte
  pipeta(x, y_top, y_tip)                 pipeta aforada
  aforado(x, y, h, liquido, texto)        matraz aforado
  vaso(x, y, w, h, liquido, ...)          vaso de precipitados con pico
  flecha(x1, y1, x2, y2, texto, curva)    flecha morada (recta o curva) con texto
  rotulo(x, y, lineas, ...)               texto con varias líneas (la primera en negrita)
  leyenda(x, y)                           leyenda de colores de los iones
Colores de los iones (rol): r ámbar = reacciona · e verde = espectador · p morado = producto · x rojo = sobra
"""
import html

FONT = "font-family='Open Sans, Arial, sans-serif'"
GLASS = "#4a5560"
LIQ = {'acido': '#f6e7b8', 'base': '#d8e8fb', 'agua': '#e3f0fb', 'rosa': '#f8d3e6', 'violeta': '#e3c8f3',
       'naranja': '#fbd9b0', 'verde': '#d5efd9', 'gris': '#eceae4'}
ION = {'r': ('#FAEEDA', '#BA7517', '#633806'), 'e': ('#E1F5EE', '#1D9E75', '#085041'),
       'p': ('#EEEDFE', '#7F77DD', '#3C3489'), 'x': ('#FCEBEB', '#E24B4A', '#791F1F'),
       'n': ('#F1EFE8', '#888780', '#444441')}


def esc(s):
    return html.escape(s, quote=False)


def texto(x, y, t, size=11, weight='normal', color='#222', anchor='middle', italic=False):
    st = " font-style='italic'" if italic else ''
    return f"<text x='{x}' y='{y}' text-anchor='{anchor}' font-size='{size}' font-weight='{weight}' fill='{color}'{st} {FONT}>{esc(t)}</text>"


def rotulo(x, y, lineas, size=11, anchor='middle', color='#222', first_color='#7209b9'):
    o = []
    for i, l in enumerate(lineas):
        o.append(texto(x, y + i * (size + 3), l, size if i else size + .5, 'bold' if i == 0 else 'normal',
                       first_color if i == 0 else color, anchor))
    return ''.join(o)


def ion(x, y, t, rol):
    f, s, tc = ION.get(rol, ION['n'])
    r = max(11, 3 + 3.3 * len(t))
    return (f"<ellipse cx='{x}' cy='{y}' rx='{r}' ry='10' fill='{f}' stroke='{s}' stroke-width='1'/>"
            f"<text x='{x}' y='{y+3.5}' text-anchor='middle' font-size='9' font-weight='bold' fill='{tc}' {FONT}>{esc(t)}</text>")


def burbujas(x, y, n=5, alto=40, texto_gas=None):
    o = []
    for i in range(n):
        bx = x + (-8, 6, -3, 9, -6, 4)[i % 6]
        by = y - i * alto / n
        r = 2.2 + (i % 3) * .9
        o.append(f"<circle cx='{bx}' cy='{by}' r='{r}' fill='white' stroke='#6b7c8c' stroke-width='.9'/>")
    if texto_gas:
        o.append(texto(x + 16, y - alto - 4, texto_gas, 10.5, 'bold', '#5a6b7a', 'start'))
        o.append(f"<path d='M{x+2} {y-alto+4} q-4 -8 2 -14 q6 -6 0 -12' fill='none' stroke='#8a9aa8' stroke-width='1.3' stroke-dasharray='2 2'/>")
    return ''.join(o)


def erlenmeyer(x, y, w=110, h=120, liquido='acido', nivel=.45, iones=(), solido=None, gas=None, etiqueta=None):
    """x = centro, y = base. nivel = fracción de la altura del cuerpo llena."""
    cuello_w, cuello_h = w * .26, h * .28
    top = y - h
    body_top = top + cuello_h
    xl, xr = x - w / 2, x + w / 2
    nl, nr = x - cuello_w / 2, x + cuello_w / 2
    # silueta
    path = (f"M{nl-3} {top} H{nr+3} M{nl} {top} V{body_top} L{xl+6} {y-8} Q{xl} {y} {xl+10} {y} "
            f"H{xr-10} Q{xr} {y} {xr-6} {y-8} L{nr} {body_top} V{top}")
    o = []
    # líquido: trapecio hasta el nivel
    ly = y - (y - body_top) * nivel
    def xat(yy, side):
        t = (y - 8 - yy) / (y - 8 - body_top)
        return (xl + 6) + t * (nl - (xl + 6)) if side < 0 else (xr - 6) - t * ((xr - 6) - nr)
    col = LIQ.get(liquido, liquido)
    o.append(f"<path d='M{xat(ly,-1)} {ly} Q{x} {ly+4} {xat(ly,1)} {ly} L{xr-6} {y-8} Q{xr} {y} {xr-10} {y} "
             f"H{xl+10} Q{xl} {y} {xl+6} {y-8} Z' fill='{col}' stroke='none'/>")
    o.append(f"<path d='{path}' fill='none' stroke='{GLASS}' stroke-width='1.8' stroke-linejoin='round'/>")
    # brillo del vidrio
    o.append(f"<path d='M{xl+16} {y-14} L{nl+4} {body_top+8}' stroke='white' stroke-width='3' opacity='.8'/>")
    # graduaciones
    for i in range(3):
        gy = y - 18 - i * (h * .14)
        o.append(f"<line x1='{x-w*.12}' y1='{gy}' x2='{x+w*.12}' y2='{gy}' stroke='#9aa5ae' stroke-width='.8'/>")
    if solido:
        o.append(f"<path d='M{x-w*.28} {y-2} Q{x} {y-20} {x+w*.28} {y-2} Z' fill='#f3f1ea' stroke='#8d8a80'/>")
        for dx, dy in ((-10, -6), (4, -9), (12, -5), (-2, -4), (-16, -3)):
            o.append(f"<circle cx='{x+dx}' cy='{y+dy}' r='1.3' fill='#8d8a80'/>")
        o.append(texto(x, y + 13, solido, 9.5, 'bold', '#5c5a52'))
    # iones dentro del líquido
    pos = [(-.2, .42), (.2, .42), (0, .8), (-.33, .82), (.33, .82), (0, .2)]
    for (t, rol), (fx, fy) in zip(iones, pos):
        iy = ly + (y - 10 - ly) * fy
        o.append(ion(x + fx * w, iy, t, rol))
    if gas:
        o.append(burbujas(x + 4, ly - 4, 5, 45 + cuello_h * .3, gas))
    if etiqueta:
        o.append(rotulo(x, y + (28 if solido else 18), etiqueta, 10.5))
    return ''.join(o)


def vaso(x, y, w=100, h=110, liquido='agua', nivel=.6, iones=(), solido=None, gas=None, etiqueta=None):
    xl, xr, top = x - w / 2, x + w / 2, y - h
    o = []
    ly = y - h * nivel
    o.append(f"<rect x='{xl+1}' y='{ly}' width='{w-2}' height='{y-ly-1}' fill='{LIQ.get(liquido, liquido)}'/>")
    o.append(f"<path d='M{xl-6} {top-4} Q{xl} {top} {xl} {top+6} V{y-4} Q{xl} {y} {xl+4} {y} H{xr-4} Q{xr} {y} {xr} {y-4} V{top}' "
             f"fill='none' stroke='{GLASS}' stroke-width='1.8'/>")
    for i in range(4):
        gy = y - 15 - i * h * .18
        o.append(f"<line x1='{xr-18}' y1='{gy}' x2='{xr-6}' y2='{gy}' stroke='#9aa5ae' stroke-width='.8'/>")
    o.append(f"<line x1='{xl+8}' y1='{top+14}' x2='{xl+8}' y2='{y-10}' stroke='white' stroke-width='3' opacity='.8'/>")
    if solido:
        o.append(f"<path d='M{x-w*.3} {y-1} Q{x} {y-18} {x+w*.3} {y-1} Z' fill='#f3f1ea' stroke='#8d8a80'/>")
        o.append(texto(x, y + 13, solido, 9.5, 'bold', '#5c5a52'))
    pos = [(-.25, .3), (.22, .3), (0, .62), (-.28, .78), (.28, .72), (0, .1)]
    zt = min(ly, y - 62)
    for (t, rol), (fx, fy) in zip(iones, pos):
        o.append(ion(x + fx * w, zt + (y - 12 - zt) * fy + 6, t, rol))
    if gas:
        o.append(burbujas(x, ly - 2, 5, 40, gas))
    if etiqueta:
        o.append(rotulo(x, y + (28 if solido else 18), etiqueta, 10.5))
    return ''.join(o)


def balanza(x, y, lectura='0,0000 g', sustancia=None, polvo=True):
    """x = centro, y = base de la balanza."""
    o = [f"<rect x='{x-62}' y='{y-46}' width='124' height='46' rx='6' fill='#eef0f2' stroke='{GLASS}' stroke-width='1.6'/>",
         f"<rect x='{x-44}' y='{y-36}' width='88' height='22' rx='3' fill='#1f2a33'/>",
         texto(x, y - 20, lectura, 12.5, 'bold', '#7dfc9b'),
         f"<circle cx='{x+50}' cy='{y-9}' r='3.5' fill='#c9cfd4' stroke='{GLASS}'/>",
         f"<circle cx='{x+38}' cy='{y-9}' r='3.5' fill='#c9cfd4' stroke='{GLASS}'/>",
         f"<rect x='{x-8}' y='{y-54}' width='16' height='8' fill='#c9cfd4' stroke='{GLASS}'/>",
         f"<rect x='{x-46}' y='{y-58}' width='92' height='5' rx='2' fill='#d6dbe0' stroke='{GLASS}'/>",
         # vidrio de reloj
         f"<path d='M{x-34} {y-60} Q{x} {y-50} {x+34} {y-60}' fill='#f4f8fb' stroke='{GLASS}' stroke-width='1.3'/>"]
    if polvo:
        o.append(f"<path d='M{x-20} {y-59} Q{x} {y-78} {x+20} {y-59} Z' fill='#f3f1ea' stroke='#8d8a80'/>")
        for dx, dy in ((-8, -64), (3, -68), (10, -63), (-2, -62), (-12, -61), (6, -60)):
            o.append(f"<circle cx='{x+dx}' cy='{y+dy}' r='1.2' fill='#8d8a80'/>")
    if sustancia:
        o.append(texto(x, y - 84, sustancia, 12, 'bold', '#222'))
    return ''.join(o)


def bureta(x, y_top, y_tip, texto_bureta=None, gastado=None, soporte=True, liquido='base', y_base=None):
    """bureta centrada en x, desde y_top hasta la punta y_tip (con llave y gota)."""
    tube_w = 12
    y_llave = y_tip - 26
    o = []
    if soporte:
        yb = y_base or (y_tip + 110)
        o.append(f"<rect x='{x-58}' y='{y_top+30}' width='5' height='{yb-y_top-30}' fill='#9aa3ab'/>")
        o.append(f"<rect x='{x-75}' y='{yb}' width='150' height='7' rx='2' fill='#9aa3ab'/>")
        o.append(f"<rect x='{x-58}' y='{y_top+40}' width='52' height='5' fill='#9aa3ab'/>")
        o.append(f"<rect x='{x-10}' y='{y_top+34}' width='20' height='16' rx='3' fill='none' stroke='#7d868e' stroke-width='2'/>")
    # líquido (hasta un nivel que ya ha bajado)
    o.append(f"<rect x='{x-tube_w/2+1}' y='{y_top+30}' width='{tube_w-2}' height='{y_llave-y_top-30}' fill='{LIQ.get(liquido, liquido)}'/>")
    o.append(f"<rect x='{x-tube_w/2}' y='{y_top}' width='{tube_w}' height='{y_llave-y_top}' rx='2' fill='none' stroke='{GLASS}' stroke-width='1.6'/>")
    for i in range(int((y_llave - y_top - 10) / 9)):
        gy = y_top + 8 + i * 9
        ln = 6 if i % 5 == 0 else 3
        o.append(f"<line x1='{x-tube_w/2}' y1='{gy}' x2='{x-tube_w/2+ln}' y2='{gy}' stroke='#7d868e' stroke-width='.8'/>")
    # llave
    o.append(f"<rect x='{x-11}' y='{y_llave}' width='22' height='7' rx='2' fill='#2f6fb3' stroke='#1e4b7a'/>")
    o.append(f"<path d='M{x-3} {y_llave+7} L{x-1.5} {y_tip-4} H{x+1.5} L{x+3} {y_llave+7}' fill='{LIQ.get(liquido, liquido)}' stroke='{GLASS}' stroke-width='1.2'/>")
    # gota
    o.append(f"<path d='M{x} {y_tip+1} q-4 7 0 10 q4 -3 0 -10' fill='#9cc3ee' stroke='#4f86c2' stroke-width='.8'/>")
    if texto_bureta:
        o.append(rotulo(x + 16, y_top + 8, texto_bureta, 10.5, 'start'))
    if gastado:
        o.append(rotulo(x + 16, y_top + 8 + 14 * (len(texto_bureta or []) + .4), gastado, 10.5, 'start', '#222', '#c0392b'))
    return ''.join(o)


def pipeta(x, y_top, y_tip, liquido='acido'):
    o = [f"<rect x='{x-2.5}' y='{y_top}' width='5' height='{(y_tip-y_top)*.35}' fill='#fff' stroke='{GLASS}' stroke-width='1.2'/>",
         f"<line x1='{x-4}' y1='{y_top+12}' x2='{x+4}' y2='{y_top+12}' stroke='#c0392b' stroke-width='1.2'/>"]
    by = y_top + (y_tip - y_top) * .35
    o.append(f"<ellipse cx='{x}' cy='{by+16}' rx='8' ry='17' fill='{LIQ.get(liquido, liquido)}' stroke='{GLASS}' stroke-width='1.2'/>")
    o.append(f"<path d='M{x-2.5} {by+32} L{x-1} {y_tip} H{x+1} L{x+2.5} {by+32}' fill='{LIQ.get(liquido, liquido)}' stroke='{GLASS}' stroke-width='1.2'/>")
    return ''.join(o)


def aforado(x, y, h=130, liquido='agua', etiqueta=None):
    r = h * .26
    o = [f"<circle cx='{x}' cy='{y-r}' r='{r}' fill='{LIQ.get(liquido, liquido)}' stroke='{GLASS}' stroke-width='1.8'/>",
         f"<rect x='{x-6}' y='{y-h}' width='12' height='{h-2*r+4}' fill='{LIQ.get(liquido, liquido)}' stroke='{GLASS}' stroke-width='1.8'/>",
         f"<rect x='{x-5}' y='{y-h}' width='10' height='{h*.25}' fill='white'/>",
         f"<line x1='{x-9}' y1='{y-h*.72}' x2='{x+9}' y2='{y-h*.72}' stroke='#c0392b' stroke-width='1.3'/>",
         f"<rect x='{x-8}' y='{y-h-8}' width='16' height='8' rx='2' fill='#2f6fb3'/>"]
    if etiqueta:
        o.append(rotulo(x, y + 18, etiqueta, 10.5))
    return ''.join(o)


def flecha(x1, y1, x2, y2, txt=None, curva=0, color='#7209b9', txt_dy=-8):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - curva
    d = f"M{x1} {y1} Q{mx} {my} {x2} {y2}" if curva else f"M{x1} {y1} L{x2} {y2}"
    o = [f"<path d='{d}' fill='none' stroke='{color}' stroke-width='2.2' marker-end='url(#pta)'/>"]
    if txt:
        lines = txt.split('|')
        ty = (my if curva else my) + txt_dy - (len(lines) - 1) * 12
        for i, l in enumerate(lines):
            o.append(texto(mx, ty + i * 12 - (curva * .45 if curva else 0), l, 10, 'bold', color))
    return ''.join(o)


def caja(x, y, w, h, lineas, color='#7209b9', fondo='#f6effb'):
    o = [f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='7' fill='{fondo}' stroke='{color}' stroke-width='1.4'/>"]
    n = len(lineas)
    for i, l in enumerate(lineas):
        o.append(texto(x + w / 2, y + h / 2 - (n - 1) * 7.5 + i * 15 + 4, l, 11 if i == 0 else 10.5,
                       'bold' if i == 0 else 'normal', color if i == 0 else '#333'))
    return ''.join(o)


def numero(x, y, n, txt):
    return (f"<circle cx='{x}' cy='{y}' r='10' fill='#7209b9'/>" + texto(x, y + 4, str(n), 11, 'bold', 'white') +
            texto(x + 16, y + 4, txt, 11.5, 'bold', '#7209b9', 'start'))


def leyenda(x, y):
    o = []
    for i, (rol, t) in enumerate((('r', 'reacciona'), ('e', 'espectador'), ('p', 'producto'), ('x', 'sobra'))):
        f, s, _ = ION[rol]
        o.append(f"<circle cx='{x+i*78}' cy='{y}' r='5' fill='{f}' stroke='{s}'/>" + texto(x + i * 78 + 9, y + 3.5, t, 9, 'normal', '#555', 'start'))
    return ''.join(o)


def svg(w, h, cuerpo):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='{w}' height='{h}'>"
            "<defs><marker id='pta' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'>"
            "<path d='M0 0 L10 5 L0 10 z' fill='#7209b9'/></marker></defs>"
            f"<rect width='{w}' height='{h}' fill='white'/>{cuerpo}</svg>")


def mechero(x, y):
    """mechero Bunsen: x centro, y = base"""
    return (f"<rect x='{x-16}' y='{y-6}' width='32' height='6' rx='2' fill='#7d868e'/>"
            f"<rect x='{x-5}' y='{y-34}' width='10' height='28' fill='#a7b0b8' stroke='{GLASS}'/>"
            f"<path d='M{x-6} {y-36} Q{x} {y-66} {x+6} {y-36} Z' fill='#9cc3ee' stroke='#4f86c2'/>"
            f"<path d='M{x-3} {y-37} Q{x} {y-54} {x+3} {y-37} Z' fill='#f5b041'/>")


def crisol(x, y, solido=None):
    """crisol sobre triángulo y trípode, con mechero debajo. y = base del mechero"""
    cy = y - 80
    o = [f"<line x1='{x-34}' y1='{cy+12}' x2='{x-26}' y2='{y}' stroke='#7d868e' stroke-width='2.5'/>",
         f"<line x1='{x+34}' y1='{cy+12}' x2='{x+26}' y2='{y}' stroke='#7d868e' stroke-width='2.5'/>",
         f"<line x1='{x-40}' y1='{cy+12}' x2='{x+40}' y2='{cy+12}' stroke='#7d868e' stroke-width='3'/>",
         f"<path d='M{x-24} {cy-20} L{x-16} {cy+14} H{x+16} L{x+24} {cy-20} Z' fill='#f4f1ea' stroke='{GLASS}' stroke-width='1.6'/>",
         f"<path d='M{x-15} {cy+10} Q{x} {cy-4} {x+15} {cy+10} Z' fill='#e8e4d8' stroke='#8d8a80'/>",
         mechero(x, y)]
    if solido:
        o.append(texto(x, cy - 28, solido, 10, 'bold', '#5c5a52'))
    return ''.join(o)


def barra(x, ytop, h, txt, recubierta=False):
    o = []
    if recubierta:
        o.append(f"<rect x='{x-17}' y='{ytop+h*.45}' width='34' height='{h*.55}' rx='3' fill='#d9d9d9' stroke='#8f8f8f'/>")
        for i in range(6):
            o.append(f"<circle cx='{x-13+(i%3)*13}' cy='{ytop+h*.55+(i//3)*h*.22}' r='2' fill='#b8b8b8'/>")
    o.append(f"<rect x='{x-12}' y='{ytop}' width='24' height='{h}' rx='2' fill='#9a9893' stroke='#5F5E5A'/>")
    o.append(f"<line x1='{x-6}' y1='{ytop+4}' x2='{x-6}' y2='{ytop+h-4}' stroke='white' stroke-width='2' opacity='.5'/>")
    o.append(texto(x, ytop - 6, txt, 10.5, 'bold', '#444'))
    return ''.join(o)


# --------- traductor de los dibujos antiguos (labspecs7) al estilo nuevo ---------
OLDCOL = {'#FFF6E8': 'acido', '#DCEBFA': 'base'}


def _liq(p):
    c = p.get('color')
    if c:
        return OLDCOL.get(c, c)
    return 'agua'


def draw2(panels, arrows=(), bottom=None):
    n = len(panels)
    W = 700
    pw = (W - 20) / n
    hay_bureta = any(p.get('burette') for p in panels)
    alto = any(p.get('gas') or p.get('bar') for p in panels)
    base = 300 if hay_bureta else (232 if alto else 200)
    o = []
    for i, p in enumerate(panels):
        cx = 10 + pw / 2 + i * pw
        t = p.get('title', '')
        num, _, tt = t.partition('. ')
        if num.isdigit():
            o.append(numero(cx - pw / 2 + 14, 22, num, ''))
            o.append(texto(cx - pw / 2 + 28, 26, tt, 11, 'bold', '#7209b9', 'start'))
        else:
            o.append(texto(cx, 26, t, 11, 'bold', '#7209b9'))
        k = p.get('kind', 'beaker')
        eq_w = min(pw - 40, 120)
        bot = base
        if k == 'balance':
            o.append(balanza(cx, base, p.get('mass', ''), None))
            o.append(texto(cx, base - 84, p.get('solid', ''), 11, 'bold', '#222'))
        elif k == 'crucible':
            o.append(crisol(cx, base, p.get('solid')))
        elif k == 'text':
            lines = p.get('lines', [])
            hh = 22 + 17 * len(lines)
            o.append(caja(cx - pw / 2 + 30, base - 70 - hh / 2, pw - 60, hh, lines, '#0a5d0a', '#f2fbf2'))
        elif k == 'flask':
            if p.get('burette'):
                o.append(bureta(cx, base - 236, base - 128, None, None, y_base=base + 1))
                o.append(rotulo(cx + 10, base - 252, [p['burette']], 10.5, 'middle'))
            o.append(erlenmeyer(cx, base, eq_w, 105 if p.get('burette') else 125, _liq(p),
                                0 if p.get('liquid') is False else .5, p.get('ions', []), p.get('solid'), (p['gas'] + ' ↑') if p.get('gas') else None))
        else:  # beaker
            h = 125
            if p.get('heat'):
                o.append(f"<line x1='{cx-eq_w/2}' y1='{base-62}' x2='{cx+eq_w/2}' y2='{base-62}' stroke='#7d868e' stroke-width='3'/>")
                o.append(f"<line x1='{cx-eq_w/2+8}' y1='{base-62}' x2='{cx-eq_w/2+2}' y2='{base}' stroke='#7d868e' stroke-width='2.5'/>")
                o.append(f"<line x1='{cx+eq_w/2-8}' y1='{base-62}' x2='{cx+eq_w/2-2}' y2='{base}' stroke='#7d868e' stroke-width='2.5'/>")
                o.append(mechero(cx, base))
                vb, h = base - 64, 95
            else:
                vb = base
            if p.get('bar'):
                bt, rec = p['bar']
                o.append(vaso(cx, vb, eq_w, h, _liq(p), 0 if p.get('liquid') is False else .62,
                              [ii for ii in p.get('ions', [])][:4], None, None))
                o.append(barra(cx, vb - h - 22, h + 8, bt, rec))
                if p.get('gas'):
                    o.append(burbujas(cx + eq_w * .3, vb - h * .62 - 4, 4, 36, p['gas'] + ' ↑'))
            else:
                if p.get('burette'):
                    o.append(bureta(cx, base - 236, base - 128, None, None, y_base=base + 1))
                    o.append(rotulo(cx + 10, base - 252, [p['burette']], 10.5, 'middle'))
                    h = 100
                o.append(vaso(cx, vb, eq_w, h, _liq(p), 0 if p.get('liquid') is False else .62,
                              p.get('ions', []), p.get('solid'), (p['gas'] + ' ↑') if p.get('gas') else None))
            if p.get('solid'):
                bot += 12
        notes = p.get('note', [])
        for j, l in enumerate(notes):
            o.append(texto(cx, bot + 22 + j * 14, l, 10.3, 'bold' if j == 0 else 'normal', '#222'))
        if i < n - 1:
            ax = cx + pw / 2
            yy = base - 70
            lab = arrows[i] if i < len(arrows) else ''
            o.append(flecha(ax - 16, yy, ax + 16, yy, lab or None, txt_dy=-10))
    nb = max(len(p.get('note', [])) for p in panels)
    y = base + 34 + 14 * nb + (12 if any(p.get('solid') and p.get('kind', 'beaker') != 'balance' for p in panels) else 0)
    if bottom:
        bl = bottom.split('|')
        bh = 18 + 16 * len(bl)
        o.append(caja(30, y, W - 60, bh, bl))
        y += bh + 14
    o.append(leyenda(W - 330, y + 2))
    return svg(W, y + 12, ''.join(o))
