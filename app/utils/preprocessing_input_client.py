import pandas as pd

def input_to_right_col(input):
    row = {
        "LivingArea": [input.LivingArea],
        "BedroomCount": [input.BedroomCount],
        'Province_Antwerp' : [1 if input.Province == "Antwerp" else 0],
        'Province_Brussels' : [1 if input.Province == "Brussels" else 0],
        'Province_East Flanders' : [1 if input.Province == "East Flanders" else 0],
        'Province_Flemish Brabant' : [1 if input.Province == "Flemish Brabant" else 0],
        'Province_Hainaut' : [1 if input.Province == "Hainaut" else 0],
        'Province_Liege' : [1 if input.Province == "Liege" else 0],
        'Province_Limburg' : [1 if input.Province == "Limburg" else 0],
        'Province_Luxembourg' : [1 if input.Province == "Luxembourg" else 0],
        'Province_Namur' : [1 if input.Province == "Namur" else 0],
        'Province_Walloon Brabant' : [1 if input.Province == "Walloon Brabant" else 0],
        'Province_West Flanders' : [1 if input.Province == "West Flanders" else 0]
    }
    df_input = pd.DataFrame.from_dict(row)

    return df_input


