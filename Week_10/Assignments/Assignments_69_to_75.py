# ========================================
# === Assignments For Lessons 69 To 71 ===
# ========================================

# ========================
# === First Assignment ===
# ========================

# Create var contain false & true values
values = (0, 1, 2)

# Check if any value in the tuple is true
if any(values):

    # If any value in the tuple is true: create: my_var = 0
    my_var = 0

# Create new list contain variety of data types
my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# Check if the element in in my_list from index O to index 3 is true
# or from index O to index 6 is true
# or from all the list
# all(my_list[:4]) is true
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    # If one from the chooses is true print Good
    print("Good")

else:

    # If no choose from chooses is true print Bad
    print("Bad")

# Output is: Good

# =========================
# === Second Assignment ===
# =========================

print("#" * 50)

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

print("#" * 50)

# ========================
# === Third Assignment ===
# ========================

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

    print("Good")

# Output => Good

print("#" * 50)

# ========================
# === Fourd Assignment ===
# ========================

# my_all


def my_all(iterable):

    for item in iterable:

        if not item:

            return False

    else:

        return True


print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False

# my_any


def my_any(iterable):

    for item in iterable:

        if item:

            return True
    else:

        return False


print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False

# my_min


def my_min(iterable):

    iterator = iter(iterable)
    smallest = next(iterator)

    for item in iterator:

        if item < smallest:

            smallest = item

    return smallest


print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100

# my_max


def my_max(iterable):

    iterator = iter(iterable)
    greatest = next(iterator)

    for item in iterator:

        if item > greatest:

            greatest = item

    return greatest


print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700

# ========================================
# === Assignments For Lessons 72 To 75 ===
# ========================================

print("#" * 50)

# ========================
# === First Assignment ===
# ========================

# def remove_chars(string):

#     string = string[1:-1]
#     return string

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

new_string = map(lambda string: string[1:-1], friends_map)

for string in new_string:

    print(string)

print("#" * 50)

# =========================
# === Second Assignment ===
# =========================

# def get_names(name):

#     return name.endswith("m")

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(lambda name: name.endswith("m"), friends_filter)

for name in names:

    print(name)

print("#" * 50)

# =========================
# === Third Assignment ====
# =========================

from functools import reduce

nums = [2, 4, 6, 2]

# def sum(num1, num2):

#   return num1 * num2

reduced_nums = reduce(lambda num1, num2: num1 * num2, nums)

print(reduced_nums)

print("#" * 50)

# =========================
# === Third Assignment ====
# =========================

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for counter, skill in enumerate(reversed(skills), 50):

    if type(skill) is int:

        continue

    print(f"{counter} - {skill}")
