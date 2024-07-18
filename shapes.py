import pgzrun

TITLE="Shapes"
HEIGHT=300
WIDTH=300

def draw():
    screen.fill("white")
    screen.draw.line((50,50), (250,250), (183, 122, 78))
    screen.draw.filled_circle((150,150), 20, (0, 0, 0))
    rect=Rect(0,30,60,90)
    screen.draw.rect(rect, (198, 220, 56))




pgzrun.go()