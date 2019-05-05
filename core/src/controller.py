from flask import Flask,request,jsonify
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import RPi.GPIO as GPIO
import time

# Configure the PIN # 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setwarnings(False)



@app.route("/right")
def right():

    return "Right"


@app.route("/stop")
def stop():
    return "Stop"

@app.route("/left")
def left():
    return "Left"

@app.route("/forward")
def forward():
    return "Forward"

@app.route("/backward")
def backward():
    return "Backward"

@app.route("/green")
def green():
    GPIO.output(36, True)
    GPIO.output(38, False)
    GPIO.output(40, False)
    return "Green"

@app.route("/blue")
def blue():
    GPIO.output(36, False)
    GPIO.output(38, True)
    GPIO.output(40, False)
    return "Blue"

@app.route("/yellow")
def yellow():
    GPIO.output(36, False)
    GPIO.output(38, False)
    GPIO.output(40, True)
    return "Yellow"
