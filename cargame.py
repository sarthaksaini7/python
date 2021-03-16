help = """
Start - To start the car
Stop - To stop the car
Quit - to exit the game
"""
state = "stopped"
command = ""
while command.upper != "QUIT":
    user_input = input(">")
    if user_input.upper() == "HELP":
        print(help)
    elif user_input.upper() == "START" and state != "started":
        print(f'Car Started... Ready to GO')
        state = "started"
    elif user_input.upper() == "START" and state == "started":
        print(f'Car is already running')
    elif user_input.upper() == "STOP" and state != "stopped":
        print(f'Car Stopped')
        state = "stopped"
    elif user_input.upper() == "STOP" and state == "stopped":
        print(f'Car is already stopped')
    elif user_input.upper() == "QUIT":
        print(f'Quitting the game. Goodbye.')
        break
    else:
        print("I dont understand that")
