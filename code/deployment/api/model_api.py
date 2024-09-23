# model_api.py
from fastapi import FastAPI
import pickle
from pydantic import BaseModel

# Load the trained model
with open('/app/models/trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

# Define input structure
class InputData(BaseModel):
    data: list

@app.post('/predict')
def predict(input_data: InputData):
    print(f'input_data: {input_data}')
    X_new = [input_data.data]
    print(f'X_new: {X_new}')
    prediction = model.predict(X_new)
    print(f'prediction: {prediction}')
    return {"prediction": prediction.tolist()}
