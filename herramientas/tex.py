"""Convierte las cuentas en línea ("a / b = c") en ecuaciones de bloque KaTeX con fracciones."""
import re, sys

SUP = {'⁻': '-', '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}
SUB = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9'}

def sup(s):
    return re.sub(r'[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+', lambda m: '^{' + ''.join(SUP[c] for c in m.group(0)) + '}', s)

def chem_text(w):
    # texto con subíndices/superíndices químicos -> \text{} con _{} y ^{}
    out = ''; buf = ''
    i = 0
    def flush():
        nonlocal buf, out
        if buf:
            b = buf.replace('⦅', '(').replace('⦆', ')').replace('%', r'\%').replace('÷', '/')
            out += r'\text{' + b + '}'
            buf = ''
    while i < len(w):
        c = w[i]
        if c in SUB:
            j = i
            while j < len(w) and w[j] in SUB: j += 1
            flush(); out += '_{' + ''.join(SUB[x] for x in w[i:j]) + '}'; i = j; continue
        if c in SUP or c in '⁺':
            j = i
            while j < len(w) and (w[j] in SUP or w[j] == '⁺'): j += 1
            s = ''.join('+' if x == '⁺' else SUP[x] for x in w[i:j])
            flush(); out += '^{' + s + '}'; i = j; continue
        buf += c; i += 1
    flush()
    return out

def term(s):
    """un término (sin '=' ni '/' de nivel superior) -> LaTeX"""
    s = s.strip()
    s = s.replace('**', '')
    # numeros: 1,234·10⁻⁴
    def num(m):
        n = m.group(1).replace(',', '{,}')
        e = m.group(2)
        if e:
            n += '\\cdot10^{' + ''.join(SUP[c] for c in e) + '}'
        return '\x00' + n + '\x01'
    s = re.sub(r'(\d+(?:,\d+)?)(?:·10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+))?', num, s)
    s = s.replace('·', ' \\cdot ').replace('×', ' \\times ').replace('−', '-')
    # trozos de texto (lo que no es número ni operador)
    parts = re.split(r'(\x00[^\x01]*\x01|\\cdot|\\times|[-+()\[\]])', s)
    out = ''
    for p in parts:
        if not p: continue
        if p.startswith('\x00'):
            if out.endswith('}') and not out.endswith('right)}'):
                out += '\\ '
            out += p[1:-1]
        elif p in ('\\cdot', '\\times', '-', '+', '(', ')', '[', ']'):
            out += {'(': '\\left(', ')': '\\right)', '[': '[', ']': ']'}.get(p, ' ' + p + ' ')
        else:
            t = p.strip()
            if t:
                lead = '\\ ' if p[:1] == ' ' and out and not out.endswith(' ') else ''
                out += lead + chem_text(t)
    return out

def split_top(s, sep):
    """divide por sep fuera de paréntesis"""
    depth = 0; parts = []; cur = ''
    i = 0
    while i < len(s):
        c = s[i]
        if c in '([': depth += 1
        if c in ')]': depth -= 1
        if depth == 0 and s.startswith(sep, i):
            parts.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    parts.append(cur)
    return parts

def expr(s):
    s = s.strip().replace('**', '')
    s = re.sub(r'(?<![\d,])(\d)/(\d)(?![\d,])', lambda m: m.group(1) + '÷' + m.group(2), s)
    for _ in range(3):
        s = re.sub(r'\(([^()\s]*[A-Za-zÀ-ÿ][^()\s]*)\)', lambda m: '⦅' + m.group(1) + '⦆' if not re.match(r'^\d', m.group(1)) else m.group(0), s)
    fr = []
    def paren(m):
        inner = m.group(1)
        if '/' in inner and re.search(r'mol|g|mL|L|comercial|aleación|mezcla|muestra|μg', inner):
            if ' / ' in inner: a, b = inner.split(' / ', 1)
            else: a, b = inner.split('/', 1)
            fr.append(r'\dfrac{' + term(a) + '}{' + term(b) + '}')
            return ' QQF' + chr(97 + len(fr) - 1) + 'QQ '
        return '(' + inner + ')'
    s = re.sub(r'\(([^()]*)\)', paren, s)
    if ' / ' not in s:
        s = re.sub(r'(\d,\d+(?:·10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?)/(\d)', lambda m: m.group(1) + ' / ' + m.group(2), s, count=1)
    pieces = split_top(s, ' / ')
    if len(pieces) == 2:
        den = split_top(pieces[1], ' · ')
        extra = ''
        if len(den) > 1:
            extra = r' \cdot ' + term(' · '.join(den[1:]))
        res = r'\dfrac{' + term(pieces[0]) + '}{' + term(den[0]) + '}' + extra
    else:
        res = term(s)
    for i, f in enumerate(fr):
        res = res.replace('QQF' + chr(97 + i) + 'QQ', '}' + f + r'\text{')
    res = res.replace(r'\text{}', '').replace(r'\text{ }', '')
    return res

def equation(s):
    segs = split_top(s, ' = ')
    return ' = '.join(expr(x) for x in segs)

if __name__ == '__main__':
    for s in sys.argv[1:]:
        print(equation(s))
