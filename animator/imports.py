import tkinter
import pygame
import random
from pygame.locals import *
from tkinter import *
import random
from test import give_key

# function that allows to run OpenGL on MacOS
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
    return


monkeypatch_ctypes()

from OpenGL.GL import *
from OpenGL.GLU import *