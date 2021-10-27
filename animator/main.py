import tkinter

import pygame
import random
from pygame.locals import *
from tkinter import *
import random


def monkeypatch_ctypes():
    import os
    import ctypes.util
    uname = os.uname()
    if uname.sysname == "Darwin" and uname.release >= "20.":
        real_find_library = ctypes.util.find_library
        def find_library(name):
            if name in {"OpenGL", "GLUT"}:  # add more names here if necessary
                return f"/System/Library/Frameworks/{name}.framework/{name}"
            return real_find_library(name)
        ctypes.util.find_library = find_library
    return \

monkeypatch_ctypes()

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1), (-1, -1, -1),
    ( 1, -1,  1), ( 1,  1,  1), (-1, -1,  1), (-1,  1,  1)
)
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))
#colors = ((1, 0, 0), (0, 1, 0), (1, 0.5, 0), (1, 1, 0), (1, 1, 1), (0, 0, 1))
color_run = ((1,0.5,0),(1,1,1),(0,0,1),(1,0,0),(1,1,0),(0,1,0))
R = (1, 0, 0)
G = (0, 1, 0)
O = (1, 0.5, 0)
Y = (1, 1, 0)
W = (1, 1, 1)
B = (0, 0, 1)
colors = (R, G, O, Y, W, B,
        )
colors2 = (B,B,B,B,B,B)
class Cube():
    def __init__(self, id, N, scale):
        self.N = N
        self.scale = scale
        self.init_i = [*id]
        self.current_i = [*id]
        self.rot = [[1 if i==j else 0 for i in range(3)] for j in range(3)]

    def isAffected(self, axis, slice, dir):
        return self.current_i[axis] == slice

    def update(self, axis, slice, dir):

        if not self.isAffected(axis, slice, dir):
            return

        i, j = (axis+1) % 3, (axis+2) % 3
        for k in range(3):
            self.rot[k][i], self.rot[k][j] = -self.rot[k][j]*dir, self.rot[k][i]*dir

        self.current_i[i], self.current_i[j] = (
            self.current_i[j] if dir < 0 else self.N - 1 - self.current_i[j],
            self.current_i[i] if dir > 0 else self.N - 1 - self.current_i[i] )

    def transformMat(self):
        scaleA = [[s*self.scale for s in a] for a in self.rot]
        scaleT = [(p-(self.N-1)/2)*2.1*self.scale for p in self.current_i]
        return [*scaleA[0], 0, *scaleA[1], 0, *scaleA[2], 0, *scaleT, 1]

    def draw(self, col, surf, vert, animate, angle, axis, slice, dir):

        glPushMatrix()
        if animate and self.isAffected(axis, slice, dir):
            glRotatef( angle*dir, *[1 if i==axis else 0 for i in range(3)] )
        glMultMatrixf( self.transformMat() )

        glBegin(GL_QUADS)
        for i in range(len(surf)):
            glColor3fv(col[i])
            for j in surf[i]:
                glVertex3fv(vert[j])
        glEnd()
        glPopMatrix()

class EntireCube():
    def __init__(self, N, scale):
        self.N = N
        cr = range(self.N)
        self.cubes = [Cube((x, y, z), self.N, scale) for x in cr for y in cr for z in cr]
        self.cubes[0].update(1, 0, 1)
        self.cubes[0].transformMat()
    def mainloop(self):

        rot_cube_map  = { K_UP: (-1, 0), K_DOWN: (1, 0), K_LEFT: (0, -1), K_RIGHT: (0, 1)}
        rot_slice_map = {
            K_1: (0, 0, 1), K_2: (0, 1, 1), K_3: (0, 2, 1), K_4: (1, 0, 1), K_5: (1, 1, 1),
            K_6: (1, 2, 1), K_7: (2, 0, 1), K_8: (2, 1, 1), K_9: (2, 2, 1),
            K_F1: (0, 0, -1), K_F2: (0, 1, -1), K_F3: (0, 2, -1), K_F4: (1, 0, -1), K_F5: (1, 1, -1),
            K_F6: (1, 2, -1), K_F7: (2, 0, -1), K_F8: (2, 1, -1), K_F9: (2, 2, -1),
        }

        ang_x, ang_y, rot_cube = 0, 0, (0, 0)
        animate, animate_ang, animate_speed = False, 0, 10
        action = (0, 0, 0)
        color = (60, 60, 60)
        #width = screen.get_width()
        #height = screen.get_height()
        # defining a font
        smallfont = pygame.font.SysFont('Corbel', 35)
        # rendering a text written in
        # this font
        text = smallfont.render('quit', True, color)
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        #pygame.display.set_caption("tape tape")
        #pygame.display.blit(text, (450 / 2 + 50, 450 / 2))
        while True:
            # ici faire une boucle avec les données récupérer par kocimba
            for ev in pygame.event.get():

                if ev .type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # checks if a mouse is clicked
                """if ev.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button the game is terminated
                    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                        pygame.quit()"""



                if ev.type == KEYDOWN:
                    if ev.key == pygame.K_RETURN :
                        print("la")
                        animate,action = True,rot_slice_map[49]
                        print(ev.key)
                    if ev.key in rot_cube_map:
                        rot_cube = rot_cube_map[ev.key]
                    if not animate and ev.key in rot_slice_map:
                        animate, action = True, rot_slice_map[ev.key]
                        print(ev.key)
                if ev.type == KEYUP:
                    if ev.key in rot_cube_map:
                        rot_cube = (0, 0)
            # superimposing the text onto our button
            #screen.blit(text, (width / 2 + 50, height / 2))

            # updates the frames of the game

            ang_x += rot_cube[0]*2
            ang_y += rot_cube[1]*2

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glTranslatef(0, 0, -40)
            glRotatef(ang_y, 0, 1, 0)
            glRotatef(ang_x, 1, 0, 0)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            if animate:
                if animate_ang >= 90:
                    for cube in self.cubes:
                        cube.update(*action)
                    animate, animate_ang = False, 0

            for cube in self.cubes:
               cube.draw(colors, surfaces, vertices, animate, animate_ang, *action)

            if animate:
                animate_ang += animate_speed

            #self.cubes[0].draw(colors2, surfaces, vertices, animate, animate_ang, *action)
            pygame.display.flip()
            pygame.time.wait(10)

def main():

    #top = tkinter.Tk()
    pygame.init()
    display = (800,600)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('quit', True, (60,60,60))
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    pygame.display.set_caption("tape tape")
    screen.blit(text, (450 / 2 + 50, 450 / 2))
    #button(screen)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    NewEntireCube = EntireCube(3, 1.5)
    NewEntireCube.mainloop()

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()