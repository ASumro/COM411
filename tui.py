def started(msg=""):
    print("-------------------------------------------------------------------------------------\n")
    print("Operation started: {msg}...\n")

def completed():
    print("\n")
    print("Operation completed.\n")
    print("-------------------------------------------------------------------------------------")

def error(msg):
    print("Error! {msg}")

def menu():
    print("Please select one of the following options: \n")
    print(f"{'[years]':<10} {'List unique years':25}\n")
    print(f"{'[tally]':<10} {'Tally up medals':10}")
    print(f"{'[team]':<10} {'Tally up medals for each team':25}")
    print(f"{'[exit]':<10} {'Exit the program:25}")
    print("Your selection: ")

def display_medal_tally(tally):
    for key, value in tally.items():
        print(f"'|{key'':<10}: {value}")