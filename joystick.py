import qwiic_joystick
import time
import sys
import requests
from CONFIG import HORN_BLINKERS_URL, ACCELERATE_BRAKE_URL

def runExample():
    print("\nStarting Joystick\n")
    myJoystick = qwiic_joystick.QwiicJoystick()
    
    if myJoystick.connected == False:
        print("The Qwiic Joystick device isn't connected to the system.",
              file=sys.stderr)
        return
    
    myJoystick.begin()
    
    print("Initialized")
    
    while True:
        x = myJoystick.horizontal
        y = myJoystick.vertical
        b = myJoystick.button
        
        if x > 575:
            print("Left")                        
            url = HORN_BLINKERS_URL + "left"
            response = requests.get(url)
            print(response)
        elif x < 450:
            print("Right")            
            url = HORN_BLINKERS_URL + "right"
            response = requests.get(url)
            print(response)
            
        if y > 575:
            print("Up")            
            url = ACCELERATE_BRAKE_URL + "accelerate"
            response = requests.get(url)
            print(response)
        elif y < 450:
            print("Down")            
            url = ACCELERATE_BRAKE_URL + "brake"
            response = requests.get(url)
            print(response)
        
        if b == 0:
            print("Button")            
            url = HORN_BLINKERS_URL + "horn"
            response = requests.get(url)
            print(response)
        
        time.sleep(.4)
    
if __name__ == '__main__':
    try:
        runExample()
    except(KeyboardInterrupt, SystemExit) as exErr:
        print("\Ending Joystick")
        sys.exit(0)