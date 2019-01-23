from flask import Flask,render_template
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

pins = {
		20 : {'name' : 'GPIO 20', 'state' : 0},
		21 : {'name' : 'GPIO 21', 'state' : 0}
		#######_________________CAN ADD MORE GPIO HERE___________________#########
		}
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

app=Flask(__name__)

def cleanup():
	for pin in pins:
		GPIO.output(pin, 0)
	

@app.route('/')
def index():
	templateData = {
		'pins' : pins    ###PINs NAM KE PURE DICTONARY SEND HOGE PINS NAME SAI
      }
	return render_template('index.html', **templateData)

@app.route("/<action>")
def action(action): 
	if action == "open":
		GPIO.output(20, 1)
		GPIO.output(21, 0)
		sleep(2.5)
		cleanup()


	elif action == "close":
		GPIO.output(20, 0)
		GPIO.output(21, 1)
		sleep(2.5)
		cleanup()

	templateData = {
              'pins'    : pins,
								}
	return render_template('index.html', **templateData)
 

if(__name__=='__main__'):
	app.run(debug=True,host='0.0.0.0')
