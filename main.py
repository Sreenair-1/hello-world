from flask import Flask

app = Flask(__name__)

@app.route('/')
def run():
    print("User Authentication Feature Added")
    return "Hello World"

app.run()