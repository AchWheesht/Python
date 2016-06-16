#The events module is in charge of storing, managing and executing events. This module is still very much under develeopment,
#awaiting a proper design session with Sam and a theory session with Johnny.

import random
import time
import json
import os
import parser

class Eventsclass:
    def __init__(self):
        self.events_dict_text = {}
        self.filename = "events_dict.json"
        if os.path.isfile(self.filename):
            self.load_file()

    def load_file(self):
        with open(self.filename, "r") as file:
            coded = file.read()
        self.events_dict = json.loads(coded)

    def save_file(self):
        coded = json.dumps(self.Events)
        with open(self.filename, "w") as file:
            file.write(coded)


    #Checks to see if the player is alive.

    def status_check(self):
        if Stats.supplies["Food"] <=0:
            Stats.is_alive = False
        elif Stats.supplies["Water"] <= 0:
            Stats.is_alive = False
        elif Stats.supplies["Air"] <= 0:
            Stats.is_alive = False

    def run_event(self, mode, event_name, Nobles, Stats, Events, Event_Function, event_database):
        event_running = True
        choice = None
        if mode == "manual":
            event_lookup = Event_Function.function_database[event_name]
            event_mode = "start"
            while event_running == True:
                values = event_lookup(event_mode, choice, event_name, event_database, Nobles, Stats, Events)
                event_mode = values[1]
                if event_mode == "done":
                    break
                valid_choices = values[0]
                while True:
                    choice = int(input("Which Option?"))
                    if not isinstance(choice, int):
                        print("Please enter a number")
                    elif choice in valid_choices:
                        break
                    else:
                        print("Not a valid choice")





    #Automatically kills the player
    def kill_self(self, Stats):
        Stats.is_alive = False

#All code below here is events
#
