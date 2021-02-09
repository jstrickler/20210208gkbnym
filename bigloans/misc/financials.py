
COLORS = ['red', 'blue', 'green']

def spam():
    """
    Just a silly function
    """
    print("Hello from spam()")


def ham():
    print("Hello from ham()")
    _toast()


def _toast():  # "private", internal
    print("   and _toast()")

print("MY NAME IS", __name__)

if __name__ == '__main__':
    print("Hi Mom!")
    ham()
    spam()
