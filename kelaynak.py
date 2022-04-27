from gpiozero import MotionSensor, Buzzer, LED, Button
import time

PIR = MotionSensor(23)
BUZ = Buzzer(24)
LED = LED(18)
BUTTON = Button(2)

print("\n \n \n \n \n \n \n \n \n \n \n \n \n")
print("Calibrating Infrared Motion Sensor...")
PIR.wait_for_no_motion()

while True:
    LED.off()
    print("System Ready")
    PIR.wait_for_motion()
    LED.on()
    print("Motion Sensor Triggered!!")
    BUZ.beep(0.5, 0.25, 6)
    time.sleep(3)
    LED.off()

    BUTTON.wait_for_release()
    LED.on()
    print("Door is opened!")
    BUZ.beep(0.5, 0.25, 6)
    time.sleep(3)
    LED.off()
