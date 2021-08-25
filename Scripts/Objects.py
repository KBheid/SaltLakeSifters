import pygame

class Object:
    def __init__(self):
        pass

class Renderable(Object):
    def __init__(self):
        Object.__init__()

class Nonrenderable(Object):
    def __init__(self):
        Object.__init__()