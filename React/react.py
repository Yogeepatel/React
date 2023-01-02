
import time
import turtle
from random import randint

global gameplay
gameplay = False
global p
global playagain
p = True
playagain = False
def playclick(x,y):
    global gameplay
    if x>-89 and x<125 and y>-76 and y<-15:
        gameplay=True


def newclicked(x,y):
    global gameplay
    global playagain
    if x>193 and x<299 and y>-33 and y<-2:
        gameplay=False
        
    elif x>-295 and x<-60 and y<-2 and y>-34:
        playagain=True
def clicked(x,y):
    p=int(x)
    q=int(y)
    global valx
    global valy
    global disappear
    #print(x,y)
    if q>(valx-10) and q<(valx+10) and p>(valy-10) and p<(10+valy):
        #print(x,y)
        disappear=True
        
def postscreen(wn,a):
    wn.reset()
    a.reset()
    a.penup()
    a.hideturtle()
    a.goto(0,100)
    a.write("Your Score is {}".format(score),align="center",font=("calibiri", 30))
    a.goto(-300,-50)
    a.write("Play Again                EXIT",align="left",font=("calibiri", 40))
    wn.update()

def square(a,valy,valx):
    
    a.shape("square")
    a.color("red")
    
    a.penup()
    a.speed(0)
    a.goto(valy,valx)

def game(wn,a,starttime):
    global valx
    global valy
    global disappear
    global gameplay
    global score
    wn.reset()
    
    valx=randint(-240,240)
    valy=randint(-410,410)
    square(a,valy,valx)
    wn.update()
    score=0
    wn.onscreenclick(clicked)
    wn.listen()
    wn.update()
    while (time.time()-starttime<=10.5):
        wn.update()
        wn.listen()
        if disappear==True:
            wn.reset()
            a.reset()
            valx=randint(-240,240)
            valy=randint(-410,410)
            square(a,valy,valx)
            score=score+1
            disappear=False
    



global valx
global valy
global disappear
global score
score =0
disappear=False

wn=turtle.Screen()
wn.title("React")
wn.bgcolor("white")
wn.setup(width=900,height=560)
wn.tracer(0)

a=turtle.Turtle()
a.hideturtle()
a.penup()
a.goto(-200,150)
a.write("Click on red sqaure boxes ",align="left",font=("calibiri", 30))
a.goto(-250,50)
a.write("as much as you can in 10 seconds",align="left",font=("calibiri", 30))
a.goto(-100,-100)
a.write("PLAY",align="left",font=("calibiri", 70))

wn.listen()
while True:
    wn.update()
    wn.onscreenclick(playclick)
    if gameplay==True:
        break
'''if gameplay==True:
    
    starttime=time.time()
    game(wn,a)'''



while gameplay:
    if p == True:
        starttime=time.time()
        game(wn,a,starttime)
        postscreen(wn,a)
        p=False
        playagain = False
    wn.update()
    wn.onscreenclick(newclicked)
    if gameplay==False:
        wn.bye()
    elif playagain == True:
        p=True
wn.mainloop()