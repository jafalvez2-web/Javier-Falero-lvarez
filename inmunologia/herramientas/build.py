"""Monta los apuntes de Inmunología con la plantilla de Javier (INMUNO T1.docx) y los exporta a PDF.

Uso:  python3 build.py fuente.txt "salida.docx" [--pdf]

Marcas de línea en la fuente (una por línea; las líneas en blanco se ignoran):
  T:   título del tema
  H1:  apartado numerado ("1. TÍTULO"); si termina en " IMP", el IMP sale en rojo
  H2:  subapartado ("1.1 Título"); también admite " IMP" al final
  P:   párrafo
  B:   viñeta ●          B2: viñeta de segundo nivel
  X:   línea de examen en rojo ("📝 Ha caído en: …")
  N:   nota en cursiva gris (aclaraciones tipo "completado: no está en las diapositivas")
  IMG: ruta | pie de figura | ancho_cm (opcional, por defecto 15)
  PB:  salto de página
Dentro del texto: **negrita**.
"""
import re
import subprocess
import sys
import copy
from pathlib import Path

import docx
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PLANTILLA = Path(__file__).resolve().parent.parent / "plantilla" / "INMUNO T1.docx"
ROJO = RGBColor(0xE0, 0x10, 0x10)
GRIS = RGBColor(0x66, 0x66, 0x66)


def runs(par, texto, color=None, italic=False, size=None):
    for i, trozo in enumerate(re.split(r"\*\*", texto)):
        if not trozo:
            continue
        r = par.add_run(trozo)
        r.bold = bool(i % 2) or None
        if color is not None:
            r.font.color.rgb = color
        if italic:
            r.italic = True
        if size:
            r.font.size = Pt(size)


def con_imp(par, texto):
    imp = texto.rstrip().endswith(" IMP")
    if imp:
        texto = texto.rstrip()[:-4]
    runs(par, texto)
    if imp:
        r = par.add_run(" IMP")
        r.font.color.rgb = ROJO
        r.bold = True


def viñeta(doc, texto, nivel):
    p = doc.add_paragraph(style="normal")
    pPr = p._p.get_or_add_pPr()
    numPr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl"); ilvl.set(qn("w:val"), str(nivel))
    numId = OxmlElement("w:numId"); numId.set(qn("w:val"), "1")
    numPr.append(ilvl); numPr.append(numId)
    pPr.insert(0, numPr)
    sp = OxmlElement("w:spacing"); sp.set(qn("w:before"), "60"); sp.set(qn("w:after"), "0")
    pPr.append(sp)
    ind = OxmlElement("w:ind"); ind.set(qn("w:left"), str(720 + 360 * nivel)); ind.set(qn("w:hanging"), "360")
    pPr.append(ind)
    runs(p, texto)


def construir(fuente, salida):
    doc = docx.Document(str(PLANTILLA))
    body = doc.element.body
    for el in list(body):
        if el.tag != qn("w:sectPr"):
            body.remove(el)
    for linea in Path(fuente).read_text(encoding="utf-8").splitlines():
        if not linea.strip() or linea.startswith("#"):
            continue
        marca, _, texto = linea.partition(":")
        texto = texto.strip()
        if marca == "T":
            runs(doc.add_paragraph(style="Title"), texto)
        elif marca == "H1":
            con_imp(doc.add_paragraph(style="Heading 1"), texto)
        elif marca == "H2":
            p = doc.add_paragraph(style="Heading 2")
            con_imp(p, texto)
            for r in p.runs:
                if r.text != " IMP":
                    r.font.color.rgb = RGBColor(0x09, 0x09, 0xB9)
        elif marca == "P":
            runs(doc.add_paragraph(style="normal"), texto)
        elif marca == "B":
            viñeta(doc, texto, 0)
        elif marca == "B2":
            viñeta(doc, texto, 1)
        elif marca == "X":
            runs(doc.add_paragraph(style="normal"), "📝 " + texto, color=ROJO)
        elif marca == "N":
            runs(doc.add_paragraph(style="normal"), texto, color=GRIS, italic=True, size=9)
        elif marca == "IMG":
            partes = [s.strip() for s in texto.split("|")]
            ancho = float(partes[2]) if len(partes) > 2 and partes[2] else 15
            p = doc.add_paragraph(style="normal")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(partes[0], width=Cm(ancho))
            if len(partes) > 1 and partes[1]:
                c = doc.add_paragraph(style="normal")
                c.alignment = WD_ALIGN_PARAGRAPH.CENTER
                runs(c, partes[1], color=GRIS, italic=True, size=9)
        elif marca == "PB":
            doc.add_page_break()
        else:
            raise SystemExit(f"Marca desconocida: {linea[:60]}")
    doc.save(salida)


if __name__ == "__main__":
    fuente, salida = sys.argv[1], sys.argv[2]
    construir(fuente, salida)
    if "--pdf" in sys.argv:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir",
                        str(Path(salida).resolve().parent), salida], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
