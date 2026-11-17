"""Dibujos de laboratorio en viñetas (SVG) para los problemas.
Cada dibujo = lista de viñetas; cada viñeta = dict con:
  title, kind ('beaker'|'flask'|'balance'|'crucible'|'text'), ions=[(texto, rol)], solid='texto', bar=('texto', recubierta?),
  gas='texto', burette='texto', heat=True, note=['línea', ...], liquid=True/False, color='#hex'
rol: 'r' reacciona (ámbar), 'e' espectador (verde azulado), 'p' producto (morado), 'x' exceso/sobra (rojo suave)
Entre viñetas: arrows=['texto flecha', ...]
"""
import html

C = {'r': ('#FAEEDA', '#BA7517', '#633806'), 'e': ('#E1F5EE', '#1D9E75', '#085041'),
     'p': ('#EEEDFE', '#7F77DD', '#3C3489'), 'x': ('#FCEBEB', '#E24B4A', '#791F1F'),
     'n': ('#F1EFE8', '#888780', '#444441')}
FONT = "font-family='Open Sans, Arial, sans-serif'"

def esc(s):
    return html.escape(s, quote=False)

def ion(x, y, t, role):
    f, s, tc = C.get(role, C['n'])
    r = max(14, 4 + 3.6 * len(t))
    return (f"<ellipse cx='{x}' cy='{y}' rx='{r}' ry='13' fill='{f}' stroke='{s}' stroke-width='1'/>"
            f"<text x='{x}' y='{y+4}' text-anchor='middle' font-size='10.5' fill='{tc}' {FONT}>{esc(t)}</text>")

def label(x, y, t, size=11, weight='normal', color='#333', anchor='middle'):
    return f"<text x='{x}' y='{y}' text-anchor='{anchor}' font-size='{size}' font-weight='{weight}' fill='{color}' {FONT}>{esc(t)}</text>"

def beaker(cx, top, w, h, p):
    o = []
    x0, x1, y1 = cx - w / 2, cx + w / 2, top + h
    liq = p.get('color', '#DCEBFA')
    if p.get('liquid', True):
        o.append(f"<rect x='{x0+2}' y='{top+28}' width='{w-4}' height='{h-30}' fill='{liq}'/>")
    o.append(f"<path d='M{x0} {top} V{y1-5} Q{x0} {y1} {x0+5} {y1} H{x1-5} Q{x1} {y1} {x1} {y1-5} V{top}' fill='none' stroke='#555' stroke-width='1.6'/>")
    # barra metálica
    bx = None
    if p.get('bar'):
        t, coated = p['bar']
        bw = 26
        bx = cx
        if coated:
            o.append(f"<rect x='{cx-bw/2-5}' y='{top-22}' width='{bw+10}' height='{h-10}' rx='3' fill='#D3D1C7' stroke='#888780'/>")
        o.append(f"<rect x='{cx-bw/2}' y='{top-22}' width='{bw}' height='{h-16}' rx='2' fill='#9a9893' stroke='#5F5E5A'/>")
        o.append(label(cx, top + h / 2, t, 10.5, 'bold', '#fff'))
    # sólido en el fondo
    if p.get('solid'):
        o.append(f"<path d='M{x0+8} {y1-3} Q{cx} {y1-30} {x1-8} {y1-3} Z' fill='#E8E6DE' stroke='#888780'/>")
        o.append(label(cx, y1 - 9, p['solid'], 10, 'bold', '#444'))
    # iones
    ions = p.get('ions', [])
    cols = 2 if bx is not None else 2
    xs = [x0 + w * 0.24, x1 - w * 0.24] if bx is None else [x0 + w * 0.18, x1 - w * 0.18]
    if bx is None and len(ions) > 4:
        xs = [x0 + w * 0.22, cx, x1 - w * 0.22]
    ytop = top + 48
    ybot = y1 - (40 if p.get('solid') else 18)
    rows = max(1, -(-len(ions) // len(xs)))
    dy = (ybot - ytop) / max(1, rows - 1) if rows > 1 else 0
    for i, (t, role) in enumerate(ions):
        r_, c_ = divmod(i, len(xs))
        y = ytop + r_ * dy if rows > 1 else (ytop + ybot) / 2
        o.append(ion(xs[c_], y, t, role))
    # gas
    if p.get('gas'):
        for k, (dx, dy2) in enumerate(((-14, 0), (2, -14), (14, -4))):
            o.append(f"<circle cx='{cx+dx+ (w/3 if bx else 0)}' cy='{top+18+dy2}' r='4' fill='none' stroke='#888'/>")
        gx = cx + (w / 3 if bx else 0)
        o.append(f"<line x1='{gx}' y1='{top+6}' x2='{gx}' y2='{top-26}' stroke='#888' stroke-width='1.3' marker-end='url(#ar)'/>")
        o.append(label(gx, top - 32, p['gas'] + '↑', 10.5, 'bold', '#555'))
    # bureta
    if p.get('burette'):
        o.append(f"<rect x='{cx-6}' y='{top-78}' width='12' height='62' fill='#FFF6E8' stroke='#555'/>")
        o.append(f"<path d='M{cx-3} {top-16} L{cx} {top-6} L{cx+3} {top-16}' fill='none' stroke='#555'/>")
        o.append(label(cx + 10, top - 60, p['burette'], 10, 'bold', '#633806', 'start'))
    if p.get('heat'):
        for dx in (-12, 0, 12):
            o.append(f"<path d='M{cx+dx-5} {y1+22} Q{cx+dx} {y1+4} {cx+dx+5} {y1+22} Z' fill='#EF9F27' stroke='#D85A30'/>")
    return o

def flask(cx, top, w, h, p):
    o = []
    y1 = top + h
    neck = 16
    liq = p.get('color', '#DCEBFA')
    path = f"M{cx-neck/2} {top} V{top+h*0.35} L{cx-w/2} {y1-4} Q{cx-w/2} {y1} {cx-w/2+5} {y1} H{cx+w/2-5} Q{cx+w/2} {y1} {cx+w/2} {y1-4} L{cx+neck/2} {top+h*0.35} V{top}"
    o.append(f"<path d='M{cx-w/2+6} {y1-2} L{cx-w*0.3} {top+h*0.62} H{cx+w*0.3} L{cx+w/2-6} {y1-2} Z' fill='{liq}'/>")
    o.append(f"<path d='{path}' fill='none' stroke='#555' stroke-width='1.6'/>")
    ions = p.get('ions', [])
    for i, (t, role) in enumerate(ions[:3]):
        o.append(ion(cx + (-24, 24, 0)[i] if len(ions) > 1 else cx, y1 - 18 - (14 if i == 2 else 0), t, role))
    if p.get('burette'):
        o.append(f"<rect x='{cx-6}' y='{top-70}' width='12' height='62' fill='#FFF6E8' stroke='#555'/>")
        o.append(f"<path d='M{cx-3} {top-8} L{cx} {top+2} L{cx+3} {top-8}' fill='none' stroke='#555'/>")
        o.append(label(cx + 10, top - 52, p['burette'], 10, 'bold', '#633806', 'start'))
    return o

def balance(cx, top, w, h, p):
    o = []
    y = top + h - 30
    o.append(f"<rect x='{cx-w/2+6}' y='{y}' width='{w-12}' height='26' rx='4' fill='#F1EFE8' stroke='#555'/>")
    o.append(f"<rect x='{cx-26}' y='{y+5}' width='52' height='14' rx='2' fill='#fff' stroke='#888'/>")
    o.append(label(cx, y + 16, p.get('mass', ''), 9.5, 'bold', '#222'))
    o.append(f"<line x1='{cx-w/2+16}' y1='{y-4}' x2='{cx+w/2-16}' y2='{y-4}' stroke='#555' stroke-width='2'/>")
    o.append(f"<path d='M{cx-26} {y-6} Q{cx} {y-34} {cx+26} {y-6} Z' fill='#E8E6DE' stroke='#888780'/>")
    sl = p.get('solid', '')
    o.append(label(cx, y - 13 if len(sl) <= 9 else y - 42, sl, 10 if len(sl) <= 16 else 9, 'bold', '#444'))
    return o

def crucible(cx, top, w, h, p):
    o = []
    y = top + h - 50
    o.append(f"<path d='M{cx-30} {y} L{cx-22} {y+30} H{cx+22} L{cx+30} {y} Z' fill='#F1EFE8' stroke='#555' stroke-width='1.5'/>")
    o.append(f"<path d='M{cx-20} {y+26} Q{cx} {y+4} {cx+20} {y+26} Z' fill='#E8E6DE' stroke='#888780'/>")
    o.append(label(cx, y - 8, p.get('solid', ''), 10, 'bold', '#444'))
    for dx in (-12, 0, 12):
        o.append(f"<path d='M{cx+dx-5} {y+52} Q{cx+dx} {y+34} {cx+dx+5} {y+52} Z' fill='#EF9F27' stroke='#D85A30'/>")
    return o

def textpanel(cx, top, w, h, p):
    o = [f"<rect x='{cx-w/2+4}' y='{top}' width='{w-8}' height='{h}' rx='8' fill='#F6FBF6' stroke='#9bc79b'/>"]
    lines = p.get('lines', [])
    y0 = top + h / 2 - (len(lines) - 1) * 9
    for i, l in enumerate(lines):
        o.append(label(cx, y0 + i * 18, l, 11, 'bold' if i == 0 else 'normal', '#0a5d0a' if i == 0 else '#333'))
    return o

KIND = {'beaker': beaker, 'flask': flask, 'balance': balance, 'crucible': crucible, 'text': textpanel}

def draw(panels, arrows=(), bottom=None, title=None):
    n = len(panels)
    W = 680
    gap = 34
    pw = (W - 20 - gap * (n - 1)) / n
    top = 112 if any(p.get('burette') for p in panels) else (78 if any(p.get('gas') or p.get('bar') for p in panels) else 44)
    ph = 170
    H = top + ph + 70 + (58 if bottom else 0)
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W}' height='{H}'>",
         "<defs><marker id='ar' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='6' markerHeight='6' orient='auto-start-reverse'><path d='M2 1L8 5L2 9' fill='none' stroke='context-stroke' stroke-width='1.6'/></marker></defs>",
         f"<rect width='{W}' height='{H}' fill='#fff'/>"]
    for i, p in enumerate(panels):
        cx = 10 + pw / 2 + i * (pw + gap)
        o.append(label(cx, 20, p.get('title', ''), 11.5, 'bold', '#7209b9'))
        bw = min(pw - 30, 150)
        o += KIND[p.get('kind', 'beaker')](cx, top, bw, ph, p)
        for k, l in enumerate(p.get('note', [])):
            o.append(label(cx, top + ph + 22 + k * 15, l, 10.2, 'normal', '#333'))
        if i < n - 1:
            ax0 = cx + pw / 2 - 4
            ax1 = ax0 + gap - 2
            o.append(f"<line x1='{ax0}' y1='{top+ph/2}' x2='{ax1}' y2='{top+ph/2}' stroke='#7209b9' stroke-width='1.6' marker-end='url(#ar)'/>")
            if i < len(arrows) and arrows[i]:
                for k, l in enumerate(arrows[i].split('|')):
                    o.append(label((ax0 + ax1) / 2, top + ph / 2 - 10 - 12 * (len(arrows[i].split('|')) - 1 - k), l, 9.5, 'bold', '#7209b9'))
    if bottom:
        y = top + ph + 62
        o.append(f"<rect x='20' y='{y}' width='{W-40}' height='46' rx='8' fill='#EEEDFE' stroke='#7F77DD'/>")
        bl = bottom.split('|')
        for k, l in enumerate(bl):
            o.append(label(W / 2, y + 19 + k * 17 - (8 if len(bl) == 1 else 0) + (8 if len(bl) == 1 else 0), l, 11.5 if k == 0 else 10.5, 'bold' if k == 0 else 'normal', '#3C3489'))
    # leyenda
    o.append(label(W - 12, H - 6, 'ámbar = reacciona · verde = espectador · morado = producto · rojo = sobra (exceso)', 8.5, 'normal', '#888', 'end'))
    o.append('</svg>')
    return '\n'.join(o)
