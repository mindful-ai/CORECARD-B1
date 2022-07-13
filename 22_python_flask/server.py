from flask import Flask

app = Flask(__name__)

@app.route("/")    # http://127.0.0.1:5000/  capturing the request
def index():       # This is the response
    return ( "<h1>Hello world!</h1>" )

# http://127.0.0.1:5000/myname
@app.route("/myname")
def myname():       # This is the response
    return ( "<h1 style=\"color:blue\">{}</h1>".format('Purushotham') )

    
# LAB: Create a view for 127.0.0.1:5000/today to display today's date and time



if __name__ == "__main__":
    app.run()
