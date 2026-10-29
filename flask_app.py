from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    """Serve the FCC slip-system visualizer page."""
    return render_template("index.html")


if __name__ == "__main__":
    # Open http://127.0.0.1:5000 in your browser after starting the app.
    app.run(host="127.0.0.1", port=5000, debug=True)
