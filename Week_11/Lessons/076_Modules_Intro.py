# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import main module
import random

print(random)
print(f"Print random float number {random.random()}")

# Show all functions inside module
import random

print(dir(random))

# Import one or two functions from module
from random import *  # randint, random

print(f"Print random integer {randint(100, 900)}")
print(f"Print random float {random()}")
