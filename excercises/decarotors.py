class shape():
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property
    def width(self):
        return f"width-{self._width} cm"
    @property
    def height(self):
        return f"height-{self._height} cm"
    @width.setter
    def width(self,n_width):
        self._width=n_width
    @height.setter
    def height(self,n_height):
        self._height=n_height

    @width.deleter
    def width(self):
        del self._width
        print("width deleted succesfuuly")
    @height.deleter
    def height(self):
        del self._height
        print("height deleted succesfuuly")

rect=shape(3,5)
print(rect.width)
print(rect.height)
rect.width=10
rect.height=20
print(rect.width)
print(rect.height)
del rect.width
del rect.height


