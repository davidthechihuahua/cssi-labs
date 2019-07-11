import random
die1 = (random.randint(1,6))
die2 = (random.randint(1,6))

sum = die1 + die2


if die1 == die2:
    print("this is your sum: %s"% (str(sum)))
    print("roll again")

else:
    print("this is your sum: %s"% (str(sum)))
    print("next players turn")
