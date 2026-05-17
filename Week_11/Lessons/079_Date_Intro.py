# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print the current date and time
print(datetime.datetime.now())

print("#" * 50)

# Print the current year
print(datetime.datetime.now().year)


# Print the current month
print(datetime.datetime.now().month)

# Print the current day
print(datetime.datetime.now().day)

print("#" * 50)

# Print start and end of date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 50)

# print(dir(datetime.datetime.now()))

# Print the current time
print(datetime.datetime.now().time())

# Print the current time hour
print(datetime.datetime.now().time().hour)

# Print the current time minute
print(datetime.datetime.now().time().minute)

# Print the current time second
print(datetime.datetime.now().time().second)

print("#" * 50)

# Print start and end of time
print(datetime.time.min)
print(datetime.time.max)

# Print specefic date
print(datetime.datetime(2011, 2, 20))
print(datetime.datetime(2011, 2, 20, 1, 34, 23, 123412))

myBirthDay = datetime.datetime(2011, 2, 20)
dateNow = datetime.datetime.now()

print(f"My birthday {myBirthDay}", end=" and ")
print(f"Date now is{dateNow}.")

print(f"I lived for {dateNow - myBirthDay}.")
print(f"I lived for {dateNow - myBirthDay.days} days.")