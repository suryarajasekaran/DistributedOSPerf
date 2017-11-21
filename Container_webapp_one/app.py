# this imports flask framework from Flask
from flask import Flask

# create an object of flask (flask is a web framework)
app = Flask(__name__)

# hello is a function with route on /test
@app.route("/test1")
def test():
    return "Hello World!"

# main function, entry point
if __name__ == "__main__":
    # invokes app and runs the application
    app.run(host="0.0.0.0", port=8881)