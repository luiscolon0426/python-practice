#!/usr/bin/python3

# Have the user enter their investment amount and expect interest
# Each year their investment will increase by their investment + their investment
# * rate is
# print out the earnings after a 10 year period

money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")

# convert money to float
money = float(money)

# convert value to a float and a round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

# cycles through 10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)

print("Investment after 10 years : {:.2f}".format(money))
