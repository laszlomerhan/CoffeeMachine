class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}!"


hello = Person(input())
print(hello.greet())
