"""Genera 62_ajustes.md: el ajuste redox DESDE CERO de cada problema del apartado 6 del Tema 7.

Javier pidió (nov. 2026) que en cada ejercicio de redox se ajuste la reacción poco a poco,
porque el enunciado solo da las parejas (MnO₄⁻ → Mn²⁺, ...) y la ecuación ajustada es parte
de la solución del profesor. Cada semirreacción se define una vez (con sus pasos) y se
comprueba automáticamente que todas las ecuaciones finales están ajustadas (átomos y carga).

Uso: python gen_ajustes.py   (escribe 62_ajustes.md en esta carpeta)
"""
import os, re
from collections import Counter

# ---------------------------------------------------------------- comprobador
SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
SUP = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}


def _especie(s):
    s = s.strip()
    m = re.match(r'^(\d+(?:/\d+)?)\s+(.*)$', s)
    coef = 1.0
    if m:
        a = m.group(1)
        coef = eval(a.replace('/', '/')) if '/' in a else float(a)
        s = m.group(2)
    if s in ('e⁻', 'e-'):
        return coef, Counter(), -1
    carga = 0
    mm = re.search(r'([⁰¹²³⁴⁵⁶⁷⁸⁹]*)([⁺⁻])$', s)
    if mm:
        n = int(''.join(SUP[c] for c in mm.group(1)) or 1)
        carga = n if mm.group(2) == '⁺' else -n
        s = s[:mm.start()]
    s = s.translate(SUB).replace('↓', '').replace('↑', '')

    def parse(f, i=0):
        c = Counter()
        while i < len(f):
            if f[i] == '(':
                sub, i = parse(f, i + 1)
                m2 = re.match(r'\d+', f[i:])
                k = int(m2.group()) if m2 else 1
                i += len(m2.group()) if m2 else 0
                for e, v in sub.items():
                    c[e] += v * k
            elif f[i] == ')':
                return c, i + 1
            else:
                m2 = re.match(r'([A-Z][a-z]?)(\d*)', f[i:])
                c[m2.group(1)] += int(m2.group(2) or 1)
                i += len(m2.group())
        return c, i
    at, _ = parse(s)
    return coef, at, carga


def ajustada(ec):
    izq, der = ec.split('→')
    def lado(t):
        A, Q = Counter(), 0.0
        for p in t.split(' + '):
            if not p.strip():
                continue
            c, at, q = _especie(p)
            for e, v in at.items():
                A[e] += c * v
            Q += c * q
        return A, Q
    a1, q1 = lado(izq)
    a2, q2 = lado(der)
    return all(abs(a1[e] - a2[e]) < 1e-9 for e in set(a1) | set(a2)) and abs(q1 - q2) < 1e-9


# ---------------------------------------------------------------- semirreacciones
# Cada una: (qué cambia, cómo se calcula el estado de oxidación, pasos [(qué hago, ecuación)], final, e⁻)
H = {}
H['MnO4'] = dict(
    tipo='red', que='MnO₄⁻ → Mn²⁺',
    eo='En el MnO₄⁻: los 4 O valen 4·(−2) = −8 y la carga total es −1, así que Mn − 8 = −1 → **Mn = +7**. En el Mn²⁺, **Mn = +2**. Baja de +7 a +2: **gana 5 e⁻, se reduce** (es el oxidante).',
    pasos=[('Ajusto el Mn (1 a cada lado, ya está)', 'MnO₄⁻ → Mn²⁺'),
           ('Ajusto el O con H₂O: hay 4 O a la izquierda → 4 H₂O a la derecha', 'MnO₄⁻ → Mn²⁺ + 4 H₂O'),
           ('Ajusto el H con H⁺: ahora hay 8 H a la derecha → 8 H⁺ a la izquierda', 'MnO₄⁻ + 8 H⁺ → Mn²⁺ + 4 H₂O'),
           ('Ajusto la carga con e⁻: izquierda −1 + 8 = +7; derecha +2. Para que la izquierda baje a +2 añado 5 e⁻ a la izquierda', None)],
    fin='MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O', e=5)
H['Cr2O7'] = dict(
    tipo='red', que='Cr₂O₇²⁻ → Cr³⁺',
    eo='En el Cr₂O₇²⁻: 7 O valen −14 y la carga es −2, así que 2 Cr = +12 → **Cr = +6**. En el Cr³⁺, **Cr = +3**. Cada Cr gana 3 e⁻, y hay 2 Cr: **gana 6 e⁻, se reduce** (es el oxidante).',
    pasos=[('Ajusto el Cr: hay 2 a la izquierda → 2 Cr³⁺', 'Cr₂O₇²⁻ → 2 Cr³⁺'),
           ('Ajusto el O con H₂O: 7 O a la izquierda → 7 H₂O a la derecha', 'Cr₂O₇²⁻ → 2 Cr³⁺ + 7 H₂O'),
           ('Ajusto el H con H⁺: 14 H a la derecha → 14 H⁺ a la izquierda', 'Cr₂O₇²⁻ + 14 H⁺ → 2 Cr³⁺ + 7 H₂O'),
           ('Ajusto la carga con e⁻: izquierda −2 + 14 = +12; derecha 2·(+3) = +6. Añado 6 e⁻ a la izquierda', None)],
    fin='Cr₂O₇²⁻ + 14 H⁺ + 6 e⁻ → 2 Cr³⁺ + 7 H₂O', e=6)
H['IO3_I2'] = dict(
    tipo='red', que='IO₃⁻ → I₂',
    eo='En el IO₃⁻: 3 O valen −6 y la carga es −1 → **I = +5**. En el I₂ (elemento) **I = 0**. Cada I gana 5 e⁻ y el I₂ tiene 2 I: **gana 10 e⁻, se reduce**.',
    pasos=[('Ajusto el I: el I₂ tiene 2 I → 2 IO₃⁻', '2 IO₃⁻ → I₂'),
           ('Ajusto el O con H₂O: 6 O a la izquierda → 6 H₂O a la derecha', '2 IO₃⁻ → I₂ + 6 H₂O'),
           ('Ajusto el H con H⁺: 12 H a la derecha → 12 H⁺ a la izquierda', '2 IO₃⁻ + 12 H⁺ → I₂ + 6 H₂O'),
           ('Ajusto la carga con e⁻: izquierda −2 + 12 = +10; derecha 0. Añado 10 e⁻ a la izquierda', None)],
    fin='2 IO₃⁻ + 12 H⁺ + 10 e⁻ → I₂ + 6 H₂O', e=10)
H['H2O2_red'] = dict(
    tipo='red', que='H₂O₂ → H₂O',
    eo='En el H₂O₂ (peróxido): 2 H valen +2 y es neutro, así que 2 O = −2 → **O = −1**. En el H₂O, **O = −2**. Cada O gana 1 e⁻ y hay 2: **gana 2 e⁻, se reduce** (aquí el H₂O₂ es el oxidante).',
    pasos=[('Ajusto el O con H₂O: el H₂O₂ tiene 2 O → 2 H₂O', 'H₂O₂ → 2 H₂O'),
           ('Ajusto el H con H⁺: izquierda 2 H, derecha 4 H → 2 H⁺ a la izquierda', 'H₂O₂ + 2 H⁺ → 2 H₂O'),
           ('Ajusto la carga con e⁻: izquierda +2; derecha 0. Añado 2 e⁻ a la izquierda', None)],
    fin='H₂O₂ + 2 H⁺ + 2 e⁻ → 2 H₂O', e=2)
H['NO3'] = dict(
    tipo='red', que='NO₃⁻ → NO₂',
    eo='En el NO₃⁻: 3 O valen −6 y la carga es −1 → **N = +5**. En el NO₂: 2 O valen −4 → **N = +4**. **Gana 1 e⁻, se reduce** (el HNO₃ es el oxidante).',
    pasos=[('El N ya está ajustado (1 y 1)', 'NO₃⁻ → NO₂'),
           ('Ajusto el O con H₂O: 3 O a la izquierda y 2 a la derecha → 1 H₂O a la derecha', 'NO₃⁻ → NO₂ + H₂O'),
           ('Ajusto el H con H⁺: 2 H a la derecha → 2 H⁺ a la izquierda', 'NO₃⁻ + 2 H⁺ → NO₂ + H₂O'),
           ('Ajusto la carga con e⁻: izquierda −1 + 2 = +1; derecha 0. Añado 1 e⁻ a la izquierda', None)],
    fin='NO₃⁻ + 2 H⁺ + e⁻ → NO₂ + H₂O', e=1)
H['MnO2'] = dict(
    tipo='red', que='MnO₂ → Mn²⁺',
    eo='En el MnO₂: 2 O valen −4 y es neutro → **Mn = +4**. En el Mn²⁺, **Mn = +2**. **Gana 2 e⁻, se reduce**.',
    pasos=[('El Mn ya está ajustado', 'MnO₂ → Mn²⁺'),
           ('Ajusto el O con H₂O: 2 O a la izquierda → 2 H₂O a la derecha', 'MnO₂ → Mn²⁺ + 2 H₂O'),
           ('Ajusto el H con H⁺: 4 H a la derecha → 4 H⁺ a la izquierda', 'MnO₂ + 4 H⁺ → Mn²⁺ + 2 H₂O'),
           ('Ajusto la carga con e⁻: izquierda +4; derecha +2. Añado 2 e⁻ a la izquierda', None)],
    fin='MnO₂ + 4 H⁺ + 2 e⁻ → Mn²⁺ + 2 H₂O', e=2)
H['CrO4'] = dict(
    tipo='red', que='CrO₄²⁻ → Cr(OH)₃',
    eo='En el CrO₄²⁻: 4 O valen −8 y la carga es −2 → **Cr = +6**. En el Cr(OH)₃: 3 OH valen −3 → **Cr = +3**. **Gana 3 e⁻, se reduce**.',
    pasos=[('El Cr ya está ajustado', 'CrO₄²⁻ → Cr(OH)₃'),
           ('Ajusto el O con H₂O: 4 O a la izquierda y 3 a la derecha → 1 H₂O a la derecha', 'CrO₄²⁻ → Cr(OH)₃ + H₂O'),
           ('Ajusto el H con H⁺: a la derecha hay 3 + 2 = 5 H → 5 H⁺ a la izquierda', 'CrO₄²⁻ + 5 H⁺ → Cr(OH)₃ + H₂O'),
           ('Ajusto la carga con e⁻: izquierda −2 + 5 = +3; derecha 0. Añado 3 e⁻ a la izquierda', None)],
    fin='CrO₄²⁻ + 5 H⁺ + 3 e⁻ → Cr(OH)₃ + H₂O', e=3)
H['Ce'] = dict(
    tipo='red', que='Ce⁴⁺ → Ce³⁺',
    eo='El Ce pasa de **+4 a +3**: **gana 1 e⁻, se reduce** (es el oxidante). No hay O ni H que ajustar.',
    pasos=[('Solo ajusto la carga: izquierda +4, derecha +3 → 1 e⁻ a la izquierda', None)],
    fin='Ce⁴⁺ + e⁻ → Ce³⁺', e=1)
H['Cu_CuI'] = dict(
    tipo='red', que='Cu²⁺ → CuI',
    eo='El Cu pasa de **+2 (Cu²⁺) a +1 (en el CuI, porque el I⁻ vale −1)**: **gana 1 e⁻, se reduce**. El I⁻ que entra en el CuI no cambia (sigue en −1); solo hace falta para formar el sólido.',
    pasos=[('Ajusto los átomos: el CuI necesita 1 I⁻', 'Cu²⁺ + I⁻ → CuI'),
           ('Ajusto la carga: izquierda +2 − 1 = +1; derecha 0. Añado 1 e⁻ a la izquierda', None)],
    fin='Cu²⁺ + I⁻ + e⁻ → CuI', e=1)
H['I2_red'] = dict(
    tipo='red', que='I₂ → I⁻',
    eo='El I pasa de **0 (I₂) a −1 (I⁻)**. Hay 2 I: **gana 2 e⁻, se reduce**.',
    pasos=[('Ajusto el I: 2 I⁻', 'I₂ → 2 I⁻'),
           ('Ajusto la carga: izquierda 0; derecha −2. Añado 2 e⁻ a la izquierda', None)],
    fin='I₂ + 2 e⁻ → 2 I⁻', e=2)
# ---- oxidaciones
H['Fe'] = dict(
    tipo='ox', que='Fe²⁺ → Fe³⁺',
    eo='El Fe pasa de **+2 a +3**: **pierde 1 e⁻, se oxida** (es el reductor).',
    pasos=[('Solo ajusto la carga: izquierda +2, derecha +3 → 1 e⁻ a la derecha', None)],
    fin='Fe²⁺ → Fe³⁺ + e⁻', e=1)
H['H2C2O4'] = dict(
    tipo='ox', que='H₂C₂O₄ → CO₂',
    eo='En el H₂C₂O₄: 2 H valen +2 y 4 O valen −8; es neutro, así que 2 C = +6 → **C = +3**. En el CO₂, **C = +4**. Cada C pierde 1 e⁻ y hay 2 C: **pierde 2 e⁻, se oxida** (es el reductor).',
    pasos=[('Ajusto el C: 2 C → 2 CO₂', 'H₂C₂O₄ → 2 CO₂'),
           ('El O ya cuadra (4 y 4). Ajusto el H con H⁺: 2 H a la izquierda → 2 H⁺ a la derecha', 'H₂C₂O₄ → 2 CO₂ + 2 H⁺'),
           ('Ajusto la carga con e⁻: izquierda 0; derecha +2. Añado 2 e⁻ a la derecha', None)],
    fin='H₂C₂O₄ → 2 CO₂ + 2 H⁺ + 2 e⁻', e=2)
H['C2O4'] = dict(
    tipo='ox', que='C₂O₄²⁻ → CO₂',
    eo='En el C₂O₄²⁻: 4 O valen −8 y la carga es −2 → 2 C = +6 → **C = +3**. En el CO₂, **C = +4**. Hay 2 C: **pierde 2 e⁻, se oxida** (es el reductor).',
    pasos=[('Ajusto el C: 2 CO₂. El O ya cuadra (4 y 4)', 'C₂O₄²⁻ → 2 CO₂'),
           ('Ajusto la carga con e⁻: izquierda −2; derecha 0. Añado 2 e⁻ a la derecha', None)],
    fin='C₂O₄²⁻ → 2 CO₂ + 2 e⁻', e=2)
H['H2O2_ox'] = dict(
    tipo='ox', que='H₂O₂ → O₂',
    eo='En el H₂O₂, **O = −1** (es un peróxido). En el O₂ (elemento), **O = 0**. Hay 2 O: **pierde 2 e⁻, se oxida** (aquí el H₂O₂ es el reductor).',
    pasos=[('El O ya está ajustado (2 y 2)', 'H₂O₂ → O₂'),
           ('Ajusto el H con H⁺: 2 H a la izquierda → 2 H⁺ a la derecha', 'H₂O₂ → O₂ + 2 H⁺'),
           ('Ajusto la carga: izquierda 0; derecha +2. Añado 2 e⁻ a la derecha', None)],
    fin='H₂O₂ → O₂ + 2 H⁺ + 2 e⁻', e=2)
H['N2H4'] = dict(
    tipo='ox', que='N₂H₄ → N₂',
    eo='En el N₂H₄: 4 H valen +4 y es neutro, así que 2 N = −4 → **N = −2**. En el N₂, **N = 0**. Cada N pierde 2 e⁻ y hay 2: **pierde 4 e⁻, se oxida**.',
    pasos=[('El N ya está ajustado (2 y 2). No hay O. Ajusto el H con H⁺: 4 H a la izquierda → 4 H⁺ a la derecha', 'N₂H₄ → N₂ + 4 H⁺'),
           ('Ajusto la carga: izquierda 0; derecha +4. Añado 4 e⁻ a la derecha', None)],
    fin='N₂H₄ → N₂ + 4 H⁺ + 4 e⁻', e=4)
H['S2O4'] = dict(
    tipo='ox', que='S₂O₄²⁻ → SO₃²⁻',
    eo='En el S₂O₄²⁻: 4 O valen −8 y la carga es −2 → 2 S = +6 → **S = +3**. En el SO₃²⁻: 3 O valen −6 y la carga es −2 → **S = +4**. Hay 2 S: **pierde 2 e⁻, se oxida**.',
    pasos=[('Ajusto el S: 2 S → 2 SO₃²⁻', 'S₂O₄²⁻ → 2 SO₃²⁻'),
           ('Ajusto el O con H₂O: 4 O a la izquierda y 6 a la derecha → 2 H₂O a la izquierda', 'S₂O₄²⁻ + 2 H₂O → 2 SO₃²⁻'),
           ('Ajusto el H con H⁺: 4 H a la izquierda → 4 H⁺ a la derecha', 'S₂O₄²⁻ + 2 H₂O → 2 SO₃²⁻ + 4 H⁺'),
           ('Ajusto la carga: izquierda −2; derecha −4 + 4 = 0. Añado 2 e⁻ a la derecha', None)],
    fin='S₂O₄²⁻ + 2 H₂O → 2 SO₃²⁻ + 4 H⁺ + 2 e⁻', e=2)
H['SO3'] = dict(
    tipo='ox', que='SO₃²⁻ → SO₄²⁻',
    eo='En el SO₃²⁻: **S = +4**. En el SO₄²⁻: 4 O valen −8 y la carga es −2 → **S = +6**. **Pierde 2 e⁻, se oxida**.',
    pasos=[('El S ya está ajustado', 'SO₃²⁻ → SO₄²⁻'),
           ('Ajusto el O con H₂O: 3 O a la izquierda y 4 a la derecha → 1 H₂O a la izquierda', 'SO₃²⁻ + H₂O → SO₄²⁻'),
           ('Ajusto el H con H⁺: 2 H a la izquierda → 2 H⁺ a la derecha', 'SO₃²⁻ + H₂O → SO₄²⁻ + 2 H⁺'),
           ('Ajusto la carga: izquierda −2; derecha −2 + 2 = 0. Añado 2 e⁻ a la derecha', None)],
    fin='SO₃²⁻ + H₂O → SO₄²⁻ + 2 H⁺ + 2 e⁻', e=2)
H['SO2'] = dict(
    tipo='ox', que='SO₂ → SO₄²⁻',
    eo='En el SO₂: 2 O valen −4 y es neutro → **S = +4**. En el SO₄²⁻, **S = +6**. **Pierde 2 e⁻, se oxida**.',
    pasos=[('El S ya está ajustado', 'SO₂ → SO₄²⁻'),
           ('Ajusto el O con H₂O: 2 O a la izquierda y 4 a la derecha → 2 H₂O a la izquierda', 'SO₂ + 2 H₂O → SO₄²⁻'),
           ('Ajusto el H con H⁺: 4 H a la izquierda → 4 H⁺ a la derecha', 'SO₂ + 2 H₂O → SO₄²⁻ + 4 H⁺'),
           ('Ajusto la carga: izquierda 0; derecha −2 + 4 = +2. Añado 2 e⁻ a la derecha', None)],
    fin='SO₂ + 2 H₂O → SO₄²⁻ + 4 H⁺ + 2 e⁻', e=2)
H['AsH3'] = dict(
    tipo='ox', que='AsH₃ → AsO₄³⁻',
    eo='En el AsH₃: 3 H valen +3 y es neutro → **As = −3**. En el AsO₄³⁻: 4 O valen −8 y la carga es −3 → **As = +5**. Sube de −3 a +5: **pierde 8 e⁻, se oxida**.',
    pasos=[('El As ya está ajustado', 'AsH₃ → AsO₄³⁻'),
           ('Ajusto el O con H₂O: 4 O a la derecha → 4 H₂O a la izquierda', 'AsH₃ + 4 H₂O → AsO₄³⁻'),
           ('Ajusto el H con H⁺: a la izquierda hay 3 + 8 = 11 H → 11 H⁺ a la derecha', 'AsH₃ + 4 H₂O → AsO₄³⁻ + 11 H⁺'),
           ('Ajusto la carga: izquierda 0; derecha −3 + 11 = +8. Añado 8 e⁻ a la derecha', None)],
    fin='AsH₃ + 4 H₂O → AsO₄³⁻ + 11 H⁺ + 8 e⁻', e=8)
H['Sn'] = dict(
    tipo='ox', que='Sn → SnO₂',
    eo='El Sn metálico (elemento) tiene **Sn = 0**. En el SnO₂: 2 O valen −4 → **Sn = +4**. **Pierde 4 e⁻, se oxida**.',
    pasos=[('El Sn ya está ajustado', 'Sn → SnO₂'),
           ('Ajusto el O con H₂O: 2 O a la derecha → 2 H₂O a la izquierda', 'Sn + 2 H₂O → SnO₂'),
           ('Ajusto el H con H⁺: 4 H a la izquierda → 4 H⁺ a la derecha', 'Sn + 2 H₂O → SnO₂ + 4 H⁺'),
           ('Ajusto la carga: izquierda 0; derecha +4. Añado 4 e⁻ a la derecha', None)],
    fin='Sn + 2 H₂O → SnO₂ + 4 H⁺ + 4 e⁻', e=4)
H['Cu'] = dict(
    tipo='ox', que='Cu → Cu²⁺',
    eo='El Cu metálico tiene **Cu = 0**; en el Cu(NO₃)₂ está como **Cu²⁺ (+2)**. **Pierde 2 e⁻, se oxida**.',
    pasos=[('Solo ajusto la carga: izquierda 0, derecha +2 → 2 e⁻ a la derecha', None)],
    fin='Cu → Cu²⁺ + 2 e⁻', e=2)
H['I_I2'] = dict(
    tipo='ox', que='I⁻ → I₂',
    eo='El I pasa de **−1 (I⁻) a 0 (I₂)**. Para formar 1 I₂ hacen falta 2 I⁻: **pierden 2 e⁻, se oxidan**.',
    pasos=[('Ajusto el I: 2 I⁻ → I₂', '2 I⁻ → I₂'),
           ('Ajusto la carga: izquierda −2; derecha 0. Añado 2 e⁻ a la derecha', None)],
    fin='2 I⁻ → I₂ + 2 e⁻', e=2)
H['I_ICl'] = dict(
    tipo='ox', que='I⁻ → ICl',
    eo='En el I⁻, **I = −1**. En el ICl el Cl (más electronegativo) vale −1, así que **I = +1**. Sube de −1 a +1: **pierde 2 e⁻, se oxida**. El Cl⁻ lo pone el HCl del medio y no cambia (sigue en −1).',
    pasos=[('Ajusto los átomos: el ICl necesita 1 Cl⁻', 'I⁻ + Cl⁻ → ICl'),
           ('Ajusto la carga: izquierda −2; derecha 0. Añado 2 e⁻ a la derecha', None)],
    fin='I⁻ + Cl⁻ → ICl + 2 e⁻', e=2)
H['S2O3'] = dict(
    tipo='ox', que='S₂O₃²⁻ → S₄O₆²⁻',
    eo='En el S₂O₃²⁻: 3 O valen −6 y la carga es −2 → 2 S = +4 → **S = +2** (de media). En el S₄O₆²⁻: 6 O valen −12 y la carga es −2 → 4 S = +10 → **S = +2,5** (de media). Hay que juntar 2 S₂O₃²⁻ para formar 1 S₄O₆²⁻, y entre los dos **pierden 2 e⁻: se oxidan**.',
    pasos=[('Ajusto el S: el S₄O₆²⁻ tiene 4 S → 2 S₂O₃²⁻. El O ya cuadra (6 y 6)', '2 S₂O₃²⁻ → S₄O₆²⁻'),
           ('Ajusto la carga: izquierda −4; derecha −2. Añado 2 e⁻ a la derecha', None)],
    fin='2 S₂O₃²⁻ → S₄O₆²⁻ + 2 e⁻', e=2)


def mult(ec, k):
    """multiplica una ecuación por k (entero) en el texto"""
    if k == 1:
        return ec
    out = []
    for lado in ec.split(' → '):
        ps = []
        for p in lado.split(' + '):
            m = re.match(r'^(\d+)\s+(.*)$', p)
            c = int(m.group(1)) if m else 1
            ps.append(f'{c*k} {m.group(2) if m else p}')
        out.append(' + '.join(ps))
    return ' → '.join(out)


def semi(h, k=1):
    d = H[h]
    titulo = 'Semirreacción de **reducción**' if d['tipo'] == 'red' else 'Semirreacción de **oxidación**'
    L = [f'*{titulo}: {d["que"]}*', '', f'- Estados de oxidación: {d["eo"]}']
    for qh, ec in d['pasos']:
        L.append(f'- {qh}' + (f': {ec}' if ec else '.'))
    L += ['', f'**{d["fin"]}**', '']
    assert ajustada(d['fin']), d['fin']
    return L


# ---------------------------------------------------------------- reacciones de cada problema
def redox(da, red, ox, kr, ko, suma, final, extra=(), rel=''):
    """da: lo que dice el enunciado; red/ox: claves; kr/ko: multiplicadores; suma: suma sin simplificar;
    final: iónica simplificada; extra: [(texto, ecuación)] (neutras, básico...); rel: relación que uso"""
    er, eo = H[red]['e'], H[ox]['e']
    assert er * kr == eo * ko, (red, ox)
    L = [f'**Qué me da el enunciado:** {da}', '']
    L += semi(red) + semi(ox)
    mcm = er * kr
    L.append(f'*Igualo los electrones:* la reducción gana {er} e⁻ y la oxidación pierde {eo} e⁻. '
             + (f'Ya son iguales, así que sumo tal cual.' if kr == ko == 1 else
                f'Para que sean los mismos ({mcm} e⁻) multiplico la reducción × {kr} y la oxidación × {ko}:'))
    L.append('')
    if not (kr == ko == 1):
        L += [f'- {mult(H[red]["fin"], kr)}', f'- {mult(H[ox]["fin"], ko)}', '']
    L.append(f'*Sumo y tacho los {mcm} e⁻' + (' (y junto o tacho lo que sale repetido a los dos lados)' if suma != final else '') + ':*')
    L.append('')
    if suma != final:
        L += [f'- Sin simplificar: {suma}', '']
    L += [f'**{final}**', '']
    assert ajustada(final), final
    for t, ec in extra:
        L.append(f'*{t}*')
        L.append('')
        if ec:
            assert ajustada(ec), ec
            L += [f'**{ec}**', '']
    L.append(f'*Compruebo:* átomos y cargas iguales a los dos lados ✓')
    L.append('')
    if rel:
        L += [f'> **Relación que voy a usar:** {rel}', '']
    return L


def simple(titulo, ec, nota=''):
    assert ajustada(ec), ec
    return [f'*{titulo}*', '', f'**{ec}**', ''] + ([nota, ''] if nota else [])


P = {}
MnOx = lambda da, neutra=None, rel='2 MnO₄⁻ por cada 5 oxálicos': redox(
    da, 'MnO4', 'H2C2O4', 2, 5,
    '2 MnO₄⁻ + 16 H⁺ + 5 H₂C₂O₄ → 2 Mn²⁺ + 8 H₂O + 10 CO₂ + 10 H⁺',
    '2 MnO₄⁻ + 5 H₂C₂O₄ + 6 H⁺ → 2 Mn²⁺ + 10 CO₂ + 8 H₂O',
    neutra or [], rel)
NEUTRA_MNOX = [('A especies neutras: el MnO₄⁻ va como KMnO₄ (añado 2 K⁺) y los 6 H⁺ los pone el H₂SO₄ (añado 3 SO₄²⁻). Pongo los mismos iones a los dos lados: a la derecha quedan 2 K⁺ + 2 Mn²⁺ + 3 SO₄²⁻ = K₂SO₄ + 2 MnSO₄',
                '2 KMnO₄ + 5 H₂C₂O₄ + 3 H₂SO₄ → K₂SO₄ + 2 MnSO₄ + 10 CO₂ + 8 H₂O')]
MnC2O4 = lambda da, rel='2 MnO₄⁻ por cada 5 oxalatos': redox(
    da, 'MnO4', 'C2O4', 2, 5,
    '2 MnO₄⁻ + 16 H⁺ + 5 C₂O₄²⁻ → 2 Mn²⁺ + 8 H₂O + 10 CO₂',
    '2 MnO₄⁻ + 5 C₂O₄²⁻ + 16 H⁺ → 2 Mn²⁺ + 10 CO₂ + 8 H₂O', [], rel)
MnH2O2 = lambda da, neutra=None: redox(
    da, 'MnO4', 'H2O2_ox', 2, 5,
    '2 MnO₄⁻ + 16 H⁺ + 5 H₂O₂ → 2 Mn²⁺ + 8 H₂O + 5 O₂ + 10 H⁺',
    '2 MnO₄⁻ + 5 H₂O₂ + 6 H⁺ → 2 Mn²⁺ + 5 O₂ + 8 H₂O', neutra or [], '2 MnO₄⁻ por cada 5 H₂O₂')
NEUTRA_MNH2O2 = [('A especies neutras: añado 2 K⁺ (KMnO₄) y 3 SO₄²⁻ (los 6 H⁺ vienen del H₂SO₄) a los dos lados',
                  '2 KMnO₄ + 5 H₂O₂ + 3 H₂SO₄ → K₂SO₄ + 2 MnSO₄ + 5 O₂ + 8 H₂O')]
CrFe = lambda da, neutra=None: redox(
    da, 'Cr2O7', 'Fe', 1, 6,
    'Cr₂O₇²⁻ + 14 H⁺ + 6 Fe²⁺ → 2 Cr³⁺ + 7 H₂O + 6 Fe³⁺',
    'Cr₂O₇²⁻ + 6 Fe²⁺ + 14 H⁺ → 2 Cr³⁺ + 6 Fe³⁺ + 7 H₂O', neutra or [], '1 Cr₂O₇²⁻ por cada 6 Fe²⁺')
MnFe = lambda da: redox(
    da, 'MnO4', 'Fe', 1, 5,
    'MnO₄⁻ + 8 H⁺ + 5 Fe²⁺ → Mn²⁺ + 4 H₂O + 5 Fe³⁺',
    'MnO₄⁻ + 5 Fe²⁺ + 8 H⁺ → Mn²⁺ + 5 Fe³⁺ + 4 H₂O', [], '1 MnO₄⁻ por cada 5 Fe²⁺')
TIO = lambda da: redox(
    da, 'I2_red', 'S2O3', 1, 1, 'I₂ + 2 S₂O₃²⁻ → 2 I⁻ + S₄O₆²⁻', 'I₂ + 2 S₂O₃²⁻ → 2 I⁻ + S₄O₆²⁻', [], '1 I₂ por cada 2 S₂O₃²⁻')

P['P7-6.1'] = redox('IO₃⁻ → I₂ y N₂H₄ → N₂, en medio ácido. ⚠️ La ecuación ajustada (4 IO₃⁻ + 5 N₂H₄ + 4 H⁺ → …) **no la da el enunciado**: es de la solución del profesor. Hay que sacarla.',
                    'IO3_I2', 'N2H4', 2, 5,
                    '4 IO₃⁻ + 24 H⁺ + 5 N₂H₄ → 2 I₂ + 12 H₂O + 5 N₂ + 20 H⁺',
                    '4 IO₃⁻ + 5 N₂H₄ + 4 H⁺ → 2 I₂ + 5 N₂ + 12 H₂O', [], '4 IO₃⁻ por cada 5 N₂H₄')
_ca = 'El CaC₂O₄ se disuelve en H₂SO₄ y queda ácido oxálico (H₂C₂O₄); el KMnO₄ pasa a Mn²⁺ y el oxálico a CO₂ (medio ácido).'
P['P7-6.2'] = MnOx(_ca + ' Piden la reacción en especies neutras.', NEUTRA_MNOX)
P['P7-6.3'] = MnOx(_ca.replace('en H₂SO₄', 'en ácido') + ' (Mn²⁺, CO₂ y agua).')
P['P7-6.4'] = redox('CrO₄²⁻ → Cr(OH)₃ y S₂O₄²⁻ → SO₃²⁻, en medio **básico**. Como dijo el profesor en clase: se ajusta primero en ácido (con H⁺) y al final se pasa a básico.',
                    'CrO4', 'S2O4', 2, 3,
                    '2 CrO₄²⁻ + 10 H⁺ + 3 S₂O₄²⁻ + 6 H₂O → 2 Cr(OH)₃ + 2 H₂O + 6 SO₃²⁻ + 12 H⁺',
                    '2 CrO₄²⁻ + 3 S₂O₄²⁻ + 4 H₂O → 2 Cr(OH)₃ + 6 SO₃²⁻ + 2 H⁺',
                    [('Paso a medio básico: añado 2 OH⁻ a los dos lados. A la derecha 2 H⁺ + 2 OH⁻ = 2 H₂O; a la izquierda quedan 2 OH⁻. Quito el agua que se repite (4 H₂O a la izquierda, 2 a la derecha → quedan 2 a la izquierda)',
                      '2 CrO₄²⁻ + 3 S₂O₄²⁻ + 2 H₂O + 2 OH⁻ → 2 Cr(OH)₃ + 6 SO₃²⁻')],
                    '3 S₂O₄²⁻ por cada 2 CrO₄²⁻, y 1 Cr(OH)₃ por cada CrO₄²⁻')
P['P7-6.5'] = redox('I⁻ → ICl y Ce⁴⁺ → Ce³⁺, en presencia de HCl. (El enunciado pone «Ce₂SO₄»: es una errata; el sulfato de cerio(IV) es Ce(SO₄)₂. No cambia el cálculo.)',
                    'Ce', 'I_ICl', 2, 1,
                    '2 Ce⁴⁺ + 2 e⁻ + I⁻ + Cl⁻ → 2 Ce³⁺ + ICl + 2 e⁻',
                    'I⁻ + Cl⁻ + 2 Ce⁴⁺ → ICl + 2 Ce³⁺', [], '2 Ce⁴⁺ por cada I⁻')
P['P7-6.6'] = MnH2O2('MnO₄⁻ → Mn²⁺ y H₂O₂ → O₂, con H₂SO₄. Piden la reacción en especies neutras.', NEUTRA_MNH2O2)
P['P7-6.7'] = MnC2O4('MnO₄⁻ → Mn²⁺ y C₂O₄²⁻ (del Na₂C₂O₄) → CO₂, en medio ácido.')
P['P7-6.8'] = redox('Cu → Cu(NO₃)₂ y HNO₃ → NO₂. Piden usar especies neutras. (Es la reacción que hizo el profesor en la pizarra.)',
                    'NO3', 'Cu', 2, 1,
                    '2 NO₃⁻ + 4 H⁺ + Cu → 2 NO₂ + 2 H₂O + Cu²⁺',
                    'Cu + 2 NO₃⁻ + 4 H⁺ → Cu²⁺ + 2 NO₂ + 2 H₂O',
                    [('A especies neutras (en clase): los 4 H⁺ los pone el HNO₃, pero solo hay 2 NO₃⁻. Añado 2 NO₃⁻ más a los dos lados: a la izquierda 4 H⁺ + 4 NO₃⁻ = 4 HNO₃, y a la derecha Cu²⁺ + 2 NO₃⁻ = Cu(NO₃)₂',
                      'Cu + 4 HNO₃ → Cu(NO₃)₂ + 2 NO₂ + 2 H₂O'),
                     ('Ojo (lo dijo el profesor): la iónica da 1 Cu : 2 NO₃⁻, pero la neutra da 1 Cu : 4 HNO₃, porque el HNO₃ también pone los NO₃⁻ del Cu(NO₃)₂. Para la cantidad de ácido, la buena es la neutra.', None)],
                    '1 Cu por cada 4 HNO₃ (neutra)')
P['P7-6.9'] = MnH2O2('H₂O₂ → O₂ y MnO₄⁻ → Mn²⁺, en medio ácido.')
P['P7-6.10'] = CrFe('El Fe²⁺ se valora con K₂Cr₂O₇, que pasa a Cr³⁺, en medio ácido (el Fe²⁺ pasa a Fe³⁺).')
P['P7-6.11'] = CrFe('Fe²⁺ → Fe³⁺ y Cr₂O₇²⁻ → Cr³⁺.')
P['P7-6.12'] = CrFe('Fe²⁺ → Fe³⁺ y Cr₂O₇²⁻ → Cr³⁺, con H₂SO₄. Piden la reacción en especies neutras.',
                    [('A especies neutras: el Cr₂O₇²⁻ va como K₂Cr₂O₇ (2 K⁺), el Fe²⁺ como FeSO₄ (6 SO₄²⁻) y los 14 H⁺ los pone el H₂SO₄ (7 SO₄²⁻). A la derecha: 2 Cr³⁺ → Cr₂(SO₄)₃; 6 Fe³⁺ → 3 Fe₂(SO₄)₃; 2 K⁺ → K₂SO₄ (en total 3 + 9 + 1 = 13 SO₄, los mismos que a la izquierda)',
                      'K₂Cr₂O₇ + 6 FeSO₄ + 7 H₂SO₄ → Cr₂(SO₄)₃ + 3 Fe₂(SO₄)₃ + K₂SO₄ + 7 H₂O')])
P['P7-6.13'] = (['#### Reacción 1 · H₂O₂ con permanganato (aquí el H₂O₂ se OXIDA)', '']
                + MnH2O2('H₂O₂ → O₂ y MnO₄⁻ → Mn²⁺, en medio ácido.')
                + ['#### Reacción 2 · H₂O₂ con Fe²⁺ (aquí el H₂O₂ se REDUCE)', '']
                + redox('Fe²⁺ → Fe³⁺ y H₂O₂ → H₂O.', 'H2O2_red', 'Fe', 1, 2,
                        'H₂O₂ + 2 H⁺ + 2 Fe²⁺ → 2 H₂O + 2 Fe³⁺', 'H₂O₂ + 2 Fe²⁺ + 2 H⁺ → 2 Fe³⁺ + 2 H₂O', [], '1 H₂O₂ por cada 2 Fe²⁺'))
P['P7-6.14'] = MnH2O2('MnO₄⁻ → Mn²⁺ y H₂O₂ → O₂, con H₂SO₄. Piden la reacción en especies neutras.', NEUTRA_MNH2O2)
P['P7-6.15'] = (['**Qué me da el enunciado:** el IO₃⁻ oxida al SO₃²⁻, que pasa a SO₄²⁻, en medio ácido. **No dicen en qué se convierte el yodo**: eso es lo que hay que averiguar. Así que primero ajusto solo la mitad que conozco, cuento electrones y después escribo la reacción entera.', '']
                + semi('SO3')
                + ['*Con los moles del problema sale que cada I coge 5 e⁻: pasa de +5 a 0 → I₂* (lo verás en la resolución). Con eso ya puedo ajustar la otra mitad:', '']
                + semi('IO3_I2')
                + ['*Igualo los electrones:* 10 e⁻ en la reducción y 2 e⁻ en la oxidación → la oxidación × 5:', '',
                   '- 2 IO₃⁻ + 12 H⁺ + 10 e⁻ → I₂ + 6 H₂O', '- 5 SO₃²⁻ + 5 H₂O → 5 SO₄²⁻ + 10 H⁺ + 10 e⁻', '',
                   '*Sumo y tacho (10 e⁻, 10 H⁺ y 5 H₂O):*', '', '**2 IO₃⁻ + 5 SO₃²⁻ + 2 H⁺ → I₂ + 5 SO₄²⁻ + H₂O**', '',
                   '*Compruebo:* átomos y cargas iguales a los dos lados ✓. Y cuadra con los datos: 0,01625 mol de SO₃²⁻ ÷ 6,495·10⁻³ mol de IO₃⁻ = 2,5 = 5/2 ✓', ''])
assert ajustada('2 IO₃⁻ + 5 SO₃²⁻ + 2 H⁺ → I₂ + 5 SO₄²⁻ + H₂O')
P['P7-6.16'] = MnFe('Fe²⁺ → Fe³⁺ y MnO₄⁻ → Mn²⁺ (medio ácido).')
P['P7-6.17'] = redox('Cr₂O₇²⁻ → Cr³⁺ y AsH₃ → AsO₄³⁻ (medio ácido).', 'Cr2O7', 'AsH3', 4, 3,
                     '4 Cr₂O₇²⁻ + 56 H⁺ + 3 AsH₃ + 12 H₂O → 8 Cr³⁺ + 28 H₂O + 3 AsO₄³⁻ + 33 H⁺',
                     '4 Cr₂O₇²⁻ + 3 AsH₃ + 23 H⁺ → 8 Cr³⁺ + 3 AsO₄³⁻ + 16 H₂O', [],
                     '3 AsH₃ por cada 4 Cr₂O₇²⁻ (es lo mismo que contar electrones: 4·6 = 24 e⁻ = 3·8)')
P['P7-6.18'] = CrFe('Fe²⁺ → Fe³⁺ y Cr₂O₇²⁻ → Cr³⁺. (El Ba se mide por gravimetría: Ba²⁺ + SO₄²⁻ → BaSO₄↓, que no es redox.)')
P['P7-6.19'] = redox('MnO₄⁻ → Mn²⁺ y SO₂ → SO₄²⁻.', 'MnO4', 'SO2', 2, 5,
                     '2 MnO₄⁻ + 16 H⁺ + 5 SO₂ + 10 H₂O → 2 Mn²⁺ + 8 H₂O + 5 SO₄²⁻ + 20 H⁺',
                     '2 MnO₄⁻ + 5 SO₂ + 2 H₂O → 2 Mn²⁺ + 5 SO₄²⁻ + 4 H⁺', [], '2 MnO₄⁻ por cada 5 SO₂')
P['P7-6.20'] = (['#### Reacción 1 · el Cu²⁺ con el I⁻', '']
                + redox('Cu²⁺ → Cu⁺ (como CuI) y I⁻ → I₂.', 'Cu_CuI', 'I_I2', 2, 1,
                        '2 Cu²⁺ + 2 I⁻ + 2 I⁻ → 2 CuI + I₂', '2 Cu²⁺ + 4 I⁻ → 2 CuI + I₂', [], '2 Cu²⁺ forman 1 I₂')
                + ['#### Reacción 2 · el I₂ con el tiosulfato', '']
                + TIO('S₂O₃²⁻ → S₄O₆²⁻ e I₂ → I⁻.')
                + ['> **Juntando las dos:** 2 Cu²⁺ → 1 I₂ → 2 S₂O₃²⁻, así que **1 Cu por cada S₂O₃²⁻**.', ''])
P['P7-6.21'] = (['#### Reacción 1 · el NaI pasa a I₂', '',
                 '**Qué me da el enunciado:** «se añade un oxidante» y todo el NaI pasa a I₂. No dicen qué oxidante es, así que solo puedo ajustar la mitad del yodo (y es lo único que necesito, porque sigo al yodo):', '']
                + semi('I_I2')
                + ['> Relación: 2 I⁻ forman 1 I₂.', '', '#### Reacción 2 · el I₂ con el tiosulfato', '']
                + TIO('I₂ → I⁻ y S₂O₃²⁻ → S₄O₆²⁻.')
                + ['> **Juntando las dos:** 2 I⁻ → 1 I₂ → 2 S₂O₃²⁻, así que **1 I⁻ por cada S₂O₃²⁻**.', ''])
P['P7-6.22'] = (['#### Reacción 1 · el Sn con el HNO₃ (redox)', '']
                + redox('Sn → SnO₂ y HNO₃ → NO₂.', 'NO3', 'Sn', 4, 1,
                        '4 NO₃⁻ + 8 H⁺ + Sn + 2 H₂O → 4 NO₂ + 4 H₂O + SnO₂ + 4 H⁺',
                        'Sn + 4 NO₃⁻ + 4 H⁺ → SnO₂ + 4 NO₂ + 2 H₂O',
                        [('A especies neutras: 4 H⁺ + 4 NO₃⁻ = 4 HNO₃ (aquí no hace falta añadir nada, porque el SnO₂ ya es neutro)',
                          'Sn + 4 HNO₃ → SnO₂ + 4 NO₂ + 2 H₂O')], '1 Sn por cada 4 HNO₃')
                + ['#### Reacción 2 · el HNO₃ que sobra con la NaOH (ácido-base, no redox)', '']
                + simple('Neutralización 1 : 1', 'HNO₃ + NaOH → NaNO₃ + H₂O'))
P['P7-6.23'] = (['#### Reacción 1 · el MnO₂ con el oxálico', '']
                + redox('MnO₂ → Mn²⁺ y H₂C₂O₄ → CO₂, en medio ácido.', 'MnO2', 'H2C2O4', 1, 1,
                        'MnO₂ + 4 H⁺ + H₂C₂O₄ → Mn²⁺ + 2 H₂O + 2 CO₂ + 2 H⁺',
                        'MnO₂ + H₂C₂O₄ + 2 H⁺ → Mn²⁺ + 2 CO₂ + 2 H₂O', [], '1 MnO₂ por cada oxálico')
                + ['#### Reacción 2 · el oxálico que sobra con el permanganato', '']
                + MnOx('H₂C₂O₄ → CO₂ y MnO₄⁻ → Mn²⁺.'))
P['P7-6.24'] = (simple('No redox: el Ca²⁺ precipita como oxalato (1 Ca por cada oxalato)', 'Ca²⁺ + C₂O₄²⁻ → CaC₂O₄')
                + MnC2O4('MnO₄⁻ → Mn²⁺ y C₂O₄²⁻ → CO₂ (el CaC₂O₄ disuelto en H₂SO₄).'))
P['P7-6.25'] = (['#### Reacción 1 · KIO₃ + KI → I₂ (el yodo acaba en I₂ desde los dos lados)', '']
                + redox('IO₃⁻ → I₂ y I⁻ → I₂, en medio ácido (H₂SO₄). Piden sales neutras.', 'IO3_I2', 'I_I2', 1, 5,
                        '2 IO₃⁻ + 12 H⁺ + 10 I⁻ → I₂ + 6 H₂O + 5 I₂',
                        '2 IO₃⁻ + 10 I⁻ + 12 H⁺ → 6 I₂ + 6 H₂O',
                        [('Divido todo entre 2 (todos los coeficientes son pares)', 'IO₃⁻ + 5 I⁻ + 6 H⁺ → 3 I₂ + 3 H₂O'),
                         ('A sales neutras: el IO₃⁻ y el I⁻ van con K⁺ (KIO₃ y 5 KI: 6 K⁺) y los 6 H⁺ los pone el H₂SO₄ (3 SO₄²⁻). A la derecha: 6 K⁺ + 3 SO₄²⁻ = 3 K₂SO₄',
                          'KIO₃ + 5 KI + 3 H₂SO₄ → 3 I₂ + 3 K₂SO₄ + 3 H₂O')], '1 KIO₃ forma 3 I₂')
                + ['#### Reacción 2 · el I₂ con el tiosulfato', '']
                + TIO('I₂ → I⁻ y S₂O₃²⁻ → S₄O₆²⁻.')
                + simple('En sales neutras (con Na⁺)', 'I₂ + 2 Na₂S₂O₃ → 2 NaI + Na₂S₄O₆'))
P['P7-6.26'] = (simple('Reacción 1 · ácido-base (no redox): el oxálico tiene 2 H ácidos', 'H₂C₂O₄ + 2 NaOH → Na₂C₂O₄ + 2 H₂O', '> 1 oxálico por cada 2 NaOH.')
                + ['#### Reacción 2 · el oxálico con el permanganato (redox)', '']
                + MnOx('El oxálico pasa a CO₂ y el MnO₄⁻ a Mn²⁺.'))
P['P7-6.27'] = (['#### Reacción 1 · el permanganato solo ve el Fe²⁺', '']
                + MnFe('Fe²⁺ → Fe³⁺ y se forman iones Mn²⁺ (medio ácido).')
                + simple('El Zn reduce todo el Fe³⁺ a Fe²⁺ (Zn 0 → +2 pierde 2 e⁻; cada Fe³⁺ gana 1)', 'Zn + 2 Fe³⁺ → Zn²⁺ + 2 Fe²⁺',
                         'No hace falta para las cuentas: solo sirve para que todo el hierro quede como Fe²⁺.')
                + ['#### Reacción 2 · el dicromato ve todo el hierro', '']
                + CrFe('Fe²⁺ → Fe³⁺ y se forman iones Cr³⁺.'))
P['P7-6.28'] = (['#### Reacción 1 · el FeSO₄ con el dicromato (para saber la [FeSO₄])', '']
                + CrFe('Fe²⁺ → Fe³⁺ y Cr₂O₇²⁻ → Cr³⁺.')
                + ['#### Reacción 2 · el FeSO₄ con el permanganato', '']
                + MnFe('Fe²⁺ → Fe³⁺ y MnO₄⁻ → Mn²⁺.'))

# ---------------------------------------------------------------- salida
out = ['Ajuste DESDE CERO de cada problema de redox. Generado por gen_ajustes.py (no editar a mano).', '']
for k, L in P.items():
    out += [f'@@ {k}', ''] + L + ['']
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '62_ajustes.md'), 'w', encoding='utf-8').write('\n'.join(out))
print('ajustes:', len(P), '· todas las ecuaciones comprobadas (átomos y cargas)')
