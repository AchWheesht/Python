#Currently handles the manual running of processes.

class Controllerclass:
    def __init__(self):
        pass

    def global_commands(self, Nobles, Stats, Events, Event_Function, event_database):
        while Stats.is_alive == True:
            command = input("What now? (Nobles, Events, Office, Quit)")
            command = command.lower()
            if command == "events":
                self.event_commands(Nobles, Stats, Events, Event_Function, event_database)
            elif command == "nobles":
                self.noble_commands(Nobles, Stats, Events, Event_Function, event_database)
            elif command == "office":
                self.office_commands(Nobles, Stats, Events, Event_Function, event_database)
            elif command == "quit":
                return
            else:
                print("Speak english, motherfucker")

    def event_commands(self, Nobles, Stats, Events, Event_Function, event_database):
        while Stats.is_alive == True:
            command = input("What now? (Suicide, Run event, Display stats, Back)")
            command = command.lower()
            if command == "suicide":
                Events.kill_self(Stats)
            if command == "back":
                return
            elif command == "display stats":
                print("Your resources are:")
                print("Food: " + str(Stats.supplies["Food"]))
                print("Water: " + str(Stats.supplies["Water"]))
                print("Air: " + str(Stats.supplies["Air"]))
            elif command == "run event":
                mode = input("manual or random?")
                if mode == "manual":
                    event_name = input("Run which event?")
                    Events.run_event(mode, event_name, Nobles, Stats, Events, Event_Function, event_database)
                else:
                    print("Functionality not implemented yet")
            else:
                print("Not a valid command, dude")

    def noble_commands(self, Nobles, Stats, Events, Event_Function, event_database):
        while Stats.is_alive == True:
            raw_action = input("What next? (New, Random new, Delete, Delete all, View, View names, View everything, back)")
            action = raw_action.lower()
            if action == "back":
                return
            elif action == "new":
                Nobles.create_noble("manual")
            elif action == "random new":
                Nobles.create_noble("random")
            elif action == "delete":
                Noble = input("Delete which noble/cancel?")
                Nobles.remove_noble(Noble)
            elif action == "delete all":
                Nobles.delete_all()
            elif action == "view":
                view_names_request = input("Request whose stats/cancel?)")
                Nobles.get_stats(view_names_request)
            elif action == "view names":
                Nobles.view_names()
            elif action == "view everything":
                Nobles.view_everything()
            else:
                print("That's not a valid input, dumbass")

    def office_commands(self, Nobles, Stats, Events, Event_Function, event_database):
        while Stats.is_alive == True:
            action = input ("What next? ([View employed] nobles, [View empty] positions, [Fire] a noble, [Employ] a noble, [Back])")
            action = action.lower()
            if action == "view employed":
                Nobles.view_filled_positions()
            if action == "view empty":
                Nobles.view_empty_positions()
            if action == "employ":
                Nobles.employ_noble()
            if action == "fire":
                Nobles.fire_noble()
            if action == "back":
                return
