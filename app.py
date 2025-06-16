from flask import Flask, render_template_string

app = Flask(__name__)

# Load index.html content
with open("index.html", "r") as f:
    page = f.read()

@app.route("/")
def home():
    return render_template_string(page)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

