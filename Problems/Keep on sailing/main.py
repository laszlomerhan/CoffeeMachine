# our class Ship
class Ship:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    # the old sail method that you need to rewrite
    def sail(self):
        return "The {} has sailed for {}!".format(self.name, self.destination)


black_pearl = Ship("Black Pearl", input())
print(black_pearl.sail())
