from flask import request, Flask

app = Flask(__name__)

DATA = 'a'

@app.route('/compiler')
def compiler():
	return DATA


@app.route('/compiler', methods=['GET'])
def get():
	DATA = 'aaaa'


if __name__ == '__main__':
    app.run(debug = True, port=5555)