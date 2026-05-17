# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------


def myDecorator(func):  # Decorator

    def nestedFunc():  # Any name its just for decoration

        print("Before")  # Message from decorator

        func()  # Execute function

        print("After")  # Message from decorator

    return nestedFunc  # Return all data

@myDecorator
def sayHello():

    print("Hello from sayHello function")


@myDecorator
def sayHowAreYou():

    print("Hello from sayHowAreYou function")


sayHello()

print("#" * 50)

sayHowAreYou()
# afterDecoration = myDecorator(sayHello)

# afterDecoration()
