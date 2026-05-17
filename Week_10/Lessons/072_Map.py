# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use map with predefined function

def formatText(text):

    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]

myFormattedData = map(formatText, myTexts)

print(myFormattedData)

for name in list(map(formatText, myTexts)):

    print(name)

print("#" * 50)


def formatText(text):

    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):

    print(name)
