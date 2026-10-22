# Biofísica – Grado en Bioquímica (Universidad de Sevilla)

Profesor: Rafael J. Montoro. Dpto. de Fisiología Médica y Biofísica.

## Material

| Archivo | Contenido |
|---|---|
| `temas/Tema_10_propiedades_pasivas_membrana.pdf` | Tema 10: modelo eléctrico de la membrana, propiedades pasivas (circuito RC, τ, λ, sumación) |
| `temas/Tema_11_potencial_de_accion.pdf` | Tema 11: potencial de acción (fases, bases iónicas, voltage/patch clamp, separación de corrientes, curvas I/V, umbral, todo o nada, período refractario) |
| `temas/Tema_12_conduccion_potencial_accion.pdf` | Tema 12: conducción del potencial de acción (cono axónico, circuitos locales, mielina, nodos de Ranvier, tipos de fibras, potencial de acción compuesto). Sin transcripción todavía |
| `apuntes/tema12/` | Apuntes del Tema 12 en PDF con el modelo de Javier. Lo explicado en clase (clase04) sigue al profesor; el resto lleva «(Aún no explicado en clase)». Generados desde `tema12_apuntes.html` con Chromium headless (`--print-to-pdf`) |
| `apuntes/tema11/` | Apuntes completos del Tema 11 en PDF con el modelo de Javier (`Tema11_Potencial_de_accion_apuntes.pdf`), generados desde `tema11_apuntes.html` |
| `transcripciones/clase03_…` | Última clase del Tema 11: repaso I/V y compuerta, umbral, respuesta regenerativa, todo o nada, período refractario, propagación sin decremento (deja pregunta pendiente para la clase siguiente) |
| `transcripciones/clase04_…` | Repaso del umbral y del pico (+30 mV, Goldman), de qué depende la amplitud del potencial de acción (respuesta a la pregunta pendiente) e inicio del Tema 12 (concepto, sentido de propagación, cono axónico) |
| `temas/Tema_13_integracion_neuronal.pdf` | Tema 13: integración neuronal (aferencias, Gray I/II, potencial de reversión, compartimentos, reflejos, coactivación α-γ, localización, plasticidad NMDA) y propiedades intrínsecas (conductancias, patrones de disparo). Sin transcripción todavía |
| `apuntes/tema13/` | Apuntes del Tema 13 en PDF con el modelo de Javier, escritos solo con las diapositivas («aún no explicado en clase») |
| `transcripciones/clase01_…` | Final del Tema 10 (repaso: RC, τ, sumación temporal, λ, sumación espacial) + inicio del Tema 11 (fases, experimento de Na⁺ externo, canales de Na⁺ y K⁺) |
| `transcripciones/clase02_…` | Tema 11: voltage clamp, patch clamp (configuraciones), eliminación de corrientes pasivas, separación de I_Na e I_K, curvas I/V, conductancias, corriente de compuerta, pregunta sobre el umbral |

## Qué cubren las transcripciones frente a las diapositivas

- **Tema 10**: sin transcripción del principio (resistencia de entrada, efecto del tamaño celular, la membrana como condensador `C = εS/d`, `C_e = 1 µF/cm²`). Sí del final (τ, λ, sumación).
- **Tema 11**: completo (clases 01–03).

## Estilo del profesor (para explicar como él)

- Pregunta mucho a la clase y pide reformular «con tus palabras» / «¿otra forma de decirlo?».
- La «otra forma» que busca casi siempre es **en términos de permeabilidad y de la ecuación de Goldman**: «aumenta la permeabilidad a X → el potencial se acerca al potencial de equilibrio de X». No le basta con «sale potasio».
- Razona las corrientes con `I = g·(V_m − E_ion)`: separa siempre lo que hace la conductancia (cuántos canales abiertos) de lo que hace la fuerza impulsora (distancia al potencial de equilibrio).
- Usa ejemplos numéricos inventados sobre la marcha (−55, −50, −45, −40 mV; λ = 0,1 vs 1 mm; pulso de 10 mV ×6).
- **Cómo quiere Javier las explicaciones**: por bloques, uno cada vez, esperando a que diga que lo tiene. Cada bloque dividido en **apartados numerados (2, 2.1, 2.2…) con título y emoticono**, y en cada apartado **un párrafo pequeño (2-4 frases)** con el tono del profesor. Ni listas de frases sueltas ni parrafadas largas.
- **Apuntes**: que se lean como sus clases (tono hablado: «fijaos», «¿vale?», «de forma que…», preguntas que se responden, ejemplos con números) y que **expliquen cada gráfica/figura** (qué hay en los ejes, qué curva es cada una, en qué fijarse y qué demuestra).
- Dijo explícitamente que **en el examen hay que dibujar bien los pulsos de voltaje y las familias de corrientes** (curvas I/V, conductancias).

## Modelo de apuntes de Javier (copiar exacto)

Sacado de sus apuntes de los Temas 4–8 (PDF). Los apuntes nuevos siguen este modelo (sustituye al formato de los apuntes v1/v2 del Tema 12):

- **Título**: «TEMA N : TÍTULO» en mayúsculas, letra condensada y gruesa (tipo Oswald), negro, seguido de una línea horizontal color tostado.
- **Cada página**: línea tostada fina arriba y abajo; número de página abajo a la izquierda, debajo de la línea.
- **Secciones**: «1.TÍTULO EN MAYÚSCULAS» (número pegado al punto), negrita negra, sans (tipo Lato).
- **Subapartados**: sin número, negrita en color marrón/tostado («Las dos contribuciones al ΔG», «Ejemplo: …»).
- **Texto**: prosa clara, impersonal, interlineado amplio, términos clave en **negrita**; viñetas y listas numeradas para enumeraciones. Referencias a la clase del tipo «el profesor lo preguntó en clase».
- **Fórmulas**: bloque a todo el ancho, fondo beige claro con bordes finos arriba y abajo, fórmula centrada en serif; resultados clave en negrita.
- **Recuadros de aclaración**: fondo beige, borde izquierdo grueso tostado, título en mayúsculas pequeñas tostadas.
- **Diapositivas**: recortadas, centradas, sin pie de foto, justo después del texto que las explica; las gráficas se explican en prosa.
- **Sin emoticonos.** El subrayado amarillo lo pone él a mano; no reproducirlo.
- Lo que no dijo el profesor se marca de forma discreta (recuadro «ESTO NO LO DIJO EN CLASE» o un paréntesis).
