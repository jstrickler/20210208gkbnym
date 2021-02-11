
color = "blue"

def bark():
    print("Woof woof")

g = globals()
print(g["color"])
print(g)
b = g['bark']
b()
globals()['bark']()

g['animal'] = 'wombat'
print(animal)

g['hello'] = lambda : print("Hello, world")
hello()

# def hello():
#     print("Hello, world")

