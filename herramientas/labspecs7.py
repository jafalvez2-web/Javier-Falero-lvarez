# Dibujos del tema 7: id -> (viñetas, flechas, recuadro inferior)
S = {}

def acid_metal(metal_ions, gas_note, title_end, sal_ions, bottom, note0, note2):
    return ([{'title': '1. Pieza + HCl', 'bar': (metal_ions, False), 'ions': [('H⁺', 'r'), ('Cl⁻', 'e'), ('H⁺', 'r'), ('Cl⁻', 'e')], 'note': note0},
             {'title': '2. Reacciona', 'bar': (metal_ions, False), 'gas': 'H₂', 'ions': [('H⁺', 'r'), ('Cl⁻', 'e')] + sal_ions, 'note': ['El metal se disuelve', 'y burbujea H₂']},
             {'title': title_end, 'kind': 'text', 'lines': note2}],
            ['metal + H⁺ →|catión + H₂', 'recojo y|peso el H₂'], bottom)

S['EC 7.1'] = acid_metal('Al + Cu', 'H₂', '3. Lo que mido', [('Al³⁺', 'p')], 'Solo reacciona el Al: Al + 3 HCl → AlCl₃ + 3/2 H₂|El Cu no reacciona (se queda en la pieza); el Cl⁻ es espectador',
                         ['0,691 cm³ de aleación', '(93,7 % de Al)'], ['¿Cuánto H₂?', 'cm³ → g → g Al → mol Al', '→ mol H₂ → g H₂'])

S['EC 7.2'] = ([{'title': '1. Mezcla sólida', 'kind': 'balance', 'solid': 'MgCO₃ + Mg(OH)₂', 'mass': '425 g', 'note': ['35,2 % MgCO₃', '64,8 % Mg(OH)₂']},
                {'title': '2. Añado HCl', 'ions': [('H⁺', 'r'), ('Cl⁻', 'e'), ('Mg²⁺', 'p'), ('Cl⁻', 'e')], 'gas': 'CO₂', 'note': ['Cada sólido reacciona', 'por su lado (simultáneas)']},
                {'title': '3. Lo que busco', 'kind': 'text', 'lines': ['HCl gastado total', '= HCl del MgCO₃', '+ HCl del Mg(OH)₂']}],
               ['+ HCl', ''], 'MgCO₃ + 2 HCl → MgCl₂ + H₂O + CO₂   ·   Mg(OH)₂ + 2 HCl → MgCl₂ + 2 H₂O|No se suman las ecuaciones: se suman los moles de HCl')

S['EC 7.3'] = ([{'title': '1. Reactivos', 'kind': 'text', 'lines': ['125 g de P₄', '323 g de Cl₂', '¿quién se acaba antes?']},
                {'title': '2. Reaccionan', 'liquid': False, 'ions': [('P₄', 'x'), ('Cl₂', 'r'), ('PCl₃', 'p'), ('PCl₃', 'p')], 'note': ['P₄ + 6 Cl₂ → 4 PCl₃']},
                {'title': '3. Final', 'liquid': False, 'ions': [('P₄', 'x'), ('PCl₃', 'p'), ('PCl₃', 'p'), ('PCl₃', 'p')], 'note': ['Se acaba el Cl₂ (limitante)', 'y sobra P₄']}],
               ['', ''], 'El producto se calcula siempre desde el limitante (Cl₂)')

S['P7-1.1'] = acid_metal('Fe + Al', 'H₂', '3. Lo que mido', [('Fe²⁺', 'p'), ('Al³⁺', 'p')],
                         'Fe + 2 HCl → FeCl₂ + H₂   ·   Al + 3 HCl → AlCl₃ + 3/2 H₂|Los dos metales dan H₂ a la vez → x g de Fe y (2,05 − x) g de Al',
                         ['2,05 g de aleación', '(no sé cuánto Fe y Al)'], ['0,105 g de H₂ en total', '= H₂ del Fe + H₂ del Al'])

S['P7-1.2'] = ([{'title': '1. Inicio', 'bar': ('Zn', False), 'ions': [('Ag⁺', 'r'), ('NO₃⁻', 'e'), ('Ag⁺', 'r'), ('NO₃⁻', 'e')], 'note': ['Barra de 2,50 g', 'AgNO₃(aq) = Ag⁺ + NO₃⁻ sueltos']},
                {'title': '2. Qué pasa', 'bar': ('Zn', True), 'ions': [('Zn²⁺', 'p'), ('NO₃⁻', 'e'), ('Ag⁺', 'r'), ('NO₃⁻', 'e')], 'note': ['El Zn sale como Zn²⁺', 'la Ag⁺ se pega como Ag']},
                {'title': '3. Final', 'bar': ('Zn', True), 'ions': [('Zn²⁺', 'p'), ('NO₃⁻', 'e'), ('Zn²⁺', 'p'), ('NO₃⁻', 'e')], 'note': ['Barra de 3,37 g', '(menos Zn, con Ag encima)']}],
               ['Zn + 2 Ag⁺ →|Zn²⁺ + 2 Ag', ''], 'Por cada mol de Zn: sale 65,38 g de Zn y entran 215,74 g de Ag|la barra gana 150,36 g → con lo que gana (0,87 g) saco los moles de Zn')

def chain(titles, notes, arrows, bottom, kinds=None):
    ps = []
    for i, t in enumerate(titles):
        ps.append({'title': t, 'kind': 'text', 'lines': notes[i]})
    return (ps, arrows, bottom)

S['P7-1.3'] = ([{'title': '1. Disolución', 'ions': [('Na⁺', 'e'), ('ClO₂⁻', 'r'), ('Na⁺', 'e'), ('ClO₂⁻', 'r')], 'note': ['1 L de NaClO₂ 2,0 M']},
                {'title': '2. Burbujeo Cl₂', 'ions': [('Na⁺', 'e'), ('Cl⁻', 'p'), ('Cl₂', 'r')], 'gas': 'ClO₂', 'note': ['Se forma ClO₂ y NaCl']},
                {'title': '3. Rendimiento', 'kind': 'text', 'lines': ['Solo sale el 97 %', 'teórico × 0,97', '= real']}],
               ['+ Cl₂', ''], 'Cl₂ + 2 NaClO₂ → 2 ClO₂ + 2 NaCl|Sé el reactivo y busco el producto → el rendimiento MULTIPLICA')

S['P7-1.4'] = chain(['1. Cl₂ + KOH', '2. KClO', '3. KClO₃', '4. KClO₄'],
                    [['Cl₂ → KClO', '(rendimiento 88 %)'], ['3 KClO →', '2 KCl + KClO₃'], ['4 KClO₃ →', '3 KClO₄ + KCl'], ['Quiero 100 g', 'de KClO₄']],
                    ['', '', ''], 'Voy HACIA ATRÁS: g KClO₄ → mol KClO₄ → mol KClO₃ → mol KClO → mol Cl₂|y divido por 0,88 (hace falta más Cl₂ del teórico)')

S['P7-1.5'] = chain(['1. NaI + AgNO₃', '2. AgI + Fe', '3. FeI₂ + Cl₂', '4. I₂'],
                    [['→ AgI', '(93 %)'], ['→ FeI₂', '(89 %)'], ['→ I₂', '(72 %)'], ['Quiero 1,0 kg', 'de I₂']],
                    ['', '', ''], 'Hacia atrás desde 1,0 kg de I₂, dividiendo por cada rendimiento|1 FeI₂ → 1 I₂ · 2 AgI → 1 FeI₂ · 1 AgNO₃ → 1 AgI')

# ---------- apartado 3 ----------
def retro(t1, ions1, n1, gas, t2, ions2, n2, val, n3, arrows, bottom):
    return ([{'title': t1, 'ions': ions1, 'solid': None, 'gas': gas, 'note': n1},
             {'title': t2, 'ions': ions2, 'note': n2},
             {'title': '3. Valoro lo que sobra', 'kind': 'flask', 'burette': val, 'ions': [('H⁺', 'x')] if 'NaOH' in val or 'OH' in val else [('ácido', 'x')], 'note': n3}],
            arrows, bottom)

S['EC 7.4'] = ([{'title': '1. Mármol + HCl (exceso)', 'ions': [('H⁺', 'r'), ('Cl⁻', 'e'), ('H⁺', 'r'), ('Cl⁻', 'e')], 'solid': 'CaCO₃', 'note': ['2,00 L de HCl 2,52 M', 'el mármol es el limitante']},
                {'title': '2. Se disuelve', 'ions': [('H⁺', 'x'), ('Ca²⁺', 'p'), ('Cl⁻', 'e'), ('H⁺', 'x')], 'gas': 'CO₂', 'note': ['Queda HCl, pero menos', 'concentrado']},
                {'title': '3. Valoro 10 mL', 'kind': 'flask', 'burette': 'NaOH 0,9987 M', 'ions': [('H⁺', 'x'), ('Cl⁻', 'e')], 'note': ['gasta 24,87 mL', '→ HCl que SOBRA']}],
               ['CaCO₃ + 2 HCl →|CaCl₂ + H₂O + CO₂', 'cojo|10 mL'], 'HCl que reaccionó = HCl inicial − HCl que sobra|(todo en moles en los 2,00 L) → ÷ 2 → mol de CaCO₃')

S['P7-3.1'] = ([{'title': '1. Patrón pesado', 'kind': 'balance', 'solid': 'H₂C₂O₄·2H₂O', 'mass': '0,6477 g', 'note': ['en 100,0 mL', '→ [oxálico] exacta']},
                {'title': '2. Estandarizo NaOH', 'kind': 'flask', 'burette': 'NaOH ¿M?', 'ions': [('H₂C₂O₄', 'r')], 'note': ['5,00 mL de oxálico', 'gastan 30,0 mL de NaOH']},
                {'title': '3. Valoro el H₂SO₄', 'kind': 'flask', 'burette': 'NaOH ya conocida', 'ions': [('H₂SO₄', 'r')], 'note': ['25,0 mL de H₂SO₄', 'gastan 23,7 mL']}],
               ['', ''], 'Los dos ácidos son dipróticos: gastan 2 NaOH cada uno|1.º saco la [NaOH] con el oxálico; 2.º con esa NaOH saco la [H₂SO₄]')

S['P7-3.2'] = ([{'title': '1. Mezcla de bases', 'kind': 'balance', 'solid': 'Mg(OH)₂ + LiOH', 'mass': '0,4225 g', 'note': ['x g de Mg(OH)₂', '(0,4225 − x) g de LiOH']},
                {'title': '2. Valoro con HCl', 'kind': 'flask', 'burette': 'HCl 0,5375 M', 'ions': [('OH⁻', 'r'), ('Mg²⁺', 'e'), ('Li⁺', 'e')], 'note': ['gasta 28,28 mL', 'cada OH⁻ gasta un H⁺']},
                {'title': '3. Ecuación', 'kind': 'text', 'lines': ['H⁺ gastados =', '2·mol Mg(OH)₂', '+ mol LiOH']}],
               ['disuelvo', ''], 'Mg(OH)₂ tiene 2 OH⁻ (gasta 2 HCl) · LiOH tiene 1 OH⁻ (gasta 1 HCl)')

S['P7-3.3'] = ([{'title': '1. Disuelvo la mezcla', 'ions': [('K⁺', 'e'), ('OH⁻', 'r'), ('Li⁺', 'e'), ('OH⁻', 'r')], 'note': ['0,4324 g de KOH + LiOH', 'en 100,0 mL']},
                {'title': '2. Cojo una alícuota', 'kind': 'flask', 'burette': 'HCl 0,0352 M', 'ions': [('OH⁻', 'r')], 'note': ['10,00 mL de los 100,0', 'gastan 28,28 mL']},
                {'title': '3. Lo que pido', 'kind': 'text', 'lines': ['× 10 (alícuota)', 'x g de KOH', '→ g de LiOH → g de Li']}],
               ['10 mL', ''], 'KOH + HCl → KCl + H₂O · LiOH + HCl → LiCl + H₂O (1 : 1)|Piden % de Li (el elemento), no de LiOH')

S['P7-3.4'] = ([{'title': '1. Tableta + HCl (exceso)', 'ions': [('H⁺', 'r'), ('Cl⁻', 'e'), ('H⁺', 'r'), ('Cl⁻', 'e')], 'solid': 'CaCO₃', 'note': ['1,245 g + 50,00 mL', 'de HCl 0,5000 M']},
                {'title': '2. Se disuelve', 'ions': [('H⁺', 'x'), ('Ca²⁺', 'p'), ('Cl⁻', 'e')], 'gas': 'CO₂', 'note': ['sobra HCl']},
                {'title': '3. Valoro lo que sobra', 'kind': 'flask', 'burette': 'Ba(OH)₂ 0,1092 M', 'ions': [('H⁺', 'x')], 'note': ['gasta 40,20 mL', 'Ba(OH)₂ = 2 OH⁻']}],
               ['CaCO₃ + 2 HCl →', ''], 'HCl que reaccionó = añadido − sobrante (Ba(OH)₂ × 2)|÷ 2 → mol de CaCO₃')

S['P7-3.5'] = ([{'title': '1. X₂CO₃ + H₂SO₄ (exceso)', 'ions': [('H⁺', 'r'), ('SO₄²⁻', 'e'), ('H⁺', 'r')], 'solid': 'X₂CO₃', 'note': ['0,0555 g + 20,00 mL', 'de H₂SO₄ 0,0400 M']},
                {'title': '2. Se disuelve', 'ions': [('H⁺', 'x'), ('X⁺', 'p'), ('SO₄²⁻', 'e')], 'gas': 'CO₂', 'note': ['sobra H₂SO₄']},
                {'title': '3. Valoro lo que sobra', 'kind': 'flask', 'burette': 'NaOH 0,1000 M', 'ions': [('H⁺', 'x')], 'note': ['gasta 11,28 mL', '2 NaOH por H₂SO₄']}],
               ['', ''], 'mol de X₂CO₃ = H₂SO₄ añadido − sobrante|M(X₂CO₃) = 0,0555 g ÷ mol → M(X)')

S['P7-3.6'] = ([{'title': '1. (NH₄)₂SO₄ + NaOH', 'ions': [('NH₄⁺', 'r'), ('OH⁻', 'r'), ('SO₄²⁻', 'e'), ('Na⁺', 'e')], 'gas': 'NH₃', 'note': ['10,0 mL de muestra', 'sale NH₃ gas']},
                {'title': '2. El NH₃ entra en HCl', 'ions': [('H⁺', 'x'), ('NH₄⁺', 'p'), ('Cl⁻', 'e')], 'note': ['50,0 mL de HCl 0,1000 M', 'neutraliza parte del HCl']},
                {'title': '3. Valoro el HCl que sobra', 'kind': 'flask', 'burette': 'NaOH 0,098 M', 'ions': [('H⁺', 'x')], 'note': ['gasta 21,5 mL']}],
               ['burbujeo|el NH₃', ''], 'NH₃ recogido = HCl inicial − HCl sobrante|1 (NH₄)₂SO₄ da 2 NH₃')

S['P7-3.7'] = ([{'title': '1. XCO₃ + HCl (exceso)', 'ions': [('H⁺', 'r'), ('Cl⁻', 'e'), ('H⁺', 'r')], 'solid': 'XCO₃', 'note': ['3,542 g + 18,68 mL', 'de HCl 5,653 M']},
                {'title': '2. Se disuelve', 'ions': [('H⁺', 'x'), ('X²⁺', 'p'), ('Cl⁻', 'e')], 'gas': 'CO₂', 'note': ['sobra HCl']},
                {'title': '3. Valoro lo que sobra', 'kind': 'flask', 'burette': 'Ca(OH)₂ 1,789 M', 'ions': [('H⁺', 'x')], 'note': ['gasta 6,03 mL', 'Ca(OH)₂ = 2 OH⁻']}],
               ['XCO₃ + 2 HCl →', ''], 'HCl reaccionado ÷ 2 = mol de XCO₃ → M(XCO₃) → M(X)')

S['P7-3.8'] = ([{'title': '1. Mg + H₂SO₄ (exceso)', 'bar': ('Mg', False), 'ions': [('H⁺', 'r'), ('SO₄²⁻', 'e'), ('H⁺', 'r'), ('SO₄²⁻', 'e')], 'note': ['1,25 g de Mg impuro', '100 mL de H₂SO₄ 0,500 M']},
                {'title': '2. Se disuelve', 'ions': [('H⁺', 'x'), ('Mg²⁺', 'p'), ('SO₄²⁻', 'e')], 'gas': 'H₂', 'note': ['sobra H₂SO₄']},
                {'title': '3. Valoro lo que sobra', 'kind': 'flask', 'burette': 'NaOH 0,500 M', 'ions': [('H⁺', 'x')], 'note': ['gasta 33,4 mL']}],
               ['Mg + H₂SO₄ →|MgSO₄ + H₂', ''], 'mol de Mg = H₂SO₄ añadido − sobrante (NaOH ÷ 2)')

# ---------- apartado 4 ----------
def grav(t1, ions1, n1, reagent, solid, n2, heat_solid, mass, n3, bottom, arrows=('', '')):
    ps = [{'title': t1, 'ions': ions1, 'note': n1},
          {'title': '2. Precipito', 'ions': [(reagent, 'r')], 'solid': solid, 'note': n2}]
    if heat_solid:
        ps.append({'title': '3. Calciño', 'kind': 'crucible', 'solid': heat_solid, 'note': ['el sólido cambia,', 'el elemento no se pierde']})
    ps.append({'title': f'{len(ps)+1}. Peso', 'kind': 'balance', 'solid': heat_solid or solid, 'mass': mass, 'note': n3})
    return (ps, list(arrows) + ['filtro|y seco'] * 2, bottom)

S['EC 7.5'] = grav('1. Agua mineral', [('Mg²⁺', 'r'), ('Na⁺', 'e'), ('Cl⁻', 'e')], ['109,712 g de agua'], 'PO₄³⁻ + NH₄⁺', 'MgNH₄PO₄', ['todo el Mg precipita'],
                   'Mg₂P₂O₇', '0,0549 g', ['lo que peso'], 'Camino del Mg: Mg²⁺ → MgNH₄PO₄ → Mg₂P₂O₇|1 Mg₂P₂O₇ lleva 2 Mg → mol Mg → g Mg → ppm', ('+ reactivo', 'filtro'))

S['P7-4.1'] = ([{'title': 'Exp. 1 (2,000 g)', 'ions': [('CO₃²⁻', 'r'), ('Na⁺', 'e'), ('K⁺', 'e'), ('Cl⁻', 'e')], 'note': ['+ CaCl₂ en exceso']},
                {'title': 'Precipita y peso', 'kind': 'balance', 'solid': 'CaCO₃', 'mass': '0,800 g', 'note': ['→ mol de Na₂CO₃']},
                {'title': 'Exp. 2 (1,000 g)', 'kind': 'flask', 'burette': 'AgNO₃ 0,0750 M', 'ions': [('Cl⁻', 'r'), ('K⁺', 'e')], 'note': ['gasta 36,0 mL', '→ AgCl → mol de KCl']}],
               ['', ''], 'Dos experimentos independientes: el carbonato con Ca²⁺ (CaCO₃) y el cloruro con Ag⁺ (AgCl)|Cada uno con SU masa de muestra (2,000 g y 1,000 g)')

S['P7-4.2'] = grav('1. Alumbre disuelto', [('Al³⁺', 'r'), ('K⁺', 'e'), ('SO₄²⁻', 'e')], ['1,227 g de muestra'], 'oxina', 'Al(oxinato)₃', ['todo el Al precipita'],
                   'Al₂O₃', '0,1098 g', ['lo que peso'], '1 Al₂O₃ lleva 2 Al → mol de Al → %Al|El S sale de la fórmula del alumbre: 2 Al por cada 4 S', ('+ 8-hidroxi-|quinoleína', ''))

S['P7-4.3'] = ([{'title': '1. Hidrato', 'kind': 'balance', 'solid': 'FeClₓ·nH₂O', 'mass': '5,012 g', 'note': ['pesado tal cual']},
                {'title': '2. Seco en el horno', 'kind': 'crucible', 'solid': 'FeClₓ', 'note': ['se va el agua', 'queda 3,195 g']},
                {'title': '3. Disuelvo + AgNO₃', 'ions': [('Cl⁻', 'r'), ('Ag⁺', 'r'), ('Fe²⁺', 'e')], 'solid': 'AgCl 7,225 g', 'note': ['todo el Cl⁻ → AgCl']}],
               ['− H₂O', ''], 'agua = 5,012 − 3,195 g · Cl = del AgCl · Fe = anhidro − Cl|divido todos los moles entre los de Fe → FeCl₂·4 H₂O')

S['P7-4.4'] = ([{'title': '1. Sulfatos: 6,00 L', 'ions': [('SO₄²⁻', 'r'), ('Cl⁻', 'e'), ('Na⁺', 'e')], 'note': ['evaporo hasta el 5 %', '(los moles NO cambian)']},
                {'title': '2. + BaCl₂', 'ions': [('Ba²⁺', 'r'), ('Cl⁻', 'e')], 'solid': 'BaSO₄ 96,5 mg', 'note': ['todo el SO₄²⁻ precipita']},
                {'title': '3. Cloruros: 10,0 mL', 'kind': 'flask', 'burette': 'AgNO₃ 0,03360 M', 'ions': [('Cl⁻', 'r')], 'note': ['gasta 1,35 mL', 'Ag⁺ + Cl⁻ → AgCl']}],
               ['', ''], 'ppm de SO₄²⁻ = mg de SO₄²⁻ ÷ 6,00 L de agua ORIGINAL|ppm de Cl⁻ = mg de Cl⁻ ÷ 0,0100 L')

S['P7-4.5'] = grav('1. Disolución de CuCl₂', [('Cu²⁺', 'r'), ('Cl⁻', 'e'), ('Cu²⁺', 'r'), ('Cl⁻', 'e')], ['587 mL (de 150 g', 'de mineral)'], 'OH⁻', 'Cu(OH)₂', ['gasta 41,7 mL de', 'NaOH 0,75 M'],
                   'CuO', '¿g?', ['lo que piden'], 'Cu²⁺ + 2 OH⁻ → Cu(OH)₂ → (calor) → CuO|mol de Cu = mol de OH⁻ ÷ 2 = mol de CuO', ('+ NaOH', ''))

S['P7-4.6'] = ([{'title': '1. Mezcla disuelta', 'ions': [('Na⁺', 'e'), ('Cl⁻', 'r'), ('Ca²⁺', 'e'), ('Cl⁻', 'r')], 'note': ['0,8870 g de NaCl + CaCl₂']},
                {'title': '2. + AgNO₃ (exceso)', 'ions': [('Ag⁺', 'r'), ('NO₃⁻', 'e')], 'solid': 'AgCl', 'note': ['TODO el Cl⁻ precipita']},
                {'title': '3. Peso', 'kind': 'balance', 'solid': 'AgCl', 'mass': '2,210 g', 'note': ['= mol de Cl⁻ total']}],
               ['', 'filtro|y seco'], 'mol Cl⁻ = mol NaCl + 2 · mol CaCl₂ (el CaCl₂ lleva 2 Cl)|x g de NaCl y (0,8870 − x) g de CaCl₂')

S['P7-4.7'] = ([{'title': '1. Antiácido + HCl', 'ions': [('H⁺', 'r'), ('Cl⁻', 'e'), ('Al³⁺', 'p'), ('Mg²⁺', 'p')], 'note': ['0,600 g + 50,0 mL HCl', 'Al(OH)₃ y Mg(OH)₂ se disuelven']},
                {'title': '2. Valoro el HCl que sobra', 'kind': 'flask', 'burette': 'NaOH 0,377 M', 'ions': [('H⁺', 'x')], 'note': ['16,5 mL → OH⁻ totales', 'del antiácido']},
                {'title': '3. Gravimetría del Mg', 'kind': 'balance', 'solid': 'Mg₂P₂O₇', 'mass': '303 mg', 'note': ['→ mol de Mg(OH)₂']}],
               ['', ''], 'Gravimetría → Mg(OH)₂ · Retrovaloración → OH⁻ totales|OH⁻ del Al(OH)₃ = totales − 2·mol Mg(OH)₂ → ÷ 3 → mol Al(OH)₃')

# ---------- apartado 6 ----------
def titr(t1, ions1, n1, bur, ions2, n2, t3_lines, bottom, arrows=('', ''), extra=None):
    ps = [{'title': t1, 'ions': ions1, 'note': n1},
          {'title': '2. Valoro', 'kind': 'flask', 'burette': bur, 'ions': ions2, 'note': n2},
          {'title': '3. Qué saco', 'kind': 'text', 'lines': t3_lines}]
    return (ps, list(arrows), bottom)

S['P7-6.1'] = titr('1. Hidracina', [('N₂H₄', 'r'), ('N₂H₄', 'r')], ['30,0 mL de N₂H₄ 0,1622 M'], 'KIO₃ 0,1070 M', [('N₂H₄', 'r'), ('IO₃⁻', 'r')], ['¿cuántos mL?'],
                   ['mol N₂H₄', '× 4/5', '= mol IO₃⁻ → V'], '4 IO₃⁻ + 5 N₂H₄ + 4 H⁺ → 5 N₂ + 2 I₂ + 12 H₂O', ('', ''))

S['P7-6.2'] = ([{'title': '1. Sangre + oxalato', 'ions': [('Ca²⁺', 'r'), ('C₂O₄²⁻', 'r')], 'solid': 'CaC₂O₄', 'note': ['10,0 mL de sangre', 'todo el Ca precipita']},
                {'title': '2. Disuelvo en H₂SO₄', 'ions': [('H₂C₂O₄', 'r'), ('Ca²⁺', 'e'), ('SO₄²⁻', 'e')], 'note': ['1 Ca → 1 oxalato']},
                {'title': '3. Valoro el oxalato', 'kind': 'flask', 'burette': 'KMnO₄ 9,56·10⁻⁴ M', 'ions': [('H₂C₂O₄', 'r')], 'color': '#F4C0D1', 'note': ['24,2 mL (vira a rosa)']}],
               ['filtro', ''], 'Camino: Ca²⁺ → CaC₂O₄ → H₂C₂O₄ → gasta MnO₄⁻|2 MnO₄⁻ por cada 5 oxálicos → mol de Ca → μg/mL')
S['P7-6.3'] = S['P7-6.2']

S['P7-6.4'] = ([{'title': '1. Agua residual', 'ions': [('CrO₄²⁻', 'r'), ('Na⁺', 'e'), ('OH⁻', 'e')], 'note': ['100,0 L, 0,0148 M', 'en medio básico']},
                {'title': '2. + ditionito', 'ions': [('S₂O₄²⁻', 'r'), ('SO₃²⁻', 'p'), ('Na⁺', 'e')], 'solid': 'Cr(OH)₃', 'note': ['el Cr(OH)₃ precipita', 'el SO₃²⁻ queda disuelto']},
                {'title': '3. Lo que piden', 'kind': 'text', 'lines': ['g de Na₂S₂O₄', 'g de Cr(OH)₃']}],
               ['+ Na₂S₂O₄', ''], '2 CrO₄²⁻ + 3 S₂O₄²⁻ + 2 H₂O + 2 OH⁻ → 2 Cr(OH)₃ + 6 SO₃²⁻|ajuste en medio BÁSICO: primero en ácido y luego + OH⁻ a los dos lados')

S['P7-6.5'] = titr('1. Muestra con I⁻', [('I⁻', 'r'), ('K⁺', 'e')], ['250 mL', '+ HCl'], 'Ce⁴⁺ 0,050 M', [('I⁻', 'r'), ('Cl⁻', 'e')], ['gasta 20,0 mL'],
                   ['I⁻ → ICl: 2 e⁻', 'Ce⁴⁺ → Ce³⁺: 1 e⁻', '2 Ce⁴⁺ por I⁻'], 'mol I⁻ = mol Ce⁴⁺ ÷ 2 → mg de I ÷ 250 mL')

S['P7-6.6'] = titr('1. Agua oxigenada', [('H₂O₂', 'r'), ('H⁺', 'e')], ['5,00 mL', '+ H₂SO₄'], 'KMnO₄ 0,01250 M', [('H₂O₂', 'r')], ['gasta 28,0 mL'],
                   ['mol MnO₄⁻ × 5/2', '= mol H₂O₂', '→ g → %'], '2 MnO₄⁻ + 5 H₂O₂ + 6 H⁺ → 2 Mn²⁺ + 5 O₂ + 8 H₂O|% en peso: 5,00 mL ≈ 5,00 g (densidad ≈ 1)')

S['P7-6.7'] = titr('1. Disolución saturada', [('C₂O₄²⁻', 'r'), ('Na⁺', 'e')], ['5,00 mL de Na₂C₂O₄', 'saturada'], 'KMnO₄ 0,02140 M', [('C₂O₄²⁻', 'r')], ['gasta 25,8 mL'],
                   ['mol MnO₄⁻ × 5/2', '= mol oxalato', '÷ 5,00 mL → g/L'], 'La "solubilidad" es solo la concentración de la saturada (g/L)')

S['P7-6.8'] = ([{'title': '1. Aleación + HNO₃', 'bar': ('Cu + Au', False), 'ions': [('H⁺', 'r'), ('NO₃⁻', 'r'), ('H⁺', 'r'), ('NO₃⁻', 'r')], 'note': ['100,0 g (85 % Cu)', 'HNO₃ comercial 62 %']},
                {'title': '2. Se disuelve el Cu', 'bar': ('Au', False), 'gas': 'NO₂', 'ions': [('Cu²⁺', 'p'), ('NO₃⁻', 'e')], 'note': ['el Au no reacciona', '(se recupera)']},
                {'title': '3. Cuánto ácido', 'kind': 'text', 'lines': ['1 Cu gasta 4 HNO₃', 'g puros → g comercial', '→ mL (densidad)']}],
               ['', ''], 'Cu + 4 HNO₃ → Cu(NO₃)₂ + 2 NO₂ + 2 H₂O (en especies NEUTRAS)|el HNO₃ hace de oxidante (→ NO₂) y además pone los NO₃⁻ del Cu(NO₃)₂')

S['P7-6.9'] = titr('1. Agua oxigenada', [('H₂O₂', 'r')], ['20,00 mL de producto', '+ 20 mL de agua'], 'KMnO₄ 0,1050 M', [('H₂O₂', 'r')], ['gasta 15,5 mL'],
                   ['mol H₂O₂', 'estaban en los', '20,00 mL de producto'], 'El agua que añado no cambia los moles: divido entre los 20,00 mL del producto')

S['P7-6.10'] = titr('1. Mineral disuelto', [('Fe²⁺', 'r'), ('Cl⁻', 'e')], ['0,9132 g → Fe²⁺'], 'K₂Cr₂O₇ 0,05051 M', [('Fe²⁺', 'r')], ['gasta 28,72 mL'],
                    ['1 Cr₂O₇²⁻', 'oxida 6 Fe²⁺', '→ g Fe → %'], 'Cr₂O₇²⁻ + 6 Fe²⁺ + 14 H⁺ → 2 Cr³⁺ + 6 Fe³⁺ + 7 H₂O')

S['P7-6.11'] = ([{'title': '1. Mineral en 500 mL', 'ions': [('Fe²⁺', 'r'), ('Cl⁻', 'e'), ('Fe²⁺', 'r')], 'note': ['0,9132 g → Fe²⁺']},
                 {'title': '2. Valoro 50 mL', 'kind': 'flask', 'burette': 'K₂Cr₂O₇ 0,00506 M', 'ions': [('Fe²⁺', 'r')], 'note': ['gasta 32,03 mL']},
                 {'title': '3. Alícuota', 'kind': 'text', 'lines': ['mol Fe en 50 mL', '× 500/50 = × 10', '→ toda la muestra']}],
                ['cojo|50 mL', ''], '1 Cr₂O₇²⁻ por 6 Fe²⁺ y luego × 10 por la alícuota')

S['P7-6.12'] = ([{'title': '1. Patrón pesado', 'kind': 'balance', 'solid': 'K₂Cr₂O₇', 'mass': '1,692 g', 'note': ['en 500,0 mL']},
                 {'title': '2. Cojo 25,00 mL', 'ions': [('Cr₂O₇²⁻', 'r'), ('K⁺', 'e')], 'note': ['25,00 de 500,0 mL']},
                 {'title': '3. Valoro con FeSO₄', 'kind': 'flask', 'burette': 'FeSO₄ ¿M?', 'ions': [('Cr₂O₇²⁻', 'r')], 'note': ['gasta 13,76 mL']}],
                ['', ''], 'mol Cr₂O₇²⁻ en los 25 mL × 6 = mol Fe²⁺ → ÷ 13,76 mL = [FeSO₄]')

S['P7-6.13'] = ([{'title': '1. [H₂O₂] con MnO₄⁻', 'kind': 'flask', 'burette': 'KMnO₄ 0,5000 M', 'ions': [('H₂O₂', 'r')], 'note': ['50,0 mL gastan 32,10 mL', 'H₂O₂ = REDUCTOR']},
                 {'title': '2. H₂O₂ + Fe²⁺', 'ions': [('H₂O₂', 'r'), ('Fe²⁺', 'r'), ('Fe³⁺', 'p')], 'note': ['50,00 g de FeSO₄', 'H₂O₂ = OXIDANTE']},
                 {'title': '3. Volumen', 'kind': 'text', 'lines': ['1 H₂O₂ por 2 Fe²⁺', 'mol H₂O₂ ÷ [H₂O₂]', '= mL']}],
                ['', ''], 'El H₂O₂ cambia de papel: con MnO₄⁻ se oxida (→ O₂) y con Fe²⁺ se reduce (→ H₂O)')

S['P7-6.14'] = titr('1. Disolución de H₂O₂', [('H₂O₂', 'r')], ['25,00 mL'], 'KMnO₄ 0,01652 M', [('H₂O₂', 'r')], ['gasta 36,44 mL'],
                    ['mol MnO₄⁻ × 5/2', '÷ 25,00 mL', '= [H₂O₂]'], '2 MnO₄⁻ + 5 H₂O₂ + 6 H⁺ → 2 Mn²⁺ + 5 O₂ + 8 H₂O')

S['P7-6.15'] = ([{'title': '1. Yodato', 'ions': [('IO₃⁻', 'r'), ('K⁺', 'e')], 'note': ['1,390 g de KIO₃ (I = +5)']},
                 {'title': '2. + sulfito', 'ions': [('SO₃²⁻', 'r'), ('SO₄²⁻', 'p'), ('I?', 'p')], 'note': ['32,5 mL de SO₃²⁻ 0,500 M', 'cada SO₃²⁻ cede 2 e⁻']},
                 {'title': '3. Cuento e⁻', 'kind': 'text', 'lines': ['e⁻ cedidos ÷ mol de I', '= 5 e⁻ por I', '+5 → 0: I₂']}],
                ['', ''], 'Si no te dicen el producto, cuéntalo con electrones: e⁻ cedidos = e⁻ captados')

S['P7-6.16'] = ([{'title': '1. Óxido de Fe', 'kind': 'balance', 'solid': 'FeₓOᵧ', 'mass': '0,2729 g', 'note': ['se disuelve → Fe²⁺']},
                 {'title': '2. Valoro el Fe²⁺', 'kind': 'flask', 'burette': 'KMnO₄ 0,01621 M', 'ions': [('Fe²⁺', 'r')], 'note': ['gasta 42,17 mL']},
                 {'title': '3. Fórmula', 'kind': 'text', 'lines': ['g Fe (valoración)', 'g O = total − Fe', 'O/Fe = 1,5 → Fe₂O₃']}],
                ['', ''], '1 MnO₄⁻ oxida 5 Fe²⁺ → mol Fe; el O es lo que falta hasta 0,2729 g')

S['P7-6.17'] = ([{'title': '1. Todo el As → AsH₃', 'ions': [('AsH₃', 'r'), ('AsH₃', 'r')], 'note': ['6,20 g → 100 mL']},
                 {'title': '2. Valoro 10 mL', 'kind': 'flask', 'burette': 'K₂Cr₂O₇ 0,0125 M', 'ions': [('AsH₃', 'r')], 'note': ['gasta 36,7 mL']},
                 {'title': '3. Electrones', 'kind': 'text', 'lines': ['As: −3 → +5 (8 e⁻)', 'Cr₂O₇²⁻: 6 e⁻', '× 10 (alícuota)']}],
                ['cojo|10 mL', ''], '8 · mol As = 6 · mol Cr₂O₇²⁻ → mol As en 10 mL → × 10 → %As')

S['P7-6.18'] = ([{'title': '1. Disolución A (100 mL)', 'ions': [('Fe²⁺', 'r'), ('Ba²⁺', 'r'), ('Cl⁻', 'e')], 'note': ['4,000 g de mineral']},
                 {'title': '2. Fe: 50 mL', 'kind': 'flask', 'burette': 'K₂Cr₂O₇ 0,0250 M', 'ions': [('Fe²⁺', 'r')], 'note': ['gasta 15,04 mL', '× 2 (alícuota)']},
                 {'title': '3. Ba: 5 mL', 'ions': [('SO₄²⁻', 'r')], 'solid': 'BaSO₄ 0,1366 g', 'note': ['+ H₂SO₄ y peso', '× 20 (alícuota)']}],
                ['', ''], 'Dos análisis distintos de la MISMA disolución con alícuotas distintas (50 mL y 5 mL)')

S['P7-6.19'] = ([{'title': '1. Aire con SO₂', 'liquid': False, 'ions': [('SO₂', 'r'), ('N₂', 'e'), ('O₂', 'e')], 'note': ['10 L (2011) o 100 L (2012)']},
                 {'title': '2. Burbujeo en 250 mL', 'ions': [('SO₂', 'r'), ('SO₂', 'r')], 'note': ['todo el SO₂ se disuelve']},
                 {'title': '3. Valoro 10 mL', 'kind': 'flask', 'burette': 'KMnO₄ 8,00·10⁻³ M', 'ions': [('SO₂', 'r')], 'note': ['gasta 7,35 mL', '× 25 (alícuota)']}],
                ['', 'cojo|10 mL'], '2 MnO₄⁻ + 5 SO₂ + 2 H₂O → 2 Mn²⁺ + 5 SO₄²⁻ + 4 H⁺|mol SO₂ → g, o → volumen (PV = nRT) → % en volumen')

S['P7-6.20'] = ([{'title': '1. Cu²⁺ + KI', 'ions': [('Cu²⁺', 'r'), ('I⁻', 'r'), ('K⁺', 'e')], 'solid': 'CuI', 'note': ['2 Cu²⁺ → 1 I₂']},
                 {'title': '2. Se forma I₂', 'ions': [('I₂', 'p'), ('K⁺', 'e')], 'color': '#F5E1B8', 'note': ['(color pardo)']},
                 {'title': '3. Valoro el I₂', 'kind': 'flask', 'burette': 'S₂O₃²⁻ 0,200 M', 'ions': [('I₂', 'r')], 'note': ['gasta 76,5 mL', '1 I₂ gasta 2 S₂O₃²⁻']}],
                ['', ''], 'El I₂ es solo un intermediario: 2 Cu²⁺ → 1 I₂ → 2 S₂O₃²⁻ ⇒ 1 Cu por cada S₂O₃²⁻')

S['P7-6.21'] = ([{'title': '1. NaI pesado', 'kind': 'balance', 'solid': 'NaI', 'mass': '2,0031 g'},
                 {'title': '2. Oxido → I₂', 'ions': [('I₂', 'p'), ('Na⁺', 'e')], 'color': '#F5E1B8', 'note': ['todo el I⁻ → I₂']},
                 {'title': '3. Valoro el I₂', 'kind': 'flask', 'burette': 'S₂O₃²⁻ ¿M?', 'ions': [('I₂', 'r')], 'note': ['gasta 20,4 mL']}],
                ['', ''], '2 I⁻ → 1 I₂ → 2 S₂O₃²⁻ ⇒ 1 I⁻ por cada S₂O₃²⁻')

S['P7-6.22'] = ([{'title': '1. Sn + HNO₃ (exceso)', 'bar': ('Sn', False), 'ions': [('H⁺', 'r'), ('NO₃⁻', 'r'), ('H⁺', 'r'), ('NO₃⁻', 'r')], 'note': ['1,00 L de HNO₃ 1,000 M']},
                 {'title': '2. Reacciona', 'gas': 'NO₂', 'ions': [('H⁺', 'x'), ('NO₃⁻', 'x')], 'solid': 'SnO₂', 'note': ['sobra HNO₃']},
                 {'title': '3. Valoro 10 mL', 'kind': 'flask', 'burette': 'NaOH 0,1250 M', 'ions': [('H⁺', 'x')], 'note': ['gasta 28,3 mL', '× 100 (alícuota)']}],
                ['Sn + 4 HNO₃ →', 'cojo|10 mL'], 'HNO₃ que reaccionó = añadido − sobrante → ÷ 4 → mol de Sn|(el dato de la muestra estaba mal: el profesor lo corrige)')

S['P7-6.23'] = ([{'title': '1. MnO₂ + oxálico (exceso)', 'ions': [('H₂C₂O₄', 'r'), ('H⁺', 'e')], 'solid': 'MnO₂', 'note': ['1,179 g de oxálico']},
                 {'title': '2. Reacciona', 'gas': 'CO₂', 'ions': [('Mn²⁺', 'p'), ('H₂C₂O₄', 'x')], 'note': ['sobra oxálico']},
                 {'title': '3. Valoro lo que sobra', 'kind': 'flask', 'burette': 'KMnO₄ 0,1000 M', 'ions': [('H₂C₂O₄', 'x')], 'note': ['gasta 30,06 mL']}],
                ['MnO₂ + H₂C₂O₄ →', ''], 'Retrovaloración REDOX: oxálico que reaccionó = añadido − sobrante|MnO₂ : oxálico = 1 : 1')

S['P7-6.24'] = ([{'title': '1. Caliza disuelta', 'ions': [('Ca²⁺', 'r'), ('C₂O₄²⁻', 'r')], 'solid': 'CaC₂O₄', 'note': ['5,18 g de caliza']},
                 {'title': '2. En H₂SO₄ (100 mL)', 'ions': [('H₂C₂O₄', 'r'), ('SO₄²⁻', 'e')], 'note': ['cojo 10,0 mL']},
                 {'title': '3. Valoro', 'kind': 'flask', 'burette': 'KMnO₄ 0,0500 M', 'ions': [('H₂C₂O₄', 'r')], 'note': ['gasta 40,0 mL', '× 10 (alícuota)']}],
                ['filtro', ''], 'Ca → CaC₂O₄ → H₂C₂O₄ → MnO₄⁻ (2 MnO₄⁻ : 5 ox) · 1 Ca = 1 CaO')

S['P7-6.25'] = ([{'title': '1. KIO₃ + KI + H₂SO₄', 'ions': [('IO₃⁻', 'r'), ('I⁻', 'x'), ('H⁺', 'r'), ('K⁺', 'e')], 'note': ['¿quién limita? el KIO₃']},
                 {'title': '2. Se forma I₂', 'ions': [('I₂', 'p'), ('K⁺', 'e')], 'color': '#F5E1B8', 'note': ['1 IO₃⁻ → 3 I₂']},
                 {'title': '3. Valoro el I₂', 'kind': 'flask', 'burette': 'S₂O₃²⁻ 0,24 M', 'ions': [('I₂', 'r')], 'note': ['1 I₂ gasta 2 S₂O₃²⁻']}],
                ['', ''], 'IO₃⁻ + 5 I⁻ + 6 H⁺ → 3 I₂ + 3 H₂O|1 IO₃⁻ → 3 I₂ → 6 S₂O₃²⁻')

S['P7-6.26'] = ([{'title': '1. Oxálico (15,0 mL)', 'ions': [('H₂C₂O₄', 'r'), ('H₂C₂O₄', 'r')], 'note': ['¿cuántos moles?']},
                 {'title': '2. Ácido-base', 'kind': 'flask', 'burette': 'NaOH 0,149 M', 'ions': [('H₂C₂O₄', 'r')], 'note': ['25,2 mL · 2 NaOH por ox']},
                 {'title': '3. Redox', 'kind': 'flask', 'burette': 'KMnO₄ 0,122 M', 'ions': [('H₂C₂O₄', 'r')], 'note': ['¿mL? · 2 MnO₄⁻ : 5 ox']}],
                ['', ''], 'La misma muestra valorada de dos formas: con NaOH (ácido-base) y con MnO₄⁻ (redox)')

S['P7-6.27'] = ([{'title': '1. Fe²⁺ y Fe³⁺ (25,0 mL)', 'ions': [('Fe²⁺', 'r'), ('Fe³⁺', 'e'), ('Fe²⁺', 'r')], 'note': ['el MnO₄⁻ solo ve el Fe²⁺']},
                 {'title': '2. MnO₄⁻ → Fe²⁺', 'kind': 'flask', 'burette': 'KMnO₄ 0,0200 M', 'ions': [('Fe²⁺', 'r')], 'note': ['gasta 23,0 mL → Fe²⁺']},
                 {'title': '3. Zn y luego Cr₂O₇²⁻', 'kind': 'flask', 'burette': 'K₂Cr₂O₇ 0,0150 M', 'ions': [('Fe²⁺', 'r')], 'note': ['40,0 mL → Fe TOTAL']}],
                ['', 'Zn: todo|a Fe²⁺'], 'Fe³⁺ = Fe total (dicromato) − Fe²⁺ (permanganato)')

S['P7-6.28'] = ([{'title': '1. Estandarizo FeSO₄', 'kind': 'flask', 'burette': 'FeSO₄ ¿M?', 'ions': [('Cr₂O₇²⁻', 'r')], 'note': ['1,0346 g de K₂Cr₂O₇', 'gasta 20,32 mL']},
                 {'title': '2. KMnO₄ comercial', 'kind': 'balance', 'solid': 'KMnO₄ impuro', 'mass': '0,9560 g'},
                 {'title': '3. Lo valoro', 'kind': 'flask', 'burette': 'FeSO₄ 1,0385 M', 'ions': [('MnO₄⁻', 'r')], 'color': '#F4C0D1', 'note': ['gasta 25,64 mL']}],
                ['', ''], '1.º [FeSO₄] con el dicromato (1 : 6) · 2.º KMnO₄ puro con el FeSO₄ (1 : 5) → riqueza')
