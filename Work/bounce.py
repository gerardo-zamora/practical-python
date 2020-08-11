# bounce.py
#
# Exercise 1.5
height = 100.0
i = 1

print(height)

while i <= 10:
    height = height * 3 / 5
    print(str(i) + " " + str(round(height, 4)))
    i = i + 1

print("-----End of Program-----")