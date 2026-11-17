<div class="portada" markdown="1">

# Tema 7 · Reacciones químicas

**Química General · 1.º de Bioquímica · 2.º parcial**

Teoría necesaria (clases del profesor + diapositivas) · método paso a paso · **todos** los problemas de examen 2011–2026 y los ejercicios de clase, clasificados por tipo y del más reciente al más antiguo

</div>

<div class="newpage"></div>

## Cómo usar este documento

- Cada apartado empieza por la **teoría necesaria**: lo que dijo el profesor en clase (marcado como *"en clase"*) y lo de las diapositivas.
- Después vienen los **ejercicios de clase** (EC 7.x) y los **problemas de examen**, agrupados por **tipo** (banda morada). Cada tipo tiene un **"Cómo se hace"**, **trampas** y **"Se repite en…"**.
- En cada problema de examen aparece el **recorte del PDF del profesor** (enunciado + su resultado) y debajo el **desarrollo paso a paso**.
- **Problemas que mezclan temas:** si el matiz es de un tema posterior, aquí solo hay un **aviso** y se resuelven en ese tema.

### El método que sirve para todo el parcial (lo repite en todas las clases)

1. **Entender qué pasa** — *"imagínate que lo haces en el laboratorio, con tus gafas y tu bata"*: qué reacciona, qué no, qué precipita, qué gas sale, qué sobra, para qué se hace cada paso. Hay datos que sobran.
2. **Escribir la reacción y ajustarla.** *"Cuando tengo la reacción ajustada, ya he ganado la mitad del ejercicio. Si considero todas las reacciones mol a mol, voy abocado al precipicio."*
3. **Factores de conversión encadenados**, con "apellidos" en las unidades (g *de aleación*, mol *de Al*…). Si las unidades se cancelan, el cálculo está bien. En **una sola operación**, sin redondear entre pasos.
4. **Cifras significativas**: al multiplicar/dividir, las del dato con menos cifras; al **sumar/restar, los decimales**. Los 100 de los % y los coeficientes estequiométricos son exactos.

> *"Los problemas van a ser siempre completamente nuevos… no intentes tirar de memoria porque lo más seguro es que haya cambiado algo."* — Siempre pregunta lo mismo, pero nunca repite igual, y mete trampas.

### El esquema de moles (la columna vertebral de todos los problemas)

<div class="tex">\text{dato} \xrightarrow{\;M\cdot V,\ m/M\;} \text{mol de lo que sé} \xrightarrow{\;\text{coeficientes}\;} \text{mol de lo que busco} \xrightarrow{\;\times M,\ \div V,\ \times\frac{V_{total}}{V_{alícuota}}\;} \text{lo que piden}</div>

## Índice del tema y recuento

| Apartado | Teoría (exámenes) | Problemas de examen | Ejercicios de clase |
|---|---|---|---|
| 1. Estequiometría, limitante, rendimiento | 1 | 5 | EC 7.1, 7.2, 7.3 |
| 2. Reacciones en disolución acuosa | 0 | 0 | — |
| 3. Ácido-base: valoraciones y retrovaloraciones | 0 | 8 | EC 7.4 |
| 4. Precipitación y gravimetría | 1 | 7 | EC 7.5 |
| 5. Formación de complejos | 0 | 0 (todos → tema 12) | — |
| 6. Oxidación-reducción | 0 | 33 (en 28 fichas: los repetidos van juntos) | EC 7.6 |
| 7. Reacciones de química molecular | 0 | 0 | — |
| **Total** | **2** | **53** | **6** |

Avisos (problemas del tema 7 que se resuelven en otro tema): 6, listados en cada apartado.


<div class="newpage"></div>

## Caja de herramientas: las 8 operaciones que salen en todos los problemas

Antes de los problemas, estas son **todas** las cuentas que vas a necesitar. Si las tienes claras, cada problema es combinarlas en el orden correcto.

| # | Si tengo… | y quiero… | hago… | ejemplo |
|---|---|---|---|---|
| 1 | gramos de una sustancia | moles | **n = m / M** (divido por la masa molar) | 10,0 g de NaOH / 40,00 g/mol = 0,250 mol |
| 2 | moles | gramos | **m = n · M** | 0,250 mol · 40,00 g/mol = 10,0 g |
| 3 | volumen y molaridad de una disolución | moles de soluto | **n = M · V** (V en **litros**) | 25,0 mL = 0,0250 L · 0,100 M = 2,50·10⁻³ mol |
| 4 | moles y volumen | molaridad | **M = n / V** | 2,50·10⁻³ mol / 0,0100 L = 0,250 M |
| 5 | moles de A | moles de B | **regla de tres con los coeficientes** de la reacción ajustada | si 2 A → 1 B: n(B) = n(A) · 1/2 |
| 6 | lo que hay en una **alícuota** (un trocito que he cogido) | lo que hay en **toda** la disolución | **× V_total / V_alícuota** | 10 mL de 100 mL → × 10 |
| 7 | masa de una disolución comercial | masa del compuesto puro | **× riqueza / 100**; y si me dan volumen, antes **× densidad** | 10 mL · 1,19 g/mL · 37/100 = 4,40 g de HCl |
| 8 | masa del analito y masa de muestra | porcentaje / ppm | **% = m_analito / m_muestra · 100** · **ppm = m_analito / m_muestra · 10⁶** (≈ mg/L en agua) | 0,25 g / 2,00 g · 100 = 12,5 % |

**Truco de los mililitros:** mL × M = **mmol** (milimoles). Si trabajas todo en mmol y mL, no tienes que pasar a litros: 25,0 mL × 0,100 M = 2,50 mmol.

### Cómo están explicadas las soluciones

Todas siguen el mismo guion, que es el que tienes que seguir tú en el examen:

1. **Datos** (lo que me dan) y **qué me piden**.
2. **¿Qué está pasando?** — contado como si lo hicieras en el laboratorio.
3. **La reacción ajustada**, explicando cómo se ajusta.
4. **El plan**: en qué orden voy a ir de los datos al resultado.
5. **Los cálculos, uno por paso**, cada uno con **por qué** lo hago.
6. **Resultado** con sus cifras significativas.
7. **Lo que tienes que llevarte** de ese problema (la idea que se repite en otros).


<div class="newpage"></div>

## 1. Reacción química. Estequiometría

### Teoría necesaria

**Reacción y ecuación química.** Reactivos → productos, con su **estado físico**: (g), (l), (s), (aq). En una reacción los átomos **se reorganizan**: el número de átomos de cada tipo es el mismo antes y después (conservación de la masa). Los números que ajustan la ecuación son los **coeficientes estequiométricos** y dicen **cuántos moles** de cada especie intervienen.

**Ajuste por tanteo** (diapositivas): 1) primero los elementos que aparecen en un solo compuesto a cada lado; 2) al final los elementos libres (O₂, H₂, metales); 3) los grupos que no cambian (SO₄²⁻, NO₃⁻…) se ajustan como una unidad; 4) se pueden usar fracciones y quitarlas al final multiplicando.

**Reacciones consecutivas** (en clase): los productos de una son los reactivos de la siguiente. **Se pueden sumar** en una **reacción neta**; lo que se forma y se gasta son **intermedios de reacción**.

**Reacciones simultáneas** (en clase): independientes, aunque compartan reactivo o producto. **No se suman**: si sumas la combustión del CH₄ y la del C₂H₆, obligas a que reaccione un CH₄ por cada C₂H₆, y con 99 CH₄ y 1 C₂H₆ no quedan 98 CH₄ sin reaccionar.

**Reactivo limitante.** El que se gasta primero y para la reacción; **los productos se calculan siempre desde él**. Para encontrarlo: calcula cuánto necesitarías del otro reactivo y compáralo con lo que tienes.

**Rendimiento.** La reacción puede no ir al 100 % (equilibrio, reacciones secundarias).

$$\%\ \text{rendimiento}=\frac{\text{lo que obtengo de verdad}}{\text{lo que obtendría al 100 \%}}\times100$$

- Me dan reactivos y busco producto → **× rendimiento/100** (obtengo menos).
- Me dan el producto que quiero y busco reactivo → **÷ rendimiento/100** (necesito más).

#### Teoría · Tipo A · Reacciones consecutivas y simultáneas

##### T7-1.1 · 1ª convocatoria (Enero), 23 de enero de 2025 (ej. 1b)

[[SOL 180:100-255]]

> **Respuesta de 10:** En las **consecutivas**, los productos de una reacción son los reactivos de la siguiente (A → B → C); se pueden sumar en una reacción neta y las especies que se forman y se consumen son intermedios de reacción. Las **simultáneas** son reacciones independientes que ocurren a la vez (p. ej., la combustión de una mezcla de CH₄ y C₂H₆): **no se pueden sumar**, porque eso impondría una relación fija entre ambas que no existe; cada una se trata con su propia estequiometría.



### Ejercicios de clase

##### EC 7.1 · Ejercicio de clase (resuelto en la pizarra) · Aleación Al/Cu + HCl

<div class="enun" markdown="1">
Una aleación que se emplea en estructuras de aviones está formada por 93,7% de Al y 6,3% de Cu. La aleación tiene una densidad de 2,85 g/cm³. Una pieza de 0,691 cm³ de esta aleación reacciona con un exceso de HCl(aq). Si suponemos que todo el Al pero nada del Cu reacciona con el HCl(aq), ¿qué masa de H₂ se obtiene? M(Al) = 26,98 g/mol; M(H₂) = 2,0159 g/mol
</div>

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_EC_7_1.svg 100%]]


**Datos:** V(pieza) = 0,691 cm³ · densidad = 2,85 g de aleación/cm³ · 93,7 % de Al. **Me piden:** masa de H₂ (g).

**¿Qué pasa?** Echo la pieza en HCl. El Cu no reacciona; el Al sí y burbujea H₂. Que sea "de aviones" o el 6,3 % de Cu **no sirve para nada**.

**Reacción.** Metal + ácido → sal del metal + H₂. El Al forma Al³⁺ → la sal es AlCl₃. Sin ajustar: Al + HCl → AlCl₃ + H₂. Hay 3 Cl a la derecha → pongo **3 HCl**; entonces hay 3 H a la izquierda → **3/2 H₂** a la derecha:

$$\text{Al}+3\,\text{HCl}\rightarrow\text{AlCl}_3+\tfrac32\,\text{H}_2$$

**Plan:** cm³ de pieza → g de pieza → g de Al → mol de Al → mol de H₂ → g de H₂.

**Paso 1 · Masa de la pieza.** La densidad dice cuántos gramos pesa cada cm³:

$$\text{m} = \text{densidad} \cdot \text{V}$$

$$\text{m(pieza)} = 2{,}85\ \text{g/cm}^{3} \cdot 0{,}691\ \text{cm}^{3} = 1{,}969\ \text{g de aleación}$$


**Paso 2 · Masa de Al.**

De cada 100 g de aleación, 93,7 g son Al:

$$\text{m(Al)} = \text{m(pieza)} \cdot \text{\%/}\ 100$$

$$\text{m(Al)} = 1{,}969\ \text{g de aleación} \cdot \dfrac{93{,}7\ \text{g de Al}}{100\ \text{g de aleación}} = 1{,}845\ \text{g de Al}$$


**Paso 3 · Moles de Al.**

$$\text{n} = \dfrac{\text{m}}{\text{M}}$$

$$\text{n(Al)} = \dfrac{1{,}845\ \text{g de Al}}{26{,}98\ \text{g/mol}} = 0{,}06839\ \text{mol de Al}$$


**Paso 4 · Moles de H₂.** La reacción dice: 1 mol de Al → 3/2 mol de H₂
$$\text{n(H}_{2}\text{)} = 0{,}06839\ \text{mol de Al} \cdot \dfrac{3\text{/}\ 2\ \text{mol de H}_{2}}{1\ \text{mol de Al}} = 0{,}1026\ \text{mol de H}_{2}$$


**Paso 5 · Masa de H₂.**

$$\text{m} = \text{n} \cdot \text{M}$$

$$\text{m(H}_{2}\text{)} = 0{,}1026\ \text{mol de H}_{2} \cdot 2{,}0159\ \text{g/mol} = 0{,}2068\ \text{g de H}_{2}$$


**Cifras:** los datos tienen 3 cifras (0,691; 2,85; 93,7) → **0,207 g de H₂**.

**Resumen, como lo escribió el profesor** (los mismos 5 pasos seguidos, sin redondear entre ellos):

$$0{,}691\,\text{cm}^3_{\text{aleación}}\cdot\frac{2{,}85\,\text{g}_{\text{aleación}}}{1\,\text{cm}^3_{\text{aleación}}}\cdot\frac{93{,}7\,\text{g Al}}{100\,\text{g}_{\text{aleación}}}\cdot\frac{1\,\text{mol Al}}{26{,}98\,\text{g Al}}\cdot\frac{3/2\,\text{mol H}_2}{1\,\text{mol Al}}\cdot\frac{2{,}0159\,\text{g H}_2}{1\,\text{mol H}_2}=0{,}207\,\text{g H}_2$$

**Lo que tienes que llevarte:** cada fracción de la cadena es uno de los pasos. Si las unidades con su "apellido" se van tachando (cm³ de aleación con cm³ de aleación, g de Al con g de Al…), está bien hecho.

##### EC 7.2 · Ejercicio de clase · Mezcla MgCO₃/Mg(OH)₂ + HCl

<div class="enun" markdown="1">
¿Cuántos gramos de HCl se consumen en la reacción de 425 g de una mezcla que contiene 35,2% de MgCO₃ y 64,8% de Mg(OH)₂ (% en masa, reacciones sin ajustar)? M(MgCO₃) = 84,31 g/mol, M(Mg(OH)₂) = 58,32 g/mol, M(HCl) = 36,46 g/mol. Mg(OH)₂ + HCl → MgCl₂ + H₂O; MgCO₃ + HCl → MgCl₂ + H₂O + CO₂(g)
</div>

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_EC_7_2.svg 100%]]


**Datos:** 425 g de mezcla · 35,2 % de MgCO₃ · 64,8 % de Mg(OH)₂. **Me piden:** masa de HCl gastado (g).

**¿Qué pasa?** Los dos componentes reaccionan con el HCl **cada uno por su lado** → son **simultáneas**: **no sumo las ecuaciones**; calculo el HCl de cada uno y al final sumo los **moles de HCl**.

**Ajuste:**
- Mg(OH)₂ + HCl → MgCl₂ + H₂O: 2 Cl a la derecha → **2 HCl**; ahora hay 2 + 2 = 4 H a la izquierda → **2 H₂O**: **Mg(OH)₂ + 2 HCl → MgCl₂ + 2 H₂O**
- MgCO₃ + HCl → MgCl₂ + H₂O + CO₂: 2 Cl → **2 HCl**; esos 2 H forman 1 H₂O ✓: **MgCO₃ + 2 HCl → MgCl₂ + H₂O + CO₂**

**Paso 1 · Masa de cada componente.**

$$\text{m} = \text{m(mezcla)} \cdot \text{\%/}\ 100$$

$$\text{m(MgCO}_{3}\text{)} = 425\ \text{g de mezcla} \cdot \dfrac{35{,}2\ \text{g MgCO}_{3}}{100\ \text{g de mezcla}} = 149{,}6\ \text{g de MgCO}_{3}$$

$$\text{m(Mg(OH)}_{2}\text{)} = 425\ \text{g de mezcla} \cdot \dfrac{64{,}8\ \text{g Mg(OH)}_{2}}{100\ \text{g de mezcla}} = 275{,}4\ \text{g de Mg(OH)}_{2}$$


**Paso 2 · Moles de cada uno.**

$$\text{n} = \text{m/M}$$

$$\text{n(MgCO}_{3}\text{)} = \dfrac{149{,}6\ \text{g}}{84{,}31\ \text{g/mol}} = 1{,}774\ \text{mol de MgCO}_{3}$$

$$\text{n(Mg(OH)}_{2}\text{)} = \dfrac{275{,}4\ \text{g}}{58{,}32\ \text{g/mol}} = 4{,}722\ \text{mol de Mg(OH)}_{2}$$


**Paso 3 · Moles de HCl que gasta cada uno** (los dos gastan 2 HCl por mol):
$$\text{n(HCl)}_{1} = 1{,}774\ \text{mol de MgCO}_{3} \cdot \dfrac{2\ \text{mol HCl}}{1\ \text{mol MgCO}_{3}} = 3{,}549\ \text{mol de HCl}$$

$$\text{n(HCl)}_{2} = 4{,}722\ \text{mol de Mg(OH)}_{2} \cdot \dfrac{2\ \text{mol HCl}}{1\ \text{mol Mg(OH)}_{2}} = 9{,}444\ \text{mol de HCl}$$

Total:

$$3{,}549 + 9{,}444 = 12{,}99\ \text{mol de HCl}$$


**Paso 4 · Masa de HCl.**

$$\text{m} = \text{n} \cdot \text{M} = 12{,}99\ \text{mol de HCl} \cdot 36{,}46\ \text{g/mol} = 474\ \text{g de HCl}$$


**Lo que tienes que llevarte:** con mezclas, **una reacción por componente** y se suman los moles al final.

##### EC 7.3 · Ejercicio de clase · PCl₃ (reactivo limitante)

<div class="enun" markdown="1">
El tricloruro de fósforo se obtiene por combinación directa del fósforo (P₄) y el cloro. ¿Qué masa de tricloruro de fósforo se forma en la reacción de 125 g de P₄ con 323 g de Cl₂? M(P₄) = 123,9 g/mol; M(Cl₂) = 70,91 g/mol; M(PCl₃) = 137,33 g/mol
</div>

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_EC_7_3.svg 100%]]


**Datos:** 125 g de P₄ · 323 g de Cl₂. **Me piden:** masa de PCl₃ (g).

**¿Qué pasa?** Me dan **los dos reactivos** → primero tengo que ver cuál se acaba antes (el limitante).

**Ajuste:** P₄ + Cl₂ → PCl₃. 4 P a la izquierda → **4 PCl₃**; eso son 12 Cl a la derecha → **6 Cl₂**: **P₄ + 6 Cl₂ → 4 PCl₃**

**Paso 1 · Moles de cada reactivo.**

$$\text{n} = \text{m/M}$$

$$\text{n(P}_{4}\text{)} = \dfrac{125\ \text{g}}{123{,}9\ \text{g/mol}} = 1{,}009\ \text{mol de P}_{4}$$

$$\text{n(Cl}_{2}\text{)} = \dfrac{323\ \text{g}}{70{,}91\ \text{g/mol}} = 4{,}555\ \text{mol de Cl}_{2}$$


**Paso 2 · ¿Quién es el limitante?** Calculo cuánto Cl₂ haría falta para gastar todo el P₄:
$$\text{n(Cl}_{2}\text{) necesario} = 1{,}009\ \text{mol de P}_{4} \cdot \dfrac{6\ \text{mol Cl}_{2}}{1\ \text{mol P}_{4}} = 6{,}05\ \text{mol de Cl}_{2}$$

Tengo solo 4,555 mol de Cl₂ < 6,05 mol → **el Cl₂ se acaba antes: es el limitante** (sobra P₄).

**Paso 3 · Moles de producto, desde el limitante** (6 Cl₂ → 4 PCl₃):
$$\text{n(PCl}_{3}\text{)} = 4{,}555\ \text{mol de Cl}_{2} \cdot \dfrac{4\ \text{mol PCl}_{3}}{6\ \text{mol Cl}_{2}} = 3{,}037\ \text{mol de PCl}_{3}$$


**Paso 4 · Masa.**

$$\text{m} = \text{n} \cdot \text{M} = 3{,}037\ \text{mol} \cdot 137{,}33\ \text{g/mol} = 417\ \text{g de PCl}_{3}$$


**Lo que tienes que llevarte:** el limitante **no** es el que tiene menos gramos ni menos moles; es el que se acaba antes **según los coeficientes**.

### Problemas de examen

#### Problemas · Tipo A · Mezclas que reaccionan a la vez (reacciones simultáneas) y balances de masa

**Cómo se hace:** una reacción **por cada componente** (nunca sumadas). Llama *x* a la masa de uno y (total − *x*) a la del otro, y plantea **una ecuación con lo que tienen en común** (moles de gas, de precipitado, de ácido…). Se despeja *x*.

**Trampas:** cada metal da su propia sal (FeCl₂ pero AlCl₃ → distinto H₂ por mol). En los balances de masa, piensa qué entra y qué sale.

**Se repite en:** mezclas KOH/LiOH y Mg(OH)₂/LiOH (apartado 3), NaCl/CaCl₂ (apartado 4).

##### P7-1.1 · Segundo parcial, 11 de enero de 2016 (ej. 4) · Aleación Fe/Al + HCl

[[SOL 63:522-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-1_1.svg 100%]]


**Datos:** 2,05 g de aleación (Fe + Al) · se forman 0,105 g de H₂. **Me piden:** % en masa de Fe y de Al.

**¿Qué pasa?** Echo la aleación en HCl en exceso: **los dos metales reaccionan**, cada uno por su lado, y **entre los dos** dan 0,105 g de H₂. No sé cuánto hay de cada uno → esa es la incógnita.

**Reacciones** (el Fe forma Fe²⁺ con HCl y el Al forma Al³⁺):
- **Fe + 2 HCl → FeCl₂ + H₂** → 1 mol de Fe da **1 mol de H₂**
- **Al + 3 HCl → AlCl₃ + 3/2 H₂** → 1 mol de Al da **3/2 mol de H₂**

**Plan:** *x* = gramos de Fe → gramos de Al = (2,05 − *x*). Escribo los moles de H₂ que da cada metal en función de *x* y su suma la igualo al H₂ total.

**Paso 1 · Moles de H₂ totales.**

$$\text{n} = \text{m/M}$$

$$\text{n(H}_{2}\text{)} = \dfrac{0{,}105\ \text{g de H}_{2}}{2{,}016\ \text{g/mol}} = 0{,}05208\ \text{mol de H}_{2}$$


**Paso 2 · H₂ que da el Fe** (en función de x):
$$\text{n(Fe)} = \dfrac{\text{x g}}{55{,}85\ \text{g/mol}}$$

$$\text{n}\left(\text{H}_{2}\text{ del Fe}\right) = \text{(x/}\ 55{,}85\text{) mol de Fe} \cdot \dfrac{1\ \text{mol H}_{2}}{1\ \text{mol Fe}} = \text{x/}\ 55{,}85\ \text{mol de H}_{2}$$


**Paso 3 · H₂ que da el Al:**
$$\text{n(Al)} = \dfrac{\left(2{,}05 - \text{x}\right)\ \text{g}}{26{,}98\ \text{g/mol}}$$

$$\text{n}\left(\text{H}_{2}\text{ del Al}\right) = [\left(2{,}05 - \text{x}\right)\text{/}\ 26{,}98]\ \text{mol de Al} \cdot $$

(3/2 mol H₂/1 mol Al)


**Paso 4 · La suma es el H₂ total:**

$$\underbrace{\frac{x}{55{,}85}}_{\text{mol H}_2\text{ del Fe}}+\underbrace{\frac32\cdot\frac{2{,}05-x}{26{,}98}}_{\text{mol H}_2\text{ del Al}}=\underbrace{0{,}05208}_{\text{mol H}_2\text{ total}}$$

**Paso 5 · Resuelvo** (número a número):
- x/55,85 = 0,01791·x
- (3/2)/26,98 = 0,05560 → 0,05560·(2,05 − x) = 0,1140 − 0,05560·x
- 0,01791·x + 0,1140 − 0,05560·x = 0,05208 → −0,03769·x = −0,06190 → **x = 1,642 g de Fe**


$$\text{Al} = 2{,}05\ \text{g} - 1{,}642\ \text{g} = 0{,}408\ \text{g de Al}$$


**Paso 6 · Porcentajes.**

$$\text{\%} = \text{m(metal)/m(aleación)} \cdot 100$$

$$\text{\%Fe} = \dfrac{1{,}642\ \text{g}}{2{,}05\ \text{g}} \cdot 100 = 80\ \text{\%} \cdot \text{\%Al} = \dfrac{0{,}408\ \text{g}}{2{,}05\ \text{g}} \cdot 100 = 20\ \text{\%}$$


**Comprobación:** H₂ del Fe = 1,642 g / 55,85 g/mol = 0,02940 mol; H₂ del Al = 0,408 g / 26,98 g/mol · 3/2 = 0,02268 mol; suma = 0,0521 mol ✓.

**Lo que tienes que llevarte:** "x y total − x" + **una ecuación con lo que tienen en común** (aquí el H₂).

##### P7-1.2 · Segundo parcial, 15 de enero de 2013 (ej. 3) · Barra de Zn en AgNO₃

[[SOL 30:586-706]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-1_2.svg 100%]]


**Datos:** barra de Zn de 2,50 g · después pesa 3,37 g. **Me piden:** % del Zn inicial que se ha disuelto y masa de Ag depositada.

**¿Qué pasa (laboratorio)?** Meto la barra en la disolución de Ag⁺. El Zn de la superficie **se disuelve** (Zn → Zn²⁺: la barra pierde Zn) y la plata **se pega a la barra** (Ag⁺ → Ag: la barra gana Ag). Al final pesa más porque **entra más masa de Ag de la que sale de Zn**.

**Reacción** (el Zn da 2 e⁻ y cada Ag⁺ coge 1 → hacen falta 2 Ag⁺): **Zn + 2 Ag⁺ → Zn²⁺ + 2 Ag**

**Plan:** calculo cuánto cambia la masa de la barra **por cada mol de Zn que reacciona**, y lo comparo con lo que ha cambiado de verdad.

**Paso 1 · Cambio de masa por mol de Zn:**


Sale 1 mol de Zn:

$$1\ \text{mol} \cdot 65{,}38\ \text{g/mol} =  - 65{,}38\ \text{g}$$



Entran 2 mol de Ag:

$$2\ \text{mol} \cdot 107{,}87\ \text{g/mol} =  + 215{,}74\ \text{g}$$



Balance:

$$ - 65{,}38\ \text{g} + 215{,}74\ \text{g} =  + 150{,}36\ \text{g por cada mol de Zn que reacciona}$$


**Paso 2 · Cuánto ha ganado la barra:**

$$\text{Δm} = 3{,}37\ \text{g} - 2{,}50\ \text{g} = 0{,}87\ \text{g}$$


**Paso 3 · Moles de Zn que han reaccionado** (si 1 mol de Zn hace ganar 150,36 g, ¿cuántos moles hacen ganar 0,87 g?):
$$\text{n(Zn)} = \dfrac{0{,}87\ \text{g}}{\dfrac{150{,}36\ \text{g}}{\text{mol de Zn}}} = 5{,}79\cdot10^{-3}\ \text{mol de Zn}$$


**Paso 4 · Zn disuelto.**

$$\text{m} = \text{n} \cdot \text{M} = 5{,}79\cdot10^{-3}\ \text{mol} \cdot 65{,}38\ \text{g/mol} = 0{,}378\ \text{g de Zn}$$

$$\dfrac{0{,}378\ \text{g}}{2{,}50\ \text{g}} \cdot 100 = 15{,}1\ \text{\%}$$


**Paso 5 · Ag depositada** (2 Ag por cada Zn):
$$\text{n(Ag)} = 5{,}79\cdot10^{-3}\ \text{mol de Zn} \cdot \dfrac{2\ \text{mol Ag}}{1\ \text{mol Zn}} = 0{,}01158\ \text{mol de Ag}$$

$$\text{m} = 0{,}01158\ \text{mol} \cdot 107{,}87\ \text{g/mol} = 1{,}25\ \text{g de Ag}$$


**Lo que tienes que llevarte:** la trampa es pensar "lo que gana la barra = la Ag". No: a la vez pierde Zn. Siempre pregúntate **qué entra y qué sale**.

#### Problemas · Tipo B · Rendimiento y reacciones consecutivas

**Cómo se hace:** ajusta cada paso. Si piden **reactivo para obtener una cantidad de producto**, ve **del final hacia el principio**: moles de producto → (coeficientes) → moles del paso anterior → **÷ rendimiento** en cada paso. Si dan el reactivo y piden producto, de principio a fin y **× rendimiento**.

**Trampas:** el rendimiento afecta solo al paso donde se indica; en las dismutaciones el Cl se reparte entre dos productos.

**Se repite en:** dicromato + KI con rendimiento (Segundo parcial 18-dic-2025, tema 9).

##### P7-1.3 · 1ª convocatoria, 5 de febrero de 2021 (ej. 5) · ClO₂ con rendimiento del 97 %

[[SOL 133:512-648]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-1_3.svg 100%]]


**Datos:** 1 L de NaClO₂ 2,0 M · rendimiento 97 %. **Me piden:** masa de ClO₂ por litro.

**¿Qué pasa?** Paso Cl₂ por la disolución de NaClO₂ → salen ClO₂ y NaCl. Me dan **el reactivo** y piden **el producto** → el rendimiento **multiplica** (sale menos).

**Ajuste** (especies neutras): Cl₂ + NaClO₂ → ClO₂ + NaCl. El Cl₂ tiene 2 Cl que van a NaCl → **2 NaCl** → necesito 2 Na → **2 NaClO₂** → salen **2 ClO₂**. Compruebo: Cl: 2 + 2 = 4 | 2 + 2 = 4 ✓; O: 4 | 4 ✓; Na: 2 | 2 ✓.

**Cl₂ + 2 NaClO₂ → 2 ClO₂ + 2 NaCl**

**Paso 1 · Moles de NaClO₂.**

$$\text{n} = \text{M} \cdot \text{V} = 2{,}0\ \text{mol NaClO}_{2}\text{/L} \cdot 1\ \text{L} = 2{,}0\ \text{mol de NaClO}_{2}$$


**Paso 2 · Moles de ClO₂ teóricos**

(al 100 %):

$$\text{n(ClO}_{2}\text{)} = 2{,}0\ \text{mol NaClO}_{2} \cdot \dfrac{2\ \text{mol ClO}_{2}}{2\ \text{mol NaClO}_{2}} = 2{,}0\ \text{mol de ClO}_{2}$$


**Paso 3 · Moles de ClO₂ reales**

(solo sale el 97 %):

$$2{,}0\ \text{mol} \cdot 97\text{/}\ 100 = 1{,}94\ \text{mol de ClO}_{2}$$


**Paso 4 · Masa.**

$$\text{m} = \text{n} \cdot \text{M} = 1{,}94\ \text{mol} \cdot 67{,}45\ \text{g/mol} = 130{,}9\ \text{g}$$

→ **1,3·10² g de ClO₂ por litro** (2 cifras, por el "2,0 M")


**Lo que tienes que llevarte:** reactivo → producto: **×** rendimiento.

##### P7-1.4 · Tercera convocatoria (Diciembre), 3 de diciembre de 2018 (ej. 4) · KClO₄ en tres pasos

[[SOL 96:182-302]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-1_4.svg 100%]]


**Datos:** quiero 100 g de KClO₄ · tres reacciones consecutivas (la primera al 88 %). **Me piden:** masa de Cl₂.

**¿Qué pasa?** Cl₂ → KClO → KClO₃ → KClO₄. Me dan **el producto final** y piden **el reactivo inicial** → voy **hacia atrás** y el rendimiento **divide** (necesito más).

**Ajuste de cada paso:**
- **Cl₂ + 2 KOH → KCl + KClO + H₂O.** Los 2 Cl del Cl₂ van uno al KCl y otro al KClO → 2 K → **2 KOH**; sobran 2 H y 1 O → **H₂O**.
- **3 KClO → 2 KCl + KClO₃.** Dismutación (Cl +1 → −1 y +5). El KClO₃ tiene 3 O → **3 KClO**; de los 3 K y 3 Cl, 1 va al KClO₃ y **2 al KCl**.
- **4 KClO₃ → 3 KClO₄ + KCl.** Dismutación (Cl +5 → +7 y −1). 3 KClO₄ son 12 O → **4 KClO₃**; sobran 1 K y 1 Cl → **KCl**.

**Paso 1 · Moles de KClO₄.**

$$\text{n} = \text{m/M} = \dfrac{100\ \text{g}}{138{,}55\ \text{g/mol}} = 0{,}7218\ \text{mol de KClO}_{4}$$


**Paso 2 · KClO₃ necesario**

→ (4 KClO₃

3 KClO₄):

$$\text{n} = 0{,}7218\ \text{mol KClO}_{4} \cdot \dfrac{4\ \text{mol KClO}_{3}}{3\ \text{mol KClO}_{4}} = 0{,}9624\ \text{mol de KClO}_{3}$$


**Paso 3 · KClO necesario**

→ (3 KClO

1 KClO₃):

$$\text{n} = 0{,}9624\ \text{mol KClO}_{3} \cdot \dfrac{3\ \text{mol KClO}}{1\ \text{mol KClO}_{3}} = 2{,}887\ \text{mol de KClO}$$


**Paso 4 · Cl₂ al 100 %**

→ (1 Cl₂

1 KClO):

$$\text{n} = 2{,}887\ \text{mol KClO} \cdot \dfrac{1\ \text{mol Cl}_{2}}{1\ \text{mol KClO}} = 2{,}887\ \text{mol de Cl}_{2}$$


**Paso 5 · Corrijo el 88 %**

→ (solo se aprovecha el 88 %

necesito más):

$$\text{n} = \dfrac{2{,}887\ \text{mol}}{\left(88\text{/}\ 100\right)} = 3{,}281\ \text{mol de Cl}_{2}$$


**Paso 6 · Masa.**

$$\text{m} = \text{n} \cdot \text{M} = 3{,}281\ \text{mol} \cdot 70{,}906\ \text{g/mol} = 232{,}6\ \text{g}$$

→ **2,3·10² g de Cl₂**


**Lo que tienes que llevarte:** producto → reactivo: **÷** rendimiento. Comprueba que tiene sentido: necesitas **más** que el teórico.

##### P7-1.5 · Primera convocatoria, 6 de febrero de 2015 (ej. 5) · I₂ desde salmueras (tres rendimientos)

[[SOL 57:257-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-1_5.svg 100%]]


**Datos:** quiero 1,0 kg = 1000 g de I₂ · rendimientos 93 %, 89 % y 72 %. **Me piden:** masa de AgNO₃ (kg).

**¿Qué pasa?** NaI → AgI → FeI₂ → I₂. Producto final conocido → **hacia atrás, dividiendo por cada rendimiento**.

**Ajuste** (primero formulo):
- **NaI + AgNO₃ → AgI + NaNO₃** (1 : 1)
- **2 AgI + Fe → FeI₂ + 2 Ag** (el FeI₂ lleva 2 I → 2 AgI → salen 2 Ag)
- **2 FeI₂ + 3 Cl₂ → 2 FeCl₃ + 2 I₂** (FeCl₃ tiene 3 Cl y Cl₂ tiene 2 → 6 Cl: 2 FeCl₃ y 3 Cl₂; 2 FeI₂ llevan 4 I → 2 I₂)

**Paso 1 · Moles de I₂.**

$$\text{n} = \dfrac{1000\ \text{g}}{253{,}8\ \text{g/mol}} = 3{,}940\ \text{mol de I}_{2}$$


**Paso 2 · FeI₂ necesario** (2 FeI₂ → 2 I₂) y ÷ 0,72:
$$\text{n} = \dfrac{3{,}940\ \text{mol I}_{2} \cdot \dfrac{2\ \text{mol FeI}_{2}}{2\ \text{mol I}_{2}}}{0{,}72} = 5{,}472\ \text{mol de FeI}_{2}$$


**Paso 3 · AgI necesario** (2 AgI → 1 FeI₂) y ÷ 0,89:
$$\text{n} = \dfrac{5{,}472\ \text{mol FeI}_{2} \cdot \dfrac{2\ \text{mol AgI}}{1\ \text{mol FeI}_{2}}}{0{,}89} = 12{,}30\ \text{mol de AgI}$$


**Paso 4 · AgNO₃ necesario** (1 : 1) y ÷ 0,93:
$$\text{n} = \dfrac{12{,}30\ \text{mol AgI} \cdot \dfrac{1\ \text{mol AgNO}_{3}}{1\ \text{mol AgI}}}{0{,}93} = 13{,}22\ \text{mol de AgNO}_{3}$$


**Paso 5 · Masa.**

$$\text{m} = 13{,}22\ \text{mol} \cdot 169{,}87\ \text{g/mol} = 2246\ \text{g}$$

→ **2,2 kg de AgNO₃**


**Lo que tienes que llevarte:** cada rendimiento se aplica **en su paso** (o todos juntos: 0,93 · 0,89 · 0,72 = 0,596, y se divide una vez).

### Avisos de este apartado (se resuelven en otro tema)

- **Convocatoria de Febrero, 6 de febrero de 2012 (ej. 4):** fórmula molecular por combustión + **presión osmótica** → **tema 8**.
- **Mezclar K₂CrO₄ y AgNO₃** (reactivo limitante + precipitado; Segundo parcial 27-ene-2021, 1ª conv. 20-ene-2022, 1ª conv. 2023) → **tema 11**.


<div class="newpage"></div>

## 2. Reacciones en disolución acuosa

### Teoría necesaria

- **Electrolito** (en clase): sustancia que, al disolverse en agua, hace que el agua **conduzca la electricidad** porque genera **iones**. El agua pura no conduce (agua Milli-Q: 18 MΩ, es un aislante); el agua normal conduce por las sales disueltas.
- **No electrolitos:** no generan iones (glucosa, etanol, metanol).
- **Electrolitos fuertes:** se disocian al **100 %** (sales solubles como NaCl, ácidos fuertes, bases fuertes; suelen ser inorgánicos). MgCl₂(s) → Mg²⁺(aq) + 2 Cl⁻(aq).
- **Electrolitos débiles:** solo una pequeña parte forma iones (ácidos carboxílicos, aminas: R-NH₂ + H₂O ⇌ R-NH₃⁺ + OH⁻).
- **Tipos de reacción en agua:** ácido-base, precipitación, formación de complejos y redox. Todas se usan en **valoraciones**.

> **Se repite en:** el número de partículas de un electrolito es el **factor *i* de van't Hoff** (tema 8) y la diferencia fuerte/débil es la base del tema 10.

<div class="newpage"></div>

## 3. Reacciones ácido-base: valoraciones y retrovaloraciones

### Teoría necesaria

- **Brønsted-Lowry:** el ácido **da** H⁺ y la base lo **acepta**. En agua el H⁺ está como **H₃O⁺**, pero en estequiometría se puede escribir H⁺ o la fórmula del ácido.
- **En el tema 7 todo es estequiométrico** (en clase): si al menos uno es **fuerte**, la neutralización es **completa (100 %)**, sin equilibrio: ácido + base → sal + agua. La "sal" está disociada (electrolito fuerte). El posible carácter ácido/básico de la sal (hidrólisis) se ve en el tema 10.
- **Valoración (volumetría):** un **valorante** de concentración conocida (disolución **patrón**) reacciona con el **analito**; del volumen gastado se sacan los moles de valorante → (estequiometría) → moles de analito.

$$n_{\text{valorante}}=M\cdot V\;\xrightarrow{\text{coef.}}\;n_{\text{analito}}\;\Rightarrow\;[\text{analito}]=\frac{n_{\text{analito}}}{V_{\text{alícuota}}}$$

- **Truco de clase:** si dejas los volúmenes en **mL arriba y abajo**, sale directamente mol/L.
- **La concentración es intensiva** (en clase): la de la alícuota de 10 mL es la misma que la del matraz de 2 L; **los moles no**. Por eso: concentración en la alícuota → **moles en el volumen total**.
- **Estandarizar** una disolución = valorarla frente a un **patrón primario** pesado (ácido oxálico dihidratado, K₂Cr₂O₇…) para conocer su concentración exacta.
- **Retrovaloración (valoración por retroceso)** (en clase, mármol): se añade un **exceso conocido** de reactivo (HCl), reacciona con la muestra, y se valora **lo que sobra**.

$$n_{\text{reaccionan}}=n_{\text{añadidos}}-n_{\text{sobrantes (valorados)}}$$

  Para no restar concentraciones, **trabaja en moles** (en clase).
- **En la valoración, la base reacciona con el ácido más fuerte presente** (en clase: la NaOH valora el HCl que sobra, no el CaCl₂ ni el CO₂).



### Ejercicios de clase

##### EC 7.4 · Ejercicio de clase (resuelto en la pizarra) · Mármol con HCl en exceso

<div class="enun" markdown="1">
Un trozo de mármol (compuesto por CaCO₃) reacciona con 2,00 litros de HCl 2,52 M. Después de disolverse, se retiran 10,00 ml de la disolución y se valora con 24,87 ml de NaOH 0,9987 M. ¿Cuánto CaCO₃ contenía el trozo de mármol original? M(CaCO₃) = 100,09 g/mol.
</div>

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_EC_7_4.svg 100%]]


**Datos:** 2,00 L de HCl 2,52 M · alícuota de 10,00 mL · gasta 24,87 mL de NaOH 0,9987 M. **Me piden:** masa de CaCO₃ (g).

**¿Qué pasa? (como lo contó el profesor)**
1. Tengo un "barreño" con 2 L de HCl. Echo el mármol: burbujea (sale CO₂) y se disuelve entero, porque el **HCl está en exceso**.
2. Parte del HCl se ha gastado → el barreño tiene ahora HCl **menos concentrado** que 2,52 M.
3. Cojo **10 mL** de ese barreño y los valoro con NaOH para saber **cuánto HCl queda**.
4. HCl que había − HCl que queda = **HCl que se comió el mármol** → con la reacción saco el CaCO₃.

**Reacciones:**
- **CaCO₃ + 2 HCl → CaCl₂ + H₂O + CO₂** (cada CaCO₃ gasta **2** HCl: el carbonato capta 2 H⁺)
- **NaOH + HCl → NaCl + H₂O** (1 : 1). *La NaOH reacciona con el ácido más fuerte que hay, el HCl (en clase).*

**Paso 1 · Moles de NaOH gastados.**

$$\text{n} = \text{M} \cdot \text{V}$$

$$\text{n(NaOH)} = 0{,}9987\ \text{mol NaOH/L} \cdot 0{,}02487\ \text{L} = 0{,}02484\ \text{mol de NaOH}$$


**Paso 2 · Moles de HCl en los 10 mL** (1 mol HCl por cada mol de NaOH):
$$\text{n(HCl)} = 0{,}02484\ \text{mol NaOH} \cdot \dfrac{1\ \text{mol HCl}}{1\ \text{mol NaOH}} = 0{,}02484\ \text{mol de HCl en}\ 10{,}00\ \text{mL}$$


**Paso 3 · Concentración de HCl que queda.**

$$\text{M} = \text{n/V}$$

$$[\text{HCl}] = \dfrac{0{,}02484\ \text{mol de HCl}}{0{,}01000\ \text{L}} = 2{,}484\ \text{mol/L}$$

*Es la misma concentración en los 10 mL que en los 2 L (la concentración es intensiva); los moles no.*

**Paso 4 · Moles de HCl en todo el barreño, antes y después.**

$$\text{n} = \text{M} \cdot \text{V}$$



Antes:

$$\text{n}_{0} = 2{,}52\ \text{mol/L} \cdot 2{,}00\ \text{L} = 5{,}04\ \text{mol de HCl}$$



Después:

$$\text{n_f} = 2{,}484\ \text{mol/L} \cdot 2{,}00\ \text{L} = 4{,}968\ \text{mol de HCl}$$


**Paso 5 · HCl que reaccionó con el mármol:**

$$\text{n} = 5{,}04\ \text{mol} - 4{,}968\ \text{mol} = 0{,}072\ \text{mol de HCl}$$


**Paso 6 · Moles y masa de CaCO₃** (2 mol HCl por cada mol de CaCO₃):
$$\text{n(CaCO}_{3}\text{)} = 0{,}072\ \text{mol HCl} \cdot \dfrac{1\ \text{mol CaCO}_{3}}{2\ \text{mol HCl}} = 0{,}036\ \text{mol de CaCO}_{3}$$

$$\text{m(CaCO}_{3}\text{)} = 0{,}036\ \text{mol} \cdot 100{,}09\ \text{g/mol} = 3{,}6\ \text{g de CaCO}_{3}$$


**Cifras (la regla de la resta):** 5,04 mol tiene 2 decimales → la resta solo puede tener 2 decimales: 0,07 mol. Estrictamente el resultado tendría una sola cifra (≈ 4 g); el número del cálculo es 3,62 g.

**Lo que tienes que llevarte:** el esquema de toda **retrovaloración**: **reaccionados = añadidos − sobrantes**, y los sobrantes los da la valoración (corrigiendo la alícuota).

### Problemas de examen

#### Problemas · Tipo A · Valoración directa, estandarización y mezclas de bases

**Cómo se hace:** moles de valorante (n = M·V) → estequiometría → moles de analito → corrijo la **alícuota** (× V_total/V_alícuota). Si es una **mezcla de dos bases**, sistema con *x* y (masa − *x*), igualando los moles de H⁺ gastados.

**Trampas:** H₂SO₄ y el ácido oxálico son **dipróticos** (2 NaOH cada uno); Ba(OH)₂, Mg(OH)₂ y Ca(OH)₂ dan **2 OH⁻**; el oxálico **dihidratado** pesa con sus aguas.

**Se repite en:** curvas de valoración (tema 10).

##### P7-3.1 · 3ª convocatoria, 16 de octubre de 2025 (ej. 4) · Oxálico → NaOH → H₂SO₄ (dos estandarizaciones)

[[SOL 182:668-842 183:40-171]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_1.svg 100%]]


**Datos:** 0,6477 g de H₂C₂O₄·2H₂O (M = 126,07 g/mol) en 100,0 mL · 5,00 mL de oxálico gastan 30,0 mL de NaOH · 25,0 mL de H₂SO₄ gastan 23,7 mL de NaOH. **Me piden:** [H₂SO₄].

**¿Qué pasa?** Dos valoraciones encadenadas: no conozco la [NaOH], así que primero la calculo con el oxálico, que he **pesado** (patrón). Después, con esa NaOH, valoro el H₂SO₄.

**Reacciones** (los dos ácidos tienen 2 H ácidos → 2 NaOH cada uno):
- **H₂C₂O₄ + 2 NaOH → Na₂C₂O₄ + 2 H₂O**
- **H₂SO₄ + 2 NaOH → Na₂SO₄ + 2 H₂O**

**Paso 1 · Concentración del oxálico.** n = m/M y

$$\text{M} = \text{n/V}$$

$$\text{n(oxálico)} = \dfrac{0{,}6477\ \text{g}}{126{,}07\ \text{g/mol}} = 5{,}138\cdot10^{-3}\ \text{mol}$$

$$[\text{ox}] = \dfrac{5{,}138\cdot10^{-3}\ \text{mol}}{0{,}1000\ \text{L}} = 0{,}05138\ \text{mol/L}$$


**Paso 2 · Oxálico en los 5,00 mL valorados.**

$$\text{n} = \text{M} \cdot \text{V} = 0{,}05138\ \text{mol/L} \cdot 0{,}00500\ \text{L} = 2{,}569\cdot10^{-4}\ \text{mol de oxálico}$$


**Paso 3 · [NaOH]** (2 mol NaOH por cada mol de oxálico):
$$\text{n(NaOH)} = 2{,}569\cdot10^{-4}\ \text{mol ox} \cdot \dfrac{2\ \text{mol NaOH}}{1\ \text{mol ox}} = 5{,}138\cdot10^{-4}\ \text{mol de NaOH, que estaban en}\ 30{,}0\ \text{mL}$$

$$[\text{NaOH}] = \dfrac{5{,}138\cdot10^{-4}\ \text{mol}}{0{,}0300\ \text{L}} = 0{,}01713\ \text{mol/L}$$


**Paso 4 · NaOH gastada con el H₂SO₄.**

$$\text{n} = \text{M} \cdot \text{V} = 0{,}01713\ \text{mol/L} \cdot 0{,}0237\ \text{L} = 4{,}059\cdot10^{-4}\ \text{mol de NaOH}$$


**Paso 5 · [H₂SO₄]** (1 mol H₂SO₄ por cada 2 mol NaOH):
$$\text{n(H}_{2}\text{SO}_{4}\text{)} = 4{,}059\cdot10^{-4}\ \text{mol NaOH} \cdot \dfrac{1\ \text{mol H}_{2}\text{SO}_{4}}{2\ \text{mol NaOH}} = 2{,}030\cdot10^{-4}\ \text{mol de H}_{2}\text{SO}_{4}\text{ en}\ 25{,}0\ \text{mL}$$

$$[\text{H}_{2}\text{SO}_{4}] = \dfrac{2{,}030\cdot10^{-4}\ \text{mol}}{0{,}0250\ \text{L}} = 8{,}12\cdot10^{-3}\ \text{mol/L}$$


**Lo que tienes que llevarte:** **estandarizar** = averiguar la concentración exacta de una disolución valorándola con algo que he pesado.

##### P7-3.2 · 3ª convocatoria (Diciembre), 1 de diciembre de 2021 (ej. 4) · Mezcla Mg(OH)₂/LiOH

[[SOL 139:445-537]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_2.svg 100%]]


**Datos:** 0,4225 g de mezcla · gasta 28,28 mL de HCl 0,5375 M. **Me piden:** % de cada hidróxido.

**¿Qué pasa?** Las dos bases se neutralizan con el HCl a la vez; cada OH⁻ gasta un H⁺.

**Reacciones:** Mg(OH)₂ + 2 HCl → MgCl₂ + 2 H₂O (**2** mol HCl por mol) · LiOH + HCl → LiCl + H₂O (**1** mol HCl por mol)

**Paso 1 · HCl gastado.**

$$\text{n} = \text{M} \cdot \text{V} = 0{,}5375\ \text{mol HCl/L} \cdot 0{,}02828\ \text{L} = 0{,}01520\ \text{mol de HCl}$$


**Paso 2 · Planteo**

→ con x = g de Mg(OH)₂

$$\text{g de LiOH} = \left(0{,}4225 - \text{x}\right)\text{:}$$



$$\text{HCl que gasta el Mg(OH)}_{2} = \text{(x/}\ 58{,}320\text{) mol Mg(OH)}_{2} \cdot 2\ \text{mol HCl/mol}$$



$$\text{HCl que gasta el LiOH} = \left(\left(0{,}4225 - \text{x}\right)\text{/}\ 23{,}948\right)\ \text{mol LiOH} \cdot 1\ \text{mol HCl/mol}$$


$$\underbrace{\frac{2x}{58{,}320}}_{\text{mol HCl del Mg(OH)}_2}+\underbrace{\frac{0{,}4225-x}{23{,}948}}_{\text{mol HCl del LiOH}}=\underbrace{0{,}01520}_{\text{mol HCl total}}$$

**Paso 3 · Resuelvo:** 0,03429·x + 0,01764 − 0,04176·x = 0,01520 → −0,00747·x = −0,00244 → **x = 0,327 g de Mg(OH)₂**

**Paso 4 · %.**

$$\text{\%Mg(OH)}_{2} = \dfrac{0{,}327\ \text{g}}{0{,}4225\ \text{g}} \cdot 100 = 77{,}4\ \text{\%} \cdot \text{\%LiOH} = 22{,}6\ \text{\%}$$


**Lo que tienes que llevarte:** mismo esquema que la aleación Fe/Al: x y (total − x), igualando lo común (los H⁺).

##### P7-3.3 · Segunda convocatoria, 14 de septiembre de 2017 (ej. 4) · Mezcla KOH/LiOH (%Li)

[[SOL 82:457-561]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_3.svg 100%]]


**Datos:** 0,4324 g de mezcla en 100,0 mL · una alícuota de 10,00 mL gasta 28,28 mL de HCl 0,0352 M. **Me piden:** % de **Li** (del elemento).

**¿Qué pasa?** Disuelvo todo en 100 mL y **solo valoro 10 mL** → lo que salga lo multiplico por 10.

**Reacciones:** KOH + HCl → KCl + H₂O · LiOH + HCl → LiCl + H₂O (las dos 1 : 1)

**Paso 1 · HCl gastado en la alícuota.**

$$\text{n} = 0{,}0352\ \text{mol/L} \cdot 0{,}02828\ \text{L} = 9{,}955\cdot10^{-4}\ \text{mol de HCl}$$


**Paso 2 · OH⁻ en toda la muestra** (la alícuota es 10,00 mL de 100,0 mL):
$$\text{n(OH}^{-}\text{)} = 9{,}955\cdot10^{-4}\ \text{mol} \cdot \dfrac{100{,}0\ \text{mL}}{10{,}00\ \text{mL}} = 9{,}955\cdot10^{-3}\ \text{mol de OH}^{-}$$


**Paso 3 · Planteo** con x = g de KOH:
$$\text{(x/}\ 56{,}106\text{) mol KOH} + \left(\left(0{,}4324 - \text{x}\right)\text{/}\ 23{,}948\right)\ \text{mol LiOH} = 9{,}955\cdot10^{-3}\ \text{mol}$$

0,01782·x + 0,01806 − 0,04176·x = 0,009955

→ **x = 0,3385 g de KOH**

$$\text{LiOH} = 0{,}4324\ \text{g} - 0{,}3385\ \text{g} = 0{,}0939\ \text{g de LiOH}$$


**Paso 4 · Masa de Li dentro del LiOH** (en 23,948 g de LiOH hay 6,941 g de Li):
$$\text{m(Li)} = 0{,}0939\ \text{g LiOH} \cdot \left(6{,}941\ \text{g Li /}\ 23{,}948\ \text{g LiOH}\right) = 0{,}0272\ \text{g de Li}$$


**Paso 5 · %Li**

$$\dfrac{\text{=}\ 0{,}0272\ \text{g}}{0{,}4324\ \text{g}} \cdot 100 = 6{,}29\ \text{\%}$$


**Lo que tienes que llevarte:** lee bien qué % piden (compuesto o elemento) y no olvides la alícuota.

#### Problemas · Tipo B · Retrovaloraciones (exceso de ácido o base)

**Cómo se hace:** (1) moles **añadidos** del reactivo en exceso; (2) moles **sobrantes** = los que gasta el valorante; (3) **reaccionados = añadidos − sobrantes**; (4) estequiometría con la muestra.

**Trampas:** H₂SO₄ = 2 H⁺; Ba(OH)₂ y Ca(OH)₂ = 2 OH⁻; los carbonatos gastan **2 H⁺**; la alícuota.

**Se repite en:** retrovaloraciones redox (apartado 6) y tampones (tema 10).

##### P7-3.4 · Primera convocatoria, 20 de enero de 2022 (ej. 5) · CaCO₃ en un suplemento (HCl / Ba(OH)₂)

[[SOL 149:234-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_4.svg 100%]]


**Datos:** tableta de 1,245 g · 50,00 mL de HCl 0,5000 M (exceso) · el HCl sobrante gasta 40,20 mL de Ba(OH)₂ 0,1092 M. **Me piden:** % de CaCO₃.

**¿Qué pasa?** Igual que el mármol: el HCl ataca el CaCO₃ y **sobra HCl**; el sobrante lo valoro con Ba(OH)₂.

**Reacciones:** **CaCO₃ + 2 HCl → CaCl₂ + H₂O + CO₂** · **Ba(OH)₂ + 2 HCl → BaCl₂ + 2 H₂O** (2 OH⁻ → gasta 2 HCl)

**Paso 1 · HCl añadido.**

$$\text{n} = 0{,}5000\ \text{mol/L} \cdot 0{,}05000\ \text{L} = 0{,}02500\ \text{mol de HCl}$$


**Paso 2 · HCl sobrante.**

$$\text{n(Ba(OH)}_{2}\text{)} = 0{,}1092\ \text{mol/L} \cdot 0{,}04020\ \text{L} = 4{,}390\cdot10^{-3}\ \text{mol de Ba(OH)}_{2}$$

$$\text{n}\left(\text{HCl sobrante}\right) = 4{,}390\cdot10^{-3}\ \text{mol Ba(OH)}_{2} \cdot \dfrac{2\ \text{mol HCl}}{1\ \text{mol Ba(OH)}_{2}} = 8{,}780\cdot10^{-3}\ \text{mol de HCl}$$


**Paso 3 · HCl que reaccionó con el CaCO₃:**

$$0{,}02500\ \text{mol} - 0{,}00878\ \text{mol} = 0{,}01622\ \text{mol de HCl}$$


**Paso 4 · CaCO₃:**

$$\text{n} = 0{,}01622\ \text{mol HCl} \cdot \dfrac{1\ \text{mol CaCO}_{3}}{2\ \text{mol HCl}} = 8{,}110\cdot10^{-3}\ \text{mol}$$

$$\text{m} = 8{,}110\cdot10^{-3}\ \text{mol} \cdot 100{,}0869\ \text{g/mol} = 0{,}8117\ \text{g de CaCO}_{3}$$


**Paso 5 · %**

$$\dfrac{\text{=}\ 0{,}8117\ \text{g}}{1{,}245\ \text{g}} \cdot 100 = 65{,}20\ \text{\%}$$


**Lo que tienes que llevarte:** el Ba(OH)₂ "vale doble". Si se te olvida, te sale 81,7 %.

##### P7-3.5 · Primera convocatoria, 23 de enero de 2020 (ej. 5) · Carbonato desconocido X₂CO₃

[[SOL 120:233-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_5.svg 100%]]


**Datos:** 0,0555 g de X₂CO₃ · 20,00 mL de H₂SO₄ 0,0400 M (exceso) · el sobrante gasta 11,28 mL de NaOH 0,1000 M. **Me piden:** M(X₂CO₃) y M(X).

**¿Qué pasa?** Retrovaloración: saco los **moles** de carbonato y, como sé su masa, su masa molar (M = m/n).

**Reacciones:** **X₂CO₃ + H₂SO₄ → X₂SO₄ + H₂O + CO₂** (1 : 1) · **H₂SO₄ + 2 NaOH → Na₂SO₄ + 2 H₂O**

**Paso 1 · H₂SO₄ añadido.**

$$\text{n} = 0{,}0400\ \text{mol/L} \cdot 0{,}02000\ \text{L} = 8{,}00\cdot10^{-4}\ \text{mol de H}_{2}\text{SO}_{4}$$


**Paso 2 · H₂SO₄ sobrante.**

$$\text{n(NaOH)} = 0{,}1000\ \text{mol/L} \cdot 0{,}01128\ \text{L} = 1{,}128\cdot10^{-3}\ \text{mol}$$

$$\text{n(H}_{2}\text{SO}_{4}\text{)} = 1{,}128\cdot10^{-3}\ \text{mol NaOH} \cdot \dfrac{1\ \text{mol H}_{2}\text{SO}_{4}}{2\ \text{mol NaOH}} = 5{,}64\cdot10^{-4}\ \text{mol de H}_{2}\text{SO}_{4}$$


**Paso 3 · H₂SO₄ que reaccionó = mol de X₂CO₃:**

$$8{,}00\cdot10^{-4} - 5{,}64\cdot10^{-4} = 2{,}36\cdot10^{-4}\ \text{mol de X}_{2}\text{CO}_{3}$$


**Paso 4 · Masa molar del carbonato.**

$$\text{M} = \text{m/n} = \dfrac{0{,}0555\ \text{g}}{2{,}36\cdot10^{-4}\ \text{mol}} = 235\ \text{g/mol}$$


**Paso 5 · Masa de X.**

$$\text{M(CO}_{3}\text{)} = 12{,}01 + 3 \cdot 16{,}00 = 60{,}01\ \text{g/mol}$$

$$2 \cdot \text{M(X)} = 235 - 60{,}01\ \text{g/mol}$$

$$\text{M(X)} = 87{,}5\ \text{g/mol}$$


**Lo que tienes que llevarte:** "masa molar desconocida" = saca los **moles** por la valoración y divide la masa entre ellos.

##### P7-3.6 · Segundo parcial, 18 de enero de 2018 (ej. 2) · NH₃ desprendido absorbido en HCl

[[SOL 87:334-422]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_6.svg 100%]]


**Datos:** 10,0 mL de (NH₄)₂SO₄ + exceso de NaOH · el NH₃ se recoge en 50,0 mL de HCl 0,1000 M · el HCl sobrante gasta 21,5 mL de NaOH 0,098 M. **Me piden:** [(NH₄)₂SO₄] en g/L.

**¿Qué pasa (laboratorio)?** Con NaOH, el NH₄⁺ se convierte en **NH₃ gas**, que se escapa y lo burbujeo en un vaso con HCl, donde se neutraliza. Luego valoro el HCl que ha sobrado.

**Reacciones:** (NH₄)₂SO₄ + 2 NaOH → Na₂SO₄ + **2 NH₃** + 2 H₂O · NH₃ + HCl → NH₄Cl (1 : 1) · HCl + NaOH → NaCl + H₂O (1 : 1)

**Paso 1 · HCl en el vaso.**

$$\text{n} = 0{,}1000\ \text{mol/L} \cdot 0{,}0500\ \text{L} = 5{,}000\cdot10^{-3}\ \text{mol de HCl}$$


**Paso 2 · HCl sobrante.**

$$\text{n} = 0{,}098\ \text{mol NaOH/L} \cdot 0{,}0215\ \text{L} = 2{,}107\cdot10^{-3}\ \text{mol de HCl}$$


**Paso 3 · NH₃ desprendido**

(= HCl que lo neutralizó):

$$5{,}000\cdot10^{-3} - 2{,}107\cdot10^{-3} = 2{,}893\cdot10^{-3}\ \text{mol de NH}_{3}$$


**Paso 4 · (NH₄)₂SO₄**

(1 mol de sal da 2 mol de NH₃):

$$\text{n} = 2{,}893\cdot10^{-3}\ \text{mol NH}_{3} \cdot \dfrac{1\ \text{mol sal}}{2\ \text{mol NH}_{3}} = 1{,}446\cdot10^{-3}\ \text{mol en}\ 10{,}0\ \text{mL}$$

$$\text{M} = \dfrac{1{,}446\cdot10^{-3}\ \text{mol}}{0{,}0100\ \text{L}} = 0{,}1446\ \text{mol/L}$$


**Paso 5 · g/L:**

$$0{,}1446\ \text{mol/L} \cdot 132{,}14\ \text{g/mol} = 19\ \text{g/L}$$


**Lo que tienes que llevarte:** cuenta los átomos de N: el (NH₄)₂SO₄ lleva **dos** NH₄⁺.

##### P7-3.7 · Segundo parcial, 14 de enero de 2014 (ej. 3) · Carbonato de un metal desconocido XCO₃

[[SOL 43:526-639]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_7.svg 100%]]


**Datos:** 3,542 g de XCO₃ · 18,68 mL de HCl 5,653 M (exceso) · el sobrante gasta 6,03 mL de Ca(OH)₂ 1,789 M. **Me piden:** M(XCO₃) y M(X).

**Reacciones:** **XCO₃ + 2 HCl → XCl₂ + H₂O + CO₂** · **Ca(OH)₂ + 2 HCl → CaCl₂ + 2 H₂O** (vale doble)

**Paso 1 · HCl añadido.**

$$\text{n} = 5{,}653\ \text{mol/L} \cdot 0{,}01868\ \text{L} = 0{,}1056\ \text{mol de HCl}$$


**Paso 2 · HCl sobrante.**

$$\text{n(Ca(OH)}_{2}\text{)} = 1{,}789\ \text{mol/L} \cdot 0{,}00603\ \text{L} = 0{,}01079\ \text{mol}$$

$$\text{n(HCl)} = 0{,}01079 \cdot 2 = 0{,}02158\ \text{mol de HCl}$$


**Paso 3 · HCl que reaccionó:**

$$0{,}1056 - 0{,}02158 = 0{,}08402\ \text{mol de HCl}$$


**Paso 4 · XCO₃:**

$$\text{n} = 0{,}08402\ \text{mol HCl} \cdot \dfrac{1\ \text{mol XCO}_{3}}{2\ \text{mol HCl}} = 0{,}04201\ \text{mol}$$

$$\text{M} = \dfrac{3{,}542\ \text{g}}{0{,}04201\ \text{mol}} = 84{,}3\ \text{g/mol}$$


**Paso 5 · X:**

$$\text{M(X)} = 84{,}3 - 60{,}01\ \text{g/mol} = 24{,}3\ \text{g/mol}$$

→ es el Mg**


##### P7-3.8 · Convocatoria de Febrero, 3 de febrero de 2011 (ej. 5) · Riqueza de un Mg impuro con H₂SO₄

[[SOL 10:234-321]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-3_8.svg 100%]]


**Datos:** 1,25 g de Mg impuro · 100 mL de H₂SO₄ 0,500 M · el sobrante gasta 33,4 mL de NaOH 0,500 M. **Me piden:** riqueza (% de Mg).

**Reacciones:** **Mg + H₂SO₄ → MgSO₄ + H₂** (1 : 1) · **H₂SO₄ + 2 NaOH → Na₂SO₄ + 2 H₂O**

**Paso 1 · H₂SO₄ añadido.**

$$\text{n} = 0{,}500\ \text{mol/L} \cdot 0{,}100\ \text{L} = 0{,}0500\ \text{mol de H}_{2}\text{SO}_{4}$$


**Paso 2 · Sobrante.**

$$\text{n(NaOH)} = 0{,}500\ \text{mol/L} \cdot 0{,}0334\ \text{L} = 0{,}0167\ \text{mol}$$

$$\text{n(H}_{2}\text{SO}_{4}\text{)} = \dfrac{0{,}0167}{2} = 0{,}00835\ \text{mol de H}_{2}\text{SO}_{4}$$


**Paso 3 · Reaccionó con el Mg:**

$$0{,}0500 - 0{,}00835 = 0{,}04165\ \text{mol de H}_{2}\text{SO}_{4} = 0{,}04165\ \text{mol de Mg}$$


**Paso 4 · Riqueza.**

$$\text{m(Mg)} = 0{,}04165\ \text{mol} \cdot 24{,}31\ \text{g/mol} = 1{,}013\ \text{g}$$

$$\dfrac{1{,}013\ \text{g}}{1{,}25\ \text{g}} \cdot 100 = 81\ \text{\%}$$


### Avisos de este apartado (se resuelven en otro tema)

- **Convocatoria de Febrero, 5 de diciembre de 2011 (ej. 5):** Ca + H₂SO₄ (retrovaloración) + **Kps del CaSO₄** → **tema 11**.
- **Segundo parcial, 17 de enero de 2019 (ej. 3):** vinagre valorado con un **indicador equivocado (pH 12)** → **tema 10**.


<div class="newpage"></div>

## 4. Reacciones de precipitación y gravimetría

### Teoría necesaria

- **Precipitación** (en clase): al mezclar dos electrolitos fuertes solubles, los iones están libres; si alguna combinación catión-anión es **insoluble**, precipita inmediatamente. KBr + AgNO₃ → AgBr(s)↓ (amarillento) + KNO₃.
- **Ecuación iónica neta:** solo las especies que reaccionan: Ag⁺(aq) + Br⁻(aq) → AgBr(s). Los demás son **iones espectadores** (K⁺, NO₃⁻).
- **Gravimetría:** se convierte el analito en un **sólido de fórmula conocida**, se separa, se seca (o se calcina) y **se pesa**. Como pesar es más preciso que medir volúmenes, da resultados más exactos que una volumetría.
- **Clave de clase:** *"no me hace falta ajustar cada reacción intermedia: me hace falta el camino de conservación del elemento"*. Todo el Mg de la muestra acaba en el Mg₂P₂O₇ → 1 mol de Mg₂P₂O₇ contiene **2 mol de Mg**.
- **ppm** = g de analito por 10⁶ g de muestra = mg/kg (en agua diluida ≈ mg/L).

#### Teoría · Tipo A · Volumetría frente a gravimetría

##### T7-4.1 · Primera convocatoria, 6 de febrero de 2015 (ej. 1a)

[[SOL 56:389-605]]

> **Respuesta de 10:** Las dos son técnicas cuantitativas que se basan en una reacción de estequiometría conocida para calcular la cantidad de analito. En una **volumetría** se mide el **volumen** de un valorante de concentración conocida que reacciona exactamente con el analito (ácido-base, redox, complejos…), detectando el punto final con un indicador. En una **gravimetría** el analito se transforma en un **precipitado** de fórmula conocida que se separa, se seca o calcina y se **pesa**. La gravimetría suele ser más precisa (la balanza es más exacta que el material volumétrico), pero es más lenta.



### Ejercicios de clase

##### EC 7.5 · Ejercicio de clase (resuelto en la pizarra) · Mg en agua mineral

<div class="enun" markdown="1">
Se analiza el contenido en magnesio de una muestra de 109,712 g de agua mineral. El Mg²⁺ de la muestra se precipita como MgNH₄PO₄ y este precipitado se transforma en pirofosfato de magnesio, con un peso de 0,0549 g. Expresa en partes por millón (es decir, en gramos de magnesio por millón de gramos de agua) la cantidad de magnesio que hay en la muestra.
</div>

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_EC_7_5.svg 100%]]


**Datos:** 109,712 g de agua · 0,0549 g de Mg₂P₂O₇ pesado. **Me piden:** ppm de Mg.

**¿Qué pasa? (el "camino del Mg", como lo explicó el profesor)** Mg²⁺ en el agua → precipita como MgNH₄PO₄ → al calentarlo se convierte en Mg₂P₂O₇, que es lo que peso. **Todo el Mg de la muestra acaba en el Mg₂P₂O₇.** No hace falta ajustar las reacciones intermedias: basta con mirar la fórmula del sólido pesado, que tiene **2 Mg**.

**Paso 1 · Masa molar del Mg₂P₂O₇:**

$$2 \cdot 24{,}305 + 2 \cdot 30{,}974 + 7 \cdot 15{,}999 = 222{,}55\ \text{g/mol}$$


**Paso 2 · Moles de Mg₂P₂O₇.**

$$\text{n} = \text{m/M} = \dfrac{0{,}0549\ \text{g}}{222{,}55\ \text{g/mol}} = 2{,}467\cdot10^{-4}\ \text{mol de Mg}_{2}\text{P}_{2}\text{O}_{7}$$


**Paso 3 · Moles de Mg** (cada Mg₂P₂O₇ lleva 2 Mg):
$$\text{n(Mg)} = 2{,}467\cdot10^{-4}\ \text{mol Mg}_{2}\text{P}_{2}\text{O}_{7} \cdot \dfrac{2\ \text{mol Mg}}{1\ \text{mol Mg}_{2}\text{P}_{2}\text{O}_{7}} = 4{,}934\cdot10^{-4}\ \text{mol de Mg}$$


**Paso 4 · Masa de Mg.**

$$\text{m} = \text{n} \cdot \text{M} = 4{,}934\cdot10^{-4}\ \text{mol} \cdot 24{,}305\ \text{g/mol} = 0{,}01199\ \text{g de Mg}$$


**Paso 5 · ppm** (gramos de Mg por cada millón de gramos de agua):
$$\text{ppm} = \left(0{,}01199\ \text{g de Mg /}\ 109{,}712\ \text{g de agua}\right) \cdot 10^{6} = 109\ \text{ppm}$$


**Lo que tienes que llevarte:** en gravimetría, **sigue al elemento**: ¿cuántos átomos de él lleva la fórmula de lo que peso?

### Problemas de examen

#### Problemas · Tipo A · Gravimetrías (y gravimetría + volumetría): composición, fórmulas, ppm

**Cómo se hace:** sigue el **camino del elemento** (cuántos átomos hay en la fórmula del sólido pesado) → moles del analito → masa → % o ppm. Si hay **dos incógnitas** (mezcla o hidrato), usa dos datos: masa total + moles de precipitado, o agua perdida + moles de Cl⁻.

**Trampas:** el **volumen evaporado no cambia los moles**; la alícuota; los átomos por fórmula (Al₂O₃ → 2 Al; alumbre → 2 Al y 4 S).

**Se repite en:** el "camino del elemento" en las yodometrías (apartado 6).

##### P7-4.1 · 2ª convocatoria, 1 de julio de 2026 (ej. 4) · Mezcla KCl/Na₂CO₃ (gravimetría + volumetría)

[[SOL 191:442-567]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-4_1.svg 100%]]


**Datos:** experimento 1: 2,000 g de muestra + exceso de CaCl₂ → 0,800 g de CaCO₃. Experimento 2: 1,000 g de muestra gasta 36,0 mL de AgNO₃ 0,0750 M. **Me piden:** % de KCl y de Na₂CO₃.

**¿Qué pasa?** Son **dos experimentos independientes**, uno para cada componente: el CaCl₂ precipita el carbonato (CaCO₃) y el AgNO₃ precipita el cloruro (AgCl).

**Reacciones:** Na₂CO₃ + CaCl₂ → CaCO₃↓ + 2 NaCl (1 Na₂CO₃ → 1 CaCO₃) · KCl + AgNO₃ → AgCl↓ + KNO₃ (1 : 1)

**Na₂CO₃:**


$$\text{Paso}\ 1 \cdot \text{n(CaCO}_{3}\text{)} = \dfrac{0{,}800\ \text{g}}{100{,}09\ \text{g/mol}} = 7{,}993\cdot10^{-3}\ \text{mol de CaCO}_{3} = 7{,}993\cdot10^{-3}\ \text{mol de Na}_{2}\text{CO}_{3}$$



$$\text{Paso}\ 2 \cdot \text{m(Na}_{2}\text{CO}_{3}\text{)} = 7{,}993\cdot10^{-3}\ \text{mol} \cdot 105{,}99\ \text{g/mol} = 0{,}8472\ \text{g}$$



$$\text{Paso}\ 3 \cdot \text{\%} = \dfrac{0{,}8472\ \text{g}}{2{,}000\ \text{g de muestra}} \cdot 100 = 42{,}4\ \text{\% de Na}_{2}\text{CO}_{3}$$


**KCl:**


$$\text{Paso}\ 1 \cdot \text{n(AgNO}_{3}\text{)} = 0{,}0750\ \text{mol/L} \cdot 0{,}0360\ \text{L} = 2{,}70\cdot10^{-3}\ \text{mol} = 2{,}70\cdot10^{-3}\ \text{mol de KCl}$$



$$\text{Paso}\ 2 \cdot \text{m(KCl)} = 2{,}70\cdot10^{-3}\ \text{mol} \cdot 74{,}55\ \text{g/mol} = 0{,}2013\ \text{g}$$



$$\text{Paso}\ 3 \cdot \text{\%} = \dfrac{0{,}2013\ \text{g}}{1{,}000\ \text{g de muestra}} \cdot 100 = 20{,}1\ \text{\% de KCl}$$


**Lo que tienes que llevarte:** cada experimento usa **su propia masa de muestra** (2,000 g y 1,000 g).

##### P7-4.2 · 3ª convocatoria, 22 de octubre de 2024 (ej. 5) · Alumbre (Al y S)

[[SOL 174:656-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-4_2.svg 100%]]


**Datos:** 1,227 g de alumbre K₂SO₄·Al₂(SO₄)₃·24 H₂O impuro · todo el Al acaba como 0,1098 g de Al₂O₃. **Me piden:** % de Al y % de S.

**Paso 1 · Masa molar del Al₂O₃:**

$$2 \cdot 26{,}981 + 3 \cdot 15{,}994 = 101{,}944\ \text{g/mol}$$


**Paso 2 · Moles de Al₂O₃:**

$$\text{n} = \dfrac{0{,}1098\ \text{g}}{101{,}944\ \text{g/mol}} = 1{,}0771\cdot10^{-3}\ \text{mol}$$


**Paso 3 · Moles de Al**

(2 Al por Al₂O₃):

$$1{,}0771\cdot10^{-3} \cdot 2 = 2{,}154\cdot10^{-3}\ \text{mol de Al}$$

$$\text{m} = 2{,}154\cdot10^{-3}\ \text{mol} \cdot 26{,}981\ \text{g/mol} = 0{,}05812\ \text{g}$$

$$\text{\%} = \dfrac{0{,}05812\ \text{g}}{1{,}227\ \text{g}} \cdot 100 = 4{,}737\ \text{\% de Al}$$


**Paso 4 · Moles de S.** En la fórmula del alumbre hay **2 Al y 4 S** (1 SO₄ del K₂SO₄ + 3 del Al₂(SO₄)₃) → por cada Al hay 2 S:
$$\text{n(S)} = 2{,}154\cdot10^{-3}\ \text{mol Al} \cdot \dfrac{4\ \text{mol S}}{2\ \text{mol Al}} = 4{,}308\cdot10^{-3}\ \text{mol de S}$$

$$\text{m} = 4{,}308\cdot10^{-3}\ \text{mol} \cdot 32{,}065\ \text{g/mol} = 0{,}1381\ \text{g}$$

→ **11,26 % de S**


**Lo que tienes que llevarte:** el S no se ha medido: se saca **de la fórmula** del alumbre, a partir del Al.

##### P7-4.3 · Segunda convocatoria, 5 de julio de 2024 (ej. 4) · Fórmula de un cloruro de hierro hidratado

[[SOL 173:115-239]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-4_3.svg 100%]]


**Datos:** 5,012 g del hidrato → seco pesa 3,195 g · con AgNO₃ da 7,225 g de AgCl. **Me piden:** la fórmula FeClₓ·n H₂O.

**¿Qué pasa?** Al secarlo pierde el agua; del AgCl saco el Cl; el resto del anhidro es Fe. Con los **moles** de cada cosa saco las proporciones.

**Paso 1 · Agua.**

$$\text{m} = 5{,}012\ \text{g} - 3{,}195\ \text{g} = 1{,}817\ \text{g}$$

$$\text{n} = \dfrac{1{,}817\ \text{g}}{18{,}015\ \text{g/mol}} = 0{,}1009\ \text{mol de H}_{2}\text{O}$$


**Paso 2 · Cl.**

$$\text{M(AgCl)} = 107{,}868 + 35{,}453 = 143{,}32\ \text{g/mol}$$

$$\text{n(AgCl)} = \dfrac{7{,}225\ \text{g}}{143{,}32\ \text{g/mol}} = 0{,}05041\ \text{mol} = \text{mol de Cl}$$

$$\text{m(Cl)} = 0{,}05041\ \text{mol} \cdot 35{,}453\ \text{g/mol} = 1{,}787\ \text{g}$$


**Paso 3 · Fe.**

$$\text{m} = 3{,}195\ \text{g} - 1{,}787\ \text{g} = 1{,}408\ \text{g}$$

$$\text{n} = \dfrac{1{,}408\ \text{g}}{55{,}845\ \text{g/mol}} = 0{,}02521\ \text{mol de Fe}$$


**Paso 4 · Proporciones** (divido todo por los moles de Fe): Cl/Fe = 0,05041/0,02521 = **2,00** · H₂O/Fe = 0,1009/0,02521 = **4,00** → **FeCl₂·4 H₂O**

##### P7-4.4 · Primera convocatoria (febrero 2023; el PDF pone "12 de febrero de 2021") (ej. 5) · Sulfatos y cloruros en agua mineral (ppm)

[[SOL 160:582-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-4_4.svg 100%]]


**Datos:** sulfatos: 6,00 L de agua evaporada al 5 % → 96,5 mg de BaSO₄. Cloruros: 10,0 mL de agua gastan 1,35 mL de AgNO₃ 0,03360 M. **Me piden:** ppm de SO₄²⁻ y de Cl⁻.

**Sulfatos:**


$$\text{Paso}\ 1 \cdot \text{n(BaSO}_{4}\text{)} = \dfrac{0{,}0965\ \text{g}}{233{,}39\ \text{g/mol}} = 4{,}135\cdot10^{-4}\ \text{mol} = \text{mol de SO}_{4}^{2-}$$

(1 SO₄ por BaSO₄)



$$\text{Paso}\ 2 \cdot \text{m(SO}_{4}^{2-}\text{)} = 4{,}135\cdot10^{-4}\ \text{mol} \cdot 96{,}06\ \text{g/mol} = 0{,}0397\ \text{g} = 39{,}7\ \text{mg}$$



$$\text{Paso}\ 3 \cdot \text{ppm}\left(\text{en agua ≈ mg/L}\right) = \dfrac{39{,}7\ \text{mg}}{6{,}00\ \text{L}} = 6{,}62\ \text{ppm}$$

- **Trampa:** evaporar hasta el 5 % solo concentra para que precipite mejor: **los moles de SO₄²⁻ no cambian**. Se divide entre los 6,00 L de agua original.

**Cloruros:**


$$\text{Paso}\ 1 \cdot \text{n(Ag}^{+}\text{)} = 0{,}03360\ \text{mol/L} \cdot 0{,}00135\ \text{L} = 4{,}536\cdot10^{-5}\ \text{mol} = \text{mol de Cl}^{-}\left(\text{Ag}^{+} + \text{Cl}^{-}$$

→ AgCl, 1 : 1)



$$\text{Paso}\ 2 \cdot \text{m(Cl}^{-}\text{)} = 4{,}536\cdot10^{-5}\ \text{mol} \cdot 35{,}453\ \text{g/mol} = 1{,}608\cdot10^{-3}\ \text{g} = 1{,}608\ \text{mg en}\ 10{,}0\ \text{mL}$$



$$\text{Paso}\ 3 \cdot \text{ppm} = \dfrac{1{,}608\ \text{mg}}{0{,}0100\ \text{L}} = 161\ \text{ppm}$$


##### P7-4.5 · 2ª convocatoria (Julio), 7 de julio de 2023 (ej. 4) · Cu en un mineral (precipitación con NaOH)

[[SOL 162:601-842 163:40-68]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-4_5.svg 100%]]


**Datos:** 150 g de mineral → CuCl₂ en disolución · se gasta 41,7 mL de NaOH 0,75 M para precipitar todo el Cu(OH)₂. **Me piden:** g de CuO al calentar y kg de Cu por tonelada.

**Reacción:** **Cu²⁺ + 2 OH⁻ → Cu(OH)₂↓** (2 OH⁻ por Cu) · al calentar: Cu(OH)₂ → CuO + H₂O (mismo Cu)

**Paso 1 · OH⁻ gastados.**

$$\text{n} = 0{,}75\ \text{mol/L} \cdot 0{,}0417\ \text{L} = 0{,}03128\ \text{mol de OH}^{-}$$


**Paso 2 · Cu:**

$$\text{n} = 0{,}03128\ \text{mol OH}^{-} \cdot \dfrac{1\ \text{mol Cu}}{2\ \text{mol OH}^{-}} = 0{,}01564\ \text{mol de Cu}$$


**Paso 3 · CuO**

(1 Cu por CuO):

$$\text{m} = 0{,}01564\ \text{mol} \cdot 79{,}55\ \text{g/mol} = 1{,}2\ \text{g de CuO}$$


**Paso 4 · Cu por tonelada.**

$$\text{m(Cu)} = 0{,}01564\ \text{mol} \cdot 63{,}546\ \text{g/mol} = 0{,}994\ \text{g en}\ 150\ \text{g de mineral}$$

$$\dfrac{0{,}994\ \text{g Cu}}{150\ \text{g mineral}} = 6{,}6\cdot10^{-3}\ \text{g/g}$$

en 1 t = 10⁶ g:

$$6{,}6\cdot10^{3}\ \text{g} = 6{,}6\ \text{kg de Cu por tonelada}$$


##### P7-4.6 · Segunda convocatoria, 10 de septiembre de 2015 (ej. 5) · Mezcla NaCl/CaCl₂ (AgCl)

[[SOL 59:382-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-4_6.svg 100%]]


**Datos:** 0,8870 g de mezcla NaCl + CaCl₂ → 2,210 g de AgCl. **Me piden:** % de cada uno.

**¿Qué pasa?** Todo el Cl⁻ (de los dos) precipita como AgCl. El NaCl aporta 1 Cl y el CaCl₂ aporta **2 Cl**.

**Paso 1 · Cl⁻ total.**

$$\text{n} = \dfrac{2{,}210\ \text{g AgCl}}{143{,}32\ \text{g/mol}} = 0{,}01542\ \text{mol de Cl}^{-}$$


**Paso 2 · Planteo** con x = g de NaCl → CaCl₂ = (0,8870 − x):

$$\underbrace{\frac{x}{58{,}44}}_{\text{mol Cl del NaCl}}+\underbrace{2\cdot\frac{0{,}8870-x}{110{,}98}}_{\text{mol Cl del CaCl}_2}=\underbrace{0{,}01542}_{\text{mol Cl total}}$$

**Paso 3 · Resuelvo:** 0,01711·x + 0,01599 − 0,01802·x = 0,01542 → −0,00091·x = −0,00057 → **x ≈ 0,621 g de NaCl**

**Paso 4 · %:**

$$\dfrac{0{,}621\ \text{g}}{0{,}8870\ \text{g}} \cdot 100 = 70{,}0\ \text{\% NaCl;}\ 30{,}0\ \text{\% CaCl}_{2}$$


##### P7-4.7 · Segundo parcial, 10 de enero de 2017 (ej. 4) · Antiácido Al(OH)₃/Mg(OH)₂ (retrovaloración + gravimetría)

[[SOL 76:467-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-4_7.svg 100%]]


**Datos:** 0,600 g de antiácido · 50,0 mL de HCl 0,500 M · el sobrante gasta 16,5 mL de NaOH 0,377 M · todo el Mg da 303 mg de Mg₂P₂O₇. **Me piden:** % de Al(OH)₃, Mg(OH)₂ y otros.

**¿Qué pasa?** Hay dos incógnitas (Al(OH)₃ y Mg(OH)₂) y dos experimentos: la **gravimetría** me da el Mg directamente, y la **retrovaloración** me da los OH⁻ totales; restando los del Mg, quedan los del Al.

**Paso 1 · Mg por gravimetría** (2 Mg en cada Mg₂P₂O₇):
$$\text{n(Mg}_{2}\text{P}_{2}\text{O}_{7}\text{)} = \dfrac{0{,}303\ \text{g}}{222{,}55\ \text{g/mol}} = 1{,}361\cdot10^{-3}\ \text{mol}$$

$$\text{n(Mg)} = 2 \cdot 1{,}361\cdot10^{-3} = 2{,}723\cdot10^{-3}\ \text{mol de Mg(OH)}_{2}$$

$$\text{m(Mg(OH)}_{2}\text{)} = 2{,}723\cdot10^{-3}\ \text{mol} \cdot 58{,}320\ \text{g/mol} = 0{,}1588\ \text{g}$$

→ **26,5 %**


**Paso 2 · OH⁻ totales por retrovaloración:**
$$\text{HCl añadido} = 0{,}500\ \text{mol/L} \cdot 0{,}0500\ \text{L} = 0{,}0250\ \text{mol} \cdot \text{HCl sobrante} = 0{,}377\ \text{mol/L} \cdot 0{,}0165\ \text{L} = 6{,}22\cdot10^{-3}\ \text{mol}$$

$$\text{OH}^{-}\text{ del antiácido} = 0{,}0250 - 0{,}00622 = 0{,}01878\ \text{mol de OH}^{-}$$


**Paso 3 · OH⁻ que aporta el Mg(OH)₂**

(2 por fórmula):

$$2 \cdot 2{,}723\cdot10^{-3} = 5{,}446\cdot10^{-3}\ \text{mol}$$


**Paso 4 · OH⁻ del Al(OH)₃:**

$$0{,}01878 - 0{,}005446 = 0{,}01333\ \text{mol}$$

$$\text{n(Al(OH)}_{3}\text{)} = \dfrac{0{,}01333}{3} = 4{,}445\cdot10^{-3}\ \text{mol}$$

(3 OH⁻ por fórmula)

$$\text{m} = 4{,}445\cdot10^{-3}\ \text{mol} \cdot 78{,}003\ \text{g/mol} = 0{,}347\ \text{g}$$

→ **57,9 %**


**Paso 5 · Otros:**

$$100 - 57{,}9 - 26{,}4 = 15{,}7\ \text{\%}$$


**Lo que tienes que llevarte:** cuando hay dos incógnitas, busca **un dato para cada una**.

### Avisos de este apartado (se resuelven en otro tema)

- **Mezclar K₂CrO₄ y AgNO₃** y calcular lo que queda en disolución → **tema 11**.


<div class="newpage"></div>

## 5. Reacciones de formación de complejos

### Teoría necesaria (en clase)

- **Complejo:** un **metal central** unido por **enlaces covalentes coordinados** a moléculas o iones llamados **ligandos** (H₂O, CO, NH₃, ciclopentadienilo…). Se ve a fondo en el **tema 12**.
- Es un equilibrio, pero con **K de 10¹⁰–10¹⁴**: se considera **completamente desplazado** (estequiométrico). Ejemplo: AgCl(s) + 2 NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻.
- Muchos complejos tienen **color**: su aparición o desaparición marca el **punto de equivalencia** sin necesidad de indicador. Se usan en volumetrías de Ca²⁺ y Mg²⁺ (dureza del agua, aguas minerales).

> **Aviso:** **todos** los problemas con complejos (complejo + Kps, sacar Kf, solubilidad en un ligando) se resuelven en el **tema 12**. El primer paso de todos ellos es justo esta idea: *"el complejo se forma completo"*.

<div class="newpage"></div>

## 6. Reacciones de oxidación-reducción

### Teoría necesaria

- **Redox:** **intercambio de electrones**. El que **se oxida** pierde e⁻ (sube su estado de oxidación) y es el **reductor**; el que **se reduce** gana e⁻ (baja su estado de oxidación) y es el **oxidante**.
- **Dismutación (desproporción):** un mismo compuesto se oxida y se reduce a la vez. 2 H₂O₂ → 2 H₂O + O₂ (el agua oxigenada se descompone sola).
- **Estados de oxidación en orgánica** (en clase): **no** se calcula con la fórmula molecular (sale un promedio raro, −5/2 en el butano). Se rompe cada enlace y el par se lo lleva el **más electronegativo**; si son iguales (C–C), uno para cada uno. El estado de oxidación es la carga que queda. Butano: −3, −2, −2, −3. Al pasar a butan-1-ol, solo cambia el C unido al O: −3 → **−1**; aldehído: **+1**; ácido butanoico: **+3**. La distribución de carga real se parece más a los estados de oxidación (enlace iónico puro) que a las cargas formales (covalente puro).

### Ajuste por el método del ion-electrón (el único que recomienda)

> *"El que no falla nunca es el de protones, en medio ácido; y si tengo que pasarlo a medio básico, añado OH⁻ a ambos miembros."* El ajuste directo en medio básico con OH⁻ y agua **no lo recomienda** (a veces falla).

1. **Estados de oxidación:** quién se oxida y quién se reduce.
2. **Semirreacciones** con los **iones completos** (MnO₄⁻ → Mn²⁺, Cr₂O₇²⁻ → Cr³⁺…).
3. Ajusta los átomos que no son H ni O.
4. **O** con **H₂O**.
5. **H** con **H⁺**.
6. **Carga** con **e⁻**.
7. Multiplica para que los **e⁻ se igualen** y **suma**.
8. **Pasa a especies neutras** añadiendo los **mismos contraiones a los dos lados** (*"para que no hagamos tongo"*).
9. **Medio básico:** añade a los dos lados tantos OH⁻ como H⁺ haya; H⁺ + OH⁻ → H₂O; quita el agua sobrante.

**Por qué hay que llegar a la ecuación neutra (en clase, Cu + HNO₃):**

$$\text{Cu}\rightarrow\text{Cu}^{2+}+2e^-\qquad \text{NO}_3^-+2\text{H}^++e^-\rightarrow\text{NO}_2+\text{H}_2\text{O}\;(\times2)$$

$$\text{Cu}+2\text{NO}_3^-+4\text{H}^+\rightarrow\text{Cu}^{2+}+2\text{NO}_2+2\text{H}_2\text{O}\;\;\Rightarrow\;\;\text{Cu}+4\,\text{HNO}_3\rightarrow\text{Cu(NO}_3)_2+2\,\text{NO}_2+2\,\text{H}_2\text{O}$$

La iónica da Cu : HNO₃ = 1 : 2, pero la **neutra da 1 : 4**: el HNO₃ además de oxidante aporta los H⁺ y los NO₃⁻ que acompañan al Cu²⁺. **Si te piden cantidad de ácido, usa la neutra.**

### Las semirreacciones que más caen (apréndetelas)

| Especie | Semirreacción (medio ácido) | e⁻ |
|---|---|---|
| Permanganato | MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O | 5 |
| Dicromato | Cr₂O₇²⁻ + 14 H⁺ + 6 e⁻ → 2 Cr³⁺ + 7 H₂O | 6 |
| Hierro | Fe²⁺ → Fe³⁺ + e⁻ | 1 |
| Oxalato | H₂C₂O₄ → 2 CO₂ + 2 H⁺ + 2 e⁻ | 2 |
| Agua oxigenada (reductor) | H₂O₂ → O₂ + 2 H⁺ + 2 e⁻ | 2 |
| Agua oxigenada (oxidante) | H₂O₂ + 2 H⁺ + 2 e⁻ → 2 H₂O | 2 |
| Yoduro | 2 I⁻ → I₂ + 2 e⁻ | 2 |
| Tiosulfato | 2 S₂O₃²⁻ → S₄O₆²⁻ + 2 e⁻ | 2 (1 por S₂O₃²⁻) |

**Atajo para la estequiometría:** en el punto de equivalencia, **e⁻ cedidos = e⁻ captados**: n(red)·e⁻(red) = n(ox)·e⁻(ox). Así sale MnO₄⁻ : Fe²⁺ = 1 : 5, Cr₂O₇²⁻ : Fe²⁺ = 1 : 6, MnO₄⁻ : oxalato = 2 : 5, MnO₄⁻ : H₂O₂ = 2 : 5. **Pero si piden masa de un reactivo neutro (ácido), ajusta la ecuación completa.**



### Ajustes resueltos paso a paso (los que más caen)

#### Ajuste 1 · Permanganato + Fe²⁺ (medio ácido)

**Semirreacción de reducción** (el Mn pasa de +7 en MnO₄⁻ a +2):
1. MnO₄⁻ → Mn²⁺ (el Mn ya está ajustado: 1 y 1)
2. **O:** a la izquierda hay 4 O → pongo **4 H₂O** a la derecha: MnO₄⁻ → Mn²⁺ + 4 H₂O
3. **H:** ahora hay 8 H a la derecha → pongo **8 H⁺** a la izquierda: MnO₄⁻ + 8 H⁺ → Mn²⁺ + 4 H₂O
4. **Carga:** izquierda −1 + 8 = **+7**; derecha **+2** → faltan 5 cargas negativas a la izquierda → **+ 5 e⁻**:

**MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O**

**Semirreacción de oxidación:** **Fe²⁺ → Fe³⁺ + 1 e⁻**

**Igualar electrones:** la del Fe × 5 → 5 Fe²⁺ → 5 Fe³⁺ + 5 e⁻. Sumo y se van los 5 e⁻:

**MnO₄⁻ + 5 Fe²⁺ + 8 H⁺ → Mn²⁺ + 5 Fe³⁺ + 4 H₂O** → **1 MnO₄⁻ por cada 5 Fe²⁺**

#### Ajuste 2 · Dicromato + Fe²⁺ (medio ácido)

1. Cr₂O₇²⁻ → **2** Cr³⁺ (ajusto el Cr: 2 y 2)
2. **O:** 7 O → **7 H₂O** a la derecha
3. **H:** 14 H a la derecha → **14 H⁺** a la izquierda
4. **Carga:** izquierda −2 + 14 = +12; derecha 2·(+3) = +6 → **+ 6 e⁻** a la izquierda:

**Cr₂O₇²⁻ + 14 H⁺ + 6 e⁻ → 2 Cr³⁺ + 7 H₂O**

Fe²⁺ → Fe³⁺ + e⁻ (× 6) → **Cr₂O₇²⁻ + 6 Fe²⁺ + 14 H⁺ → 2 Cr³⁺ + 6 Fe³⁺ + 7 H₂O** → **1 dicromato por cada 6 Fe²⁺**

#### Ajuste 3 · Permanganato + ácido oxálico (medio ácido)

**Oxidación** (el C pasa de +3 a +4; hay 2 C): H₂C₂O₄ → **2** CO₂; los 2 H sobran → **+ 2 H⁺**; carga: 0 | +2 → **+ 2 e⁻** a la derecha:

**H₂C₂O₄ → 2 CO₂ + 2 H⁺ + 2 e⁻**

**Reducción:** MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O

**Igualar electrones** (mínimo común múltiplo de 2 y 5 = 10): permanganato × 2, oxálico × 5:  
2 MnO₄⁻ + 16 H⁺ + 5 H₂C₂O₄ → 2 Mn²⁺ + 8 H₂O + 10 CO₂ + 10 H⁺ → quito 10 H⁺ de cada lado:

**2 MnO₄⁻ + 5 H₂C₂O₄ + 6 H⁺ → 2 Mn²⁺ + 10 CO₂ + 8 H₂O** → **2 MnO₄⁻ por cada 5 oxálicos**

**A especies neutras** (el H⁺ lo da el H₂SO₄; el MnO₄⁻ va como KMnO₄): añado 2 K⁺ y 3 SO₄²⁻ a los dos lados:

**2 KMnO₄ + 5 H₂C₂O₄ + 3 H₂SO₄ → K₂SO₄ + 2 MnSO₄ + 10 CO₂ + 8 H₂O**

> **El H₂O₂ con permanganato es igual que el oxálico** (H₂O₂ → O₂ + 2 H⁺ + 2 e⁻): **2 MnO₄⁻ por cada 5 H₂O₂**.

### Ejercicios de clase

##### EC 7.6 · Ejercicio de clase · Cu/Au con HNO₃ comercial

Es el mismo problema que el **P7-6.8** (Segundo parcial, 13 de enero de 2022), resuelto abajo con la solución del profesor. El ajuste es el de la pizarra: **Cu + 4 HNO₃ → Cu(NO₃)₂ + 2 NO₂ + 2 H₂O**.

### Problemas de examen

#### Problemas · Tipo A · Volumetría redox directa

**Cómo se hace:** (1) ajusta (o usa el atajo: e⁻ cedidos = e⁻ captados); (2) moles de valorante = M · V; (3) relación de los coeficientes → moles de analito; (4) **alícuotas** (× V_total/V_alícuota); (5) expresa como piden: M, g/L, %, μg/mL, ppm, % en volumen (gases: PV = nRT).

**Trampas:** medio **básico**; "especies neutras" cuando piden la ecuación o la masa de un ácido; estado de oxidación final desconocido; % en peso de una disolución diluida (densidad ≈ 1 g/mL); unidades raras (μg/mL, kg/t).

**Se repite en:** dos pasos (Tipo B) y tema 9 (rendimiento + reparto).

##### P7-6.1 · 1ª convocatoria (Enero), 22 de enero de 2026 (ej. 5) · Hidracina con yodato

[[SOL 190:595-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_1.svg 100%]]


**Datos:** 30,0 mL de N₂H₄ 0,1622 M · KIO₃ 0,1070 M. **Me piden:** volumen de KIO₃ (mL).

**Reacción** (ya la dan ajustada): **4 IO₃⁻ + 5 N₂H₄ + 4 H⁺ → 5 N₂ + 2 I₂ + 12 H₂O** → 4 IO₃⁻ por cada 5 N₂H₄.  
*Comprobación con electrones:* N de −2 a 0 → 4 e⁻ por N₂H₄ (×5 = 20 e⁻); I de +5 a 0 → 5 e⁻ por IO₃⁻ (×4 = 20 e⁻) ✓.

**Paso 1 · Moles de hidracina.**

$$\text{n} = \text{M} \cdot \text{V} = 0{,}1622\ \text{mol/L} \cdot 0{,}0300\ \text{L} = 4{,}866\cdot10^{-3}\ \text{mol de N}_{2}\text{H}_{4}$$


**Paso 2 · Moles de IO₃⁻.**

$$\text{n} = 4{,}866\cdot10^{-3}\ \text{mol N}_{2}\text{H}_{4} \cdot \dfrac{4\ \text{mol IO}_{3}^{-}}{5\ \text{mol N}_{2}\text{H}_{4}} = 3{,}893\cdot10^{-3}\ \text{mol de IO}_{3}^{-}$$


**Paso 3 · Volumen de KIO₃.**

$$\text{V} = \text{n/M} = \dfrac{3{,}893\cdot10^{-3}\ \text{mol}}{0{,}1070\ \text{mol/L}} = 0{,}03638\ \text{L} = 36{,}4\ \text{mL}$$


##### P7-6.2 · 2ª convocatoria (Julio), 4 de julio de 2025 (ej. 4) · Ca en sangre (oxalato + permanganato)

[[SOL 181:524-681]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_2.svg 100%]]


**Datos:** 10,0 mL de sangre · el oxalato gasta 24,2 mL de KMnO₄ 9,56·10⁻⁴ M. **Me piden:** μg de Ca por mL de sangre.

**¿Qué pasa (laboratorio)?** El Ca²⁺ de la sangre se precipita como CaC₂O₄ (1 Ca por cada oxalato). Ese sólido se disuelve en H₂SO₄ (queda H₂C₂O₄) y el oxalato se valora con permanganato. **Todo el Ca → todo el oxalato → gasta permanganato.**

**Reacción:** la del **Ajuste 3** → **2 KMnO₄ + 5 H₂C₂O₄ + 3 H₂SO₄ → K₂SO₄ + 2 MnSO₄ + 10 CO₂ + 8 H₂O**

**Paso 1 · Moles de MnO₄⁻.**

$$\text{n} = 9{,}56\cdot10^{-4}\ \text{mol/L} \cdot 0{,}0242\ \text{L} = 2{,}314\cdot10^{-5}\ \text{mol de MnO}_{4}^{-}$$


**Paso 2 · Moles de oxalato**

(5 por cada 2 MnO₄⁻):

$$\text{n} = 2{,}314\cdot10^{-5}\ \text{mol} \cdot \left(5\text{/}\ 2\right) = 5{,}784\cdot10^{-5}\ \text{mol de oxalato} = \text{mol de Ca}$$


**Paso 3 · Masa de Ca.**

$$\text{m} = 5{,}784\cdot10^{-5}\ \text{mol} \cdot 40{,}078\ \text{g/mol} = 2{,}318\cdot10^{-3}\ \text{g} = 2318\ \text{μg}$$

(1 g = 10⁶ μg)


**Paso 4 · Por mL de sangre:**

$$\dfrac{2318\ \text{μg}}{10{,}0\ \text{mL}} = 232\ \text{μg/mL}$$


##### P7-6.3 · Segundo parcial, 16 de enero de 2012 (ej. 2) · Ca en sangre (mismo método)

[[SOL 20:350-470]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_3.svg 100%]]


Mismo razonamiento que el anterior.

**Paso 1 · Moles de MnO₄⁻.**

$$\text{n} = 9{,}76\cdot10^{-4}\ \text{mol/L} \cdot 0{,}00212\ \text{L} = 2{,}069\cdot10^{-6}\ \text{mol de MnO}_{4}^{-}$$


**Paso 2 · Moles de oxalato = moles de Ca**

(5 por cada 2 MnO₄⁻):

$$\text{n} = 2{,}069\cdot10^{-6}\ \text{mol MnO}_{4}^{-} \cdot \dfrac{5\ \text{mol ox}}{2\ \text{mol MnO}_{4}^{-}} = 5{,}173\cdot10^{-6}\ \text{mol de Ca}$$


**Paso 3 · Masa de Ca.**

$$\text{m} = 5{,}173\cdot10^{-6}\ \text{mol} \cdot 40{,}08\ \text{g/mol} = 2{,}073\cdot10^{-4}\ \text{g de Ca}\left(\text{=}\ 207\ \text{μg}\right)$$


**Paso 4 · Por mL de sangre.**

$$\dfrac{207\ \text{μg}}{10{,}0\ \text{mL}} = 20{,}7\ \text{μg/mL}$$


##### P7-6.4 · 1ª convocatoria (Enero), 23 de enero de 2025 (ej. 2) · Ditionito + cromato en **medio básico**

[[SOL 180:259-405]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_4.svg 100%]]


**Datos:** 100,0 L de agua con CrO₄²⁻ 0,0148 M · el cromato pasa a Cr(OH)₃ y el ditionito (S₂O₄²⁻) a sulfito (SO₃²⁻). **Me piden:** masa mínima de Na₂S₂O₄ y masa de Cr(OH)₃ formado.

**Ajuste (método del profesor: primero en ácido y luego paso a básico):**
- **Reducción** (Cr +6 → +3): CrO₄²⁻ → Cr(OH)₃. O: 4 a la izquierda, 3 a la derecha → **+ 1 H₂O** a la derecha. H: 3 + 2 = 5 a la derecha → **+ 5 H⁺** a la izquierda. Carga: −2 + 5 = +3 | 0 → **+ 3 e⁻** a la izquierda:
  CrO₄²⁻ + 5 H⁺ + 3 e⁻ → Cr(OH)₃ + H₂O
- **Oxidación** (S +3 → +4, hay 2 S): S₂O₄²⁻ → **2** SO₃²⁻. O: 4 | 6 → **+ 2 H₂O** a la izquierda. H: 4 → **+ 4 H⁺** a la derecha. Carga: −2 | −4 + 4 = 0 → **+ 2 e⁻** a la derecha:
  S₂O₄²⁻ + 2 H₂O → 2 SO₃²⁻ + 4 H⁺ + 2 e⁻
- **Igualo** (6 e⁻): cromo × 2, azufre × 3 y sumo:
  2 CrO₄²⁻ + 10 H⁺ + 3 S₂O₄²⁻ + 6 H₂O → 2 Cr(OH)₃ + 2 H₂O + 6 SO₃²⁻ + 12 H⁺ → simplifico: **2 CrO₄²⁻ + 3 S₂O₄²⁻ + 4 H₂O → 2 Cr(OH)₃ + 6 SO₃²⁻ + 2 H⁺**
- **A medio básico:** sumo 2 OH⁻ a los dos lados (2 H⁺ + 2 OH⁻ = 2 H₂O) y quito el agua sobrante:
  **2 CrO₄²⁻ + 3 S₂O₄²⁻ + 2 H₂O + 2 OH⁻ → 2 Cr(OH)₃ + 6 SO₃²⁻** → **3 S₂O₄²⁻ por cada 2 CrO₄²⁻**

**Paso 1 · Moles de cromato.**

$$\text{n} = 0{,}0148\ \text{mol/L} \cdot 100{,}0\ \text{L} = 1{,}48\ \text{mol de CrO}_{4}^{2-}$$


**Paso 2 · Ditionito.**

$$\text{n} = 1{,}48\ \text{mol CrO}_{4}^{2-} \cdot \dfrac{3\ \text{mol S}_{2}\text{O}_{4}^{2-}}{2\ \text{mol CrO}_{4}^{2-}} = 2{,}22\ \text{mol}$$

$$\text{m} = 2{,}22\ \text{mol} \cdot 174{,}107\ \text{g/mol} = 387\ \text{g de Na}_{2}\text{S}_{2}\text{O}_{4}$$


**Paso 3 · Cr(OH)₃**

(1 por cada CrO₄²⁻):

$$\text{m} = 1{,}48\ \text{mol} \cdot 103{,}018\ \text{g/mol} = 152\ \text{g de Cr(OH)}_{3}$$


##### P7-6.5 · 3ª convocatoria (Octubre), 20 de octubre de 2023 (ej. 4) · Yoduro con Ce⁴⁺

[[SOL 164:647-842 165:40-68]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_5.svg 100%]]


**Datos:** 250 mL de muestra · gasta 20,0 mL de Ce⁴⁺ 0,050 M · I⁻ → ICl y Ce⁴⁺ → Ce³⁺. **Me piden:** concentración de yodo en mg/mL.

**Electrones:** I⁻ (−1) → ICl (+1): cede **2 e⁻** · Ce⁴⁺ → Ce³⁺: capta **1 e⁻** → hacen falta **2 Ce⁴⁺ por cada I⁻**.

**Paso 1 · Moles de Ce⁴⁺.**

$$\text{n} = 0{,}050\ \text{mol/L} \cdot 0{,}0200\ \text{L} = 1{,}0\cdot10^{-3}\ \text{mol}$$


**Paso 2 · Moles de I⁻:**

$$\text{n} = 1{,}0\cdot10^{-3}\ \text{mol Ce}^{4+} \cdot \dfrac{1\ \text{mol I}^{-}}{2\ \text{mol Ce}^{4+}} = 5{,}0\cdot10^{-4}\ \text{mol de I}^{-}$$


**Paso 3 · Masa:**

$$\text{m} = 5{,}0\cdot10^{-4}\ \text{mol} \cdot 126{,}90\ \text{g/mol} = 0{,}0635\ \text{g} = 63{,}5\ \text{mg en}\ 250\ \text{mL}$$

$$\dfrac{63{,}5\ \text{mg}}{250\ \text{mL}} = 0{,}25\ \text{mg/mL}$$

*(El PDF pone "0,25 g/mL": es una errata; son mg/mL.)*

##### P7-6.6 · 3ª convocatoria (Noviembre), 21 de noviembre de 2022 (ej. 4) · % de H₂O₂ en agua oxigenada

[[SOL 154:305-429]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_6.svg 100%]]


**Datos:** 5,00 mL de agua oxigenada · gastan 28,0 mL de KMnO₄ 0,01250 M. **Me piden:** % en peso de H₂O₂.

**Reacción** (como el oxálico): **2 KMnO₄ + 5 H₂O₂ + 3 H₂SO₄ → K₂SO₄ + 2 MnSO₄ + 5 O₂ + 8 H₂O**

**Paso 1 · MnO₄⁻.**

$$\text{n} = 0{,}01250\ \text{mol/L} \cdot 0{,}0280\ \text{L} = 3{,}50\cdot10^{-4}\ \text{mol}$$


**Paso 2 · H₂O₂:**

$$\text{n} = 3{,}50\cdot10^{-4}\ \text{mol} \cdot \left(5\text{/}\ 2\right) = 8{,}75\cdot10^{-4}\ \text{mol}$$

$$\text{m} = 8{,}75\cdot10^{-4}\ \text{mol} \cdot 34{,}014\ \text{g/mol} = 0{,}0298\ \text{g}$$


**Paso 3 · %.**

Los 5,00 mL de disolución diluida pesan ≈ 5,00 g (densidad ≈ 1 g/mL):

$$\text{\%} = \dfrac{0{,}0298\ \text{g}}{5{,}00\ \text{g}} \cdot 100 = 0{,}595\ \text{\%}$$


##### P7-6.7 · Segunda convocatoria, 13 de septiembre de 2022 (ej. 4) · Solubilidad del Na₂C₂O₄ por valoración redox

[[SOL 151:665-842 152:40-67]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_7.svg 100%]]


**Datos:** 5,00 mL de disolución saturada de Na₂C₂O₄ · gasta 25,8 mL de KMnO₄ 0,02140 M. **Me piden:** solubilidad en g/L.

**Paso 1 · MnO₄⁻.**

$$\text{n} = 0{,}02140\ \text{mol/L} \cdot 0{,}0258\ \text{L} = 5{,}521\cdot10^{-4}\ \text{mol}$$


**Paso 2 · Oxalato**

(5 por cada 2):

$$\text{n} = 5{,}521\cdot10^{-4}\ \text{mol} \cdot 5\text{/}\ 2 = 1{,}380\cdot10^{-3}\ \text{mol en}\ 5{,}00\ \text{mL}$$

$$\text{M} = \dfrac{1{,}380\cdot10^{-3}\ \text{mol}}{0{,}00500\ \text{L}} = 0{,}2761\ \text{mol/L}$$


**Paso 3 · g/L:**

$$0{,}2761\ \text{mol/L} \cdot 134{,}00\ \text{g/mol} = 37{,}0\ \text{g/L}$$


**Ojo:** aquí "solubilidad" es solo la concentración de la disolución saturada; no hay Kps (eso es tema 11).

##### P7-6.8 · Segundo parcial, 13 de enero de 2022 (ej. 1) · Cu/Au con HNO₃ comercial (= EC 7.6)

[[SOL 143:203-334]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_8.svg 100%]]


**Datos:** 100,0 g de aleación con 85 % de Cu · HNO₃ comercial del 62 % y densidad 1,3667 g/mL. **Me piden:** volumen mínimo de ácido comercial.

**¿Qué pasa?** El HNO₃ disuelve el Cu (se oxida a Cu²⁺) y se reduce a NO₂; el Au no reacciona (por eso se recupera).

**Reacción** (la de la pizarra, **en especies neutras**): **Cu + 4 HNO₃ → Cu(NO₃)₂ + 2 NO₂ + 2 H₂O** → 4 HNO₃ por cada Cu.  
*Con la iónica (Cu : HNO₃ = 1 : 2) te saldría la mitad: el HNO₃ también aporta los NO₃⁻ del Cu(NO₃)₂.*

**Paso 1 · Masa y moles de Cu.**

$$\text{m} = 100{,}0\ \text{g} \cdot 85\text{/}\ 100 = 85{,}0\ \text{g de Cu}$$

$$\text{n} = \dfrac{85{,}0\ \text{g}}{63{,}546\ \text{g/mol}} = 1{,}338\ \text{mol de Cu}$$


**Paso 2 · Moles de HNO₃:**

$$\text{n} = 1{,}338\ \text{mol Cu} \cdot \dfrac{4\ \text{mol HNO}_{3}}{1\ \text{mol Cu}} = 5{,}350\ \text{mol de HNO}_{3}$$


**Paso 3 · Masa de HNO₃ puro:**

$$\text{m} = 5{,}350\ \text{mol} \cdot 63{,}02\ \text{g/mol} = 337{,}2\ \text{g de HNO}_{3}$$


**Paso 4 · Masa de ácido comercial**

(de cada 100 g de comercial, 62 son HNO₃):

$$\text{m} = 337{,}2\ \text{g HNO}_{3} \cdot \dfrac{100\ \text{g comercial}}{62\ \text{g HNO}_{3}} = 543{,}8\ \text{g de comercial}$$


**Paso 5 · Volumen**

→ (densidad = masa/volumen

V = m/d):

$$\text{V} = \dfrac{543{,}8\ \text{g}}{1{,}3667\ \text{g/mL}} = 398\ \text{mL}$$

→ **4,0·10² mL**


##### P7-6.9 · SEGUNDO PARCIAL, 15 de enero de 2020 (ej. 1) · H₂O₂ comercial en g/L

[[SOL 115:189-321]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_9.svg 100%]]


**Datos:** 20,00 mL de agua oxigenada (diluidos con 20 mL de agua) · gastan 15,5 mL de KMnO₄ 0,1050 M. **Me piden:** [H₂O₂] del producto comercial en g/L.

**Paso 1 · MnO₄⁻.**

$$\text{n} = 0{,}1050\ \text{mol/L} \cdot 0{,}0155\ \text{L} = 1{,}628\cdot10^{-3}\ \text{mol}$$


**Paso 2 · H₂O₂**

(5 por cada 2):

$$\text{n} = 1{,}628\cdot10^{-3}\ \text{mol} \cdot 5\text{/}\ 2 = 4{,}069\cdot10^{-3}\ \text{mol, que estaban en los}\ 20{,}00\ \text{mL de producto}$$

(el agua añadida no cambia los moles)


**Paso 3 · Concentración:**

$$\text{M} = \dfrac{4{,}069\cdot10^{-3}\ \text{mol}}{0{,}02000\ \text{L}} = 0{,}2034\ \text{mol/L}$$

$$0{,}2034\ \text{mol/L} \cdot 34{,}015\ \text{g/mol} = 6{,}92\ \text{g/L}$$


##### P7-6.10 · Fe con dicromato (%Fe): 2ª conv. 11-sep-2020 (ej. 4) = 3ª conv. 1-dic-2020 (ej. 4) = Segundo parcial 18-ene-2011 (ej. 3)

[[SOL 123:351-450]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_10.svg 100%]]


**Datos:** 0,9132 g de mineral → Fe²⁺ · gasta 28,72 mL de K₂Cr₂O₇ 0,05051 M. **Me piden:** % de Fe.

**Reacción:** la del **Ajuste 2** → 1 Cr₂O₇²⁻ por cada 6 Fe²⁺.

**Paso 1 · Dicromato.**

$$\text{n} = 0{,}05051\ \text{mol/L} \cdot 0{,}02872\ \text{L} = 1{,}4506\cdot10^{-3}\ \text{mol}$$


**Paso 2 · Fe:**

$$\text{n} = 1{,}4506\cdot10^{-3}\ \text{mol Cr}_{2}\text{O}_{7}^{2-} \cdot \dfrac{6\ \text{mol Fe}^{2+}}{1\ \text{mol Cr}_{2}\text{O}_{7}^{2-}} = 8{,}704\cdot10^{-3}\ \text{mol de Fe}$$


**Paso 3 · %:**

$$\text{m} = 8{,}704\cdot10^{-3}\ \text{mol} \cdot 55{,}845\ \text{g/mol} = 0{,}4861\ \text{g}$$

$$\dfrac{0{,}4861\ \text{g}}{0{,}9132\ \text{g}} \cdot 100 = 53{,}23\ \text{\%}$$


##### P7-6.11 · Segundo parcial, 19 de enero de 2012 (ej. 2) · Fe con dicromato con **alícuota**

[[SOL 21:475-579]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_11.svg 100%]]


**Datos:** 0,9132 g de mineral disueltos en 0,5 L (500 mL) · se valoran **50 mL** con 32,03 mL de K₂Cr₂O₇ 0,00506 M. **Me piden:** % de Fe.

**Paso 1 · Moles de dicromato.**

$$\text{n} = 0{,}00506\ \text{mol/L} \cdot 0{,}03203\ \text{L} = 1{,}621\cdot10^{-4}\ \text{mol de Cr}_{2}\text{O}_{7}^{2-}$$


**Paso 2 · Fe en los 50 mL**

(6 Fe²⁺ por cada Cr₂O₇²⁻):

$$\text{n} = 1{,}621\cdot10^{-4}\ \text{mol Cr}_{2}\text{O}_{7}^{2-} \cdot \dfrac{6\ \text{mol Fe}^{2+}}{1\ \text{mol Cr}_{2}\text{O}_{7}^{2-}} = 9{,}724\cdot10^{-4}\ \text{mol de Fe}$$


**Paso 3 · Fe en toda la muestra**

(alícuota de 50 mL de 500 mL):

$$\text{n} = 9{,}724\cdot10^{-4}\ \text{mol} \cdot \dfrac{500\ \text{mL}}{50\ \text{mL}} = 9{,}724\cdot10^{-3}\ \text{mol de Fe}$$


**Paso 4 · Masa y %.**

$$\text{m} = 9{,}724\cdot10^{-3}\ \text{mol} \cdot 55{,}84\ \text{g/mol} = 0{,}5430\ \text{g de Fe}$$


**Paso 5 · %Fe.**

$$\text{\%} = \dfrac{0{,}5430\ \text{g}}{0{,}9132\ \text{g}} \cdot 100 = 59{,}5\ \text{\%}$$


##### P7-6.12 · Segunda convocatoria, 13 de septiembre de 2019 (ej. 4) · Molaridad del FeSO₄ con dicromato

[[SOL 108:100-248]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_12.svg 100%]]


**Datos:** 1,692 g de K₂Cr₂O₇ en 500,0 mL · 25,00 mL de esa disolución gastan 13,76 mL de FeSO₄. **Me piden:** [FeSO₄] y la reacción en especies neutras.

**Paso 1 · Moles de dicromato pesados.**

$$\text{n} = \dfrac{1{,}692\ \text{g}}{294{,}18\ \text{g/mol}} = 5{,}752\cdot10^{-3}\ \text{mol de K}_{2}\text{Cr}_{2}\text{O}_{7}$$


**Paso 2 · Dicromato en los 25,00 mL valorados.**

$$\text{n} = 5{,}752\cdot10^{-3}\ \text{mol} \cdot \dfrac{25{,}00\ \text{mL}}{500{,}0\ \text{mL}} = 2{,}876\cdot10^{-4}\ \text{mol de Cr}_{2}\text{O}_{7}^{2-}$$


**Paso 3 · Fe²⁺ que reaccionó.**

$$\text{n} = 2{,}876\cdot10^{-4}\ \text{mol Cr}_{2}\text{O}_{7}^{2-} \cdot \dfrac{6\ \text{mol Fe}^{2+}}{1\ \text{mol Cr}_{2}\text{O}_{7}^{2-}} = 1{,}725\cdot10^{-3}\ \text{mol de Fe}^{2+}$$


**Paso 4 · Concentración de FeSO₄.**

$$\text{M} = \dfrac{1{,}725\cdot10^{-3}\ \text{mol}}{0{,}01376\ \text{L}} = 0{,}1254\ \text{M}$$


**Neutra** (Ajuste 2 + contraiones K⁺ y SO₄²⁻): **K₂Cr₂O₇ + 6 FeSO₄ + 7 H₂SO₄ → Cr₂(SO₄)₃ + 3 Fe₂(SO₄)₃ + K₂SO₄ + 7 H₂O**

##### P7-6.13 · Primera convocatoria, 5 de febrero de 2019 (ej. 5) · H₂O₂ que oxida Fe²⁺

[[SOL 105:218-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_13.svg 100%]]


**Datos:** 50,0 mL de H₂O₂ gastan 32,10 mL de KMnO₄ 0,5000 M · quiero oxidar 50,00 g de FeSO₄. **Me piden:** volumen de H₂O₂.

**¿Qué pasa?** Dos partes: primero saco la [H₂O₂] con el permanganato (el H₂O₂ es **reductor**). Luego el H₂O₂ oxida al Fe²⁺ (ahora es **oxidante**).

**Paso 1 · [H₂O₂].**

$$\text{n(MnO}_{4}^{-}\text{)} = 0{,}5000\ \text{mol/L} \cdot 0{,}03210\ \text{L} = 0{,}01605\ \text{mol}$$

$$\text{n(H}_{2}\text{O}_{2}\text{)} = 0{,}01605 \cdot 5\text{/}\ 2 = 0{,}04013\ \text{mol en}\ 50{,}0\ \text{mL}$$

→ **0,803 M**


**Paso 2 · Reacción con el Fe²⁺** (H₂O₂ + 2 H⁺ + 2 e⁻ → 2 H₂O; Fe²⁺ → Fe³⁺ + e⁻ × 2):

**H₂O₂ + 2 Fe²⁺ + 2 H⁺ → 2 Fe³⁺ + 2 H₂O** → 1 H₂O₂ por cada 2 Fe²⁺

**Paso 3 · Moles de Fe²⁺:**

$$\text{n} = \dfrac{50{,}00\ \text{g}}{151{,}91\ \text{g/mol}} = 0{,}3291\ \text{mol}$$

$$\text{n(H}_{2}\text{O}_{2}\text{)} = \dfrac{0{,}3291}{2} = 0{,}1646\ \text{mol}$$


**Paso 4 · Volumen:**

$$\text{V} = \dfrac{0{,}1646\ \text{mol}}{0{,}803\ \text{mol/L}} = 0{,}205\ \text{L} = 205\ \text{mL}$$


##### P7-6.14 · Segunda convocatoria, 4 de septiembre de 2018 (ej. 4) · Molaridad de H₂O₂

[[SOL 93:724-842 94:40-156]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_14.svg 100%]]


**Datos:** 25,00 mL de H₂O₂ gastan 36,44 mL de KMnO₄ 0,01652 M. **Me piden:** [H₂O₂].

**Paso 1 · Moles de MnO₄⁻.**

$$\text{n} = 0{,}01652\ \text{mol/L} \cdot 0{,}03644\ \text{L} = 6{,}020\cdot10^{-4}\ \text{mol de MnO}_{4}^{-}$$


**Paso 2 · Moles de H₂O₂**

(5 por cada 2 MnO₄⁻):

$$\text{n} = 6{,}020\cdot10^{-4}\ \text{mol MnO}_{4}^{-} \cdot \dfrac{5\ \text{mol H}_{2}\text{O}_{2}}{2\ \text{mol MnO}_{4}^{-}} = 1{,}505\cdot10^{-3}\ \text{mol de H}_{2}\text{O}_{2}$$


**Paso 3 · Concentración.**

$$\text{M} = \dfrac{1{,}505\cdot10^{-3}\ \text{mol}}{0{,}02500\ \text{L}} = 0{,}06020\ \text{M}$$


##### P7-6.15 · Primera convocatoria, 5 de febrero de 2018 (ej. 4) · Estado de oxidación final del yodo

[[SOL 91:296-396]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_15.svg 100%]]


**¿Qué pasa?** No dicen en qué se convierte el IO₃⁻: lo saco **contando electrones**.

**Paso 1 · Moles de IO₃⁻.**

$$\text{n} = \dfrac{1{,}390\ \text{g KIO}_{3}}{214{,}00\ \text{g/mol}} = 6{,}495\cdot10^{-3}\ \text{mol}$$


**Paso 2 · Electrones que dan los sulfitos.**

$$\text{n(SO}_{3}^{2-}\text{)} = 0{,}500\ \text{mol/L} \cdot 0{,}0325\ \text{L} = 0{,}01625\ \text{mol; cada SO}_{3}^{2-}$$

→ SO₄²⁻ (S +4

→ +6) cede **2 e⁻**

$$0{,}01625 \cdot 2 = 0{,}0325\ \text{mol de e}^{-}$$


**Paso 3 · Electrones que coge cada I:**

$$\dfrac{0{,}0325\ \text{mol e}^{-}}{6{,}495\cdot10^{-3}\ \text{mol I}} = 5\ \text{e}^{-}\text{ por átomo de I}$$


**Paso 4 ·** El I estaba en **+5** (IO₃⁻) y coge 5 e⁻ → queda en **0** → **I₂**

##### P7-6.16 · Tercera convocatoria, 4 de diciembre de 2017 (ej. 4) · Fórmula empírica de un óxido de hierro

[[SOL 84:453-569]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_16.svg 100%]]


**Datos:** 0,2729 g de óxido de Fe → Fe²⁺ · gasta 42,17 mL de KMnO₄ 0,01621 M. **Me piden:** fórmula empírica.

**Paso 1 · Moles de MnO₄⁻.**

$$\text{n} = 0{,}01621\ \text{mol/L} \cdot 0{,}04217\ \text{L} = 6{,}836\cdot10^{-4}\ \text{mol de MnO}_{4}^{-}$$


**Paso 2 · Moles de Fe**

(5 Fe²⁺ por cada MnO₄⁻):

$$\text{n} = 6{,}836\cdot10^{-4}\ \text{mol MnO}_{4}^{-} \cdot \dfrac{5\ \text{mol Fe}}{1\ \text{mol MnO}_{4}^{-}} = 3{,}418\cdot10^{-3}\ \text{mol de Fe}$$


**Paso 3 · Masa de Fe.**

$$\text{m} = 3{,}418\cdot10^{-3}\ \text{mol} \cdot 55{,}845\ \text{g/mol} = 0{,}1909\ \text{g de Fe}$$


**Paso 4 · Masa de O**

$$\left(\text{el resto del óxido}\right)\text{. m(O)} = 0{,}2729\ \text{g} - 0{,}1909\ \text{g} = 0{,}0820\ \text{g de O}$$


**Paso 5 · Moles de O.**

$$\text{n(O)} = \dfrac{0{,}0820\ \text{g}}{16{,}00\ \text{g/mol}} = 5{,}127\cdot10^{-3}\ \text{mol de O}$$


**Paso 6 · Proporción.**

$$\text{O/Fe} = \dfrac{5{,}127\cdot10^{-3}\ \text{mol}}{3{,}418\cdot10^{-3}\ \text{mol}} = 1{,}50$$

→ 3 O por cada 2 Fe

→ **Fe₂O₃**


##### P7-6.17 · Contenido en As (AsH₃ con dicromato): 1ª conv. 2013 (el PDF pone "4 de febrero de 2012") (ej. 4) = Tercera convocatoria, 11-dic-2013 (ej. 4)

[[SOL 35:290-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_17.svg 100%]]


**Datos:** 6,20 g de compuesto → todo el As como AsH₃ en 100 mL · 10 mL gastan 36,7 mL de K₂Cr₂O₇ 0,0125 M · AsH₃ → AsO₄³⁻. **Me piden:** % de As.

**Electrones:** As de −3 (AsH₃) a +5 (AsO₄³⁻) → cede **8 e⁻** por As · Cr₂O₇²⁻ → 2 Cr³⁺ → capta **6 e⁻** por dicromato.

**Paso 1 · Moles de dicromato.**

$$\text{n} = 0{,}0125\ \text{mol/L} \cdot 0{,}0367\ \text{L} = 4{,}588\cdot10^{-4}\ \text{mol de Cr}_{2}\text{O}_{7}^{2-}$$


**Paso 2 · Electrones que captan.**

$$\text{n(e}^{-}\text{)} = 4{,}588\cdot10^{-4}\ \text{mol Cr}_{2}\text{O}_{7}^{2-} \cdot \dfrac{6\ \text{mol e}^{-}}{1\ \text{mol Cr}_{2}\text{O}_{7}^{2-}} = 2{,}753\cdot10^{-3}\ \text{mol de e}^{-}$$


**Paso 3 · As en los 10 mL**

(cada As da 8 e⁻):

$$\text{n} = 2{,}753\cdot10^{-3}\ \text{mol e}^{-} \cdot \dfrac{1\ \text{mol As}}{8\ \text{mol e}^{-}} = 3{,}441\cdot10^{-4}\ \text{mol de As}$$


**Paso 4 · As en toda la muestra**

(alícuota 10 mL de 100 mL):

$$\text{n} = 3{,}441\cdot10^{-4}\ \text{mol} \cdot \dfrac{100\ \text{mL}}{10\ \text{mL}} = 3{,}441\cdot10^{-3}\ \text{mol de As}$$


**Paso 5 · Masa de As.**

$$\text{m} = 3{,}441\cdot10^{-3}\ \text{mol} \cdot 74{,}92\ \text{g/mol} = 0{,}2578\ \text{g de As}$$


**Paso 6 · %As.**

$$\text{\%} = \dfrac{0{,}2578\ \text{g}}{6{,}20\ \text{g}} \cdot 100 = 4{,}16\ \text{\%}$$


##### P7-6.18 · Fe y Ba en un mineral (dicromato + gravimetría de BaSO₄): Convocatoria de Junio, 10-jun-2013 (ej. 3) = 3ª convocatoria, 2-dic-2019 (ej. 4)

[[SOL 111:72-251]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_18.svg 100%]]


**Datos:** 4,000 g de mineral en 100,0 mL (disolución A) · 50,0 mL de A gastan 15,04 mL de K₂Cr₂O₇ 0,0250 M · 5,00 mL de A dan 0,1366 g de BaSO₄. **Me piden:** % de Fe y % de Ba.

**Fe (volumetría)**

**Paso 1 · Moles de dicromato.**

$$\text{n} = 0{,}0250\ \text{mol/L} \cdot 0{,}01504\ \text{L} = 3{,}760\cdot10^{-4}\ \text{mol de Cr}_{2}\text{O}_{7}^{2-}$$


**Paso 2 · Fe en los 50,0 mL.**

$$\text{n} = 3{,}760\cdot10^{-4}\ \text{mol Cr}_{2}\text{O}_{7}^{2-} \cdot \dfrac{6\ \text{mol Fe}}{1\ \text{mol Cr}_{2}\text{O}_{7}^{2-}} = 2{,}256\cdot10^{-3}\ \text{mol de Fe}$$


**Paso 3 · Fe en toda la muestra**

$$\left(50{,}0\ \text{de}\ 100{,}0\ \text{mL}\right)\text{. n} = 2{,}256\cdot10^{-3}\ \text{mol} \cdot \dfrac{100{,}0\ \text{mL}}{50{,}0\ \text{mL}} = 4{,}512\cdot10^{-3}\ \text{mol de Fe}$$


**Paso 4 · Masa de Fe.**

$$\text{m} = 4{,}512\cdot10^{-3}\ \text{mol} \cdot 55{,}85\ \text{g/mol} = 0{,}2520\ \text{g de Fe}$$


**Paso 5 · %Fe.**

$$\text{\%} = \dfrac{0{,}2520\ \text{g}}{4{,}000\ \text{g}} \cdot 100 = 6{,}30\ \text{\%}$$


**Ba (gravimetría)**

**Paso 6 · Ba en los 5,00 mL**

$$\left(1\ \text{Ba por BaSO}_{4}\right)\text{. n} = \dfrac{0{,}1366\ \text{g}}{233{,}39\ \text{g/mol}} = 5{,}853\cdot10^{-4}\ \text{mol de Ba}$$


**Paso 7 · Ba en toda la muestra**

$$\left(5{,}00\ \text{de}\ 100{,}0\ \text{mL}\right)\text{. n} = 5{,}853\cdot10^{-4}\ \text{mol} \cdot \dfrac{100{,}0\ \text{mL}}{5{,}00\ \text{mL}} = 0{,}01171\ \text{mol de Ba}$$


**Paso 8 · Masa de Ba.**

$$\text{m} = 0{,}01171\ \text{mol} \cdot 137{,}33\ \text{g/mol} = 1{,}608\ \text{g de Ba}$$


**Paso 9 · %Ba.**

$$\text{\%} = \dfrac{1{,}608\ \text{g}}{4{,}000\ \text{g}} \cdot 100 = 40{,}2\ \text{\%}$$


**Trampa:** las alícuotas son distintas (50 mL y 5 mL).

##### P7-6.19 · SO₂ en aire con permanganato: Convocatoria de Junio, 17-jun-2011 (ej. 4) y Convocatoria de Diciembre, 10-dic-2012 (ej. 4)

[[SOL 13:99-249]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_19.svg 100%]]


**Datos:** el SO₂ del aire se disuelve en 250 mL de agua · 10,0 mL gastan 7,35 mL de KMnO₄ 8,00·10⁻³ M · SO₂ → SO₄²⁻. En 2011 son 10 L de aire; en 2012, 100 L. **Me piden:** masa de SO₂ y su % en volumen (2011) o mg/L (2012).

**Ajuste:** SO₂ + 2 H₂O → SO₄²⁻ + 4 H⁺ + 2 e⁻ (S +4 → +6) · MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O. Igualo a 10 e⁻ (× 5 y × 2): **2 MnO₄⁻ + 5 SO₂ + 2 H₂O → 2 Mn²⁺ + 5 SO₄²⁻ + 4 H⁺** (5 SO₂ por cada 2 MnO₄⁻)

**Paso 1 · Moles de MnO₄⁻.**

$$\text{n} = 8{,}00\cdot10^{-3}\ \text{mol/L} \cdot 0{,}00735\ \text{L} = 5{,}88\cdot10^{-5}\ \text{mol de MnO}_{4}^{-}$$


**Paso 2 · SO₂ en los 10,0 mL.**

$$\text{n} = 5{,}88\cdot10^{-5}\ \text{mol MnO}_{4}^{-} \cdot \dfrac{5\ \text{mol SO}_{2}}{2\ \text{mol MnO}_{4}^{-}} = 1{,}470\cdot10^{-4}\ \text{mol de SO}_{2}$$


**Paso 3 · SO₂ en los 250 mL**

$$\left(\text{alícuota}\ 10\ \text{de}\ 250\ \text{mL}\right)\text{. n} = 1{,}470\cdot10^{-4}\ \text{mol} \cdot \dfrac{250\ \text{mL}}{10{,}0\ \text{mL}} = 3{,}675\cdot10^{-3}\ \text{mol de SO}_{2}$$


**Paso 4 · Masa de SO₂.**

$$\text{m} = 3{,}675\cdot10^{-3}\ \text{mol} \cdot 64{,}06\ \text{g/mol} = 0{,}236\ \text{g de SO}_{2}$$


**Paso 5 (2011) · Volumen de SO₂ como gas a 1 atm y 25 °C.**

$$\text{V} = \dfrac{3{,}675\cdot10^{-3}\ \text{mol} \cdot 0{,}08206\ \text{atm} \cdot \text{L/(mol} \cdot \text{K)} \cdot 298\ \text{K}}{1\ \text{atm}} = 0{,}0899\ \text{L de SO}_{2}$$


**Paso 6 (2011) · % en volumen.**

$$\text{\%} = \dfrac{0{,}0899\ \text{L}}{10\ \text{L}} \cdot 100 = 0{,}90\ \text{\%}$$


**Paso 5 (2012) · mg por litro de aire.**

$$\text{c} = \dfrac{236\ \text{mg}}{100\ \text{L}} = 2{,}36\ \text{mg/L}$$


#### Problemas · Tipo B · Valoraciones redox en dos pasos (yodometrías, retrovaloraciones, estandarizaciones)

**Cómo se hace:** escribe **las dos reacciones** y sigue **el camino de los moles** de principio a fin (como el Mg en la gravimetría): analito → intermedio (I₂, oxalato, Fe²⁺) → valorante. Si es **retrovaloración redox**, reaccionados = añadidos − sobrantes.

**Atajos que se repiten:** **2 Cu²⁺ → 1 I₂ → 2 S₂O₃²⁻ ⇒ Cu : S₂O₃²⁻ = 1 : 1**; **2 I⁻ → I₂ → 2 S₂O₃²⁻ ⇒ I⁻ : S₂O₃²⁻ = 1 : 1**; **IO₃⁻ → 3 I₂ → 6 S₂O₃²⁻**.

**Trampas:** comprobar el limitante en el primer paso; un paso ácido-base y otro redox en el mismo problema.

##### P7-6.20 · SEGUNDO PARCIAL, 21 de diciembre de 2023 (ej. 2) · Cu por yodometría

[[SOL 168:281-399]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_20.svg 100%]]


**Datos:** 2,00 g de mineral → Cu²⁺ · + KI → I₂ · el I₂ gasta 76,5 mL de Na₂S₂O₃ 0,200 M. **Me piden:** % de Cu.

**¿Qué pasa?** El Cu²⁺ oxida al I⁻ y se forma I₂ (el Cu²⁺ pasa a CuI). Ese I₂ se valora con tiosulfato. El I₂ es solo un **intermediario**.

**Reacciones:**
- **2 Cu²⁺ + 4 I⁻ → 2 CuI + I₂** (2 Cu²⁺ dan 1 I₂)
- **I₂ + 2 S₂O₃²⁻ → 2 I⁻ + S₄O₆²⁻** (1 I₂ gasta 2 S₂O₃²⁻)
- Juntando: 2 Cu²⁺ → 1 I₂ → 2 S₂O₃²⁻ ⇒ **1 Cu por cada S₂O₃²⁻**

**Paso 1 · Tiosulfato.**

$$\text{n} = 0{,}200\ \text{mol/L} \cdot 0{,}0765\ \text{L} = 0{,}0153\ \text{mol de S}_{2}\text{O}_{3}^{2-}$$


**Paso 2 · Cu:**

→ n = 0,0153 mol (1 : 1)

$$\text{m} = 0{,}0153\ \text{mol} \cdot 63{,}546\ \text{g/mol} = 0{,}972\ \text{g}$$


**Paso 3 · %:**

$$\dfrac{0{,}972\ \text{g}}{2{,}00\ \text{g}} \cdot 100 = 48{,}6\ \text{\%}$$


##### P7-6.21 · SEGUNDO PARCIAL, 27 de enero de 2021 (ej. 1) · Estandarización de tiosulfato con NaI → I₂

[[SOL 129:203-334]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_21.svg 100%]]


**Datos:** 2,0031 g de NaI → todo pasa a I₂ · el I₂ gasta 20,4 mL de tiosulfato. **Me piden:** [Na₂S₂O₃].

**Camino:** 2 I⁻ → 1 I₂ → 2 S₂O₃²⁻, así que **1 I⁻ por cada S₂O₃²⁻**

**Paso 1 · Moles de I⁻.**

$$\text{n} = \dfrac{2{,}0031\ \text{g}}{149{,}89\ \text{g/mol}} = 0{,}01336\ \text{mol de I}^{-}$$


**Paso 2 · Moles de I₂.**

$$\text{n} = 0{,}01336\ \text{mol I}^{-} \cdot \dfrac{1\ \text{mol I}_{2}}{2\ \text{mol I}^{-}} = 6{,}682\cdot10^{-3}\ \text{mol de I}_{2}$$


**Paso 3 · Moles de tiosulfato.**

$$\text{n} = 6{,}682\cdot10^{-3}\ \text{mol I}_{2} \cdot \dfrac{2\ \text{mol S}_{2}\text{O}_{3}^{2-}}{1\ \text{mol I}_{2}} = 0{,}01336\ \text{mol de S}_{2}\text{O}_{3}^{2-}$$


**Paso 4 · Concentración.**

$$\text{M} = \dfrac{0{,}01336\ \text{mol}}{0{,}0204\ \text{L}} = 0{,}655\ \text{M}$$


##### P7-6.22 · SEGUNDO PARCIAL, 22 de diciembre de 2022 (ej. 3) · Sn con HNO₃ en exceso (retrovaloración ácido-base)

[[SOL 158:367-468]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_22.svg 100%]]


**Datos:** 9,00 g de muestra con Sn · 1,00 L de HNO₃ 1,000 M (exceso) · 10,0 mL del resultado gastan 28,3 mL de NaOH 0,1250 M. **Me piden:** % de Sn.

**¿Qué pasa?** El HNO₃ oxida el Sn a SnO₂ (redox) y sobra HNO₃; ese sobrante lo valoro con NaOH (ácido-base): **retrovaloración**.

**Reacción redox** (Sn 0 → +4 da 4 e⁻; cada N +5 → +4 coge 1 e⁻, así que 4 HNO₃ por Sn): **Sn + 4 HNO₃ → SnO₂ + 4 NO₂ + 2 H₂O**

**Paso 1 · HNO₃ añadido.**

$$\text{n} = 1{,}000\ \text{mol/L} \cdot 1{,}00\ \text{L} = 1{,}000\ \text{mol de HNO}_{3}$$


**Paso 2 · HNO₃ sobrante en los 10,0 mL**

(NaOH 1 :

$$1\right)\text{. n =}\ 0{,}1250\ \text{mol/L} \cdot 0{,}0283\ \text{L =}\ 3{,}538\cdot10^{-3}\ \text{mol de HNO}_{3}$$


**Paso 3 · HNO₃ sobrante en el litro**

$$\left(\text{alícuota}\ 10{,}0\ \text{de}\ 1000\ \text{mL}\right)\text{. n} = 3{,}538\cdot10^{-3}\ \text{mol} \cdot \dfrac{1000\ \text{mL}}{10{,}0\ \text{mL}} = 0{,}3538\ \text{mol de HNO}_{3}$$


**Paso 4 · HNO₃ que reaccionó con el Sn.**

$$\text{n} = 1{,}000\ \text{mol} - 0{,}3538\ \text{mol} = 0{,}6463\ \text{mol de HNO}_{3}$$


**Paso 5 · Moles de Sn.**

$$\text{n} = 0{,}6463\ \text{mol HNO}_{3} \cdot \dfrac{1\ \text{mol Sn}}{4\ \text{mol HNO}_{3}} = 0{,}1616\ \text{mol de Sn}$$


**Paso 6 · Masa de Sn.**

$$\text{m} = 0{,}1616\ \text{mol} \cdot 118{,}71\ \text{g/mol} = 19{,}2\ \text{g de Sn}$$


**Ojo:** sale **más Sn (19,2 g) que muestra (9,00 g)**. El profesor reconoce en la solución que el dato debía ser 20,00 g (→ 95,9 %).

##### P7-6.23 · Primera convocatoria, 1 de febrero de 2017 (ej. 4) · MnO₂ con oxálico en exceso (retrovaloración redox)

[[SOL 80:553-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_23.svg 100%]]


**Datos:** 0,533 g de mineral con MnO₂ · 100 mL con 1,179 g de H₂C₂O₄ (exceso) · el oxálico sobrante gasta 30,06 mL de KMnO₄ 0,1000 M. **Me piden:** % de MnO₂.

**Reacciones:**
- **MnO₂ + H₂C₂O₄ + 2 H⁺ → Mn²⁺ + 2 CO₂ + 2 H₂O** (Mn +4 → +2 coge 2 e⁻; el oxálico cede 2 e⁻: **1 : 1**)
- Oxálico sobrante con permanganato: Ajuste 3 (2 MnO₄⁻ por 5 oxálico)

**Paso 1 · Oxálico añadido.**

$$\text{n} = \dfrac{1{,}179\ \text{g}}{90{,}034\ \text{g/mol}} = 0{,}01310\ \text{mol de oxálico}$$


**Paso 2 · Moles de MnO₄⁻ gastados.**

$$\text{n} = 0{,}1000\ \text{mol/L} \cdot 0{,}03006\ \text{L} = 3{,}006\cdot10^{-3}\ \text{mol de MnO}_{4}^{-}$$


**Paso 3 · Oxálico sobrante.**

$$\text{n} = 3{,}006\cdot10^{-3}\ \text{mol MnO}_{4}^{-} \cdot \dfrac{5\ \text{mol ox}}{2\ \text{mol MnO}_{4}^{-}} = 7{,}515\cdot10^{-3}\ \text{mol de oxálico}$$


**Paso 4 · Oxálico que reaccionó con el MnO₂ (= moles de MnO₂).**

$$\text{n} = 0{,}01310\ \text{mol} - 0{,}007515\ \text{mol} = 5{,}58\cdot10^{-3}\ \text{mol de MnO}_{2}$$


**Paso 5 · Masa de MnO₂.**

$$\text{m} = 5{,}58\cdot10^{-3}\ \text{mol} \cdot 86{,}937\ \text{g/mol} = 0{,}485\ \text{g de MnO}_{2}$$


**Paso 6 · %MnO₂.**

$$\text{\%} = \dfrac{0{,}485\ \text{g}}{0{,}533\ \text{g}} \cdot 100 = 91\ \text{\%}\left(\text{el profesor da}\ 91{,}2\ \text{\%}\right)$$


##### P7-6.24 · Tercera convocatoria, 16 de diciembre de 2016 (ej. 4) · CaO en una caliza (oxalato + permanganato)

[[SOL 71:558-690]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_24.svg 100%]]


**Datos:** 5,18 g de caliza · el Ca precipita como CaC₂O₄, que se disuelve en 100,0 mL · 10,0 mL gastan 40,0 mL de KMnO₄ 0,0500 M. **Me piden:** % de CaO.

**Paso 1 · Moles de MnO₄⁻.**

$$\text{n} = 0{,}0500\ \text{mol/L} \cdot 0{,}0400\ \text{L} = 2{,}00\cdot10^{-3}\ \text{mol de MnO}_{4}^{-}$$


**Paso 2 · Oxalato en los 10,0 mL.**

$$\text{n} = 2{,}00\cdot10^{-3}\ \text{mol MnO}_{4}^{-} \cdot \dfrac{5\ \text{mol ox}}{2\ \text{mol MnO}_{4}^{-}} = 5{,}00\cdot10^{-3}\ \text{mol de oxalato}$$


**Paso 3 · Oxalato en los 100,0 mL**

$$\left(\text{alícuota}\ 10\ \text{de}\ 100\ \text{mL;}\ 1\ \text{Ca por oxalato y}\ 1\ \text{Ca por CaO}\right)\text{. n} = 5{,}00\cdot10^{-3}\ \text{mol} \cdot \dfrac{100{,}0\ \text{mL}}{10{,}0\ \text{mL}} = 0{,}0500\ \text{mol de CaO}$$


**Paso 4 · Masa de CaO.**

$$\text{m} = 0{,}0500\ \text{mol} \cdot 56{,}0774\ \text{g/mol} = 2{,}804\ \text{g de CaO}$$


**Paso 5 · %CaO.**

$$\text{\%} = \dfrac{2{,}804\ \text{g}}{5{,}18\ \text{g}} \cdot 100 = 54{,}1\ \text{\%}$$


##### P7-6.25 · Primera convocatoria, 3 de febrero de 2016 (ej. 3) · KIO₃ + KI → I₂ → tiosulfato

[[SOL 67:197-364]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_25.svg 100%]]


**Datos:** 0,2678 g de KIO₃ + 20,0 mL de KI 2,0 M + 5,0 mL de H₂SO₄ 1,0 M · el I₂ se valora con Na₂S₂O₃ 0,24 M. **Me piden:** volumen de tiosulfato.

**Ajuste** (comproporción: IO₃⁻ +5 → 0 y I⁻ −1 → 0):
- IO₃⁻ + 6 H⁺ + 5 e⁻ → ½ I₂ + 3 H₂O · I⁻ → ½ I₂ + e⁻ (× 5)
- **IO₃⁻ + 5 I⁻ + 6 H⁺ → 3 I₂ + 3 H₂O** → neutra: **KIO₃ + 5 KI + 3 H₂SO₄ → 3 I₂ + 3 K₂SO₄ + 3 H₂O**

**Paso 1 · ¿Quién limita?**

$$\text{n(KIO}_{3}\text{)} = \dfrac{0{,}2678}{214{,}00} = 1{,}251\cdot10^{-3}\ \text{mol. Necesitaría}\ 5 \cdot 1{,}251\cdot10^{-3} = 6{,}26\cdot10^{-3}\ \text{mol de KI}\left(\text{hay}\ 0{,}040\right)\ \text{y}\ 3 \cdot 1{,}251\cdot10^{-3} = 3{,}75\cdot10^{-3}\ \text{mol de H}_{2}\text{SO}_{4}$$

(hay 5,0·10⁻³)

→ **limita el KIO₃**


**Paso 2 · I₂ formado:**

$$\text{n} = 1{,}251\cdot10^{-3}\ \text{mol KIO}_{3} \cdot 3 = 3{,}754\cdot10^{-3}\ \text{mol de I}_{2}$$


**Paso 3 · Tiosulfato**

(2 por I₂):

$$\text{n} = 7{,}51\cdot10^{-3}\ \text{mol}$$

$$\text{V} = \dfrac{7{,}51\cdot10^{-3}\ \text{mol}}{0{,}24\ \text{mol/L}} = 0{,}031\ \text{L} = 31\ \text{mL}$$


##### P7-6.26 · Segundo parcial, 13 de enero de 2015 (ej. 3) · Oxálico: ácido-base + redox

[[SOL 52:584-672]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_26.svg 100%]]


**Datos:** 15,0 mL de oxálico gastan 25,2 mL de NaOH 0,149 M. **Me piden:** volumen de KMnO₄ 0,122 M para oxidar ese oxálico.

**Paso 1 · Moles de NaOH.**

$$\text{n} = 0{,}149\ \text{mol/L} \cdot 0{,}0252\ \text{L} = 3{,}755\cdot10^{-3}\ \text{mol de NaOH}$$


**Paso 2 · Oxálico (ácido-base, diprótico).**

$$\text{n} = 3{,}755\cdot10^{-3}\ \text{mol NaOH} \cdot \dfrac{1\ \text{mol ox}}{2\ \text{mol NaOH}} = 1{,}877\cdot10^{-3}\ \text{mol de oxálico}$$


**Paso 3 · MnO₄⁻ necesario (redox, Ajuste 3).**

$$\text{n} = 1{,}877\cdot10^{-3}\ \text{mol ox} \cdot \dfrac{2\ \text{mol MnO}_{4}^{-}}{5\ \text{mol ox}} = 7{,}51\cdot10^{-4}\ \text{mol de MnO}_{4}^{-}$$


**Paso 4 · Volumen de KMnO₄.**

$$\text{V} = \dfrac{7{,}51\cdot10^{-4}\ \text{mol}}{0{,}122\ \text{mol/L}} = 6{,}15\cdot10^{-3}\ \text{L}\left(6{,}15\ \text{mL}\right)$$


**Por qué es buen problema:** la misma sustancia se valora con dos reacciones de estequiometría distinta.

##### P7-6.27 · Segunda convocatoria, 16 de junio de 2014 (ej. 4) · Fe²⁺ y Fe³⁺ en la misma disolución

[[SOL 49:327-842]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_27.svg 100%]]


**Datos:** 25,0 mL con Fe²⁺ y Fe³⁺ · gastan 23,0 mL de KMnO₄ 0,0200 M · después de reducir todo con Zn, gastan 40,0 mL de K₂Cr₂O₇ 0,0150 M. **Me piden:** [Fe²⁺] y [Fe³⁺].

**¿Qué pasa?** El permanganato **solo ve el Fe²⁺** (el Fe³⁺ ya está oxidado). Luego el Zn pasa **todo** el hierro a Fe²⁺ y el dicromato mide **el Fe total**.

**Paso 1 · Moles de MnO₄⁻.**

$$\text{n} = 0{,}0200\ \text{mol/L} \cdot 0{,}0230\ \text{L} = 4{,}60\cdot10^{-4}\ \text{mol de MnO}_{4}^{-}$$


**Paso 2 · Fe²⁺ original.**

$$\text{n} = 4{,}60\cdot10^{-4}\ \text{mol MnO}_{4}^{-} \cdot \dfrac{5\ \text{mol Fe}^{2+}}{1\ \text{mol MnO}_{4}^{-}} = 2{,}30\cdot10^{-3}\ \text{mol de Fe}^{2+}$$


**Paso 3 · [Fe²⁺].**

$$\text{M} = \dfrac{2{,}30\cdot10^{-3}\ \text{mol}}{0{,}0250\ \text{L}} = 0{,}0920\ \text{M}$$


**Paso 4 · Moles de dicromato.**

$$\text{n} = 0{,}0150\ \text{mol/L} \cdot 0{,}0400\ \text{L} = 6{,}00\cdot10^{-4}\ \text{mol de Cr}_{2}\text{O}_{7}^{2-}$$


**Paso 5 · Fe total.**

$$\text{n} = 6{,}00\cdot10^{-4}\ \text{mol Cr}_{2}\text{O}_{7}^{2-} \cdot \dfrac{6\ \text{mol Fe}}{1\ \text{mol Cr}_{2}\text{O}_{7}^{2-}} = 3{,}60\cdot10^{-3}\ \text{mol de Fe}$$


**Paso 6 · Fe³⁺ original.**

$$\text{n} = 3{,}60\cdot10^{-3}\ \text{mol} - 2{,}30\cdot10^{-3}\ \text{mol} = 1{,}30\cdot10^{-3}\ \text{mol de Fe}^{3+}$$


**Paso 7 · [Fe³⁺].**

$$\text{M} = \dfrac{1{,}30\cdot10^{-3}\ \text{mol}}{0{,}0250\ \text{L}} = 0{,}0520\ \text{M}$$


##### P7-6.28 · Primera convocatoria, 7 de febrero de 2014 (ej. 3) · Riqueza del KMnO₄ (FeSO₄ estandarizado con dicromato)

[[SOL 46:718-842 47:40-128]]

**Lo que pasa en el laboratorio:**

[[IMG img/lab7_P7-6_28.svg 100%]]


**Datos:** 20,32 mL de FeSO₄ valoran 1,0346 g de K₂Cr₂O₇ · 25,64 mL de ese FeSO₄ valoran 0,9560 g de KMnO₄ comercial. **Me piden:** riqueza del KMnO₄.

**Paso 1 · Moles de dicromato.**

$$\text{n} = \dfrac{1{,}0346\ \text{g}}{294{,}18\ \text{g/mol}} = 3{,}517\cdot10^{-3}\ \text{mol de K}_{2}\text{Cr}_{2}\text{O}_{7}$$


**Paso 2 · Fe²⁺ en los 20,32 mL.**

$$\text{n} = 3{,}517\cdot10^{-3}\ \text{mol Cr}_{2}\text{O}_{7}^{2-} \cdot \dfrac{6\ \text{mol Fe}^{2+}}{1\ \text{mol Cr}_{2}\text{O}_{7}^{2-}} = 0{,}02110\ \text{mol de Fe}^{2+}$$


**Paso 3 · [FeSO₄].**

$$\text{M} = \dfrac{0{,}02110\ \text{mol}}{0{,}02032\ \text{L}} = 1{,}0385\ \text{M}$$


**Paso 4 · Fe²⁺ gastado con el KMnO₄.**

$$\text{n} = 1{,}0385\ \text{mol/L} \cdot 0{,}02564\ \text{L} = 0{,}02663\ \text{mol de Fe}^{2+}$$


**Paso 5 · KMnO₄ puro.**

$$\text{n} = 0{,}02663\ \text{mol Fe}^{2+} \cdot \dfrac{1\ \text{mol MnO}_{4}^{-}}{5\ \text{mol Fe}^{2+}} = 5{,}325\cdot10^{-3}\ \text{mol de KMnO}_{4}$$


**Paso 6 · Masa de KMnO₄ puro.**

$$\text{m} = 5{,}325\cdot10^{-3}\ \text{mol} \cdot 158{,}03\ \text{g/mol} = 0{,}8415\ \text{g de KMnO}_{4}$$


**Paso 7 · Riqueza.**

$$\text{\%} = \dfrac{0{,}8415\ \text{g}}{0{,}9560\ \text{g}} \cdot 100 = 88{,}0\ \text{\%}$$


### Avisos de este apartado (se resuelven en otro tema)

- **Segundo parcial, 18 de diciembre de 2025 (ej. 5):** dicromato + KI con **rendimiento del 95 %** y después **extracción con K_D** → **tema 9** (equilibrio de reparto). La parte redox es como el Tipo A.


<div class="newpage"></div>

## 7. Reacciones esenciales en química molecular

### Teoría necesaria (en clase)

Todo lo de orgánica se resume, salvo las radicalarias, en cuatro tipos:
- **Sustitución:** un átomo o grupo sale y lo reemplaza otro (Cl por –OH; S_N1, S_N2).
- **Condensación:** se unen dos moléculas y se **desprende una pequeña**, normalmente **agua** (aldehído + amina/hidroxilamina).
- **Eliminación:** sale una molécula pequeña neutra (H₂O, HX) y se forma un **doble o triple enlace**.
- **Adición:** la inversa: una molécula pequeña se incorpora a un doble o triple enlace, usando los electrones del π para formar enlaces σ.

> No ha caído nunca en el examen.

## Recuento final del tema 7

| | Teoría | Problemas de examen | De ellos repetidos | Ejercicios de clase |
|---|---|---|---|---|
| Apartado 1 | 1 | 5 | — | 3 |
| Apartado 3 | 0 | 8 | — | 1 |
| Apartado 4 | 1 | 7 | — | 1 |
| Apartado 6 | 0 | 33 (28 fichas; los iguales van juntos) | Fe/dicromato ×3, As ×2, Fe/Ba ×2, SO₂ ×2 | 1 (= P7-6.8) |
| **Total** | **2** | **53** | | **6** |

**Avisos (se resuelven en otros temas):** fórmula molecular + Π (tema 8); Ca + H₂SO₄ + Kps (tema 11); mezcla K₂CrO₄/AgNO₃ ×3 (tema 11); vinagre con indicador (tema 10); dicromato + KI + K_D (tema 9).
