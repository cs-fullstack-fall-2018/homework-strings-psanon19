# Exercises Homework Problem 1: Naughty Strings
#
# What is the error message returned when you improperly use quotes inside of strings?
# Provide an example and explain the error message.
# ray=['Th'ey are using it wrong']
#      ray=['Th'ey are using it wrong']
#                ^
#           SyntaxError: invalid syntax
#
# Homework Problem 2: Fruits and Vegetables
#
# x = ["apple", "banana", "carrot"]
#
# Write one line of code that when executed returns "apples bananas and carrots".

x = ["APPLE", "BaNaNa", "carROT"]
print((x[0].lower())+'s ' + (x[1].lower()) +'s and ' + (x[2].lower()) + 's.')

#one step further