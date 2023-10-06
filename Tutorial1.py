from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
	# return "hihi <h1>hello</h1>"
	return render_template("index.html")

@app.route("/test")
def test():
	return render_template("main.html")
# @app.route("/<name>")
# def user(name):
# 	return f"Hello {name}!"
 
# @app.route("/admin")
# def admin():
# 	return redirect(url_for("user", name="admin!"))

if __name__ == "__main__":
	app.run(debug=True)
