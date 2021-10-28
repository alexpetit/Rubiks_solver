#from animator.main import display_solution
from acquis import *

R = (1, 0, 0)
G = (0, 1, 0)
O = (1, 0.5, 0)
Y = (1, 1, 0)
W = (1, 1, 1)
B = (0, 0, 1)

cube = 'RFBDUBRLRFRDDRLRLFDDUBFFDRDLUBBDFUUUURFLLDBUFLRBUBBLFL'
# Back, Left, Front, Right, Up, Down
colors = (O, Y, R, W, G, B)
cube, dict_conv = acquistion()

print(dict_conv)
print(cube)
#display_solution(cube, colors)