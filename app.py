from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def feedback():
    msg = ""

    if request.method == "POST":
        text = request.form["text"]
        msg = "Thanks for feedback 👍"

    return render_template("feedback.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
