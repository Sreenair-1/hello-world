from flask import Flask

app = Flask(__name__)

@app.route('/')
def run():
    print("User Authentication Feature Added")
    return "Hello World from Main Branch"

@app.route("/test")
def test():
    return "Application test successful"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)