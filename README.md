# MLOpsTest

## Overview

This project is part of the **Practical Machine Learning and Deep Learning** course. The main objective is to deploy a machine learning model as an API using FastAPI and create a web application using Streamlit that interacts with this API. The model API accepts input data from the web application, makes a prediction, and returns the result to the web application, which then displays the prediction.

## Main Task

The task consists of:
- **Deploying the model API**: This API receives requests from the web application, processes the input, and returns predictions.
- **Creating a web application**: The web app includes input fields for data, a button to submit the data for prediction, and a section to display the prediction result.
- **Dockerizing the application**: Both the API and the web application are deployed using Docker containers.

## Project Structure

```
├───code
│   ├───deployment
│   │   │   docker-compose.yml # Docker Compose file to manage multiple services
│   │   │
│   │   ├───api
│   │   │       Dockerfile     # Docker configuration file for the FastAPI app
│   │   │       model_api.py   # FastAPI application with the prediction endpoint
│   │   │
│   │   └───app
│   │           Dockerfile     # Docker configuration file for the Streamlit app
│   │           web_app.py     # Streamlit web application interacting with the API
│   │
│   └───models
│           train_model.py
│
├────models
|       trained_model.pkl      # Pre-trained machine learning model
|
└────README.md                 # Project documentation
```

### Files Description

- **`models/trained_model.pkl`**: The serialized machine learning model used for predictions.
- **`app/model_api.py`**: FastAPI application that serves as the API. It accepts input data, makes predictions using the pre-trained model, and returns the results.
- **`app/web_app.py`**: Streamlit web application that provides a user interface for submitting input data and displaying the prediction results.
- **`Dockerfile`**: Docker configuration for the FastAPI application.
- **`docker-compose.yml`**: Manages the deployment of both the API and the Streamlit web app within separate containers.

## How It Works

1. **Web Application**: 
    - The user enters the input data (in comma-separated format) in the input field.
    - Upon clicking the "Predict" button, the data is sent as a POST request to the FastAPI model API.

2. **Model API**: 
    - The FastAPI application receives the input data, processes it, and uses the pre-trained model to make a prediction.
    - The prediction is returned as a JSON response to the web application.

3. **Prediction Display**:
    - The Streamlit web application receives the response from the API and displays the prediction to the user.

## How to Run the Project

### Requirements

- Docker
- Docker Compose

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Post-Modern28/MLOpsTest.git
   cd MLOpsTest
   ```

2. **Build and run the Docker containers**:
   ```bash
   cd code/deployment
   docker-compose up --build
   ```

3. **Access the web application**:
   Open a browser and go to:
   ```
   http://localhost:8501
   ```

   This will open the Streamlit web application where you can enter input data for predictions.

4. **Make a prediction**:
   - Enter a comma-separated list of values into the input field (e.g., `5.1,3.5,1.4,0.2`).
   - Click the "Predict" button.
   - The prediction result will be displayed on the same page.

## API Endpoint

- **URL**: `http://localhost:8000/predict`
- **Method**: `POST`
- **Input**: JSON object containing a list of numerical values (e.g., `[5.1, 3.5, 1.4, 0.2]`).
- **Output**: JSON object with the prediction result.

### Example

#### Request
```json
{
  "data": [5.1, 3.5, 1.4, 0.2]
}
```

#### Response
```json
{
  "prediction": [0]
}
```

