import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
plt.rcParams["font.family"]=["IPAGothic"]
from PIL import Image, ImageOps, ImageEnhance
import sys
OUT="img/"
# logo grayscale
im=Image.open(sys.argv[1]).convert("RGBA")
bg=Image.new("RGBA",im.size,"white"); bg.alpha_composite(im)
g=ImageOps.grayscale(bg.convert("RGB"))
g=ImageEnhance.Contrast(g).enhance(1.6)
g.save(OUT+"logo_gray.png")

def grid(ax,lim=6,labels=True,step=1):
    ax.set_xlim(-lim-0.6,lim+0.9); ax.set_ylim(-lim-0.6,lim+0.9)
    for v in range(-lim,lim+1):
        ax.plot([v,v],[-lim,lim],color="#b0b0b0",lw=0.6,zorder=0)
        ax.plot([-lim,lim],[v,v],color="#b0b0b0",lw=0.6,zorder=0)
    ax.annotate("",xy=(lim+0.8,0),xytext=(-lim-0.4,0),arrowprops=dict(arrowstyle="-|>",color="k",lw=1.1))
    ax.annotate("",xy=(0,lim+0.8),xytext=(0,-lim-0.4),arrowprops=dict(arrowstyle="-|>",color="k",lw=1.1))
    ax.text(lim+0.75,-0.55,"x",fontsize=13,style="italic",family="serif")
    ax.text(0.2,lim+0.55,"y",fontsize=13,style="italic",family="serif")
    ax.text(-0.55,-0.6,"O",fontsize=11,family="serif")
    if labels:
        for v in (-5,5):
            ax.text(v-0.2,-0.65,str(v),fontsize=10,family="serif")
            ax.text(-0.75 if v>0 else -0.95,v-0.2,str(v),fontsize=10,family="serif")
    ax.set_aspect("equal"); ax.axis("off")

def line(ax,a,b,lim=6,lab=None,pos=None,**kw):
    xs=np.linspace(-lim,lim,400); ys=a*xs+b
    m=(ys>=-lim)&(ys<=lim)
    ax.plot(xs[m],ys[m],color="k",lw=kw.get("lw",1.6),ls=kw.get("ls","-"))
    if lab: ax.text(pos[0],pos[1],lab,fontsize=13)

def save(fig,name):
    fig.savefig(OUT+name,dpi=200,bbox_inches="tight",pad_inches=0.05); plt.close(fig)

# blank grid
fig,ax=plt.subplots(figsize=(3.2,3.2)); grid(ax); save(fig,"grid_blank.png")
# kihon: read 2 lines  (1) y=2x-3  (2) y=-x/2+2
fig,ax=plt.subplots(figsize=(3.2,3.2)); grid(ax)
line(ax,2,-3,lab="①",pos=(4.3,5.9)); line(ax,-0.5,2,lab="②",pos=(-6.6,5.3)); save(fig,"j1_read.png")
# ouyo A: triangle  l:y=2x+4  m:y=-x+7  (lim 8)
def tri(name,l,m,A,B,C,labs,shade=None,extra=None,lim=8,ticks=()):
    fig,ax=plt.subplots(figsize=(3.4,3.0))
    ax.set_xlim(-lim+3.5,lim+1); ax.set_ylim(-1.5,lim)
    ax.annotate("",xy=(lim+0.8,0),xytext=(-lim+3.6,0),arrowprops=dict(arrowstyle="-|>",color="k",lw=1.1))
    ax.annotate("",xy=(0,lim-0.2),xytext=(0,-1.4),arrowprops=dict(arrowstyle="-|>",color="k",lw=1.1))
    ax.text(lim+0.6,-0.8,"x",fontsize=13,style="italic",family="serif");ax.text(0.25,lim-0.6,"y",fontsize=13,style="italic",family="serif")
    ax.text(-0.6,-0.8,"O",fontsize=11,family="serif")
    if shade: ax.add_patch(Polygon(shade,closed=True,color="#cfcfcf",zorder=0))
    for (a,b,lab,lp) in (l,m):
        xs=np.linspace(-lim+3.5,lim+1,300); ys=a*xs+b; k=(ys>=-1.3)&(ys<=lim-0.5)
        ax.plot(xs[k],ys[k],color="k",lw=1.5); ax.text(lp[0],lp[1],lab,fontsize=13,style="italic",family=("IPAGothic" if "ℓ" in lab else "serif"))
    for p,s,o in ((A,labs[0],(0.2,0.25)),(B,labs[1],(-0.3,-0.9)),(C,labs[2],(0,-0.9))):
        ax.plot(*p,"ko",ms=3); ax.text(p[0]+o[0],p[1]+o[1],s,fontsize=12,family="serif")
    if extra: extra(ax)
    ax.set_aspect("equal"); ax.axis("off"); save(fig,name)
tri("o1_tri.png",(2,4,"ℓ ",(-2.4,2.2)),(-1,7,"m",(5.3,2.5)),(1,6),(-2,0),(7,0),("A","B","C"))
# homework graph read: (1) y=-2x+3 (2) y=x/2-2
fig,ax=plt.subplots(figsize=(3.2,3.2)); grid(ax)
line(ax,-2,3,lab="①",pos=(-2.0,6.1)); line(ax,0.5,-2,lab="②",pos=(6.1,1.0)); save(fig,"h_read.png")
# homework triangle: l:y=-x+6, m:y=x/2+3 A(2,4) B(-6,0) C(6,0)
def tri2(name,shade=None,extra=None):
    fig,ax=plt.subplots(figsize=(3.6,2.6))
    ax.set_xlim(-8,8.5); ax.set_ylim(-1.5,7.5)
    ax.annotate("",xy=(8.3,0),xytext=(-7.8,0),arrowprops=dict(arrowstyle="-|>",color="k",lw=1.1))
    ax.annotate("",xy=(0,7.3),xytext=(0,-1.4),arrowprops=dict(arrowstyle="-|>",color="k",lw=1.1))
    ax.text(8.0,-0.9,"x",fontsize=13,style="italic",family="serif");ax.text(0.25,6.9,"y",fontsize=13,style="italic",family="serif")
    ax.text(-0.7,-0.9,"O",fontsize=11,family="serif")
    if shade: ax.add_patch(Polygon(shade,closed=True,color="#cfcfcf",zorder=0))
    xs=np.linspace(-1.2,7.5,100); ax.plot(xs,-xs+6,"k",lw=1.5); ax.text(-1.6,6.8,"ℓ",fontsize=13,style="italic")
    xs=np.linspace(-7.5,7,100); ax.plot(xs,xs/2+3,"k",lw=1.5); ax.text(6.4,6.0,"m",fontsize=13,style="italic",family="serif")
    for p,s,o in (((2,4),"A",(0.1,0.35)),((-6,0),"B",(-0.3,-0.9)),((6,0),"C",(0,-0.9))):
        ax.plot(*p,"ko",ms=3); ax.text(p[0]+o[0],p[1]+o[1],s,fontsize=12,family="serif")
    if extra: extra(ax)
    ax.set_aspect("equal"); ax.axis("off"); save(fig,name)
tri2("h_tri.png")

# ===== answer/explanation figures =====
def ex1(ax):
    ax.plot([1,1],[0,6],"k--",lw=1); ax.text(1.15,2.6,"高さ6",fontsize=9,family="IPAGothic")
    ax.text(2.0,-1.35,"底辺 9",fontsize=9,family="IPAGothic")
    ax.plot(2.5,0,"ks",ms=3); ax.text(2.2,0.3,"M",fontsize=10,family="serif")
    xs=np.linspace(0.6,2.8,10); ax.plot(xs,-4*xs+10,"k",lw=1.2,ls="-.")
    ax.plot(4,3,"ks",ms=3); ax.text(4.2,3.1,"N",fontsize=10,family="serif")
    xs=np.linspace(-2.5,5,10); ax.plot(xs,xs/2+1,"k",lw=1.2,ls=":")
tri("o1_tri_ans.png",(2,4,"ℓ ",(-2.4,2.2)),(-1,7,"m",(5.3,2.5)),(1,6),(-2,0),(7,0),("A","B","C"),shade=[(1,6),(-2,0),(7,0)],extra=ex1)
def ex2(ax):
    ax.plot([2,2],[0,4],"k--",lw=1)
    ax.plot(0,0,"ks",ms=3)
    xs=np.linspace(-0.6,2.6,10); ax.plot(xs,2*xs,"k",lw=1.2,ls="-.")
    ax.plot(-2,2,"ks",ms=3); ax.text(-2.6,2.4,"N",fontsize=10,family="serif")
    xs=np.linspace(-3,7,10); ax.plot(xs,-xs/4+1.5,"k",lw=1.2,ls=":")
tri2("h_tri_ans.png",shade=[(2,4),(-6,0),(6,0)],extra=ex2)
# graph answers
fig,ax=plt.subplots(figsize=(3.2,3.2)); grid(ax)
line(ax,-2/3,2,lab="①",pos=(-6.5,5.6)); line(ax,2,-3,lab="②",pos=(4.2,5.9))
for p in [(0,2),(3,0),(0,-3),(1,-1)]: ax.plot(*p,"ko",ms=3.5)
save(fig,"o_graph_ans.png")
fig,ax=plt.subplots(figsize=(3.2,3.2)); grid(ax)
line(ax,0.75,-2,lab="①",pos=(5.0,2.4)); line(ax,-0.5,2,lab="②",pos=(-6.6,5.3)); line(ax,0,-3,lab="③",pos=(6.2,-3.3))
for p in [(0,-2),(4,1),(0,2),(4,0)]: ax.plot(*p,"ko",ms=3.5)
# slope steps for (1)
ax.plot([0,4],[-2,-2],"k:",lw=1.3); ax.plot([4,4],[-2,1],"k:",lw=1.3)
ax.text(1.5,-2.75,"右へ4",fontsize=8,family="IPAGothic"); ax.text(4.25,-1.75,"上へ3",fontsize=8,family="IPAGothic")
save(fig,"h_graph_ans.png")
# speed line diagram (homework 6(3))
fig,ax=plt.subplots(figsize=(5.2,1.3))
ax.plot([0,10],[0,0],"k",lw=1.6)
for x in (0,7.5,10): ax.plot([x,x],[-0.15,0.15],"k",lw=1.4)
ax.text(-0.3,-0.55,"家",fontsize=10,family="IPAGothic"); ax.text(9.6,-0.55,"公園",fontsize=10,family="IPAGothic")
ax.annotate("",xy=(0,0.55),xytext=(7.5,0.55),arrowprops=dict(arrowstyle="<->",lw=1))
ax.annotate("",xy=(7.5,0.55),xytext=(10,0.55),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(2.0,0.7,"自転車　時速12km　x km",fontsize=9,family="IPAGothic")
ax.text(7.6,0.7,"歩き 時速4km y km",fontsize=8,family="IPAGothic")
ax.annotate("",xy=(0,-0.85),xytext=(10,-0.85),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(3.6,-1.3,"全部で14km　／　1時間30分",fontsize=9,family="IPAGothic")
ax.set_xlim(-0.8,10.8); ax.set_ylim(-1.5,1.1); ax.axis("off"); save(fig,"h_speed.png")
