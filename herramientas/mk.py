import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import build2
src = sys.argv[1]; pdf = sys.argv[2]
html = os.path.join(build2.O, os.path.splitext(os.path.basename(src))[0] + '.html')
open(html, 'w', encoding='utf-8').write(build2.md_to_html(open(src, encoding='utf-8').read(), 'Analisis 2o parcial'))
url = 'file:///' + html.replace(os.sep, '/')
subprocess.run([build2.CHROME, *build2.CHROME_EXTRA, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=20000',
                '--print-to-pdf=' + pdf, url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
import pymupdf
print(pymupdf.open(pdf).page_count, 'pages')
