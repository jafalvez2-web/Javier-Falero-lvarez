"""Tema 7 · Planteamientos: todos los problemas con el plan en flechas.

Fuentes: herramientas/fuentes_md/tema7_planteamientos/*.md (en orden alfabético).
Salida:  tema7/apuntes/Tema7_Planteamientos.pdf

Macro nueva [[PLAN ... ]]: cada línea es una fila de cajas unidas por flechas.
    caja --[① etiqueta de la flecha]--> caja --[② ...]--> !caja final
  - "Etiqueta :: caja --[..]--> caja" pone un título a la fila (ramas).
  - Una caja que empieza por "!" es el resultado (morada).
Al final se añade solo "Repaso rápido": el título y el plan de cada ficha.

Uso: python herramientas/build_t7_planteamientos.py
"""
import glob, html, os, re, subprocess, sys

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import build2, pymupdf

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
.plan .a .l { font-size: 7.9pt; font-weight: 700; line-height: 1.1; white-space: nowrap; }
.plan .a .ar { position: relative; height: 0; border-top: 2px solid #7209b9; margin: 3px 6px 3px 0; }
.plan .a .ar::after { content: ''; position: absolute; right: -7px; top: -6px; border-left: 8px solid #7209b9; border-top: 5px solid transparent; border-bottom: 5px solid transparent; }
.plan .a .l { text-align: center; padding: 0 2px; }
.paso { font-weight: 700; color: #7209b9; margin: 8px 0 0; page-break-after: avoid; }
.res { border: 1.5px solid #09b909; background: #f2fbf2; border-radius: 4px; padding: 3px 10px; margin: 8px 0 4px; font-weight: 700; }
.tipo { font-size: 9pt; color: #555; margin: 2px 0 4px; }
h5 { margin-top: 18px; }
"""

ARROW = re.compile(r'\s*--\[(.*?)\]-->\s*')


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
                txt = html.escape(p.lstrip('!').strip())
                out.append(f'<span class="b{" fin" if fin else ""}">{txt}</span>')
            else:
                out.append(f'<span class="a"><span class="l">{html.escape(p)}</span><span class="ar"></span></span>')
        rows.append('<div class="row">' + ''.join(out) + '</div>')
    return f'\n\n<div class="plan"><div class="pt">{title}</div>{"".join(rows)}</div>\n\n'


def main():
    parts = [open(f, encoding='utf-8').read() for f in sorted(glob.glob(os.path.join(SRC, '*.md')))]
    text = '\n\n'.join(parts)

    # Repaso rápido: título de cada ficha + su plan
    rep = ['<div class="newpage"></div>', '', '## Repaso rápido: todos los planteamientos', '',
           'Solo las flechas de cada problema, en el mismo orden. Tapa la resolución e intenta llegar al resultado con esto.', '']
    for m in re.finditer(r'^##### (.+?)$(.*?)(?=^#####|^## |\Z)', text, flags=re.M | re.S):
        p = re.search(r'\[\[PLAN\n(.*?)\n\]\]', m.group(2), flags=re.S)
        if p:
            rep += [f'##### {m.group(1)}', '', '[[PLAN\n' + p.group(1) + '\n]]', '']
    text += '\n\n' + '\n'.join(rep)

    text = re.sub(r'\[\[PLAN\n(.*?)\n\]\]', lambda m: plan_html(m.group(1)), text, flags=re.S)
    # **①** al principio de línea -> etiqueta de paso
    text = re.sub(r'^\*\*([①-⑳][^*]*)\*\*(.*)$', lambda m: f'<p class="paso">{m.group(1)}<span style="font-weight:400;color:#111">{m.group(2)}</span></p>', text, flags=re.M)
    text = re.sub(r'^RESULTADO: (.*)$', lambda m: f'<div class="res" markdown="1">Resultado: {m.group(1)}</div>', text, flags=re.M)

    page = os.path.join(H, 'Tema7_Planteamientos.html')
    open(page, 'w', encoding='utf-8').write(build2.md_to_html(text, 'Tema 7 · Planteamientos'))
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
