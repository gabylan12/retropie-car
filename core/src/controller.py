from flask import Flask,request,jsonify
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import RPi.GPIO as GPIO
import time

# Configure the PIN # 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
#GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setwarnings(False)



@app.route("/right")
def right():

    return "Right"


@app.route("/stop")
def stop():
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(36, False)
    GPIO.output(38, False)
    GPIO.output(40, True)
    return "Stop"

@app.route("/left")
def left():
    return "Left"

@app.route("/forward")
def forward():
    GPIO.output(16, True)
    GPIO.output(18, False)
    GPIO.output(20, True)
    return "Forward"

@app.route("/backward")
def backward():
    GPIO.output(16, False)
    GPIO.output(18, True)
    GPIO.output(26, True)
    return "Backward"

@app.route("/green")
def green():
    GPIO.output(36, False)
    GPIO.output(38, True)
    GPIO.output(40, False)
    return "Green"

@app.route("/blue")
def blue():
    GPIO.output(36, True)
    GPIO.output(38, False)
    GPIO.output(40, False)
    return "Blue"

@app.route("/yellow")
def yellow():
    GPIO.output(36, True)
    GPIO.output(38, True)
    GPIO.output(40, False)
    return "Yellow"
