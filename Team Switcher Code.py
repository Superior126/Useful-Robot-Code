#global variables
global team # This variable will be accesased in your "autonomous()" function to tell what team the robot is on 
team = ""

def pre_autonomous():
    global team # Make this global in your "autonomous()" funtion too 
    brain.screen.clear_screen()
    brain.screen.print("pre auton code") # This is not nessasary but handy 
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
