'''Tic Tac Toe

Exercises

1. Change size and color of "X", "O" and center them.
2. Validate if box is already occupied
'''

from turtle import up
from turtle import goto
from turtle import down
from turtle import circle
from turtle import update
from turtle import setup
from turtle import hideturtle
from turtle import tracer
from turtle import onscreenclick
from turtle import done
from turtle import color

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
    
    # Change color to blue
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
    
    position = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    pos = 0

    if position == [-146.3, 119.7]:
        pos = {0:1}
    elif position == [-13.3, 119.7]:
        pos = {1:1}
    elif position == [119.7, 119.7]:
        pos = {2:1}
    elif position == [-146.3, -13.3]:
        pos = {3:1}
    elif position == [-13.3, -13.3]:
        pos = {4:1}
    elif position == [119.7, -13.3]:
        pos = {5:1}
    elif position == [-146.3, -146.3]:
        pos = {6:1}
    elif position == [-13.3, -146.3]:
        pos = {7:1}
    elif position == [119.7, -146.3]:
        pos = {8:1}

    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player
    
    if position[pos] == 0:

        position[pos] = 1

    print(position)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()