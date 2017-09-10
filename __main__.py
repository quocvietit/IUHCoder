from WebApp.app import app
import os

if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
	#app.run(debug=True)
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 80)))
=======
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
>>>>>>> 188646349210b10aff9160a200d56c4d3432cc0a
=======
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 80)))
>>>>>>> origin/master
