"""Esquemas para copiar a mano en las preguntas de desarrollo de Inmunología.

Uso:  python3 esquemas.py <carpeta_salida>
Genera un PNG por esquema. Estilo deliberadamente simple (cajas, flechas, membranas)
para que se pueda reproducir en el examen en uno o dos minutos.
"""
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Ellipse, Circle

plt.rcParams["font.family"] = ["DejaVu Sans"]
AZUL, VERDE, NARANJA, ROJO, GRIS, MORADO, AMARILLO = "#dfe7fb", "#dff2e6", "#fde9d6", "#fbe0e0", "#eef0f4", "#ece3f7", "#fbf3d0"
BORDE = "#2b3445"
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")


def lienzo(w, h):
    fig, ax = plt.subplots(figsize=(w / 10, h / 10), dpi=160)
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax


def caja(ax, x, y, texto, color=GRIS, w=None, h=7, fs=9, bold=False, borde=BORDE):
    lineas = texto.split("\n")
    if w is None:
        w = max(len(l) for l in lineas) * fs * (0.1 if bold else 0.088) + 5
    h = max(h, len(lineas) * fs * 0.16 + 3)
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc=color, ec=borde, lw=1.1))
    ax.text(x, y, texto, ha="center", va="center", fontsize=fs, weight="bold" if bold else "normal", color="#141a26")
    return (x, y, w, h)


def flecha(ax, a, b, texto=None, color=BORDE, freno=False, curva=0.0, lado="arriba", fs=8):
    st = "-[" if freno else "-|>"
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=st + (",widthB=4" if freno else ",head_width=3,head_length=5"),
                                 mutation_scale=1.6 if freno else 1.2, color=color, lw=1.4,
                                 connectionstyle=f"arc3,rad={curva}", shrinkA=2, shrinkB=2))
    if texto:
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        dy = 2.2 if lado == "arriba" else -2.2
        dx = 0
        if lado == "dcha": dx, dy = 1.5, 0
        if lado == "izq": dx, dy = -1.5, 0
        ax.text(mx + dx, my + dy, texto, ha="left" if lado == "dcha" else ("right" if lado == "izq" else "center"),
                va="center", fontsize=fs, color=color, style="italic")


def membrana(ax, x0, x1, y, grosor=4, vertical=False):
    if vertical:
        ax.add_patch(Rectangle((y, x0), grosor, x1 - x0, fc="#f3e7c9", ec="#b59a52", lw=1))
        for k in range(int(x0), int(x1), 3):
            ax.add_patch(Circle((y + 0.6, k + 1.5), 0.55, fc="#b59a52", ec="none"))
            ax.add_patch(Circle((y + grosor - 0.6, k + 1.5), 0.55, fc="#b59a52", ec="none"))
    else:
        ax.add_patch(Rectangle((x0, y), x1 - x0, grosor, fc="#f3e7c9", ec="#b59a52", lw=1))
        for k in range(int(x0), int(x1), 3):
            ax.add_patch(Circle((k + 1.5, y + 0.6), 0.55, fc="#b59a52", ec="none"))
            ax.add_patch(Circle((k + 1.5, y + grosor - 0.6), 0.55, fc="#b59a52", ec="none"))


def pieza(ax, x, y, w, h, texto, color, fs=8):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.2,rounding_size=1.5",
                                fc=color, ec=BORDE, lw=1))
    ax.text(x, y, texto, ha="center", va="center", fontsize=fs, weight="bold")


def titulo(ax, x, y, texto, fs=10):
    ax.text(x, y, texto, ha="center", va="center", fontsize=fs, weight="bold", color="#141a26")


def guardar(fig, nombre):
    fig.savefig(OUT / f"{nombre}.png", bbox_inches="tight", pad_inches=0.15, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Temas 11 y 12
def mac():
    fig, ax = lienzo(150, 62)
    xs = [18, 55, 92, 129]
    pasos = ["1. C5b se une\na C6 y C7", "2. C7 cambia de forma\ny se inserta (hidrófobo)", "3. Se une C8 y se inserta:\nporo pequeño", "4. 10–16 C9 polimerizan:\nporo de 100 Å"]
    for x, p in zip(xs, pasos):
        membrana(ax, x - 16, x + 16, 18)
        titulo(ax, x, 56, p, fs=8.5)
    ax.text(2, 12, "membrana del microbio", fontsize=7, va="center", color="#7a6630")
    # 1
    pieza(ax, 12, 38, 6, 10, "C5b", AZUL); pieza(ax, 19, 38, 5, 8, "C6", VERDE); pieza(ax, 25, 38, 5, 8, "C7", NARANJA)
    # 2
    pieza(ax, 49, 30, 6, 10, "C5b", AZUL); pieza(ax, 55, 30, 5, 8, "C6", VERDE); pieza(ax, 60.5, 21, 5, 16, "C7", NARANJA)
    # 3
    pieza(ax, 84, 30, 6, 10, "C5b", AZUL); pieza(ax, 89.5, 30, 5, 8, "C6", VERDE); pieza(ax, 95, 21, 5, 16, "C7", NARANJA); pieza(ax, 100.5, 18, 5, 20, "C8", MORADO)
    # 4: tubo de C9
    for dx in (-9, -5, 5, 9):
        pieza(ax, 129 + dx, 21, 3.6, 22, "C9", ROJO, fs=6.5)
    pieza(ax, 116, 33, 5, 8, "C5b-8", AZUL, fs=6.5)
    flecha(ax, (129, 44), (129, 12), color="#2c6fd6"); ax.text(140, 38, "agua\ne iones", fontsize=7.5, color="#2c6fd6", ha="left")
    ax.text(129, 7, "LISIS OSMÓTICA", ha="center", fontsize=9, weight="bold", color="#c23b3b")
    for a, b in ((33, 41), (70, 78), (107, 113)):
        flecha(ax, (a, 40), (b, 40))
    ax.text(75, 2, "La fase terminal no corta proteínas: solo se van uniendo y cambiando de forma.  CD59 (en nuestras células) impide la polimerización de C9.",
            ha="center", fontsize=7.5, style="italic", color="#4b5466")
    guardar(fig, "T11_mac")


def via_alternativa():
    fig, ax = lienzo(120, 112)
    caja(ax, 22, 104, "C3 del plasma", GRIS, bold=True)
    caja(ax, 72, 104, "C3b (tioéster expuesto)", AZUL, bold=True)
    flecha(ax, (34, 104), (56, 104), "hidrólisis espontánea\n(«tick-over»)")
    caja(ax, 35, 86, "En el plasma:\nreacciona con agua\nC3b INACTIVO", GRIS)
    caja(ax, 90, 86, "Sobre el microbio:\nse pega covalentemente\n(enlace éster / amida)", VERDE)
    flecha(ax, (66, 99), (42, 92)); flecha(ax, (78, 99), (88, 93))
    caja(ax, 90, 68, "C3b + factor B  →  C3bB", AZUL)
    flecha(ax, (90, 79), (90, 72))
    caja(ax, 90, 52, "C3bBb\nCONVERTASA DE C3", NARANJA, bold=True)
    flecha(ax, (90, 64), (90, 57), "factor D corta B", lado="dcha")
    caja(ax, 40, 60, "Ba se libera", GRIS, fs=8)
    flecha(ax, (78, 64), (52, 61))
    caja(ax, 40, 46, "Properdina (P)\nla ESTABILIZA", VERDE, fs=8)
    flecha(ax, (55, 47), (76, 51))
    caja(ax, 90, 34, "C3  →  C3a + muchos C3b", AZUL)
    flecha(ax, (90, 47), (90, 38))
    flecha(ax, (104, 36), (106, 82), "BUCLE DE\nAMPLIFICACIÓN", color="#c23b3b", curva=0.45, lado="dcha")
    caja(ax, 90, 18, "+ otro C3b:  C3b2Bb\nCONVERTASA DE C5", NARANJA, bold=True)
    flecha(ax, (90, 30), (90, 23))
    caja(ax, 35, 18, "C5 → C5a (inflamación)\n+ C5b → CAM (lisis)", ROJO, fs=8)
    flecha(ax, (74, 18), (53, 18))
    ax.text(60, 4, "Solo avanza sobre microbios: nuestras células tienen reguladores (factor H, DAF, MCP, CR1, factor I).",
            ha="center", fontsize=7.5, style="italic", color="#4b5466")
    guardar(fig, "T11_alternativa")


def via_clasica():
    fig, ax = lienzo(120, 92)
    caja(ax, 25, 84, "Antígeno + anticuerpo\n(1 IgM o ≥ 2 IgG juntas)", VERDE)
    caja(ax, 80, 84, "C1 = C1q + C1r₂ + C1s₂", AZUL, bold=True)
    flecha(ax, (45, 84), (60, 84), "C1q se une")
    caja(ax, 80, 68, "C1r se activa  →  activa C1s", AZUL)
    flecha(ax, (80, 79), (80, 72))
    caja(ax, 30, 52, "C4 → C4a + C4b\n(C4b se pega al microbio)", GRIS)
    caja(ax, 92, 52, "C2 → C2b + C2a\n(C2a se une a C4b)", GRIS)
    flecha(ax, (70, 64), (42, 57), "C1s corta", lado="arriba"); flecha(ax, (85, 64), (90, 58), "C1s corta", lado="dcha")
    caja(ax, 60, 36, "C4b2a\nCONVERTASA DE C3", NARANJA, bold=True)
    flecha(ax, (32, 46), (52, 40)); flecha(ax, (90, 46), (68, 40))
    caja(ax, 20, 22, "C3 → C3a + C3b\n(opsonina)", AZUL)
    flecha(ax, (48, 34), (30, 26))
    caja(ax, 60, 14, "C4b2a3b\nCONVERTASA DE C5", NARANJA, bold=True)
    flecha(ax, (60, 31), (60, 19), "+ C3b", lado="dcha")
    caja(ax, 100, 14, "C5 → C5a + C5b\n→ CAM", ROJO)
    flecha(ax, (73, 14), (88, 14))
    guardar(fig, "T11_clasica")


def via_lectinas():
    fig, ax = lienzo(120, 80)
    caja(ax, 22, 72, "IL-6 → hígado fabrica\nMBL y ficolinas", GRIS, fs=8)
    caja(ax, 78, 72, "MBL (manosa) o ficolina\n(N-acetilglucosamina)\n+ MASP-1 y MASP-2", VERDE, bold=True)
    flecha(ax, (38, 72), (56, 72))
    caja(ax, 78, 54, "Se une al azúcar del microbio\n→ se activa MASP-2", AZUL)
    flecha(ax, (78, 65), (78, 58))
    caja(ax, 30, 38, "C4 → C4a + C4b\n(se pega al microbio)", GRIS)
    caja(ax, 96, 38, "C2 → C2b + C2a", GRIS)
    flecha(ax, (66, 50), (42, 42), "MASP-2 corta"); flecha(ax, (88, 50), (94, 42), "MASP-2 corta", lado="dcha")
    caja(ax, 62, 22, "C4b2a = CONVERTASA DE C3\n(la misma que la vía clásica)", NARANJA, bold=True)
    flecha(ax, (32, 33), (50, 26)); flecha(ax, (94, 33), (76, 26))
    caja(ax, 62, 6, "C4b2a3b (convertasa de C5)  →  C5a + C5b  →  CAM", ROJO, fs=8)
    flecha(ax, (62, 17), (62, 10))
    guardar(fig, "T11_lectinas")


def reguladores():
    fig, ax = lienzo(150, 52)
    etapas = [(18, "Inicio\nC1 (C1r, C1s) / MASP"), (56, "Convertasas\nC4b2a, C3bBb"), (96, "C3b y C4b\ndepositados"), (132, "CAM\n(polimerización de C9)")]
    frenos = [(18, "C1-INH\nbloquea C1r, C1s, MASP"), (56, "DAF, CR1, MCP,\nfactor H, C4bp\nimpiden o deshacen"), (96, "Factor I\n(+ CR1, MCP, C4bp, H)\nlos degrada"), (132, "CD59\nimpide la\npolimerización de C9")]
    for (x, t), (_, f) in zip(etapas, frenos):
        caja(ax, x, 42, t, AZUL, w=30, bold=True)
        caja(ax, x, 12, f, ROJO, w=30, fs=8)
        flecha(ax, (x, 19), (x, 35), color="#c23b3b", freno=True)
    for a, b in ((33, 41), (71, 81), (111, 117)):
        flecha(ax, (a, 42), (b, 42))
    ax.text(75, 27, "Están en nuestras células y no en los microbios", ha="center", fontsize=8, style="italic", color="#c23b3b")
    guardar(fig, "T11_reguladores")


# ---------------------------------------------------------------- Tema 13
def citocinas_macrofago():
    fig, ax = lienzo(130, 80)
    caja(ax, 65, 42, "MACRÓFAGO\n(sus PRR reconocen\nal microbio)", NARANJA, w=30, h=14, bold=True)
    obj = [(22, 72, "TNF-α", "endotelio activado\n(en exceso: shock)"), (108, 72, "IL-1", "hipotálamo: FIEBRE"),
           (16, 42, "IL-6", "hígado: proteínas de\nfase aguda (PCR)"), (114, 42, "CXCL8", "atrae NEUTRÓFILOS"),
           (22, 12, "IL-12", "NK y Th1 → IFN-γ"), (108, 12, "IL-10", "FRENO de la\ninflamación")]
    for x, y, c, d in obj:
        caja(ax, x, y, d, AZUL if c != "IL-10" else VERDE, w=30, fs=8)
        sx = 65 + (x - 65) * 0.25; sy = 42 + (y - 42) * 0.28
        ex = x + (6 if x < 65 else -6) * 0 ; ey = y
        flecha(ax, (sx, sy), (x + (15 if x < 65 else -15), y), c, lado="arriba", fs=8.5)
    flecha(ax, (24, 7), (55, 36), "IFN-γ activa al macrófago (bucle)", color="#2c6fd6", curva=0.35, lado="abajo", fs=7)
    guardar(fig, "T13_macrofago")


def th1():
    fig, ax = lienzo(130, 84)
    caja(ax, 20, 74, "DC / macrófago\n(microbio intracelular)", NARANJA)
    caja(ax, 72, 74, "T CD4 virgen\n(señales 1 y 2)", GRIS)
    flecha(ax, (37, 74), (56, 74), "IL-12")
    caja(ax, 72, 54, "IL-12 → STAT4\nIFN-γ → STAT1 → T-bet", AZUL, fs=8)
    flecha(ax, (72, 69), (72, 59))
    caja(ax, 72, 36, "Th1", AZUL, w=16, bold=True, fs=11)
    flecha(ax, (72, 49), (72, 41))
    caja(ax, 115, 54, "NK", GRIS)
    flecha(ax, (110, 54), (86, 54), "IFN-γ", lado="arriba")
    efectos = [(14, 12, "Macrófago M1\n(NO, ROS: mata\nlo fagocitado)", VERDE), (44, 12, "↑ MHC I y II\n(mejor\npresentación)", VERDE),
               (76, 12, "Linfocito B:\nIgG opsonizantes", VERDE), (108, 12, "Inhibe Th2", ROJO)]
    for x, y, t, c in efectos:
        caja(ax, x, y, t, c, w=26, fs=8)
        flecha(ax, (72, 31), (x, 19), freno=(c == ROJO))
    ax.text(58, 25, "IFN-γ", fontsize=8.5, style="italic")
    caja(ax, 112, 36, "IL-2 (proliferación)\nCD40L, TNF", GRIS, fs=8)
    flecha(ax, (80, 36), (98, 36))
    flecha(ax, (10, 19), (10, 68), "más IL-12 (bucle)", color="#2c6fd6", curva=-0.3, lado="izq", fs=7)
    guardar(fig, "T13_th1")


def th2():
    fig, ax = lienzo(120, 74)
    caja(ax, 22, 66, "IL-4\n(+ IL-25 e IL-33 del epitelio\nactivan a las ILC2)", GRIS, fs=8)
    caja(ax, 80, 66, "T CD4 virgen", GRIS)
    flecha(ax, (42, 66), (68, 66))
    caja(ax, 80, 48, "IL-4 → STAT6 → GATA-3", AZUL)
    flecha(ax, (80, 61), (80, 52))
    caja(ax, 80, 32, "Th2", AZUL, w=16, bold=True, fs=11)
    flecha(ax, (80, 44), (80, 37))
    caja(ax, 20, 40, "IFN-γ", ROJO)
    flecha(ax, (27, 38), (71, 33), freno=True)
    for x, c, t in ((24, "IL-4", "Linfocito B:\ncambio a IgE"), (60, "IL-5", "Eosinófilos"), (96, "IL-13", "Moco y\nmacrófago M2")):
        caja(ax, x, 12, t, VERDE, w=26, fs=8)
        flecha(ax, (80, 27), (x, 18), c, lado="dcha" if x > 80 else "izq")
    ax.text(60, 1.5, "Funciones: defensa frente a HELMINTOS; si se dirige a antígenos inocuos: ALERGIA", ha="center", fontsize=7.5, style="italic", color="#4b5466")
    guardar(fig, "T13_th2")


def fas():
    fig, ax = lienzo(120, 70)
    ax.add_patch(Rectangle((2, 4), 30, 62, fc="#f3f4f8", ec=BORDE, lw=1))
    ax.text(17, 62, "CTL o T activado", ha="center", fontsize=9, weight="bold")
    membrana(ax, 4, 66, 36, grosor=4, vertical=True)
    ax.text(78, 64, "CÉLULA DIANA", ha="center", fontsize=9, weight="bold")
    pieza(ax, 26, 42, 8, 6, "FasL", NARANJA)
    pieza(ax, 37, 42, 12, 5, "Fas (×3)", AZUL)
    flecha(ax, (30, 42), (31.5, 42))
    caja(ax, 62, 42, "DD de Fas reclutan\nFADD", GRIS, fs=8)
    flecha(ax, (43, 42), (50, 42))
    caja(ax, 98, 42, "DED de FADD reclutan\nprocaspasa-8", GRIS, fs=8)
    flecha(ax, (74, 42), (84, 42))
    ax.add_patch(FancyBboxPatch((49, 34), 64, 16, boxstyle="round,pad=0.3", fc="none", ec="#c23b3b", lw=1.2, ls="--"))
    ax.text(81, 31, "= DISC", ha="center", fontsize=8.5, color="#c23b3b", weight="bold")
    caja(ax, 80, 20, "caspasa-8 activa  →  caspasas efectoras (caspasa-3)", AZUL, fs=8)
    flecha(ax, (98, 34), (88, 24))
    caja(ax, 80, 7, "APOPTOSIS", ROJO, bold=True)
    flecha(ax, (80, 16), (80, 11))
    guardar(fig, "T13_fas")


def tres_senales():
    fig, ax = lienzo(130, 80)
    ax.add_patch(FancyBboxPatch((4, 46), 26, 30, boxstyle="round,pad=0.3", fc=NARANJA, ec=BORDE))
    ax.text(17, 72, "APC\n(célula dendrítica)", ha="center", va="top", fontsize=9, weight="bold")
    ax.add_patch(FancyBboxPatch((86, 46), 26, 30, boxstyle="round,pad=0.3", fc=AZUL, ec=BORDE))
    ax.text(99, 72, "T CD4\nvirgen", ha="center", va="top", fontsize=9, weight="bold")
    for y, a, b, n in ((64, "MHC-II + péptido", "TCR", "Señal 1"), (56, "B7", "CD28", "Señal 2"), (48, "citocinas", "receptores", "Señal 3")):
        ax.text(31, y, a, fontsize=8, ha="left", va="center"); ax.text(85, y, b, fontsize=8, ha="right", va="center")
        flecha(ax, (48, y), (70, y), n, fs=8)
    outs = [(16, "IL-12 → Th1\n(STAT4)"), (46, "IL-4 → Th2\n(STAT6)"), (78, "TGF-β + IL-6 → Th17\n(STAT3)"), (112, "TGF-β + IL-2 → Treg")]
    for x, t in outs:
        caja(ax, x, 26, t, VERDE, w=28, fs=8)
        flecha(ax, (99, 45), (x, 31))
    caja(ax, 64, 8, "IL-2 + CD25 (receptor de alta afinidad) → STAT5 → EXPANSIÓN CLONAL (autocrina)", AMARILLO, fs=8)
    guardar(fig, "T13_tres_senales")


def cd40l():
    fig, ax = lienzo(120, 60)
    ax.add_patch(FancyBboxPatch((4, 22), 30, 32, boxstyle="round,pad=0.3", fc=AZUL, ec=BORDE))
    ax.text(19, 50, "T CD4 / Tfh\nactivado", ha="center", va="top", fontsize=9, weight="bold")
    ax.add_patch(FancyBboxPatch((84, 22), 30, 32, boxstyle="round,pad=0.3", fc=VERDE, ec=BORDE))
    ax.text(99, 50, "Linfocito B\n(ha captado el Ag)", ha="center", va="top", fontsize=9, weight="bold")
    for y, a, b in ((40, "TCR", "MHC-II + péptido"), (32, "CD40L", "CD40"), (24, "IL-4, IL-5, IL-6", "receptores")):
        ax.text(35, y, a, fontsize=8, ha="left", va="center"); ax.text(83, y, b, fontsize=8, ha="right", va="center")
        flecha(ax, (55, y), (66, y) if y != 40 else (55, y), None) if False else None
    flecha(ax, (66, 40), (50, 40)); flecha(ax, (50, 32), (66, 32), "contacto"); flecha(ax, (55, 24), (66, 24))
    caja(ax, 60, 7, "Proliferación · centro germinal · CAMBIO DE ISOTIPO · maduración de la afinidad", AMARILLO, fs=8)
    flecha(ax, (99, 21), (90, 11))
    guardar(fig, "T13_cd40l")


def jak_stat():
    fig, ax = lienzo(140, 66)
    membrana(ax, 2, 138, 40)
    pasos = [(18, "1. APROXIMAR\nla citocina junta\nlas cadenas"), (52, "2. FOSFORILAR\nlas JAK se activan\ny fosforilan el receptor"), (88, "3. ACTIVAR STAT\nse unen (SH2), se\nfosforilan y dimerizan"), (122, "4. NÚCLEO\nel dímero de STAT\nactiva genes")]
    for x, t in pasos:
        titulo(ax, x, 59, t, fs=7.5)
    for x in (18, 52, 88):
        pieza(ax, x - 3, 38, 3, 22, "", AZUL); pieza(ax, x + 3, 38, 3, 22, "", AZUL)
        ax.add_patch(Circle((x, 51), 2.4, fc=NARANJA, ec=BORDE));
        pieza(ax, x - 5.5, 31, 4, 4, "J", AMARILLO, fs=6.5); pieza(ax, x + 5.5, 31, 4, 4, "J", AMARILLO, fs=6.5)
    for x in (52, 88):
        ax.text(x - 5.5, 26, "P", fontsize=7, ha="center", color="#c23b3b", weight="bold"); ax.text(x + 5.5, 26, "P", fontsize=7, ha="center", color="#c23b3b", weight="bold")
    pieza(ax, 84, 22, 4, 5, "S", VERDE, fs=6.5); pieza(ax, 92, 22, 4, 5, "S", VERDE, fs=6.5)
    ax.add_patch(Ellipse((122, 18), 26, 18, fc="#f3f4f8", ec=BORDE, ls="--"))
    ax.text(122, 24, "núcleo", ha="center", fontsize=7.5)
    pieza(ax, 119, 17, 4, 5, "S", VERDE, fs=6.5); pieza(ax, 125, 17, 4, 5, "S", VERDE, fs=6.5)
    ax.text(122, 11, "transcripción", ha="center", fontsize=7.5)
    flecha(ax, (96, 22), (110, 18))
    for a, b in ((30, 40), (64, 76)):
        flecha(ax, (a, 50), (b, 50))
    ax.text(70, 3, "Frenos: SOCS (inducidos por los propios STAT: retroalimentación negativa) · fosfatasas · PIAS        J = JAK   S = STAT   P = fosfato",
            ha="center", fontsize=7, style="italic", color="#4b5466")
    guardar(fig, "T13_jak_stat")


def nlrp3():
    fig, ax = lienzo(130, 70)
    caja(ax, 28, 62, "SEÑAL 1 (primado)\nTLR, IL-1R o TNFR → NF-κB", AZUL, bold=True, fs=8)
    caja(ax, 28, 44, "se fabrican\npro-IL-1β y NLRP3", GRIS, fs=8)
    flecha(ax, (28, 57), (28, 49))
    caja(ax, 100, 62, "SEÑAL 2 (activación)\nsalida de K⁺ · cristales · ROS", NARANJA, bold=True, fs=8)
    caja(ax, 64, 30, "INFLAMASOMA\nNLRP3 + ASC + procaspasa-1", MORADO, bold=True, fs=8.5)
    flecha(ax, (40, 40), (56, 34)); flecha(ax, (100, 57), (74, 35), "ensamblaje", lado="dcha")
    caja(ax, 30, 10, "caspasa-1: pro-IL-1β y pro-IL-18\n→ IL-1β e IL-18 maduras", VERDE, fs=8)
    caja(ax, 98, 10, "caspasa-1 corta la gasdermina D\n→ poros → PIROPTOSIS", ROJO, fs=8)
    flecha(ax, (56, 25), (36, 15)); flecha(ax, (72, 25), (92, 15))
    guardar(fig, "T13_nlrp3")


def extravasacion():
    fig, ax = lienzo(140, 60)
    ax.text(2, 52, "SANGRE", fontsize=8, color="#c23b3b", weight="bold")
    ax.text(2, 8, "TEJIDO", fontsize=8, color="#4b5466", weight="bold")
    membrana(ax, 2, 138, 26, grosor=6)
    ax.text(137, 29, "endotelio", fontsize=7, ha="right", color="#7a6630")
    pos = [(14, 42, "1. RODAMIENTO\nselectinas"), (44, 40, "2. ACTIVACIÓN\nCXCL8 → CXCR1/2"), (74, 35.5, "3. ADHESIÓN FIRME\nLFA-1 – ICAM-1"), (102, 26, "4. DIAPÉDESIS\n(CD31)")]
    for x, y, t in pos:
        ax.add_patch(Circle((x, y), 4.2, fc="#f6d1dc", ec=BORDE))
        ax.text(x, 52 if y > 30 else 50, t, ha="center", fontsize=7.5, weight="bold")
    for a, b in ((19, 39), (49, 69), (79, 97)):
        flecha(ax, (a, 41), (b, 39))
    ax.add_patch(Circle((124, 10), 4.2, fc="#f6d1dc", ec=BORDE))
    flecha(ax, (106, 21), (119, 13), "5. MIGRA por el\ngradiente de CXCL8", lado="izq", fs=7.5)
    for k, x in enumerate(range(60, 136, 8)):
        ax.add_patch(Circle((x, 6 + (k % 2) * 3), 0.8 + k * 0.12, fc="#2c6fd6", ec="none"))
    ax.text(136, 2, "foco: más CXCL8", ha="right", fontsize=7, color="#2c6fd6")
    guardar(fig, "T13_extravasacion")


def il2r():
    fig, ax = lienzo(120, 56)
    membrana(ax, 2, 118, 22)
    grupos = [(20, ["α"], "BAJA afinidad\n(no da señal)"), (60, ["β", "γc"], "INTERMEDIA\n(NK, T en reposo)"), (100, ["α", "β", "γc"], "ALTA\n(T activado, Treg)")]
    col = {"α": "#cfd8f6", "β": NARANJA, "γc": VERDE}
    for x, cs, t in grupos:
        n = len(cs)
        for k, c in enumerate(cs):
            cx = x + (k - (n - 1) / 2) * 7
            pieza(ax, cx, 24, 5, 26 if c != "α" else 20, c, col[c], fs=8)
            if c == "β": pieza(ax, cx, 8, 6, 4, "JAK1", AMARILLO, fs=6)
            if c == "γc": pieza(ax, cx, 8, 6, 4, "JAK3", AMARILLO, fs=6)
        ax.add_patch(Circle((x, 42), 3, fc="#f6d1dc", ec=BORDE)); ax.text(x, 42, "IL-2", ha="center", va="center", fontsize=6.5)
        titulo(ax, x, 51, t, fs=8)
    ax.text(60, 0.5, "La señal (JAK1 + JAK3 → STAT5) da proliferación y supervivencia. γc la comparten IL-2, 4, 7, 9, 15 y 21: su defecto es la X-SCID.",
            ha="center", fontsize=7, style="italic", color="#4b5466")
    guardar(fig, "T13_il2r")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f in (mac, via_alternativa, via_clasica, via_lectinas, reguladores, citocinas_macrofago, th1, th2, fas,
              tres_senales, cd40l, jak_stat, nlrp3, extravasacion, il2r):
        f()
    print("ok")
