from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="iris classifier API")

# Load your trained model
model = joblib.load("iris_model.joblib")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width:  float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to iris classifier API"}

@app.post("/predict/")
def predict_species(payload: IrisInput):
    # Build a single‑row DataFrame from the JSON body
    input_df = pd.DataFrame([payload.dict()])
    prediction = model.predict(input_df)[0]
    return {"prediction_class": prediction}
