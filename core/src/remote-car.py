import RPi.GPIO as GPIO
import time

# Configure the PIN # 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setwarnings(False)

# Blink Interval 
blink_interval = .5 #Time interval in Seconds

# Blinker Loop
while True:
 GPIO.output(36, True)
 time.sleep(blink_interval)
 GPIO.output(36, False)
 time.sleep(blink_interval)
 GPIO.output(38, True)
 time.sleep(blink_interval)
 GPIO.output(38, False)
 time.sleep(blink_interval)
 GPIO.output(40, True)
 time.sleep(blink_interval)
 GPIO.output(40, False)
 time.sleep(blink_interval)
 GPIO.output(38, True)
 GPIO.output(36, True)
 time.sleep(blink_interval)
 GPIO.output(38, False)
 GPIO.output(36, False)
 time.sleep(blink_interval)
 GPIO.output(40, True)
 GPIO.output(36, True)
 time.sleep(blink_interval)
 GPIO.output(40, False)
 GPIO.output(36, False)
 time.sleep(blink_interval)
 GPIO.output(40, True)
 GPIO.output(38, True)
 time.sleep(blink_interval)
 GPIO.output(40, False)
 GPIO.output(38, False)
 time.sleep(blink_interval)
 GPIO.output(38, True)
 GPIO.output(36, True)
 GPIO.output(40, True)
 time.sleep(blink_interval)
 GPIO.output(38, False)
 GPIO.output(36, False)
 GPIO.output(40, False) 
 time.sleep(blink_interval)
# Release Resources
GPIO.cleanup()
