'''Tic Tac Toe

Exercises

1. Change size and color of "X", "O" and center them.
2. Validate if box is already occupied
'''

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
   
    color('red')
   
    line(x, y, x + 13.3, y + 13.3)
    line(x, y + 13.3, x + 13.3, y)


def drawo(x, y):
    """Draw O player."""
    
    color('blue')
    
    up()
    goto(x + 6.7, y + 0.5)
    down()
    circle(6.2)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 13.3) // 133) * 133 - 13.3


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()