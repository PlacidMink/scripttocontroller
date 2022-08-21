from graphics import *
import time
def draw(s, c, o):
    s.setFill(c)
    s.setOutline(o)
    return s
def drawStick(p, o):
    stickX = int(p[0])/(32767/25) + o[0]
    stickY = o[1] - int(p[1])/(32767/25)
    stick = Circle(Point(stickX, stickY), 17)
    stick.setFill("orange")
    stick.setOutline("white")
    return stick
def main():
    k = []
    fh = open("script.txt","r")
    for line in fh:
        j = line[0:len(line)-1].split(" ")
        k.append(j[1:len(j)])
    win = GraphWin("Controller", 600, 600,autoflush=False)
    controller = Image(Point(300,300),"controllerFinalTransparent.png")
    controller.draw(win)
    update(60)
    time.sleep(2)
    presses = ['KEY_A','KEY_B','KEY_X','KEY_Y','KEY_ZR','KEY_ZL','KEY_R','KEY_L','KEY_PLUS','KEY_MINUS','KEY_DLEFT','KEY_DRIGHT','KEY_DUP','KEY_DDOWN','KEY_LSTICK','KEY_RSTICK','NONE']
    a = draw(Circle(Point(460, 235), 16), "orange", "white")
    b = draw(Circle(Point(423, 267), 16), "orange", "white")
    x = draw(Circle(Point(423, 204), 16), "orange", "white")
    y = draw(Circle(Point(386, 235), 16), "orange", "white")
    zr = draw(Polygon(Point(381, 96), Point(386, 92), Point(468, 92), Point(473, 96), Point(473, 120), Point(468, 124), Point(386, 124), Point(381, 120)), "orange", "white")
    zl = draw(Polygon(Point(126, 96), Point(131, 92), Point(212, 92), Point(217, 96), Point(217, 120), Point(212, 124), Point(131, 124), Point(126, 120)), "orange", "white")
    r = draw(Polygon(Point(369, 147), Point(390, 136), Point(405, 136), Point(439, 142), Point(455, 148), Point(471, 159), Point(480, 174), Point(458, 163), Point(439, 155), Point(420, 150)), "orange", "white")
    l = draw(Polygon(Point(227, 147), Point(206, 136), Point(191, 136), Point(157, 142), Point(141, 148), Point(125, 159), Point(116, 174), Point(138, 163), Point(157, 155), Point(176, 150)), "orange", "white")
    plus = draw(Circle(Point(356, 200), 10), "orange", "white")
    minus = draw(Circle(Point(240, 200), 10), "orange", "white")
    l3 = draw(Polygon(Point(192, 380), Point(196, 375), Point(271, 375), Point(275, 379), Point(275, 404), Point(271, 408), Point(196, 408), Point(192, 404)), "orange", "white")
    r3 = draw(Polygon(Point(322, 380), Point(326, 375), Point(401, 375), Point(405, 380), Point(405, 404), Point(401, 408), Point(326, 408), Point(322, 404)), "orange", "white")
    buttons = [a, b, x, y, zr, zl, r, l, plus, minus, draw(Circle(Point(300,300),0), "black", "black"), draw(Circle(Point(300,300),0), "black", "black"), draw(Circle(Point(300,300),0), "black", "black"), draw(Circle(Point(300,300),0), "black", "black"), l3, r3,draw(Circle(Point(300,300),0), "black", "black")]
    update(1)
    lstick = drawStick([0,0], [169,235])
    rstick = drawStick([0,0], [361,300])
    d = 0
    for i in range(len(k)):
        lstick.undraw()
        rstick.undraw()
        keys = k[i][0].split(";")
        lStickPos = k[i][1].split(";")
        rStickPos = k[i][2].split(";")
        lstick = drawStick(lStickPos, [169, 235])
        lstick.draw(win)
        rstick = drawStick(rStickPos, [361, 300])
        rstick.draw(win)
        for p in buttons:
            p.undraw()
        for m in keys:
            if m == presses[7] and keys.index(m) < len(keys)-1 and presses.index(keys[keys.index(m)+1]) >=10 and presses.index(keys[keys.index(m)+1]) <=13:
                d = 1
                continue
            buttons[presses.index(m)].draw(win)
        update(60)
main()
