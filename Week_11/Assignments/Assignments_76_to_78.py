# ========================================
# === Assignments For Lessons 76 To 78 ===
# ========================================

# ========================
# === First Assignment ===
# ========================

import random

print(f"Random number between 10 and 50 => {random.randrange(10, 50)}")
print(f"Random number between 2 and 10 => {random.randrange(2, 10, 2)}")
print(f"Random number between 2 and 10 => {random.randrange(1, 9, 2)}")

print("#" * 50)

# ========================================
# === Second, Third, Fourth Assignments ==
# ========================================

# ../Python/my_mod.py file content

def say_hello(name):

    print(f"Hello {name}")


def say_welcome(name):

    print(f"Welcome {name}")

# ../Python/main.py file content

import sys

sys.path.append(r"E:\Python")
print(sys.path)

import my_mod

my_mod.say_hello("Hamza")
my_mod.say_welcome("Hamza")

print("#" * 50)

from my_mod import say_welcome

my_mod.say_welcome("Hamza")

print("#" * 50)

from my_mod import say_welcome as new_welcome

new_welcome("Hamza")
