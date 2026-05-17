# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------


def myDecorator(func):  # Decorator

    def nestedFunc(num1, num2):  # Any name its just for decoration

        if num1 < 0 or num2 < 0:

            print("Beware one of the numbers is less than zero.")

        func(num1, num2)  # Execute function

    return nestedFunc  # Return all data


def myDecoratorTwo(func):  # Decorator

    def nestedFunc(num1, num2):  # Any name its just for decoration

        print("Coming from decorator two.")

        func(num1, num2)  # Execute function

    return nestedFunc  # Return all data


@myDecorator
@myDecoratorTwo
def calc(n1, n2):

    print(n1 + n2)


calc(-5, 90)
