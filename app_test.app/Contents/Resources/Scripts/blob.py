from Tkinter import *
from random import randint as r
from random import choice

tk=Tk()
ca=Canvas(tk,width=500,height=500)
ca.pack()

loop=500   #Duration
spr=1      #how far a point can move from prev. location
add=1      #By what spr will increase
lvl=50     #1 in lvl chance that spr will increase
max=6      #max spr
colors=['green','purple','red','blue','black']

#14 points \/
blob=ca.create_polygon(250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,fill='white',outline=choice(colors))

dsp=ca.create_text(50,10,text='spr: '+str(spr),fill='green')
for x in range(0,loop):
       y=ca.coords(blob)
       ca.coords(blob,y[0]+r(spr*-1,spr),y[1]+r(spr*-1,spr),y[2]+r(spr*-1,spr),y[3]+r(spr*-1,spr),y[4]+r(spr*-1,spr),y[5]+r(spr*-1,spr),y[6]+r(spr*-1,spr),y[7]+r(spr*-1,spr),y[8]+r(spr*-1,spr),y[9]+r(spr*-1,spr),y[10]+r(spr*-1,spr),y[11]+r(spr*-1,spr),y[12]+r(spr*-1,spr),y[13]+r(spr*-1,spr),y[14]+r(spr*-1,spr),y[15]+r(spr*-1,spr),y[16]+r(spr*-1,spr),y[17]+r(spr*-1,spr),y[18]+r(spr*-1,spr),y[19]+r(spr*-1,spr),y[20]+r(spr*-1,spr),y[21]+r(spr*-1,spr),y[22]+r(spr*-1,spr),y[23]+r(spr*-1,spr),y[24]+r(spr*-1,spr),y[25]+r(spr*-1,spr),y[26]+r(spr*-1,spr),y[27]+r(spr*-1,spr))
       
       ca.itemconfig(dsp,text='spr: '+str(spr))
       ca.update()
       if r(0,lvl)==0:
              spr=spr+add
              if spr > max:
                     spr=max
