print()
print()
print("This should print ten asterisks in a row")
print()

for i in range(10):
    print("*", end = " ")

print()
print()
print("This should print 10, then 5, then 20 stars")
print()

for i in range(10):
    print("*", end = " ")

print()

for i in range(5):
    print("*", end = " ")

print()

for i in range(20):
    print("*", end = " ")

print()
print()
print("This should print a 10x10 grid of stars")
print()

for i in range(10):
    for i in range(10):
        print("*", end = " ")
    print()

print()
print("This should print a 5x10 grid of stars")
print()

for i in range(10):
    for i in range(5):
        print("*", end = " ")
    print()

print()
print("This should print a 20x5 rectangle")
print()

for i in range(5):
    for i in range(20):
        print("*", end = " ")
    print()

print()
print("This should print the numbers 0 to 9 ten times on different lines")
print()

for i in range(10):
    for i in range(10):
        print(i, end = " ")
    print()

print()
print("This should print the 10 zero's, then ten one's, interte until ten nine's")
print()

for i in range(10):
    for n in range(10):
        print(i, end = " ")
    print()

print()
print("This should produce a pyramid of numbers")
print()

for i in range(11):
    for n in range(i):
        print(n, end = " ")
    print()

print()
print("This should produce a reverse pyramid")
print()

for i in range(10):
    for x in range(i):
        print(" ", end = " ")
    for n in range(10- i):
        print(n, end = " ")
    print()

print()
print("This should print a multiplication table")
print()

for i in range(9):
    for n in range(9):
        if ((n+1) * (i + 1)) < 10:
            print("", end = " ")
            print(((n+1) * (i + 1)), end = " ")
        else:
            print(((n+1) * (i + 1)), end = " ")
    print()

print()
print("This should print an actual pyramid of numbers")
print()

for i in range(10):
    for first_blank in range(10 - i):
        print(" ", end = " ")
    for n in range(i):
        print(n + 1, end = " ")
    for x in range(i - 1):
        print(((i-1)-x), end = " ")
    for second_blank in range(10 - i):
        print(" ", end = " ")
    print()

print()
print("This should print three quarters of a diamond")
print()

for i in range(10):
    for first_blank in range(10 - i):
        print(" ", end = " ")
    for n in range(i):
        print(n + 1, end = " ")
    for x in range(i - 1):
        print(((i-1)-x), end = " ")
    for second_blank in range(10 - i):
        print(" ", end = " ")
    print()
for i in range(8):
    for x in range(i + 2):
        print(" ", end = " ")
    for n in range(8- i):
        print(n+1, end = " ")
    print()
