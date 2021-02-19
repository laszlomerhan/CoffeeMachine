class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = int(radius)
        self.volume = 4 / 3 * (self.PI * (self.radius ** 3))
