from random import randint
import turtle


class Point:
  def __init__(self, x, y):
    print("New: point__init__ ")
    self.x = x
    self.y = y
    print("(", self.x, ",", self.y, ")\n",)

  def falls_in_rectangle(self, rectangle):
    print("Point in rectangle?: ")
    if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
      return True
    else:
      return False



class Rectangle:

  def __init__(self, point1, point2):
    print("New: rectangle__init__ ")
    self.point1 = point1
    self.point2 = point2

    print("Rectangle Coordinates:\n",
          "(", self.point1.x, ",", self.point1.y, ")\n",
          "(", self.point2.x, ",", self.point2.y, ")")

  def area(self):
    return (self.point2.x-self.point1.x) * (self.point2.y - self.point1.y)



class GuiPoint(Point):

  def draw(self, canvas, size=5, color='red'):
    canvas.penup()
    canvas.goto(self.x, self.y)
    canvas.pendown()
    canvas.dot(size, color)



class GuiRectangle(Rectangle):

  def draw(self, canvas):
    canvas.penup()
    canvas.goto(self.point1.x, self.point1.y)
    canvas.pendown()
    canvas.forward(self.point2.x - self.point1.x)
    canvas.left(90)
    canvas.forward(self.point2.y - self.point1.y)
    canvas.left(90)
    canvas.forward(self.point2.x - self.point1.x)
    canvas.left(90)
    canvas.forward(self.point2.y - self.point1.y)




print("Point Game: Guess a coordinate. ")

userPoint = GuiPoint(
    int(input("Guess X: ")),
    int(input("\nGuess Y: "))
    )
userArea = input("Guess area of shape: ")

myturtle = turtle.Turtle()
rectangleX = GuiRectangle(Point(randint(0, 30), randint(0, 30)),
                       Point(randint(0, 30), randint(0, 30)))

print("Your point falls in the square: ", userPoint.falls_in_rectangle(rectangleX))
print("Your guess of area was off by: ", rectangleX.area() - int(userArea))

rectangleX.draw(canvas=myturtle)
userPoint.draw(canvas=myturtle)
turtle.done()
