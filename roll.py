# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

import random

die_to_roll = int(input("How many dice do you want to roll? 1, 2, or 3?"))

if die_to_roll == 1:
    print(random.randint(1,6))
elif die_to_roll == 2:
    print(random.randint(1,6))
    print(random.randint(1, 6))
elif die_to_roll == 3:
    print(random.randint(1,6))
    print(random.randint(1, 6))
    print(random.randint(1, 6))

