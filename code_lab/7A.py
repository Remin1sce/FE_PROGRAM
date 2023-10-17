class Rectangle:
    def __init__(self, width = 2, height = 1):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return self.width * 2 + self.height * 2
        
        
recA = Rectangle()
recB = Rectangle(int(input()), int(input()))
print(recA.getArea())
print(recA.getPerimeter())
print(recB.getArea())
print(recB.getPerimeter())