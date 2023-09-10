from flask import Flask, render_template
import os

app = Flask(__name__)

path = os.listdir()



@app.route('/')
def main():
	return render_template('index.html', path=path)

if __name__ == '__main__':
	app.run(debug=True)