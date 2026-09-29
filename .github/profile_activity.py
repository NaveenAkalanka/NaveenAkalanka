"""Build public GitHub activity graphics without external rendering services."""
import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import urllib.request

BG='#090d0a'; EDGE='#33402c'; AMBER='#ffbc57'; GREEN='#a6ed72'; WHITE='#e7ead8'; MUTED='#9aa88b'

def api(path):
    headers={'Accept':'application/vnd.github+json','User-Agent':'profile-activity-renderer','X-GitHub-Api-Version':'2022-11-28'}
    token=os.environ.get('GITHUB_TOKEN')
    if token: headers['Authorization']='Bearer '+token
    with urllib.request.urlopen(urllib.request.Request('https://api.github.com/'+path,headers=headers),timeout=30) as response:
        return json.load(response)

def collect(user):
    assert re.fullmatch(r'[A-Za-z0-9-]+',user), 'Invalid account name'
    account=api('users/'+user); repos=[]
    for page in range(1,11):
        batch=api(f'users/{user}/repos?type=owner&per_page=100&page={page}')
        repos.extend(batch)
        if len(batch)<100:break
    owned=[r for r in repos if not r.get('fork')]
    events=[]
    for page in range(1,4):
        batch=api(f'users/{user}/events/public?per_page=100&page={page}')
        events.extend(batch)
        if len(batch)<100:break
    now=datetime.now(timezone.utc)
    week_start=(now-timedelta(days=now.weekday())).replace(hour=0,minute=0,second=0,microsecond=0)-timedelta(weeks=7)
    weeks=[0]*8
    for e in events:
        date=datetime.fromisoformat(e['created_at'].replace('Z','+00:00'))
        index=(date-week_start).days//7
        if 0<=index<8:weeks[index]+=1
    languages=Counter(r['language'] for r in owned if r.get('language'))
    recent=sorted([r for r in owned if r['name']!=user and not r.get('archived')],key=lambda r:r.get('pushed_at',''),reverse=True)[:3]
    return {'user':user,'updated':now.strftime('%Y-%m-%d %H:%M UTC'),'repos':len(owned),'stars':sum(r.get('stargazers_count',0) for r in owned),'followers':account['followers'],'events_sampled':len(events),'weeks':weeks,'week_labels':[(week_start+timedelta(weeks=i)).strftime('%d %b') for i in range(8)],'languages':dict(languages),'recent':[{'name':r['name'],'pushed':r['pushed_at'][:10]} for r in recent]}

def txt(x,y,s,size=17,color=WHITE,anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-family="monospace">{escape(str(s))}</text>'

def render(data,mobile=False,animate=True):
    w,h=(620,940) if mobile else (1100,535)
    b=f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" fill="{BG}" stroke="{EDGE}"/>'
    b+=txt(26,33,'GITHUB / PUBLIC SIGNAL',16,AMBER)+txt(26,61,'Updated '+data['updated'],12,MUTED)
    for i,(label,key) in enumerate([('OWNED REPOS','repos'),('REPO STARS','stars'),('FOLLOWERS','followers')]):
        x=28+i*(193 if mobile else 355)
        b+=txt(x,118,data[key],38,WHITE)+txt(x,148,label,12,GREEN)
    x,y,cw,ch=40,217,540 if mobile else 590,180
    b+=txt(x,y-26,'PUBLIC EVENTS / 8 WEEKS',16,AMBER)
    maximum=max(max(data['weeks']),1)
    for tick in range(4):
        yy=y+ch-tick*ch/3
        b+=f'<path d="M{x} {yy}h{cw}" stroke="{EDGE}" stroke-dasharray="2 5"/>'
        b+=txt(x-8,yy+4,round(maximum*tick/3),10,MUTED,'end')
    bw=cw/8
    for i,count in enumerate(data['weeks']):
        bh=count/maximum*(ch-15); bx=x+i*bw+8; by=y+ch-bh
        b+=f'<rect class="bar" style="animation-delay:{i*.08}s" x="{bx}" y="{by}" width="{bw-16}" height="{bh}" rx="3" fill="{AMBER if i==7 else GREEN}"/>'
        b+=txt(bx+(bw-16)/2,by-8,count,12,WHITE,'middle')
        b+=txt(bx+(bw-16)/2,y+ch+22,data['week_labels'][i],9,MUTED,'middle')
    b+=txt(x,y+ch+44,f'Latest {data["events_sampled"]} public events sampled; current week is partial.',10,MUTED)
    lx,ly=(28,503) if mobile else (714,191)
    b+=txt(lx,ly,'REPOSITORY LANGUAGES',16,AMBER)
    langs=sorted(data['languages'].items(),key=lambda item:item[1],reverse=True)[:4]
    langtotal=sum(data['languages'].values()) or 1
    for i,(language,count) in enumerate(langs):
        yy=ly+38+i*44; extent=530 if mobile else 330
        b+=txt(lx,yy,language,16,WHITE)+txt(lx+extent,yy,f'{count} repos',12,MUTED,'end')
        b+=f'<rect x="{lx}" y="{yy+10}" width="{extent}" height="5" rx="2" fill="{EDGE}"/><rect class="bar" x="{lx}" y="{yy+10}" width="{extent*count/langtotal:.1f}" height="5" rx="2" fill="{GREEN if i%2==0 else AMBER}"/>'
    b+=txt(lx,ly+48+len(langs)*44,'Primary language per non-fork repository.',10,MUTED)
    ry=795 if mobile else 467
    b+=txt(28,ry,'RECENT PROJECT PUSHES',12,AMBER)
    for i,r in enumerate(data['recent']):
        if mobile:b+=txt(28,ry+29+i*27,r['name'],16,WHITE)+txt(587,ry+29+i*27,r['pushed'],14,GREEN,'end')
        else:b+=txt(28+i*355,ry+29,r['name']+' / '+r['pushed'],13,GREEN)
    b+=txt(28,h-16,'Source: GitHub public API / refreshed by this repository',10,MUTED)
    style='<style>.bar{transform-box:fill-box;transform-origin:bottom;animation:rise 1.4s ease-out both}@keyframes rise{from{transform:scaleY(.05);opacity:.2}to{transform:scaleY(1);opacity:1}}@media(prefers-reduced-motion:reduce){.bar{animation:none}}</style>' if animate else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Public GitHub activity dashboard for {escape(data["user"])}"><title>Public GitHub activity, updated {data["updated"]}</title>{style}{b}</svg>\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--user',default=os.environ.get('GITHUB_REPOSITORY_OWNER','NaveenAkalanka'));p.add_argument('--output',default='dist');p.add_argument('--snapshot')
    args=p.parse_args();data=json.loads(Path(args.snapshot).read_text()) if args.snapshot else collect(args.user)
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    for mobile in [False,True]:
        for animate in [True,False]:
            name='activity'+('-mobile' if mobile else '')+('' if animate else '-still')+'.svg'
            (out/name).write_text(render(data,mobile,animate),encoding='utf-8')
    (out/'activity.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    print('Updated public activity graphics at',data['updated'])

if __name__=='__main__':main()
