# ========================================
# === Assignments For Lessons 67 To 78 ===
# ========================================

# ========================
# === First Assignment ===
# ========================


def reverse_string(my_string):
    yield my_string[::-1]


# Reverse The String
for c in reverse_string("Elzero"):
    print(c)

print("#" * 50)

# =========================
# === Second Assignment ===
# =========================


def myDecorator(func):

    def nestedFunc():

        print("Sugar added from decorator")

        func()

        print("####################")

    return nestedFunc


@myDecorator
def make_tea():
    print("Tea Created")


@myDecorator
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()
