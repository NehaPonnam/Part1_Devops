from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_geek():
    print("Hello")
    return '<h1>Hello from Flask & Docker develoop changes</h2>'


if __name__ == "__main__":
    app.run(debug=True)
