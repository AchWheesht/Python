testdict1 = {
    "a": 10,
    "b": 5
    }

testdict2 = {
    "c": 7,
    "d": 3
    }

print(testdict1)
print("")
print(testdict2)
print("")

finaldict = {**testdict1, **testdict2}

print(finaldict)
