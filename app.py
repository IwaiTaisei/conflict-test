from flask import flask, render_template

app = Flask(_name_)

@app.route("/")
def top_page():
    return render_template("index.html")

if _name_ == "_main_":
    app.run(debug=true)
