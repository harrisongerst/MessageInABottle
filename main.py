from flask import Flask, render_template
from pymongo import MongoClient
from flask.ext.headers import headers

app = Flask(__name__)
client = MongoClient('ds059692.mongolab.com', 59692)
client.messageinabottle.authenticate('admin', 'password')


db = client.messageinabottle
messTable = db.messages
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/post/<string:mess_text>', methods = ['POST', 'OPTIONS'])
@headers({'Access-Control-Allow-Origin': '*'})
def post(mess_text):
	p = { 'text': mess_text

	}
	post_id = messTable.insert_one(p).inserted_id
	print post_id
	return mess_text

@app.route('/message', methods = ['GET', 'OPTIONS'])
@headers({'Access-Control-Allow-Origin': '*'})
def message():
	m = messTable.find_one()
	return m



if __name__ == '__main__':
	app.run(host = '0.0.0.0')
