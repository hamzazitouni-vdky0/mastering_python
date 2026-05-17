# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys

sys.path.append(r"E:\py-own-mod")
print(sys.path)

# import hamza

# hamza.say_hello("Ahmed")
# hamza.say_hello("Hamza")
# hamza.say_hello("Mohamed")

# hamza.say_how_are_you("Ahmed")
# hamza.say_how_are_you("Hamza")
# hamza.say_how_are_you("Mohamed")

# Alias

# import hamza as hh

# hh.say_hello("Ahmed")
# hh.say_hello("Hamza")
# hh.say_hello("Mohamed")

# hh.say_how_are_you("Ahmed")
# hh.say_how_are_you("Hamza")
# hh.say_how_are_you("Mohamed")

# from hamza import say_hello

# say_hello("Hamza")

from hamza import say_hello as ss

ss("Hamza")
