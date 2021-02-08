#!/usr/bin/env python
"""
This is the doc string for the module/script.
"""
import sys

# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)
MAX_TRIES = 5

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    function1()

def spam():
    """
    This is a silly function
    """
    print("Hello from spam()")


# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    pass

if __name__ == '__main__':  # if script, not module
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
