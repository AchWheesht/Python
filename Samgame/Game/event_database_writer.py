import json

#***Format***
#
#Name:              Name of the event (code)
#ID:                Assign unique three digit ID to event
#Title:             Title of event (in game)
#Requirements:      Specify requirements for event to occur (code)
#Description:       Text describing the event occuring
#Choices: How many choices the event has
#Choice n:          Text displayed for choice n (code). Use None if no conditions are required.
#Conditions n:      Conditions for choice n to be shown
#**Do not store event outcomes here. Event outcomes will be stored seperately in a specific function.***

Famine = {
    "Name": "famine",
    "ID": 101,
    "Title": "Famine!",
    "Description": "Famine strikes! Your people are starving. How do you react?",
    "Choices": 4,
    "Choice 1": "1. Let them starve",
    "Conditions 1": None,
    "Choice 2": "2. Force feed them water and air",
    "Conditions 2":
    "Choice 3": "3. Tax your nobles to feed them",
    "Choice 4": "4. Tax a specific noble to feed them"
    }

# Drought = {
#     "Name": "drought",
#     "ID": 102,
#     "Title": "Drought!",
#     "Function": self.drought(),
#     "Description": "Drought!

##
##final_dictionary = {
##"famine": Famine
##}
##
coded = json.dumps(noble_generator_dictionary)
with ("events_dict.json", "w") as file:
    file.write(coded)
