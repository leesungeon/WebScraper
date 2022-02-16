# sequence (string, tuple, list)

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

for day in [1, 2, 3, 4, 5]:
    print(day)

for x in days:
    if x == "Wed":
        break
    else:
        print(x)

for letter in "nicolas":
    print(letter)