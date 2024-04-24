<h1 align="center"> KSI Predictor - Model, API and UI</h1>
<div align='center'>
  <img src="https://img.shields.io/badge/Sklearn-F7931E.svg?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="numpy">
  <img src="https://img.shields.io/badge/flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="python">  
  <img src="https://img.shields.io/badge/jupyter-F37626.svg?style=for-the-badge&logo=jupyter&logoColor=white" alt="python">
</div>

# Overview

The goal of this project is to develop a predictive software tool that can assess the likelihood of fatal collisions, benefiting both the police department and the general public. For law enforcement, the tool will aid in enhancing security measures and planning road conditions in specific neighborhoods. Meanwhile, individuals will be able to utilize the tool to evaluate the necessity for additional precautions based on factors such as weather conditions and time. Leveraging a dataset collected by the Toronto police department over five years, the project aims to create a predictive service that can classify incidents as either resulting in fatality or not, using relevant features.

> Dataset sourced: [Toronto Police Service's official](https://www.kaggle.com/code/dongliai/fatal-collision-prediction?scriptVersionId=172036764&cellId=5)  
> Data shape: (18194, 57)

# Notebook

A simplified version has been published on [Kaggle](https://www.kaggle.com/code/dongliai/fatal-collision-prediction).

## Process

1. Data Exploration  
    <image src="img/geographic.png" style="height:300px;">
    <image src="img/timewise.png" style="height:200px;">
2. Data Modelling  
    <image src="img/dataModelling.png" style="height:300px;">
3. Model Building  
    <image src="img/modelBuilding.png" style="height:300px;">
4. Evaluation  
    <image src="img/evaluation.png" style="height:350px;">

## Performance

1. Confusion Metrics

    <image src="img/confusionMetrics.png" style="height:150px;">

2. Classification Reports

    ```console
    STACK_CLF
    ======================
    Accuracy, Precision, Recall, F1: 
                    precision    recall  f1-score   support

            0  1.0000000 0.9928128 0.9963934      3061
            1  0.9927892 1.0000000 0.9963816      3029

        accuracy                      0.9963875      6090
    macro avg  0.9963946 0.9964064 0.9963875      6090
    weighted avg  0.9964136 0.9963875 0.9963875      6090

    BAGGINGCLASSIFIER_5
    ======================
    Accuracy, Precision, Recall, F1: 
                    precision    recall  f1-score   support

            0  1.0000000 0.9993466 0.9996732      3061
            1  0.9993402 1.0000000 0.9996700      3029

        accuracy                      0.9996716      6090
    macro avg  0.9996701 0.9996733 0.9996716      6090
    weighted avg  0.9996718 0.9996716 0.9996716      6090

    GRADIENTBOOSTINGCLASSIFIER_16
    ======================
    Accuracy, Precision, Recall, F1: 
                    precision    recall  f1-score   support

            0  1.0000000 0.9970598 0.9985277      3061
            1  0.9970375 1.0000000 0.9985166      3029

        accuracy                      0.9985222      6090
    macro avg  0.9985188 0.9985299 0.9985221      6090
    weighted avg  0.9985265 0.9985222 0.9985222      6090
    ```

3. ROC Curves

    <image src="img/roc1.png" style="height:180px;">
    <image src="img/roc2.png" style="height:180px;">
    <image src="img/roc3.png" style="height:180px;">

# API & UI

Rather than using heavy modern frameworks, this time I tried a different approach -- put everything in a small py file.  
I had to write string html strings, but it is super fun!

## Features

- The api is a single `app.py` file, but it is versatile and convenient.  
- It has a simple UI and easy to interact.
- It can smoothly do prediction, randomly choose test record, support customizing the test data, and display the result.  

## Installation

After clone and navigate to the directory, install the required dependencies using pip:

```console
pip install flask pandas joblib
```

## Usage

1. Run the `app.py` file:

    ```console
    python app.py
    ```

2. Click <http://127.0.0.1:5000/> to run the app.

    <image src="img/app2.png" style="height:420px;">

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
    <image src="img/app1.png" style="height:420px;">

    > Note: The actual target will display in the command line.  
        <image src="img/app3.png" style="height:30px;">

3. If you want to try one more, click <kbd>One More</kbd> to restore the form, or simply click <kbd>Lucky</kbd> to fill the data in one click.
