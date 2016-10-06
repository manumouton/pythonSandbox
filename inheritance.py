class Parent():
    def __init__(self, name=None, eyes_color=None):
        self.name = name
        self.eyes_color = eyes_color

class Child(Parent):
    def __init__(self, name=None, eyes_color=None, size):
        Parent.__init__(name, eyes_color)
        self.size = size