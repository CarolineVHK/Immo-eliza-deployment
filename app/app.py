from fastapi import FastAPI
from pydantic import BaseModel, Field, conint #BaseModel gives error if the imput is not correct
from typing_extensions import Literal, Annotated
from utils.preprocessing_input_client import input_to_right_col
from predict import prediction
import pandas as pd
import joblib
import pickle


#FastAPI
app2 = FastAPI()

#class: need to determine what you want to know from client:
class Predict_item(BaseModel):
    LivingArea: Annotated[int, Field(strict=True,gt=-1,lt=1001,
                                     default=200,description="This is the livingarea of your house")]
    #conint(gt=-1,lt=1001)=Field(default=200,description="This is the livingarea")
    #Annotated[int, Field(strict=True, gt=0)]
    Province: Literal['Antwerp', 'Brussels', 'East Flanders', 'Flemish Brabant', 'Hainaut', 'Liege', 
                      'Limburg','Luxembourg', 'Namur', 'Walloon Brabant', 'West Flanders'] = Field(
                          default='Brussels',
                          description="The Province your house is based.",
                          alias="Province")
    BedroomCount: int
    PropertySubType: Literal['HOUSE'] = Field(
                          default='HOUSE',
                          description="The type of property.",
                          alias="PropertySubType")
                    #can change Literal with apartment....
   
@app2.get('/')
def index():
    return f'page is alive'

@app2.get('/Welcom/{name}')
def welcome_name(name: str):
    return f'Welcom to the page {name}'

@app2.post('/predict/houses')
def predict_house(input:Predict_item):
    df_prep = input_to_right_col(input)
    result= prediction(df_prep)
    return {result[0]}  #prediction price showing up in streamlit


#to run the app:
#i use uvicorn app:app2 --reload in terminal



