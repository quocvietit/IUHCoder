from flask import request, Flask

app = Flask(__name__)

@app.route('/runcode', methods=['POST'])
def compiler():
	s
	return 


if __name__ == '__main__':
    app.run(debug = True, port=5555)