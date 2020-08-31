{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import RPi.GPIO as GPIO\
import time\
import requests\
\
from gpiozero import MotionSensor\
from picamera import PiCamera\
from signal import pause\
from filestack import Client\
request = None\
\
try:  \
    GPIO.setmode(GPIO.BOARD)\
    PIN_TRIGGER = 7\
    PIN_ECHO = 11\
    duration = 0\
    GPIO.setup(PIN_TRIGGER,GPIO.OUT)\
    GPIO.setup(PIN_ECHO,GPIO.IN)\
    start_time = time.time()\
    duration = 0\
    while duration < (60):\
        GPIO.output(PIN_TRIGGER,GPIO.LOW)\
        time.sleep(2)\
        \
        GPIO.output(PIN_TRIGGER,GPIO.HIGH)\
        time.sleep(0.00001)\
        GPIO.output(PIN_TRIGGER,GPIO.LOW)\
        \
        while GPIO.input(PIN_ECHO)==0:\
            pulse_start_time = time.time()\
            \
        while GPIO.input(PIN_ECHO)==1:\
            pulse_end_time = time.time()\
            \
            \
        pulse_duration = pulse_end_time-pulse_start_time\
        distance1 = round(17500*pulse_duration,2)\
        print("distance detected:",distance1,"cm")\
        #write API keys\
        print("writing to ThingSpeak...")\
        RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=A919IY7SOCZWU1H8&field1='\
        RequestToThingspeak+=str(distance1)\
        request = requests.get(RequestToThingspeak)\
        if distance1 < 10:\
         if distance1 > 0:\
            \
             client = Client("ANWybKYrRoGC9LR45vC0Qz") #filestack api key = abcdefghijk\
             camera = PiCamera()\
             camera.rotation = 180\
             camera.resolution = (1920, 1080)\
             camera.framerate = 15\
             camera.capture('/home/pi/Desktop/image.jpg') #path to your image\
             print("uploading filestack...")\
             new_filelink = client.upload(filepath="/home/pi/Desktop/image.jpg") #path to you image\
             print(new_filelink.url)\
             print("Posting to IFTTT...")\
             r = requests.post(\
             "https://maker.ifttt.com/trigger/trigger/with/key/bjiw0jg3AvS3HFEo9Kv5PV",\
             json=\{"value1" : new_filelink.url\}) #one line # ifttt api key = hjklyuioi\
            \
             camera.close() \
    \
        time.sleep(15)\
        end_time = time.time()\
        duration = end_time-start_time\
        print("duration:",duration)\
finally:\
    GPIO.cleanup()}