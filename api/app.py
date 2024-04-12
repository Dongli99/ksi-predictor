from flask import Flask, request

import pandas as pd
import joblib
import random


app = Flask(__name__)

# Load the model and test data
with open("bagging_pipe.pkl", "rb") as file:
    model = joblib.load(file)
X_test = pd.read_csv("X_test.csv")
y_test = pd.read_csv("y_test.csv")

# Extract the dimension of data
n_records, n_features = X_test.shape[0], X_test.shape[1]
# Extract the specific column lists
features = X_test.columns.values
continuous = ["LATITUDE", "LONGITUDE"]
discrete = [f for f in features if f not in continuous]
integers = [f for f in features if X_test[f].dtype == "int64"]


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Index is the only page!
    It just display different pages according to the METHOD, and what button
    you clicked.
    """
    if request.method == "GET":
        page = render_form()
    else:  # If method is POST
        action = request.form.get("action")
        if action == "predict":  # Predict button is clicked
            page = render_form(display=True, predicted=True) + render_result()
        elif action == "lucky":  # Lucky button is clicked
            page = lucky()
        else:  # One More button is clicked, or any weird accident
            page = render_form()
    return page


def render_form(row=None, display=False, predicted=False):
    """
    Render the form elements in the page

    Args:
        row (int): The index of the record in data.
        display (bool): If True, display captured values rather than inputs.
        predicted (bool): If True, Turn Prediction button into One More.

    Return: The HTML string of the form
    """
    top = render_top()
    bottom = render_buttons(predicted)
    record = None if row is None else X_test.iloc[row].values
    form = top
    if display:
        form += render_display()
    else:
        form += render_table(record)
    form += bottom
    return form


def predict_data(record):
    """
    Central Control of the prediction.
    Accept a row form data, process, predict, and return the result string
    """
    try:
        record = process_input(record)
        prediction = model.predict(record)[0]
    except ValueError as ve:
        return f"{ve}"
    result = "Fatal" if prediction == 1 else "Not Fatal"
    return f"The accident is {result}."


def process_input(record):
    """
    Parse the request.form data into a single DataFrame for prediction
    """
    data = record.copy()
    for k in continuous:
        try:
            data[k] = float(data[k])
        except ValueError:  # In case a non numeric data is entered.
            raise ValueError(f"Cannot parse {k} to float.")
    for k in integers:
        data[k] = int(data[k])
    df = pd.DataFrame([[data.get(k) for k in features]], columns=features)
    return df


def lucky():
    """
    1. Generate a random index in the range of n_records
    2. Print the actual value in y_test for reference
    3. Return the rendered form with the generated index
    """
    index = random.randint(0, n_records - 1)
    print(
        f"Index: {index}, Actual Value: {y_test.iloc[index].values[0]}\
              (If never modified.)"
    )
    return render_form(index)


def render_top():
    """Render the top section of the form"""
    top = """
    <style> table { margin: 50 auto; }
            select { width: 216px; }
            caption {  }
            .result {text-align: center; color:red;}
    </style>
    <form method='POST'>
    <table><caption><h2>KSI Prediction - Group 3</h2></caption>
    """
    return top


def render_buttons(predicted=False):
    """
    Render the bottom buttons of the form
    If second button will be rendered according to the predicted parameter
    """
    buttons = """<tr><td>
        <button type="submit" name="action" value="lucky">Lucky</button>
        </td>"""
    if not predicted:
        buttons += """<td >
            <button type="submit" name="action" value="predict">Predict
            </button></td>"""
    else:
        buttons += """<td >
            <button type="submit" name="action" value="go_back">One More
            </button></td>"""
    buttons += "</tr></table></form>"
    return buttons


def render_table(record):
    """
    Render the table of the form
    If record is not None, it will fill the data in the boxes
    """
    table = ""
    for i in range(len(features)):
        f = features[i]
        if f in discrete:
            uniq_values = X_test[f].unique()
            options = ""
            for v in uniq_values:
                if record is not None and v == record[i]:
                    options += f"<option value='{v}' selected>{v}</option>"
                else:
                    options += f"<option value='{v}'>{v}</option>"
            table += f'<tr><td>{f}</td><td><select name="{f}">\
                {options}</select></td></tr>'
        else:
            if record is not None:
                table += f'<tr><td>{f}</td><td>\
                    <input type="text" name={f} size="27" value="{record[i]}">\
                    </td></tr>'
            else:
                small = X_test[f].min()
                large = X_test[f].max()
                table += f'<tr><td>{f}</td><td>\
                    <input type="text" name={f} size="27" \
                    placeholder="{small} ~ {large}"></td></tr>'
    return table


def render_display():
    """
    Render the table of submitted values after prediction is clicked.
    """
    display = ""
    for f in features:
        display += f"<tr><td>{f}</td><td>-- {request.form.get(f)} --</td></tr>"
    return display


def render_result():
    """
    Render the result of the prediction.
    """
    prediction = predict_data(request.form)
    return f'<div class="result">{prediction}</div>'


if __name__ == "__main__":
    app.run(debug=True)
