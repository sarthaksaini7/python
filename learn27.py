class Numbers:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point = Numbers(20, 30)
point.x = 11
print(point.x)
