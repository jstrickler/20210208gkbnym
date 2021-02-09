def hello():
    print("Hello, BNYM world")
    # return None if no 'return' statement

def square(x):
    return x ** 2

hello()
result = square(5)
print(result)

m = hello()
print(m)

#          positional|named
#         req     opt  req     opt
def wacky(p1, p2, *p3, p4, p5, **p6):
    """
    This function frobnicates the regurgitator.
    Blah blah blah

    :param p1: number of widgets
    :param p2: darlek value
    :param p3: some fruits
    :param p4: the wozzniator
    :param p5: frufel coordinate
    :param p6: other stuff
    :return:
    """
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)
    print("-" * 20)

wacky("a", "b", p4=10, p5=20)
wacky("a", "b", "c", "d", "e", p4=10, p5=20)
wacky("a", "b", "c", "d", "e", p4=10, p5=20, animal="wombat", value=40)

def doit(*, animal, file_name="generic.txt"):
    print(animal, file_name)

doit(animal='wombat', file_name='animals.txt')
doit(animal="pine marten")

def spam(x, y):
    return x ** y

print(spam(2, 32))
print(spam(x=2,y=32))
print(spam(y=32, x=2))

