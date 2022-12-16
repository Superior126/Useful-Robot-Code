#global variables
global team
team = ""

# Begin project code

def pre_autonomous():
    global team
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1,1)
    controller_1.screen.print("Team: None")
    while True:
        if bumper_a.pressing():
            if team == "red":
                team = "blue"
                controller_1.screen.clear_screen()
                controller_1.screen.set_cursor(1,1)
                controller_1.screen.print("Selected: " + team)
                wait(0.5,SECONDS) 
            else:
                team = "red"
                controller_1.screen.clear_screen()
                controller_1.screen.set_cursor(1,1)
                controller_1.screen.print("Selected: " + team) 
                wait(0.5,SECONDS)  
