
import phonelib
import RPi.GPIO as GPIO
import serial
import time
import json

ser = serial.Serial("/dev/ttyS0",115200)
ser.flushInput()

phone_number = '0497348026' #********** change it to the phone number you want to call
power_key = 6
rec_buff = ''

#try:
f = open('../test.json')
storage = json.load(f)
text_message = storage.get('testmessage', "default message")
phonelib.power_on(power_key)
print('Sending Short Message Test:')
phonelib.SendShortMessage(phone_number,text_message)
print('Receive Short Message Test:\n')
print('Please send message to phone ' + phone_number)
phonelib.ReceiveShortMessage()
phonelib.power_down(power_key)
# except :
# 	if ser != None:
# 		ser.close()
# 	GPIO.cleanup()