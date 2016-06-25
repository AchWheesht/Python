import random
import json

class NoblenameApp():
    def __init__(self):
        self.noblenames = self.load_file()

    def load_file(self):
        with open("noblenames.json", "r") as file:
            coded = file.read()
        noblenames = json.loads(coded)
        return noblenames

    # def print_name(self):
    #     while True:
    #         name = self.generate_name(self.noblenames)
    #         print(name)
    #         again = input("again? y/n")
    #         if again == "n": break

    def generate_name(self):
        hold = random.randint(1, 2)
        if hold == 1:
            gender = "m"
        elif hold == 2:
            gender = "f"
        nobility = random.randint(1, 10)

        if gender == "m":
            first_name = self.noblenames["first_male"]
            titles = self.noblenames["titles_male"]
        else:
            first_name = self.noblenames["first_female"]
            titles = self.noblenames["titles_female"]

        if nobility >= 7:
            placenames = self.noblenames["placenames_major"]
        elif nobility >= 4:
            placenames = self.noblenames["placenames_minor"]
        else:
            placenames = None
            titles = None

        surname = self.noblenames["surname"]
        nickname = self.noblenames["nicknames"]

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

        eggs = self.noblenames["eggs"]
        try:
            hold = eggs[full_name]
            extended_title = hold[2]
        except KeyError:
            pass

        return(extended_title)
