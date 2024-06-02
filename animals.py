class Animal:
    def move (self):
        pass
    def make_sound(self):
        pass
class Bird(Animal):
    def move(self):
        print("flying")
    def make_sound(self):
        print("chirp")
class Cat(Animal):
    def move(self):
        print("Running")
    def make_sound(self):
        print("meow")
class fish (Animal):
    def move(self):
        print("Swimming")
    def make_sound(self):
        print("Bop")
        
