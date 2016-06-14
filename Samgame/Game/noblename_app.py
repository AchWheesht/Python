import random
import json

with open("noblenames.json", "r") as file:
    coded = file.read()
noblenames = json.loads(coded)

while True:
    hold = random.randint(1, 2)
    if hold == 1:
        gender = "m"
    elif hold == 2:
        gender = "f"
    nobility = random.randint(1, 10)

    if gender == "m":
        first_name = noblenames["first_male"]
        titles = noblenames["titles_male"]
    else:
        first_name = noblenames["first_female"]
        titles = noblenames["titles_female"]

    if nobility >= 7:
        placenames = noblenames["placenames_major"]
    elif nobility >= 4:
        placenames = noblenames["placenames_minor"]
    else:
        placenames = None
        titles = None
        
    surname = noblenames["surname"]
    nickname = noblenames["nicknames"]

    full_name = "%s %s" % (
        first_name[random.randint(1, len(first_name) -1)],
        surname[random.randint(1, len(surname) -1)]
        )

    if titles:
        full_title = "%s %s" % (
            titles[random.randint(1, len(titles) -1)],
            placenames[random.randint(1, len(placenames) -1)]
            )
    else:
        full_title = None
    
    extended_title = "%s%s" % (
        full_name,
        nickname[random.randint(1, len(nickname) -1)],
        )
    
    if titles:
        extended_title = "%s, %s" % (
            extended_title,
            full_title
            )

    eggs = noblenames["eggs"]
    try:
        hold = eggs[full_name]
        extended_title = hold[2]
    except KeyError:
        pass
            
    print(extended_title)
    again = input("again? y/n")
    if again == "n":
        break
