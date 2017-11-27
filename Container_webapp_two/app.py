# this imports flask framework from Flask
from flask import Flask, render_template
from flask_restful import Api

# create an object of flask (flask is a web framework)
app = Flask(__name__)

# hello is a function with route on /test
@app.route("/test")
def test():
    return render_template("aboutme.html")

# main function, entry point
if __name__ == "__main__":
    # invokes app and runs the application
    app.run(host="0.0.0.0", port=7777)