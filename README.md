# Risk-Control-Matrix
This Flask web application helps manage security risks by allowing users to view, add, edit, and delete them along with their calculated severity levels.

## Dependencies
- brew install python@3.9
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- pip install Flask Jinja2

Run python server:
python3 risk_calculator.py

## Python Script
- Data and Functions:
  - Defines a list of dictionaries (risks) to store risk information (ID, description, likelihood, impact).
  - Includes functions to:
    - Calculate risk level based on likelihood and impact.
    - Generate unique risk IDs.
- Routes:
  - Displays a table of risks with their details and risk level on the main page (/).
  - Provides a form to add new risks (/add_risk.html).
  - Processes form data to create new risks (/create).
  - Allows updating existing risks (/update/<string:risk_id>) with GET and POST methods.
  - Deletes a risk based on ID (/delete/<string:risk_id>).
- Templates:
  - Renders the main page (index.html) displaying the risk table.
  - Provides a template (add_risk.html) for adding new risks.
  - Presents an update form (update.html) for modifying existing risks.
- Application Startup:
  - Runs the Flask application in debug mode (app.run(debug=True)) for easier development.
 
## HTML
- index.html: - Displays a table of security risks with details and risk level. - Provides a button to add new risks.
- add_risk.html: Contains a form for adding new risk information.
- update.html: Presents a pre-filled form to edit existing risk details.
