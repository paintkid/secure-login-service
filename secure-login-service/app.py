from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return("Flask server running")

if __name__ == '__main__':
    app.run(debug=True)