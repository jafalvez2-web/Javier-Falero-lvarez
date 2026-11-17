import re, sys
sys.path.insert(0, __file__.rsplit('\\', 1)[0] if '\\' in __file__ else '.')
from tex import equation

UNIT = re.compile(r'\b(mol|g|L|mL|M|ppm|μg|mg|atm)\b|%|g/mol')
VARSTART = re.compile(r'^(n|m|V|M|%|ppm|\[|Cl/Fe|H₂O/Fe|O/Fe|Δm|ppm)')

def is_calc(seg):
    return ' = ' in seg and re.search(r'\d', seg) and UNIT.search(seg) and ('/' in seg or '·' in seg or '×' in seg or ' − ' in seg or ' + ' in seg)

def convert_line(line):
    raw = line
    bullet = ''
    m = re.match(r'^(\s*-\s+)(.*)$', line)
    if m: bullet, line = m.group(1), m.group(2)
    label = ''
    m = re.match(r'^(\*\*[^*]+\*\*)\s*(.*)$', line)
    if m:
        label, line = m.group(1), m.group(2)
    if label.startswith(('**Datos', '**Reacci', '**Ajuste', '**Electrones', '**Camino', '**¿Qué', '**Lo que', '**Comprobación', '**Neutra', '**Igualar', '**Semirreacci', '**Oxidaci', '**Reducci', '**A especies', '**Trampa', '**Cifras', '**Resumen', '**Plan', '**Cómo', '**Se repite', '**Atajos', '**Por qué', '**Ojo')):
        return [raw]
    segs = [s.strip() for s in line.split(' → ')]
    if not any(is_calc(s) for s in segs):
        mf = re.match(r'^(.*?)([A-Za-z][A-Za-z()₀-₉\[\]]{0,6} = [A-Za-z ·/()%,0-9.]+)$', line)
        if label and mf and not re.search(r'\d,\d', mf.group(2)) and len(mf.group(2)) < 40:
            res = [(bullet + label + ' ' + mf.group(1)).strip(), '', '$$' + equation(mf.group(2).replace(' · ', ' · ')) + '$$', '']
            return res
        return [raw]
    out = []
    head = ''
    pieces = []
    for s in segs:
        if is_calc(s):
            # texto antes del cálculo (hasta ': ' o una frase)
            lab = ''
            mm = re.match(r'^(.*?:\s)(?=[^:]*= )', s)
            if mm and not re.search(r'\d\s*$', mm.group(1)):
                lab, s = mm.group(1).strip(), s[mm.end():]
            # comentario final entre paréntesis sin cuentas
            tail = ''
            mt = re.search(r'\s(\([^()]*\))\s*$', s)
            if mt and not UNIT.search(mt.group(1).replace('mol', '')) or (mt and re.search(r'cifras|estricta|volumen|densidad|el agua|errata|alícuota|1 g =|5 por|2 Mg|1 SO|2 OH|3 OH|1 Cu|1 : 1|×', mt.group(1))):
                tail = mt.group(1); s = s[:mt.start()]
            s = re.sub(r'\*\*', '', s)
            pieces.append(('calc', lab, s.strip(), tail))
        else:
            pieces.append(('text', s, '', ''))
    lines = []
    first_text = (bullet.strip() + ' ' if bullet else '') + label
    if first_text.strip():
        lines.append(first_text.strip().lstrip('- ').strip())
    for kind, a, b, tail in pieces:
        if kind == 'text':
            lines.append('→ ' + a if lines else a)
        else:
            if a: lines.append(a)
            try:
                eq = equation(b)
            except Exception as e:
                return [raw]
            lines.append('$$' + eq + '$$')
            if tail: lines.append(tail)
    # montar: párrafos separados
    res = []
    for l in lines:
        res.append(l); res.append('')
    return res

def process(path):
    t = open(path, encoding='utf-8').read().split('\n')
    out = []
    inenun = False
    for l in t:
        s = l.strip()
        if s.startswith('<div class="enun"'): inenun = True
        if inenun:
            out.append(l)
            if s == '</div>': inenun = False
            continue
        if s.startswith(('#', '|', '[[', '$$', '<', '>')) or not s:
            out.append(l); continue
        out.extend(convert_line(l))
    return '\n'.join(out)

if __name__ == '__main__':
    for p in sys.argv[1:]:
        open(p.replace('.md', '_tex.md'), 'w', encoding='utf-8').write(process(p))
        print('ok', p)
