from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')  # Specify template folder

# Risk-related routes
risks = [
    {"riskID": "R-0001", "riskDescription": "Risk 1", "likelihood": 2, "impact": 1},
    {"riskID": "R-0002", "riskDescription": "Risk 2", "likelihood": 3, "impact": 2},
]

def calculate_risk_level(likelihood, impact):
    risk_score = likelihood * impact
    if risk_score <= 5:
        return "Low"
    elif risk_score <= 10:
        return "Medium"
    else:
        return "High"

def generate_unique_risk_id():
    existing_ids = set(risk['riskID'] for risk in risks)
    i = 1
    while True:
        new_id = f"R-{i:04d}"
        if new_id not in existing_ids:
            return new_id
        i += 1

@app.route("/")
def index():
    for risk in risks:
        risk["risk_level"] = calculate_risk_level(risk["likelihood"], risk["impact"])
        # Check if controls data is already present, if not, assign a default value
        if "controls" not in risk:
            risk["controls"] = "Control measures here"  # Add your default control measures here
    return render_template("index.html", risks=risks)

@app.route("/add_risk.html")
def add_risk():
    return render_template("add_risk.html")

@app.route("/create", methods=["POST"])
def create():
    risk_description = request.form["riskDescription"]
    likelihood = int(request.form["likelihood"])
    impact = int(request.form["impact"])
    controls = request.form["controls"]
    new_risk = {
        "riskID": generate_unique_risk_id(),
        "riskDescription": risk_description,
        "likelihood": likelihood,
        "impact": impact,
        "controls": controls
    }
    risks.append(new_risk)
    return redirect("/")

@app.route("/update/<string:risk_id>", methods=["GET", "POST"])
def update(risk_id):
    risk_to_update = next((risk for risk in risks if risk["riskID"] == risk_id), None)
    if not risk_to_update:
        return "Risk not found!", 404

    if request.method == "POST":
        risk_to_update["riskDescription"] = request.form["riskDescription"]
        risk_to_update["likelihood"] = int(request.form["likelihood"])
        risk_to_update["impact"] = int(request.form["impact"])
        risk_to_update["controls"] = request.form["controls"]  # Update controls with control measures from form
        return redirect("/")

    return render_template("update.html", risk=risk_to_update)

@app.route("/delete/<string:risk_id>")
def delete(risk_id):
    global risks
    risks = [risk for risk in risks if risk["riskID"] != risk_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)