
class Cat():
    def speak(self):
        print("Meow")

c1 = Cat()
c2 = Cat()
c1.speak()

class_name = "Dog"
speak_function = lambda self: print("Woof! Woof!")
Dog = type(class_name, (), {'speak': speak_function})
d1 = Dog()
d1.speak()
