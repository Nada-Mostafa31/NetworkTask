from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello, Home Page"}


temperature = 27

@app.route("/temperature", methods=["GET"])
def client_get():
    return {"temperature": temperature}


@app.route("/temperature", methods=["POST"])
def client_post():
    global temperature
    data = request.get_json()
    temperature = data["temperature"]
    return {"message": "new Temperature", "value": temperature}


if __name__ == "__main__":
    app.run()
