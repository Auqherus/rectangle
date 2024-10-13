class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

def main():
    rectangle = Rectangle(5, 3)
    square = Square(4)
    print(f"Rectangle length: {rectangle.length}, Rectangle width:  {rectangle.width}")
    print(f"Rectangle area: {rectangle.get_area()}")
    print(f"Rectangle perimeter: {rectangle.get_perimeter()}\n")

    print(f"Square length: {square.length}, Square width: {square.width}")
    print(f"Square area: {square.get_area()}")
    print(f"Square perimeter: {square.get_perimeter()}")

main()