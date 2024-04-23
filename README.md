<h1 align="center"> KSI Predictor - Model, API and UI</h1>

# Overview

Rather than using heavy modern frameworks, this time I tried a different approach -- put everything in a small py file.  
I had to write string html strings, but it is super fun!

# Features

- The api is a single `app.py` file, but it is versatile and convenient.  
- It has a simple UI and easy to interact.
- It can smoothly do prediction, randomly choose test record, support customizing the test data, and display the result.  
- It also has simple error handling for critical problem such as string entered into a box for float.

## Installation

After clone and navigate to the directory, install the required dependencies using pip:

```console
pip install Flask pandas joblib
```

## Usage

1. Run the `app.py` file:

    ```console
    python app.py
    ```

2. Click <http://127.0.0.1:5000/> to run the app.

## Interaction

1. If you are tired to enter data, click <kbd>Lucky</kbd>, the system will
   - Pick a record from `X_test`
   - Fill the boxes with the values from the record
   - Get the corresponding value from the `y_test`, and display it in the *command line*, so you can check the correctness.
  
    ```console
    # In Terminal, VS Code
    127.0.0.1 - - [11/Apr/2024 11:04:24] "POST / HTTP/1.1" 200 -
    Index: 2482, Actual Value: 0 (If never modified.)
    ```

2. When the input is ready, click <kbd>Predict</kbd> button.
3. If you want to try one more, click <kbd>One More</kbd> to restore the form, or simply click <kbd>Lucky</kbd> to fill the data in one click.  
