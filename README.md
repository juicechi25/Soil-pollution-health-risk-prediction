# Is That Good Dirt?

A Flask-based machine learning web application that predicts potential health risks from soil pollution and environmental conditions.

## Overview

**Is That Good Dirt?** is a web application designed to let users enter environmental and soil-related information and receive a predicted disease-risk outcome from a trained machine learning model. The project combines a user-facing frontend, a Flask backend, and a trained prediction pipeline.

In this project, I worked on:
- building the prediction interface
- integrating the trained machine learning model into the app
- developing the full `predict.py` prediction workflow
- working with machine learning training workflows including data cleaning, preprocessing, and model training familiarity

## Features

- Web-based prediction form for user input
- Flask backend with API endpoint for predictions
- Real-time prediction response using a trained ML model
- Input preprocessing using Pandas
- Feature alignment, encoding, and scaling before inference
- Prediction output with confidence score and class distribution

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript, AJAX
- **Backend:** Flask, Python
- **Machine Learning / Data:** Pandas, Joblib, scikit-learn

## Project Structure

```text
project/
├── app.py
├── predict.py
├── scaler.pkl
├── label_encoder.pkl
├── X_encoded_columns.pkl
├── stack_model.pkl
├── templates/
│   └── index.html
└── static/
    └── app.js
```

## How It Works

1. The user fills in environmental and soil-related fields on the web interface.
2. The frontend sends the input data to the Flask backend through the `/predict` route.
3. The backend calls `handle_prediction_request()` from `predict.py`.
4. The input is cleaned, padded with defaults, encoded, aligned to training columns, and scaled.
5. The trained model generates a disease-risk prediction.
6. The app returns the predicted class, confidence score, and probability distribution as JSON.

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask pandas joblib scikit-learn
```

### 4. Run the app

```bash
python3 app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000
```

## Requirements

Make sure the following files are present in your project folder before running the app:

- `app.py`
- `predict.py`
- `scaler.pkl`
- `label_encoder.pkl`
- `X_encoded_columns.pkl`
- `stack_model.pkl`
- `templates/index.html`
- `static/app.js`

## Example Backend Routes

### Home route
- `GET /`
- Loads the main page using `index.html`

### Prediction route
- `POST /predict`
- Accepts JSON input and returns prediction results

Example response:

```json
{
  "prediction": "Disease Name",
  "confidence": 82.5,
  "distribution": {
    "Disease A": 82.5,
    "Disease B": 10.3,
    "Disease C": 7.2
  }
}
```

## Notes

- `index.html` must be placed inside the `templates/` folder.
- Any JavaScript file used by the page should be placed inside the `static/` folder.
- The `.pkl` files must be available in the correct path for the model to load successfully.
- If the page loads but prediction does not work, check whether `app.js` is correctly linked and whether the model files exist.

## Future Improvements

- Add better error handling and validation for user inputs
- Improve frontend styling and result visualisation
- Support more environmental variables and model options
- Deploy the application online for public access

## Author

**Tingyu (Judy) Chi**

