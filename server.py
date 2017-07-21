from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key='mykey'

@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0
	if not 'history' in session:
		session['history'] = ''
	data = {}
	data['gold'] = session['gold']
	data['history'] = session['history']
	return render_template('index.html', data=data)

@app.route('/process_money', methods=['POST'])
def process():
	builds = request.form['building']
	if builds == 'farm':
		randgold = random.randrange(10,20)
		message = "You earned "+str([randgold])+" gold from the farm! "
	if builds == 'cave':
		randgold = random.randrange(5,10)
		message = "You earned "+str([randgold])+" gold from the cave! "	
	if builds == 'house':
		randgold = random.randrange(2,5)
		message = "You earned "+str([randgold])+" gold from the house! "	
	elif builds == 'casino':
		randgold = random.randrange(-100, 50)
		if randgold <= 0:
			message = "You lost " + str([randgold]) + " gold to Vampire Casino! "
		elif randgold > 0:
			message = "You won " + str([randgold]) + " gold from Vampire Casino! "

	history = session['history']
	session['history'] = message + history
	session['gold'] += randgold
	print session['history']
	return redirect('/')

@app.route('/reset')
def reset():
	session['gold'] = 0
	session['history'] = ''
	return redirect('/')

app.run(debug=True)