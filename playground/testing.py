import time

def print_figure_one():
    print("")
    print(" _O_ /")
    print("/ |  ")
    print(" / \ ")
    print("")

def print_figure_two():
    print("")
    print(" _O_\ ")
    print("/ |  ")
    print(" / \ ")
    print("")

def print_space():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while True:
    print_figure_one()
    time.sleep(0.01)
    print_space()
    print_figure_two()
    time.sleep(0.01)
    print_space()
