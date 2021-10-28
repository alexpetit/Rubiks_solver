from animator.main import display_solution
from acquis import *

"""R = (1, 0, 0)
G = (0, 1, 0)
O = (1, 0.5, 0)
Y = (1, 1, 0)
W = (1, 1, 1)
B = (0, 0, 1)"""

#cube = 'RFBDUBRLRFRDDRLRLFDDUBFFDRDLUBBDFUUUURFLLDBUFLRBUBBLFL'
# Back, Left, Front, Right, Up, Down
#colors = (O, Y, R, W, G, B)
cube, dict_conv = acquistion()
dic={"blue":(0, 0, 1),"white":(1, 1, 1),"yellow":(1, 1, 0),"orange":(1, 0.5, 0),"green":(0, 1, 0),"red":(1, 0, 0)}
dict_conv_inv={v:k for k,v in dict_conv.items()}
res=[]
for  x in ['B','L','F','R','U','D']:
    res.append(dic[dict_conv_inv[x]])

colors = (res[0], res[1], res[2], res[3], res[4], res[5])
print(dict_conv)
print(cube)
display_solution(cube, colors)