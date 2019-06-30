from flask import Flask, render_template

app = Flask(__name__) #instantiate the Flask class

@app.route("/") #if the path is empty
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)