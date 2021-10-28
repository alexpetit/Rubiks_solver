from animator.main import display_solution

R = (1, 0, 0)
G = (0, 1, 0)
O = (1, 0.5, 0)
Y = (1, 1, 0)
W = (1, 1, 1)
B = (0, 0, 1)

cube = 'RFBDUBRLRFRDDRLRLFDDUBFFDRDLUBBDFUUUURFLLDBUFLRBUBBLFL'
# Back, Left, Front, Right, Up, Down
colors = (O, Y, R, W, G, B)
display_solution(cube, colors)