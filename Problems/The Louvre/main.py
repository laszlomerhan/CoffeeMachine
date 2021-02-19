class Painting:

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


paint = Painting(input(), input(), input())
