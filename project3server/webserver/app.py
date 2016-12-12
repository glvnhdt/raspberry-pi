from mpd import MPDClient
from flask import Flask, render_template
from RPi import GPIO

# initialise flask, mpd client 
app = Flask(__name__)
client = MPDClient();
client.connect("localhost", 6600)
print('client created')

# handle the button event
def buttonEventHandler (pin):
	print "handling button event " + str( pin)
	client.stop()
	
# Set the pin numbering scheme to BCM (chip)
GPIO.setmode(GPIO.BCM)

#set pin 23 to input
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# let the GPIO library listen for an event on pin 23 
# and handle it with function buttonEventHandler
GPIO.add_event_detect(23, GPIO.RISING, bouncetime=400) 
GPIO.add_event_callback(23, buttonEventHandler)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/status')
def status():
	return render_template('text.html', text=client.status()['playlistlength'])

@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

@app.route('/play')
def play():
	client.clear()
	client.add('http://mp3.streampower.be/stubru-high.mp3')
	client.play(0)
	return render_template('page.html', name='playing')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
