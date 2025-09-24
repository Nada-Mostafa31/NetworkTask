from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/Temp",methods=["POST","GET"])
def Temp():
    if request.method=="POST":
        lastTemp= request.form["temperature"]
        return redirect(url_for("lastTemp",temp= lastTemp))

    else:
        return render_template("Temp.html")


temperature = 25  

@app.route("/LocalTemp", methods=["GET"])
def client_get():
    return {"temperature": temperature}

@app.route("/LocalTemp", methods=["POST"])
def client_post():
    global temperature
    data = request.get_json()
    temperature = data["temperature"]
    return {"message": "Temperature updated", "new_value": temperature}
    
@app.route("/<temp>")   
def lastTemp(temp):
    return f"Temprature is: {temp}"

if __name__=="__main__":
    app.run()