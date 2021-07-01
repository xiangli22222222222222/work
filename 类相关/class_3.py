class Parent:
    classAttr = 100

    def __init__(self, x):
        self.x = x + Parent.classAttr


X = Parent(2)
print
X.x