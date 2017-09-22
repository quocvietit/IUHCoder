from webApp.app import app
import os

if __name__ == '__main__':
	#app.run(debug=True)
    app.secret_key = os.urandom(12)
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 80)))