import pgzrun
import random

WIDTH = 1200
HEIGHT = 800

vampire = Actor("vampire")
bow = Actor("bow")
bow.pos = (WIDTH-1100, HEIGHT/2)
def draw():
    screen.clear()
    screen.fill("light blue")
    bow.draw()

speed = 5

stakes = []
vampires = []

for x in range (5):
    for y in range (6):
        vampires.append(Actor("vampire"))
        vampires[-1].x = 800+ 50*x
        vampires[-1].y = 100 + 50*y

score = 0
direction = 1
bow.dead = False
bow.countdown = 50

def displayScore():
    screen.draw.text(str(score), (50,30))

def gameOver():
    screen.draw.text ("GAME OVER", (250,300)) 

def on_key_down(key):
    if bow.dead == False:
        if key == keys.SPACE:
            stakes.append(Actor("stake"))
            stakes[-1].y = bow.y
            stakes[-1].x = bow.x - 50

def update():
    global score
    global direction
    moveLeft = False 

    if bow.dead == False:
        if keyboard.up:
            bow.y -= speed
            if bow.y <= 0:
                bow.y = HEIGHT/2

        elif keyboard.down:
            bow.y += speed
            if bow.y >=HEIGHT:
                bow.y = HEIGHT/2

    for stake in stakes:
        if stake.x >=1200 :
            stakes.remove(stake)
        else:
            stake.x +=10

    if len(vampires) == 0:
        gameOver()

    if len(vampires)>0 and (vampires [-1].y > HEIGHT-100 or vampires[0].y <100):
        moveLeft = True
        direction = direction*-1
    for vampire in vampires:
        vampire.y += 5*direction
        if moveLeft == True:
            vampire.x -=100
        if vampire.x < 0 :
            vampires.remove(vampire)

        for stake in stakes :
            if vampire.colliderect(stake):
                score+=100
                stakes.remove(stake)

                vampires.remove(vampire)
                if len(vampires) == 0:
                    gameOver()
        if vampire.colliderect(bow) :
            bow.dead = True
if bow.dead:
    bow.countdown -=1
if bow.countdown == 0:
    bow.dead = False
    bow.countdown = 50

def draw():
    screen.clear()
    screen.fill("light blue")

    for stake in stakes:
        stake.draw()
    for vampire in vampires:
            vampire.draw()
    if bow.dead == False:
      bow.draw()
    displayScore()
    if len (vampires) == 0:
        gameOver()            


pgzrun.go()
