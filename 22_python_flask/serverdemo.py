from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/

@app.route('/')
def root():
    return ("<h1>Welcome to my website</h1>")

# http://127.0.0.1:5000/hello

@app.route('/hello')
def index():
    return ("<h1>Hello World!</h1>")

# http://127.0.0.1:5000/myname
@app.route("/myname")
def myname():       # This is the response
    return ( "<h1 style=\"color:blue\">Purushotham</h1>" )

if __name__ == "__main__":
    app.run()