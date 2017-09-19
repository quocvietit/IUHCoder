from flask import request, Flask

app = Flask(__name__)

@app.route('/compiler', methods=['POST'])
def compiler():
	request.get
	return 


if __name__ == '__main__':
    app.run(debug = True, port=5555)