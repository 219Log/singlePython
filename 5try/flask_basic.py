from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    # * Runs the development server on localhost:5000
    # ! Do not use this in production. Use a proper WSGI server.
    app.run(host="127.0.0.1", port=5000, debug=True)