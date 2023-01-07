class Circle:

    def __init__(self, x, y, radius, width=1, color=None):
        if color is None:
            color = [255, 255, 255]
        self.x = x
        self.y = y
        self.radius = radius
        self.boarder_width = width
        self.color = color
