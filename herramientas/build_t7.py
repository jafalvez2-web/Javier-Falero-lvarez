import os, re, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__))
P2 = os.path.dirname(H)
sys.path.insert(0, P2)
os.chdir(H)

# 1) sustituir fichas reescritas
if os.path.exists('newsec.md'):
    t = open('f_ap6.md', encoding='utf-8').read()
    for blk in open('newsec.md', encoding='utf-8').read().split('@@@')[1:]:
        key, body = blk.split('\n', 1)
        i = t.index('##### ' + key + ' ')
        j = t.index(']]', t.index('[[SOL', i)) + 2
        k = min(x for x in (t.find(m, j) for m in ('\n#####', '\n#### ', '\n### ')) if x != -1)
        t = t[:j] + '\n\n' + body.strip() + '\n' + t[k:]
    open('f_ap6.md', 'w', encoding='utf-8').write(t)
    os.rename('newsec.md', 'newsec_done.md')

# 2) cuentas -> ecuaciones
import apply_tex
for f in ('b_ap1_prob', 'c2_ap3', 'd2_ap4', 'f_ap6'):
    open(f + '_tex.md', 'w', encoding='utf-8').write(apply_tex.process(f + '.md'))

# 3) unir
order = ['a_intro', 'b_ap1_teoria', 'b_ap1_prob_tex', 'c_ap2_teoria3', 'c2_ap3_tex', 'd_teoria4', 'd2_ap4_tex', 'e_ap5_teoria6', 'f_ap6_tex', 'g_ap7']
L = '\n\n'.join(open(f + '.md', encoding='utf-8').read() for f in order).split('\n')
out = []
for l in L:
    if l.startswith('**') and out and out[-1].strip() and not out[-1].lstrip().startswith(('|', '>', '<', '#', '$')):
        out.append('')
    out.append(l)
L = out; out = []; inenun = False
blk = ('|', '-', '#', '<', '$', '>', '[[', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')
for i, l in enumerate(L):
    nx = L[i + 1] if i + 1 < len(L) else ''
    s = l.strip()
    if s.startswith('<div class="enun"'): inenun = True
    if s == '</div>': inenun = False
    if s and nx.strip() and not s.startswith(blk) and not nx.strip().startswith(blk) and not inenun and not l.endswith('  '):
        l = l + '  '
    out.append(l)
open('t7_full.md', 'w', encoding='utf-8').write('\n'.join(out))
print('ecuaciones:', '\n'.join(out).count('$$') // 2)

# 4) dibujos de laboratorio
import lab, labspecs7
IMG = os.path.join(os.path.dirname(P2), 'img')
t = open('t7_full.md', encoding='utf-8').read()
n = 0
for key, (panels, arrows, bottom) in labspecs7.S.items():
    fn = 'lab7_' + key.replace(' ', '_').replace('.', '_') + '.svg'
    open(os.path.join(IMG, fn), 'w', encoding='utf-8').write(lab.draw(panels, arrows, bottom))
    h = t.find('##### ' + key + ' ')
    if h == -1:
        print('NO', key); continue
    nxt = t.find('\n#####', h + 5)
    seg_end = nxt if nxt != -1 else len(t)
    s = t.find('[[SOL', h, seg_end)
    if s != -1:
        pos = t.index(']]', s) + 2
    else:
        d = t.find('</div>', h, seg_end)
        if d == -1:
            print('NOPOS', key); continue
        pos = d + 6
    ins = f'\n\n**Lo que pasa en el laboratorio:**\n\n[[IMG img/{fn} 100%]]\n'
    t = t[:pos] + ins + t[pos:]
    n += 1
open('t7_full.md', 'w', encoding='utf-8').write(t)
print('dibujos insertados:', n)
