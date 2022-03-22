from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

FONT = os.getenv("FIGLET_FONT", "standard")

def figlet(text, width=100):
    p = subprocess.Popen(["figlet", "-f", FONT, "-w", str(width), text], stdout=subprocess.PIPE)
    return p.stdout.read().decode('utf-8')

@app.route("/")
def index():
    text = request.args.get("text") or "Hello!"
    banner = figlet(text)
    return render_template("index.html", text=text, banner=banner, font=FONT)

if __name__ == "__main__":
    app.run()