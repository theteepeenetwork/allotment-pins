import json
import sys, os
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(REPO,'assets','sheets')
pins = json.load(open(sys.argv[1]))  # list of [slug, title, subtitle, [sheet names]]
H = '''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Marcellus&display=swap" rel="stylesheet">
<style>body{margin:0}*{box-sizing:border-box}</style></head><body>
<div style="width:1000px;height:1500px;position:relative;overflow:hidden;background:#F3EEE2;font-family:Marcellus,Georgia,serif;color:#2F2B26">
<div style="position:absolute;inset:24px;border:1.5px solid #A8B190"></div>
<div style="position:absolute;left:0;right:0;top:74px;text-align:center">
<div style="font-size:22px;letter-spacing:.34em;color:#5E574A">THE ALLOTMENT PLANNER</div>
<h1 style="margin:22px 0 0;font-weight:400;font-size:{fs}px;line-height:1.04;letter-spacing:.05em;white-space:pre-line">{title}</h1>
<div style="display:flex;justify-content:center;align-items:center;gap:14px;margin:24px 0 18px"><span style="width:70px;height:1.5px;background:#5E574A"></span><span style="width:9px;height:9px;background:#A8B190;transform:rotate(45deg)"></span><span style="width:70px;height:1.5px;background:#5E574A"></span></div>
<div style="font-size:27px;letter-spacing:.02em;color:#3A3630">{sub}</div></div>
{sheets}
<div style="position:absolute;left:24px;right:24px;bottom:24px;height:104px;background:#C3C9A5;border-top:1.5px solid #5E574A;display:flex;align-items:center;justify-content:center;font-size:24px;letter-spacing:.14em;color:#2F2B26">PRINTABLE PDF · A4 &amp; US LETTER · INSTANT DOWNLOAD</div>
</div></body></html>'''
def sheets(names):
    n=len(names); h=900 if n==1 else 790; w=round(h*794/1123); out=''
    top=440 if n==1 else 470
    for i,s in enumerate(names):
        if n==1: x=(1000-w)//2; rot=0
        else:
            x=(1000-w)//2 + (i-(n-1)/2)*105; rot=(i-(n-1)/2)*5
        out+=(f'<img src="file://{OUT}/{s}.jpg" style="position:absolute;left:{x:.0f}px;top:{top}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);transform-origin:50% 100%;'
              f'box-shadow:0 20px 44px rgba(60,50,35,.25),0 3px 8px rgba(60,50,35,.15)">')
    return out
for slug,title,sub,names in pins:
    fs = 78 if max(len(l) for l in title.split('\n'))<=14 else 66
    open(os.path.join(sys.argv[2], slug + '.html'),'w').write(H.replace('{fs}',str(fs)).replace('{title}',title).replace('{sub}',sub).replace('{sheets}',sheets(names)))
json.dump([p[0] for p in pins],open(os.path.join(sys.argv[2],'list.json'),'w'))
