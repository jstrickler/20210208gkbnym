
def color():
    return "blue"

def animal():
    return "wombat"

def doit(func):
    return func().upper()

x = doit(color)
y = doit(animal)
print(x, y)

def wrapper(func):
    def bar():
        func()
        print("Hello from bar()")
    return bar

def foo():
    print("Hello from foo()")

foo = wrapper(foo)
print(foo)
foo()

@wrapper
def groot():
    print("I am Groot!")
# groot = wrapper(groot)
groot()