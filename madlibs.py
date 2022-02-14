#!/usr/bin/python3


# Suppose we want to create a string that says "subscribe to ____"""

# youtuber = "luis_allen"

# """ a few ways to do this """
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(F"subscribe to {youtuber}")

adj = input("Adjetive: ")
adj2 = input("Adjetive2: ")
adj3 = input("Adjetive3: ")
pro = input("Pronoun: ")
pro2 = input("Pronoun2: ")
verb1 = input("Verb: ")
verb2 = input("Verb2: ")
act = input("action: ")
act2 = input("action2: ")
act3 = input("action3: ")


madlib = f"You were the {pro}! It was said you would {act} the {pro2} \
    not {act2}! Bring {adj} to the force, not {act3} in {adj2}! you were \
        my {adj3}!"

print(madlib)
