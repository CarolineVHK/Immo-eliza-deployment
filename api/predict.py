import pickle
import numpy as np
#from api.utils.preprocessing_input_client import clean_select_data
#from api.utils.preprocessing_input_client import encoding
#from api.utils.preprocessing_input_client import preproces_json
# import os
# import platform


def prediction(item):
    
    model = pickle.load(open("lin_regres_houses.pkl", "rb"))
    breakpoint()
    log_prices = model.predict(item)
    power_prices = np.power(10, log_prices)
    #print("This is a list of the predictions the model made: ", final_prices)

    rounded_prices = [round(price,2) for price in power_prices]
    predictions = [round(price,-2) for price in rounded_prices]

    return predictions

    #save into file:
    # predictions_df = pd.DataFrame(predictions, columns=['Predicted_Price'])
    # predictions_df.to_json('predictions_new_data.json', index=False)
