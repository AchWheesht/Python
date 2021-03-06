import json

noblenames_first_male = [
    "Jeremy",
    "Alistair",
    "David",
    "Tibalt",
    "Tycho",
    "Stevedave",
    "Sam",
    "Phil",
    "Johnny",
    "Gavin",
    "Ruriadh",
    "Michael",
    "Archibald",
    "Pip",
    "Arthur",
    "Rusty",
    "Henry",
    "Boris",
    "Kvothe",
    "Rowan",
    "Rob",
    "Tim",
    "Prashant",
    "Mustrum",
    "Stevie",
    "Guggy"
    ]

noblenames_first_female = [
    "Kristi",
    "Hannah",
    "Holly",
    "Beka",
    "Maarja",
    "Elizabeth",
    "Curly",
    "Boudica",
    "Leela",
    "Mercy",
    "Anne",
    "Megan",
    "Fiona",
    "Athena",
    "Pauline",
    "Sabriel",
    "Alice",
    "Rhyme",
    "Reason",
    "Ysri",
    "Magrat",
    "Michelle",
    "Ingrid",
    "Prudence"
    ]

noblenames_surname = [
    "Shaw",
    "Harrison",
    "Leech",
    "Morrice",
    "Uustalu",
    "Robertson",
    "Quayle",
    "Jogioja",
    "Crosher",
    "Gray",
    "Windsor",
    "Puddleson",
    "Sonson",
    "Lackless",
    "Preed",
    "Loftry",
    "Murdery",
    "Rich",
    "Stench",
    "Vimes",
    "Callarman-Williams",
    "Henthorn",
    "Merryweather",
    "Hatchet",
    "Creely",
    "Knobson",
    "J. Clark",
    '"The rock" Mcgruffy'
    ]

placenames_major = [
    "of London",
    "of Edinburgh",
    "of Devon",
    "of Mars",
    "of most of Africa",
    "of the better half of Norway",
    "of the King's sock drawer",
    "of a big place somewhere far away",
    "of Dune",
    "of Frogland",
    "of a vast expanse of nothing",
    "of all the kings horses",
    "of Wetherspoons",
    "of Scientology",
    "of lies",
    "of the view from Pride Rock",
    "beyond the wall",
    "of many places",
    "of this here swamp",
    "of the European Union!"
    ]

placenames_minor = [
    "of Peebles",
    "of South Wales",
    "of New South Wales",
    "of the shitty part of Amsterdam",
    "of Uranus (Hur hur)",
    "of Murderville",
    "of their own underwear",
    "of nowhere",
    "of Space",
    "of Imagination",
    "of SCIENCE",
    "of all floors, everywhere",
    "extroardinaire!",
    "of the boring, important bits of Europe",
    "of Buckingham Shed",
    "of the elephant graveyard",
    "of the barren north",
    "of Disneyland",
    "of 12 Forrester Walk, Milton Keynes, MK10 9TN"
    ]

titles_male = [
    "Duke",
    "Baron",
    "Earl",
    "Marquis",
    "Chief",
    "Lord",
    "Count"
    ]

titles_female = [
    "Duchess",
    "Baroness",
    "Earl",
    "Marquise",
    "Chief",
    "Lady",
    "Countess"
    ]

nicknames = [
    " the Great",
    " the not so Great",
    " the Mighty",
    " the dim",
    " the motionless",
    " the very, very old",
    " the lecher",
    " the bastard",
    " the conniving son of a bitch",
    " the euphemism",
    " the treacherous",
    " the stoner",
    " the self-awawre",
    " the jealous",
    " the vain",
    " the especially stupid",
    " the misspeled",
    " the made up",
    " the unaware",
    " the paranoid",
    " the cheese",
    " the flake",
    " the six year old",
    " the belcherous",
    " the especially unsavoury",
    " the crow",
    " the smartass",
    " the obviously fictional",
    " the munchkin",
    " the level 20 halfling rogue",
    " the ambiguous",
    " the scentless",
    " the eternally unlucky",
    " the wizard",
    " (formerly known as Prince)",
    " the cheapskate",
    " the drunk",
    " the radical",
    " the impotent",
    " the younger",
    " the snark",
    " and their pet, Gnarlius Funkmeister the belligerent rodent",
    " and their pet, Scrooge McDuck",
    " and their pet, the almighty Gronk",
    ", the last of the Mohicans",
    ", the last remaining dragon",
    " the solipsist",
    " the inexplicable",
    " the undescribable",
    ", straight from the 70's",
    ", straight outta Compton",
    " the disgruntled employee",
    " the splendiferous",
    " (yes, that one)",
    " of Top Gear fame",
    " the Eternal",
    ", Inventor of the Whirligig Thingmabob",
    ", Heavyweight Champion of the World",
    ", Booklord Primus",
    " the etheral",
    ": kill streak (16)"
    " the murdertastic"
    ]

eggs = {
    #return in format (full_name, full_title, extended_title, [intel, ambition, network, wealth, gender)
    "Gavin Leech": ["Gavin Leech", "Lord of the Shithovel", "Gavin Leech the Category Defier, Lord of the Shithovel", [10, 8, 4, 2, "m"]],
    "Rowan Callarman-Williams": ["Rowan Callarman-Williams", "First of the King's Scouts", "Rowan Callarman-Williams the restless, First of the King's Scouts", [7, 3, 8, 3, "m"]],
    "Micheal Robertson": ["Micheal Robertson", "Booklord of the Vast Archives", "Micheal Robertson the level 90 slayer, Booklord of the Vast Archives", [7, 4, 4, 5, "m"]],
    "Beka Quayle": ["Beka Quayle", "Booklady of the Vast Archives", "Beka Quayle the Absent, Booklady of the Vast Archives", [8, 6, 2, 5, "f"]],
    "Johnny Morrice": ["Johnny Morrice", "Arch-Wizard of the North", "Johnny Morrice the J-Punk star, Arch-Wizard of the North", [10, 7, 4, 6, "m"]],
    "Sam Shaw": ["Sam Shaw", "Keeper of Deeds Past", "Sam Shaw of the Scribes, Keeper of Deeds Past", [7, 3, 7, 3, "m"]],
    "Maarja Jogioja": ["Maarja Jogioja", "First Lady of the free country of Thatch", 'Maarja Jogioja a.k.a "Binksy", First Lady of the Free Country of Thatch', [8, 7, 6, 9, "f"]]
    }

noble_generator_dictionary = {
    "first_male": noblenames_first_male,
    "first_female": noblenames_first_female,
    "surname": noblenames_surname,
    "placenames_major": placenames_major,
    "placenames_minor": placenames_minor,
    "titles_male": titles_male,
    "titles_female": titles_female,
    "nicknames": nicknames,
    "eggs": eggs
    }

coded = json.dumps(noble_generator_dictionary)
with open("noblenames.json", "w") as file:
    file.write(coded)
