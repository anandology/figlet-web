from flask import Flask, render_template, request, make_response
import subprocess
import os

app = Flask(__name__)

FONT = os.getenv("FIGLET_FONT", "standard")

def figlet(text, width=100, font=FONT):
    p = subprocess.Popen(["figlet", "-f", font, "-w", str(width), text], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.stdout.read().decode('utf-8')

@app.route("/api/figlet")
def api_figlet():
    text = request.args.get("text") or "Hello!"
    font = request.args.get("font") or FONT
    output = figlet(text, font=font)
    response = make_response(output, 200)
    response.mimetype = 'text/plain'
    return response

@app.route("/")
def index():
    text = request.args.get("text") or "Hello!"
    banner = figlet(text)
    return render_template("index.html", text=text, banner=banner, font=FONT)

if __name__ == "__main__":
    app.run()