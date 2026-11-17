"""Build: md/*.md -> one PDF per file (Chrome headless) -> merge (+ apuntes T2) -> page numbers.
Macros inside md:
  [[SOL 145:40-842 146:40-260]]  -> crop(s) of the professor's exam PDF (pages 1-based, y in pt)
  [[IMG path.png 80%]]          -> image from scratchpad
Usage: python build2.py [only_prefix]
"""
import markdown, re, sys, glob, os, subprocess, hashlib
import pymupdf

O = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(O)
EXAM = os.path.join(REPO, 'examenes', 'Examenes_2010-2026_Solucionados.pdf')
APUNTES_T2 = os.path.join(REPO, 'tema2', 'apuntes_T2.pdf')
# Chrome/Chromium: Windows, nube de Claude Code (Linux) o macOS, el primero que exista
CHROME = next((c for c in [
    os.environ.get('CHROME', ''),
    r'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '/opt/pw-browsers/chromium',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
] if c and os.path.exists(c)), 'chromium')
# En Linux (nube) Chrome corre como root y necesita --no-sandbox; el proxy de la nube se pasa si existe
CHROME_EXTRA = [] if os.name == 'nt' else ['--no-sandbox'] + (['--proxy-server=' + os.environ['HTTPS_PROXY']] if os.environ.get('HTTPS_PROXY') else [])
IMG = os.path.join(O, 'img'); os.makedirs(IMG, exist_ok=True)
OUT = os.path.join(O, 'out'); os.makedirs(OUT, exist_ok=True)
exam = pymupdf.open(EXAM)

CSS = """
@page { size: A4; margin: 16mm 17mm 17mm 17mm; }
body { font-family: 'Open Sans', 'Segoe UI', Arial, sans-serif; font-size: 10pt; line-height: 1.5; color: #111; }
h1 { font-family: 'Economica', 'Open Sans', sans-serif; font-weight: 700; font-size: 27pt; text-transform: uppercase; color: #000; border-bottom: 3px solid #09b909; padding-bottom: 2px; margin: 0 0 12px; letter-spacing: .5px; }
h2 { font-size: 14.5pt; font-weight: 700; color: #000; margin: 26px 0 8px; padding-top: 6px; border-top: 3px solid #09b909; page-break-after: avoid; }
h3 { font-size: 12pt; font-weight: 700; color: #09b909; margin: 18px 0 6px; page-break-after: avoid; }
h4 { font-size: 11.2pt; font-weight: 700; color: #fff; background: #7209b9; padding: 3px 8px; border-radius: 3px; margin: 18px 0 6px; page-break-after: avoid; }
h5 { font-size: 10.6pt; font-weight: 700; color: #7209b9; margin: 14px 0 5px; page-break-after: avoid; border-bottom: 1px solid #d9c2ea; }
p { margin: 6px 0; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.2pt; }
tr { page-break-inside: avoid; }
th { background: #e7f6e7; color: #0a5d0a; text-align: left; }
th, td { border: 1px solid #b7d3b7; padding: 3px 6px; vertical-align: top; }
blockquote { margin: 6px 0 10px; padding: 4px 12px; border-left: 3px solid #09b909; background: #f6fbf6; }
.tex { margin: 8px auto; padding: 4px 10px; background: #e9e3d3; border-radius: 3px; width: fit-content; max-width: 100%; page-break-inside: avoid; }
.sol { margin: 6px 0 10px; border: 1.5px solid #c9a227; border-radius: 4px; padding: 4px; background: #fffdf3; page-break-inside: avoid; }
.sol .lab { font-size: 8.3pt; font-weight: bold; color: #8a6d00; margin: 0 0 3px 2px; }
.sol img { width: 100%; display: block; }
.fig { text-align: center; margin: 8px 0; page-break-inside: avoid; }
.fig img { max-width: 100%; }
.enun { background: #f2f2f2; border-radius: 4px; padding: 5px 10px; margin: 6px 0; font-style: italic; }
.teoria { }
hr { border: none; border-top: 1.5px dashed #9bc79b; margin: 16px 0; }
.portada { text-align: center; padding-top: 65mm; }
.portada h1 { border: none; font-size: 40pt; }
.newpage { page-break-before: always; }
ul, ol { margin: 4px 0; padding-left: 22px; }
li { margin: 2px 0; }
"""

def crop(spec):
    imgs = []
    for part in spec.split():
        pg, rng = part.split(':')
        y0, y1 = map(float, rng.split('-'))
        name = f'sol_{pg}_{int(y0)}_{int(y1)}.jpg'
        path = os.path.join(IMG, name)
        if os.path.exists(path) and os.path.getsize(path) < 3000:
            os.remove(path)
        if not os.path.exists(path):
            page = exam[int(pg) - 1]
            # auto-trim: stop at next exam header / 2nd-parcial marker, shrink to content
            clip = pymupdf.Rect(0, y0, 595, y1)
            bottom = y0
            stop = y1
            for b in page.get_text('blocks', clip=clip):
                s = b[4].strip()
                if re.match(r'^(Química General|SEGUNDO PARCIAL|C\) SEGUNDO|PRIMER PARCIAL|B\) PRIMER)', s) and b[1] > y0 + 5:
                    stop = min(stop, b[1] - 2)
            for b in page.get_text('blocks', clip=clip):
                if b[1] < stop and b[4].strip():
                    bottom = max(bottom, min(b[3], stop))
            for dr in page.get_drawings():
                r = dr['rect']
                if r.y0 >= y0 - 2 and r.y1 <= stop + 2 and r.height < 700:
                    bottom = max(bottom, r.y1)
            for info in page.get_image_info():
                r = pymupdf.Rect(info['bbox'])
                if r.y0 < stop and r.y1 > y0:
                    bottom = max(bottom, min(r.y1, stop))
            y1 = min(stop, bottom + 6)
            if y1 - y0 < 14:
                imgs.append(None); continue
            pix = page.get_pixmap(dpi=125, clip=pymupdf.Rect(40, y0, 560, y1))
            pix.save(path, jpg_quality=80)
        imgs.append(name)
    return imgs

def md_to_html(text, title):
    # drop the typed statement when the professor's crop (which contains it) follows
    text = re.sub(r'<div class="enun" markdown="1">\n(?:(?!</div>).)*\n</div>\n\n(\[\[SOL)', r'\1', text, flags=re.S)
    text = text.replace('[[SOL ', '[[SOL|Enunciado y solución del profesor (PDF de exámenes)| ')
    # blank line before lists that follow a paragraph line
    lines = text.split('\n'); out = []
    for i, l in enumerate(lines):
        if re.match(r'^(\d+\.|-|\*) ', l) and out and out[-1].strip() and not re.match(r'^\s*(\d+\.|-|\*) ', out[-1]) and not out[-1].lstrip().startswith(('|', '>')):
            out.append('')
        elif re.match(r'^> (\d+\.|-|\*) ', l) and out and re.match(r'^> \S', out[-1]) and not re.match(r'^> (\d+\.|-|\*) ', out[-1]):
            out.append('>')
        out.append(l)
    text = '\n'.join(out)
    texs = []
    def keep(m):
        texs.append(m.group(1).strip())
        return f'\n\nTEXBLOCK{len(texs)-1}ENDTEX\n\n'
    text = re.sub(r'\$\$(.+?)\$\$', keep, text, flags=re.S)
    def sol(m):
        lab = m.group(1) or 'Solución del profesor (PDF de exámenes)'
        ims = crop(m.group(2))
        return '\n\n<div class="sol"><div class="lab">' + lab + '</div>' + ''.join(f'<img src="img/{i}">' for i in ims if i) + '</div>\n\n'
    text = re.sub(r'\[\[SOL(?:\|([^\]|]*)\|)?\s+([^\]]+)\]\]', sol, text)
    def img(m):
        w = m.group(2) or '90%'
        if float(w.rstrip('%')) <= 50:
            return f'<span class="fig" style="display:inline-block;width:{w};vertical-align:top;margin:4px 0"><img src="{m.group(1)}" style="width:100%"></span>'
        return f'\n\n<div class="fig"><img src="{m.group(1)}" style="width:{w}"></div>\n\n'
    text = re.sub(r'\[\[IMG\s+(\S+)(?:\s+(\S+))?\]\]', img, text)
    h = markdown.markdown(text, extensions=['tables', 'sane_lists', 'md_in_html'])
    for i, t in enumerate(texs):
        safe = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        h = h.replace(f'<p>TEXBLOCK{i}ENDTEX</p>', f'<div class="tex">{safe}</div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="katex/katex.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Economica:wght@400;700&family=Open+Sans:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style></head><body>{h}
<script src="katex/katex.min.js"></script>
<script>document.querySelectorAll('.tex').forEach(d=>{{try{{katex.render(d.textContent,d,{{displayMode:true,throwOnError:false}})}}catch(e){{}}}});</script>
</body></html>"""

def build_one(md):
    base = os.path.splitext(os.path.basename(md))[0]
    html = os.path.join(O, base + '.html')
    pdf = os.path.join(OUT, base + '.pdf')
    open(html, 'w', encoding='utf-8').write(md_to_html(open(md, encoding='utf-8').read(), base))
    subprocess.run([CHROME, *CHROME_EXTRA, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    '--virtual-time-budget=20000', '--allow-file-access-from-files',
                    f'--print-to-pdf={pdf}', 'file:///' + html.replace('\\', '/')],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    print(base, pymupdf.open(pdf).page_count, 'pages')

def merge():
    order = sorted(glob.glob(os.path.join(OUT, '*.pdf')))
    final = pymupdf.open()
    toc = []
    for p in order:
        base = os.path.basename(p)
        if base.startswith('_'):
            continue
        doc = pymupdf.open(p)
        start = final.page_count
        final.insert_pdf(doc)
    # page numbers
    for i, page in enumerate(final):
        if i == 0:
            continue
        r = page.rect
        page.insert_text((r.width / 2 - 8, r.height - 18), f'{i + 1}', fontsize=8.5, color=(0.35, 0.35, 0.35))
    dest = os.path.join(O, 'Repaso_Quimica_1er_parcial.pdf')
    final.save(dest, garbage=3, deflate=True)
    print('FINAL', final.page_count, 'pages', round(os.path.getsize(dest) / 1e6, 1), 'MB')

if __name__ == '__main__':
    only = sys.argv[1] if len(sys.argv) > 1 else ''
    for md in sorted(glob.glob(os.path.join(O, 'md2', '*.md'))):
        if os.path.basename(md).startswith(only):
            build_one(md)
    merge()
