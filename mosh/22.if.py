#start - to start the car
#stop - to stop the car
#quit - to exit
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
           print("Car is already started!")
        else:
           started = True
           print("Car started…")
    elif command == "stop":
        if not started:
           print("Car is already stopped")
        else:
           stopped = False
           print("Cae stop")

    elif command =="help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")


