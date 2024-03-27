from fastapi import FastAPI
from pydantic import BaseModel, Field, conint #BaseModel gives error if the imput is not correct
from typing_extensions import Literal, Annotated
from utils.preprocessing_input_client import preproces_json, preprocessing_input
from predict import prediction
import pandas as pd
import joblib
import pickle


#FastAPI
app2 = FastAPI()

#class: need to determine what you want to know from client:
class Predict_item(BaseModel):
    LivingArea: Annotated[int, Field(strict=True,gt=-1,lt=1001,
                                     default=200,description="This is the livingarea")]
    #conint(gt=-1,lt=1001)=Field(default=200,description="This is the livingarea")
    #Annotated[int, Field(strict=True, gt=0)]
    Province: Literal['Antwerp', 'Brussels', 'East Flanders', 'Flemish Brabant', 'Hainaut', 'Liege', 
                      'Limburg','Luxembourg', 'Namur', 'Walloon Brabant', 'West Flanders'] = Field(
                          default='Brussels',
                          description="The Province you live in.",
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
    var = preproces_json(input.dict())
    df_prep = preprocessing_input(var)
    result= prediction(df_prep)
    print(result)




# @app2.post('/predict/houses')
# async def predict_house(item:Predict_item):
#     df = pd.DataFrame([item.dict().values()], columns = item.dict().keys())
#     ypred = prediction(df)
#     return f'price predictions is : {int(ypred)}'


# @app2.post('/predict/houses')
# def predict_hous(input:data_variables,):
#     print('One moment, the model is calculating the predictions...')
#     df = pd.DataFrame([input.dict()])
#     print(df)
#     price_prediction = prediction(df)

#     return f'Prediction price is: {price_prediction}'



# @app2.post('/predict/houses')
# def predict_price(temp_variable:data_variables):
#     temp_variable = temp_variable.dict()
#     print(temp_variable) #debug prints
#     LivingArea = temp_variable['LivingArea']
#     print(LivingArea) #debug prints
#     Province = temp_variable['Province']
#     BedroomCount = temp_variable['BedroomCount']
#     PropertySubType = temp_variable["PropertySubType"]
#     print(model.predict([[LivingArea,Province,BedroomCount,PropertySubType]])) #debug prints
#     print('hello') #debug prints
#     prediction = model.predict([[LivingArea,Province,BedroomCount,PropertySubType]])
#     #print(prediction) #debug prints
#     return f'Prediction price is: {prediction}'














#to run the app:
#i use uvicorn app:app2 --reload in terminal but you can also do:

#if __name__ == '__main__':
#uvicorn.run(app, host='127.0.0.1, port=8000)


