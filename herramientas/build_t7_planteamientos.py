"""Tema 7 · Reacciones químicas, con planteamientos en flechas.

Base: los apuntes completos del Tema 7 (herramientas/fuentes_md/tema7/t7_full.md): teoría,
preguntas de teoría, dibujos de laboratorio, Datos / ¿Qué pasa? / reacción y ajuste,
"Cómo se hace", trampas y "Lo que tienes que llevarte".
Encima: de herramientas/fuentes_md/tema7_planteamientos/*.md se toman, para cada ficha,
el tipo, el plan en flechas [[PLAN]] y la resolución flecha a flecha (①, ②…, con las
ecuaciones de x construidas pieza a pieza). Sustituyen a los "Paso k" antiguos.
00_intro.md (la receta y los retoques) se inserta después de la caja de herramientas.
05_explica.md: el párrafo "Lo que vamos a hacer" de cada ficha, que va justo antes de sus flechas.

Macro [[PLAN ... ]]: cada línea es una fila de cajas unidas por flechas.
    caja --[① etiqueta]--> caja --[② ...]--> !caja final
  "Etiqueta :: ..." pone título a la fila; una caja que empieza por "!" es el resultado.

Dibujos: lab2.py + labspecs7_v2.py (material de laboratorio) -> img/lab7v2_*.svg
Salida: tema7/apuntes/Tema7_Planteamientos.pdf
Uso:    python herramientas/build_t7_planteamientos.py
"""
import glob, html, os, re, subprocess, sys

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import build2, pymupdf

BASE = os.path.join(H, 'fuentes_md', 'tema7', 't7_full.md')
SRC = os.path.join(H, 'fuentes_md', 'tema7_planteamientos')
PDF = os.path.join(os.path.dirname(H), 'tema7', 'apuntes', 'Tema7_Planteamientos.pdf')

build2.CSS += """
.plan { border: 2px solid #7209b9; border-radius: 6px; padding: 5px 8px 6px; margin: 8px 0 10px; background: #faf5ff; page-break-inside: avoid; }
.plan .pt { font-size: 8.5pt; font-weight: 700; color: #7209b9; letter-spacing: .4px; text-transform: uppercase; }
.plan .row { display: flex; flex-wrap: wrap; align-items: center; row-gap: 5px; margin: 4px 0; }
.plan .rl { width: 100%; font-size: 8.6pt; font-weight: 700; color: #0a5d0a; margin-top: 2px; }
.plan .b { border: 1.5px solid #09b909; background: #fff; border-radius: 4px; padding: 2px 6px; font-size: 9pt; line-height: 1.25; }
.plan .b.fin { background: #7209b9; border-color: #7209b9; color: #fff; font-weight: 700; }
.plan .a { display: inline-flex; flex-direction: column; align-items: stretch; margin: 0 11px 0 4px; color: #7209b9; min-width: 30px; }
.plan .a .l { font-size: 7.9pt; font-weight: 700; line-height: 1.1; white-space: nowrap; text-align: center; padding: 0 2px; }
.plan .a .ar { position: relative; height: 0; border-top: 2px solid #7209b9; margin: 3px 6px 3px 0; }
.plan .a .ar::after { content: ''; position: absolute; right: -7px; top: -6px; border-left: 8px solid #7209b9; border-top: 5px solid transparent; border-bottom: 5px solid transparent; }
.paso { font-weight: 700; color: #7209b9; margin: 8px 0 0; page-break-after: avoid; }
.res { border: 1.5px solid #09b909; background: #f2fbf2; border-radius: 4px; padding: 3px 10px; margin: 8px 0 4px; font-weight: 700; }
.tipo { font-size: 9pt; color: #555; margin: 6px 0 2px; }
.reac { margin: 4px 0 10px; page-break-inside: avoid; }
.reac .eq { display: block; background: #fff6dc; border-left: 5px solid #e0a100; border-radius: 4px; padding: 5px 12px; margin: 4px 0;
            font-size: 11.8pt; font-weight: 700; color: #1d1d1d; letter-spacing: .2px; }
.reac .nt { font-size: 9.2pt; color: #555; font-weight: 400; margin-left: 10px; }
.rx { background: #fff1c9; border-radius: 3px; padding: 0 4px; font-weight: 700; white-space: nowrap; }
"""

ARROW = re.compile(r'\s*--\[(.*?)\]-->\s*')
CODE = r'((?:EC|P|T)\s?7[.-][\d.]+)'
END = re.compile(r'\n(?=#{2,5} |<div class="newpage">)')


def plan_html(body, title='El planteamiento'):
    rows = []
    for line in body.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        label = ''
        if ' :: ' in line:
            label, line = line.split(' :: ', 1)
        parts = ARROW.split(line)
        out = [f'<div class="rl">{html.escape(label)}</div>'] if label else []
        for i, p in enumerate(parts):
            if i % 2 == 0:
                fin = p.startswith('!')
                out.append(f'<span class="b{" fin" if fin else ""}">{html.escape(p.lstrip("!").strip())}</span>')
            else:
                out.append(f'<span class="a"><span class="l">{html.escape(p)}</span><span class="ar"></span></span>')
        rows.append('<div class="row">' + ''.join(out) + '</div>')
    return f'\n\n<div class="plan"><div class="pt">{title}</div>{"".join(rows)}</div>\n\n'


def fichas(text):
    """código -> (inicio, fin) de cada ficha ##### en el texto"""
    out = {}
    for m in re.finditer(r'^##### ' + CODE + r' ', text, flags=re.M):
        e = END.search(text, m.end())
        out[m.group(1)] = (m.start(), e.start() if e else len(text))
    return out


def nueva(seg):
    """de una ficha nueva: tipo + plan, y la resolución (de ① al resultado)"""
    tipo = re.search(r'<p class="tipo">.*?</p>', seg)
    plan = re.search(r'\[\[PLAN\n.*?\n\]\]', seg, flags=re.S)
    res = re.search(r'^\*\*①.*', seg, flags=re.M | re.S)
    if not (plan and res):
        return None
    return ((tipo.group(0) + '\n\n' if tipo else '') + plan.group(0)), res.group(0).strip()


PRE_END = re.compile(r'^(\*\*Paso|\$\$\\text\{Paso\}|\*\*Na₂CO₃:\*\*|\*\*Sulfatos:\*\*|\*\*Fe \(volumetría\)\*\*)', re.M)
TAIL = re.compile(r'^(\*\*Lo que tienes que llevarte|\*\*Cifras|\*\*Resumen|\*\*Comprobación|\*\*Trampa|\*\*Por qué es buen|\*\*Neutra)', re.M)


def _es_ec(s):
    return '→' in s and '+' in s


def _b(s):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(s, quote=False))


def _caja_reac(items):
    out = []
    for it in items:
        segs = [s for s in re.findall(r'\*\*(.+?)\*\*', it) if _es_ec(s)]
        if segs:
            resto = re.sub(r'\*\*(.+?)\*\*', lambda m: '' if _es_ec(m.group(1)) else m.group(0), it).strip(' ·.:')
            for s in segs:
                out.append(f'<div class="eq">{html.escape(s, quote=False)}</div>')
            if resto and resto not in ('→',):
                out.append(f'<div class="nt">{_b(resto)}</div>')
        elif _es_ec(it):
            m = re.match(r'^(.*?)\s*(\((?:[^()]|\([^()]*\))*\))?\s*[.]?$', it)
            ec, nota = (m.group(1), m.group(2)) if m else (it, None)
            out.append(f'<div class="eq">{_b(ec).replace("<b>", "").replace("</b>", "")}</div>')
            if nota:
                out.append(f'<div class="nt">{_b(nota)}</div>')
        else:
            out.append(f'<div class="nt">{_b(it)}</div>')
    return '<div class="reac">' + ''.join(out) + '</div>'


def reacciones(text):
    """Saca las reacciones de los párrafos y las pone en recuadros, una por línea."""
    out = []
    lab = re.compile(r'^(\*\*(?:Reacci[oó]n(?:es)?(?: redox)?|Neutra|Reacción neutra)\*\*(?:\s*\([^)]*(?:\([^)]*\)[^)]*)*\))?:?|\*\*(?:Reacci[oó]n(?:es)?(?: redox)?|Neutra)[^*]*:\*\*)\s*(.*)$')
    for line in text.split('\n'):
        s = line.rstrip()
        m = lab.match(s)
        if m and m.group(2) and '→' in m.group(2):
            items = [i.strip() for i in m.group(2).split(' · ') if i.strip()]
            out += [m.group(1).rstrip(':') + ':', '', _caja_reac(items), '']
            continue
        m2 = re.match(r'^\s*\*\*([^*]+)\*\*\s*(→.*)?$', s)
        if m2 and _es_ec(m2.group(1)) and not s.lstrip().startswith('-'):
            out += ['', _caja_reac([s.strip()]), '']
            continue
        m3 = re.match(r'^- \*\*([^*]+)\*\*(.*)$', s)
        if m3 and _es_ec(m3.group(1)):
            out += ['', _caja_reac([s[2:].strip()]), '']
            continue
        # resto: resalto las ecuaciones en negrita dentro del texto
        if '$$' not in s and not s.lstrip().startswith(('<', '|', '[[')):
            s = re.sub(r'\*\*([^*]+)\*\*', lambda mm: f'<span class="rx">{html.escape(mm.group(1), quote=False)}</span>' if _es_ec(mm.group(1)) else mm.group(0), s)
        out.append(s)
    return '\n'.join(out)


def main():
    base = open(BASE, encoding='utf-8').read()
    # dibujos de laboratorio con el estilo nuevo (lab2.py / labspecs7_v2.py)
    import labspecs7_v2
    for k, s in labspecs7_v2.todos().items():
        fn = 'lab7v2_' + k.replace(' ', '_').replace('.', '_') + '.svg'
        open(os.path.join(H, 'img', fn), 'w', encoding='utf-8').write(s)
    base = base.replace('img/lab7_', 'img/lab7v2_')
    new_txt = '\n\n'.join(open(f, encoding='utf-8').read()
                          for f in sorted(glob.glob(os.path.join(SRC, '*.md'))) if not f.endswith(('00_intro.md', '05_explica.md')))
    exp = dict(re.findall(r'^@@ (.+?)\n(.+?)(?=\n\n@@ |\Z)', open(os.path.join(SRC, '05_explica.md'), encoding='utf-8').read(), flags=re.M | re.S))
    nf = fichas(new_txt)
    hechas = []
    for code, (a, b) in sorted(fichas(base).items(), key=lambda kv: -kv[1][0]):   # de atrás adelante
        if code not in nf:
            continue
        parts = nueva(new_txt[nf[code][0]:nf[code][1]])
        if not parts:
            continue
        seg = base[a:b]
        pe = PRE_END.search(seg)
        if not pe:
            print('sin pasos:', code); continue
        pre = re.sub(r'^\*\*Plan:\*\*.*\n?', '', seg[:pe.start()], flags=re.M).rstrip()
        tm = TAIL.search(seg, pe.start())
        tail = seg[tm.start():].strip() if tm else ''
        plan, res = parts
        if code in exp:
            plan = plan.replace('[[PLAN', '**Lo que vamos a hacer:** ' + exp[code].strip() + '\n\n[[PLAN', 1)
        else:
            print('sin explicación:', code)
        seg2 = f'{pre}\n\n{plan}\n\n{res}\n\n{tail}\n'
        base = base[:a] + seg2 + base[b:]
        hechas.append(code)
    print('fichas con flechas:', len(hechas))

    # portada, guion y la receta
    base = base.replace('# Tema 7 · Reacciones químicas\n', '# Tema 7 · Reacciones químicas\n\n### con el planteamiento en flechas de cada problema\n', 1)
    base = base.replace('4. **El plan**: en qué orden voy a ir de los datos al resultado.',
                        '4. **El planteamiento en flechas** (recuadro morado): en qué orden voy de los datos al resultado.')
    base = base.replace('5. **Los cálculos, uno por paso**, cada uno con **por qué** lo hago.',
                        '5. **Los cálculos, uno por flecha** (①, ②…), cada uno con **por qué** lo hago; si hay una x, la ecuación se construye pieza a pieza.')
    intro = open(os.path.join(SRC, '00_intro.md'), encoding='utf-8').read()
    k = base.index('<div class="newpage"></div>\n\n## 1.')
    base = base[:k] + intro + '\n\n' + base[k:]

    base = reacciones(base)
    text = re.sub(r'\[\[PLAN\n(.*?)\n\]\]', lambda m: plan_html(m.group(1)), base, flags=re.S)
    text = re.sub(r'^\*\*([①-⑳][^*]*)\*\*(.*)$',
                  lambda m: f'<p class="paso">{m.group(1)}<span style="font-weight:400;color:#111">{m.group(2)}</span></p>', text, flags=re.M)
    text = re.sub(r'^RESULTADO: (.*)$', lambda m: f'<div class="res" markdown="1">Resultado: {m.group(1)}</div>', text, flags=re.M)

    page = os.path.join(H, 'Tema7_Planteamientos.html')
    open(page, 'w', encoding='utf-8').write(build2.md_to_html(text, 'Tema 7 · Reacciones químicas'))
    os.makedirs(os.path.dirname(PDF), exist_ok=True)
    subprocess.run([build2.CHROME, *build2.CHROME_EXTRA, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    '--virtual-time-budget=30000', '--allow-file-access-from-files',
                    '--print-to-pdf=' + PDF, 'file:///' + page.replace('\\', '/')],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    doc = pymupdf.open(PDF)
    for i, pg in enumerate(doc):
        if i:
            pg.insert_text((pg.rect.width / 2 - 8, pg.rect.height - 18), str(i + 1), fontsize=8.5, color=(.35, .35, .35))
    tmp = PDF + '.tmp'
    doc.save(tmp, garbage=3, deflate=True); doc.close(); os.replace(tmp, PDF)
    print(PDF, pymupdf.open(PDF).page_count, 'páginas')


if __name__ == '__main__':
    main()
