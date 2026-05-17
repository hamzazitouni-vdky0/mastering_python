# ========================================
# === Assignments For Lessons 67 To 78 ===
# ========================================

# ========================
# === First Assignment ===
# ========================

import datetime

date = datetime.datetime(2021, 6, 25)
dateNow = datetime.datetime.now()

"Days From 2021-06-25 To 2021-08-10 Is => 46"
print(f"Days from {date.date()} to {dateNow.date()} is => {(dateNow - date).days}")

print("#" * 50)

# ========================
# === Second Assignment ===
# ========================

print(f"Today is {dateNow.date()}")
print(f"Today is {dateNow.date().strftime("%b %d, %Y")}")
print(f"Today is {dateNow.date().strftime("%d - %b - %Y")}")
print(f"Today is {dateNow.date().strftime("%d / %b / %y")}")
print(f"Today is {dateNow.date().strftime("%d / %B / %Y")}")
print(f"Today is {dateNow.date().strftime("%a, %d %B %Y")}")
