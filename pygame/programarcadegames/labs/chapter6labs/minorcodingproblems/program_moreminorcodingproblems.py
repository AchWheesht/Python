"""this is the actual lab for chapter six"""

print()
print("The program starts here")
print()
print("This prints a pyramid of increasing numbers")
print()


count = 10
for i in range(10):
    for n in range(i):
        print(count, end = " ")
        count += 1
    print()

print()
print("This should print a box of height n, where n is an input")
print()

##Skipping input for testing purposes
#number = int(input("Please input n\n"))
number = 5
print()

for i in range(number):
    if i == 0:
        for n in range(number):
            print("o", end = "")
    elif i == (number-1):
        for x in range(number):
            print("o", end = "")
    else:
        for y in range(number):
            if y == 0:
                print("o", end = "")
            elif y == (number-1):
                print("o", end = "")
            else:
                print(" ", end = "")
    print()

print()
print("This should print a hollow diamond")
print()

hold = int(input("Please input a number\n"))
print()

for i in range(0, hold): #Hold is double the number entered
    for n in range(i, (hold)):
        print((2*n)+1, end = " ")
    for n in range(hold, hold-i, -1):
        print("  ", end = "  ")
    for n in range((hold)-1, i-1, -1):
        print((2*n)+1, end = " ")
    print()
for i in range(hold-1, -1, -1): #Hold is double the number entered
    for n in range(i, (hold)):
        print((2*n)+1, end = " ")
    for n in range(hold, hold-i, -1):
        print("  ", end = "  ")
    for n in range((hold)-1, i-1, -1):
        print((2*n)+1, end = " ")
    print()



#
