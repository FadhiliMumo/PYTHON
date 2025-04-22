class Animal:
    def move(self):
        return "The animal moves in its own way."

class Bird(Animal):
    def move(self):
        return "Flying in the sky 🐦."

class Fish(Animal):
    def move(self):
        return "Swimming in the water 🐟."


if __name__ == "__main__":
    bird = Bird()
    fish = Fish()

    for obj in [bird, fish]:
        print(obj.move())