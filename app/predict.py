import joblib
import numpy as np



def prediction(item):
    
    model = joblib.load('./lin_regres_houses.pkl')

    log_prices = model.predict(item)
    power_prices = np.power(10, log_prices)

    rounded_prices = [round(price,2) for price in power_prices]
    predictions = [round(price,-2) for price in rounded_prices]

    return predictions

