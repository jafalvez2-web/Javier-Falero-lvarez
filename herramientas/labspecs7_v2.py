"""Dibujos del Tema 7 con material de laboratorio (lab2.py). id -> SVG."""
from lab2 import *

D = {}


def p7_3_5():
    o = []
    # 1 · pesar
    o.append(numero(22, 24, 1, 'Peso el carbonato'))
    o.append(balanza(100, 250, '0,0555 g', 'X₂CO₃ (sólido)'))
    o.append(flecha(112, 150, 250, 150, 'lo echo|al matraz', curva=60))
    # 2 · reacciona con el H₂SO₄ en exceso
    o.append(numero(240, 24, 2, 'Lo ataco con H₂SO₄ (exceso)'))
    o.append(pipeta(318, 46, 128))
    o.append(rotulo(340, 64, ['20,00 mL', 'H₂SO₄ 0,0400 M'], 10.5, 'start'))
    o.append(erlenmeyer(318, 262, 130, 130, 'acido', .5,
                        iones=[('H⁺', 'x'), ('X⁺', 'p'), ('SO₄²⁻', 'e'), ('H⁺', 'x')], gas='CO₂ ↑'))
    o.append(rotulo(318, 282, ['Se disuelve y sale CO₂', 'sobra H₂SO₄'], 10.5))
    o.append(flecha(400, 205, 470, 205, 'valoro|lo que sobra'))
    # 3 · valoro el H₂SO₄ que sobra
    o.append(numero(470, 24, 3, 'Valoro el H₂SO₄ que sobra'))
    o.append(bureta(560, 46, 158, ['NaOH 0,1000 M'], ['gasto 11,28 mL'], y_base=263))
    o.append(erlenmeyer(560, 262, 120, 100, 'acido', .5, iones=[('H⁺', 'x'), ('X⁺', 'p'), ('SO₄²⁻', 'e')]))
    o.append(rotulo(560, 282, ['El OH⁻ neutraliza', 'solo el H⁺ que sobra'], 10.5))
    # idea
    o.append(caja(60, 318, 580, 46, ['mol de X₂CO₃ = mol de H₂SO₄ añadidos − mol de H₂SO₄ que sobran',
                                     'X₂CO₃ + H₂SO₄ → X₂SO₄ + H₂O + CO₂ (1 : 1) · H₂SO₄ + 2 NaOH → Na₂SO₄ + 2 H₂O']))
    o.append(leyenda(390, 380))
    return svg(700, 392, ''.join(o))


D['P7-3.5'] = p7_3_5
