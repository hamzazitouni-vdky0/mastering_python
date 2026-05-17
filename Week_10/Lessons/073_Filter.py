# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checkNumber(num):

    return num > 10


myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResultNumbers = filter(checkNumber, myNumbers)

for number in myResultNumbers:

    print(number)

print("#" * 50)

# Example 1


def checkName(name):

    return name.startswith("O")


myNames = ["Hamza", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myResultNames = filter(checkName, myNames)

for person in myResultNames:

    print(person)

print("#" * 50)

# Example 3

# def checkName(name):

#     return name.startswith("O")


myFriends = ["Hamza", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Amir"]

for friend in filter(lambda name: name.startswith("A"), myFriends):

    print(friend)
