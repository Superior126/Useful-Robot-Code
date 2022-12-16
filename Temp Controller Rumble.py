def controllerRumble():
    while True: 
        # Replace "motor_16" with the motor you want to monitor
        # Controller will rumble if the temp exceeds 60 degrees 
        if motor_16.temperature(PERCENT) > 60:
            # Controllers name is "controller_1" by default. If you renamed yours, make sure its the correct name here
            controller_1.rumble(".")

# Add this in your driver control function 
Thread(controllerRumble)
