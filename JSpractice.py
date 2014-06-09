import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return 'JavaScript Practice'

if __name__ == '__name__':
	app.run(debug=True)
