from flask import Flask

app= Flask(__name__)

@app.route("/")
def main ():
    return "Welcome to the service web"

if __name__ == "__main__":
    app.run()