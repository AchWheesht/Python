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

    #Automatically kills the player
    def kill_self(self, Stats):
        Stats.is_alive = False

#All code below here is events
#
