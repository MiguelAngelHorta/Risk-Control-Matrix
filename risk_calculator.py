from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')  # Specify template folder

# Placeholder data (replace with database interaction)
controls = [
    {"id": 1, "name": "Control 1", "likelihood": 2, "impact": 1, "risk_score": 2},
    {"id": 2, "name": "Control 2", "likelihood": 3, "impact": 2, "risk_score": 6},
]

@app.route("/")
def index():
    return render_template("index.html", controls=controls)

@app.route("/add_control.html")
def add_control():
    return render_template("add_control.html")

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    likelihood = int(request.form["likelihood"])
    impact = int(request.form["impact"])
    risk_score = likelihood * impact
    new_control = {"id": len(controls) + 1, "name": name, "likelihood": likelihood, "impact": impact, "risk_score": risk_score}
    controls.append(new_control)
    return redirect("/")

@app.route("/update/<int:control_id>", methods=["GET", "POST"])
def update(control_id):
    control_to_update = next((control for control in controls if control["id"] == control_id), None)
    if not control_to_update:
        return "Control not found!", 404

    if request.method == "POST":
        control_to_update["name"] = request.form["name"]
        control_to_update["likelihood"] = int(request.form["likelihood"])
        control_to_update["impact"] = int(request.form["impact"])
        control_to_update["risk_score"] = control_to_update["likelihood"] * control_to_update["impact"]
        return redirect("/")

    return render_template("update.html", control=control_to_update)

@app.route("/delete/<int:control_id>")
def delete(control_id):
    global controls
    controls = [control for control in controls if control["id"] != control_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
