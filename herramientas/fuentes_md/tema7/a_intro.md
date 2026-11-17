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
