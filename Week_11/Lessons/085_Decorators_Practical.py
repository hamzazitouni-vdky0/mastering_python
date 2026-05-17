# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time

def myDecorator(func):  # Decorator

    def nestedFunc(*numbers):  # Any name its just for decoration

        for number in numbers:

            if number < 0:

                print("Beware one of the numbers is less than zero.")

        func(*numbers)  # Execute function

    return nestedFunc  # Return all data


@myDecorator
def calc(n1, n2, n3, n4):

    print(n1 + n2 + n3 + n4)

calc(-5, 90, 50, 130)


def speedTest(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(f"Function running time is: {end - start}")
    
    return wrapper

@speedTest
def bigLoop():

    for number in range(1, 20000):

        print(number)

bigLoop()

