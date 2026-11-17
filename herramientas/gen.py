import os, sys, subprocess
H = os.path.dirname(os.path.abspath(__file__)); P2 = os.path.dirname(H); sys.path.insert(0, P2)
import lab
IMG = os.path.join(os.path.dirname(P2), 'img')
S = {
'A1': ([{'title': '1. La mezcla', 'kind': 'balance', 'solid': 'NaCl + Na₂SO₄ + NaNO₃', 'mass': '10,0 g', 'note': ['tres sales juntas']},
        {'title': '2. Análisis elemental', 'liquid': False, 'ions': [('Na', 'n'), ('Cl', 'r'), ('O', 'n'), ('S', 'n'), ('N', 'n'), ('O', 'n')], 'note': ['32,08 % Na · 36,01 % O', '19,51 % Cl']},
        {'title': '3. Dónde está cada uno', 'kind': 'text', 'lines': ['Cl → solo en NaCl', 'N → solo en NaNO₃ (sale N₂)', 'Na y O → 2 ecuaciones']}],
       ['rompo|la muestra', ''], 'El Cl da el NaCl directamente; con el Na y el O saco Na₂SO₄ (a) y NaNO₃ (b)|Na: 0,05504 + 2a + b · O: 4a + 3b'),
'A2': ([{'title': '1. Antes (0 °C)', 'liquid': False, 'ions': [('F₂', 'r'), ('Xe', 'r'), ('F₂', 'r'), ('F₂', 'r')], 'note': ['F₂: 0,60 atm · Xe: 0,12 atm', 'recipiente de 0,25 L']},
        {'title': '2. Calentar a 400 °C', 'liquid': False, 'ions': [('XeFₓ', 'p'), ('F₂', 'x')], 'heat': True, 'note': ['Xe + F₂ → sólido']},
        {'title': '3. Después (0 °C)', 'liquid': False, 'solid': 'XeFₓ (s)', 'ions': [('F₂', 'x'), ('F₂', 'x')], 'note': ['queda 0,36 atm', '= solo F₂ que sobra']}],
       ['', 'enfrío'], 'A V y T constantes, presión ∝ moles: F₂ gastado = 0,60 − 0,36 = 0,24 atm|0,24 : 0,12 = 2 F₂ por Xe → XeF₄'),
'A3': ([{'title': '1. Tostación', 'kind': 'text', 'lines': ['4 FeS₂ + 11 O₂ →', '2 Fe₂O₃ + 8 SO₂', '(90 %)']},
        {'title': '2. Oxidación', 'kind': 'text', 'lines': ['2 SO₂ + O₂ →', '2 SO₃', '(90 %)']},
        {'title': '3. Absorción', 'kind': 'text', 'lines': ['SO₃ + H₂SO₄ →', 'H₂S₂O₇', '(90 %)']},
        {'title': '4. Dilución', 'kind': 'text', 'lines': ['H₂S₂O₇ + H₂O →', '2 H₂SO₄', '(90 %)']}],
       ['', '', ''], 'Sigue al S: 1 FeS₂ tiene 2 S y cada S acaba en 1 H₂SO₄ neto|mol S × 0,9 × 0,9 × 0,9 × 0,9 = mol H₂SO₄'),
'A4': ([{'title': '1. Estandarizo el AEDT', 'kind': 'flask', 'burette': 'AEDT ¿M?', 'ions': [('Ca²⁺', 'r')], 'note': ['25,0 mL de CaCO₃ 0,3722 g/L', 'gasta 24,8 mL']},
        {'title': '2. Leche tratada (pH 12)', 'ions': [('Ca²⁺', 'r'), ('Na⁺', 'e')], 'solid': 'Mg(OH)₂', 'note': ['50,0 mL', 'el Mg²⁺ precipita y no molesta']},
        {'title': '3. Valoro la leche', 'kind': 'flask', 'burette': 'AEDT 3,749·10⁻³ M', 'ions': [('Ca²⁺', 'r')], 'note': ['gasta 18,4 mL']}],
       ['', ''], 'Ca²⁺ + AEDT⁴⁻ → [Ca(AEDT)]²⁻ (1 : 1, complejo muy estable)|1.º [AEDT] con el patrón · 2.º mol de Ca en la leche → mg por 100 mL'),
'B1': ([{'title': 'Exp. 1 (2,50 g)', 'ions': [('SO₄²⁻', 'r'), ('CO₃²⁻', 'e'), ('Na⁺', 'e'), ('Ba²⁺', 'r')], 'solid': 'BaSO₄', 'note': ['+ BaCl₂ en exceso', 'solo precipita el sulfato']},
        {'title': 'Peso', 'kind': 'balance', 'solid': 'BaSO₄', 'mass': '1,85 g', 'note': ['→ mol de Na₂SO₄']},
        {'title': 'Exp. 2 (1,20 g)', 'kind': 'flask', 'burette': 'HCl 0,500 M', 'ions': [('CO₃²⁻', 'r'), ('SO₄²⁻', 'e')], 'note': ['gasta 25,3 mL', 'solo reacciona el carbonato']}],
       ['filtro|y seco', ''], 'Ba²⁺ + SO₄²⁻ → BaSO₄ (1 : 1) · CO₃²⁻ + 2 H⁺ → CO₂ + H₂O (2 HCl por carbonato)|cada experimento con SU masa (2,50 g y 1,20 g); los 11,00 g sobran'),
'B2': ([{'title': '1. Agua con fósforo', 'ions': [('H₂PO₄⁻', 'r'), ('HPO₄²⁻', 'r'), ('Na⁺', 'e')], 'note': ['1,00·10⁴ L', '10,0 mg de P por litro']},
        {'title': '2. + CaO', 'ions': [('Ca²⁺', 'r'), ('OH⁻', 'r'), ('PO₄³⁻', 'r')], 'note': ['el OH⁻ pasa todo a PO₄³⁻']},
        {'title': '3. Precipita', 'ions': [('Na⁺', 'e')], 'solid': 'Ca₅(PO₄)₃OH', 'note': ['todo el P sale del agua']}],
       ['CaO → Ca²⁺|+ 2 OH⁻', ''], 'Mira la fórmula del precipitado: Ca₅(PO₄)₃OH → 5 Ca por cada 3 P|mol P × 5/3 = mol Ca = mol CaO'),
'B3': ([{'title': '1. Cu²⁺ + KI (exceso)', 'ions': [('Cu²⁺', 'r'), ('I⁻', 'r'), ('K⁺', 'e')], 'solid': 'CuI', 'note': ['2,00 g de mineral', '2 Cu²⁺ → 1 I₂']},
        {'title': '2. Se forma I₂', 'ions': [('I₂', 'p'), ('K⁺', 'e')], 'color': '#F5E1B8', 'note': ['(color pardo)']},
        {'title': '3. Valoro el I₂', 'kind': 'flask', 'burette': 'S₂O₃²⁻ 0,0500 M', 'ions': [('I₂', 'r')], 'note': ['gasta 76,5 mL', '1 I₂ gasta 2 S₂O₃²⁻']}],
       ['', ''], 'El I₂ es solo un intermediario: 2 Cu²⁺ → 1 I₂ → 2 S₂O₃²⁻ ⇒ 1 Cu por cada S₂O₃²⁻'),
'B4': ([{'title': '1. Mezcla', 'kind': 'balance', 'solid': 'CaCO₃ + NaHCO₃', 'mass': '8,40 g', 'note': ['x g de CaCO₃', '(8,40 − x) g de NaHCO₃']},
        {'title': '2. Calentar', 'kind': 'crucible', 'solid': 'se van CO₂ y H₂O', 'note': ['CaCO₃ → CaO + CO₂', '2 NaHCO₃ → Na₂CO₃ + H₂O + CO₂']},
        {'title': '3. Lo que queda', 'kind': 'balance', 'solid': 'CaO + Na₂CO₃', 'mass': '5,30 g', 'note': ['masa perdida = 3,10 g', '= masa de los gases']}],
       ['', ''], 'Cada g de CaCO₃ pierde 0,4397 g · cada g de NaHCO₃ pierde 0,3692 g|0,4397·x + 0,3692·(8,40 − x) = 3,10 g'),
}
for k, (p, a, b) in S.items():
    open(os.path.join(IMG, f'sem3_{k}.svg'), 'w', encoding='utf-8').write(lab.draw(p, a, b))
print('ok', len(S))
