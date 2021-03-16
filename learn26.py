class Numbers:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Numbers()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)
point2 = Numbers()
print(point2.x)
