# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------

# abs()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#" * 50)

# pow(base, exp, mod) => power
print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10


print("#" * 50)

# min(item, item, item,...,item or iterator)
print(min(1, 10, -50, 20, 30))
print(min("X", "Z", "Hamza"))
myNumbers = (1, 20, -50, -100, 100)
print(min(myNumbers))

print("#" * 50)


# max(item, item, item,...,item or iterator)
print(max(1, 10, -50, 20, 30))
print(max("X", "Z", "Hamza"))
myNumbers = (1, 20, -50, -100, 100)
print(max(myNumbers))

print("#" * 50)

# slice(start, end, step)
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
