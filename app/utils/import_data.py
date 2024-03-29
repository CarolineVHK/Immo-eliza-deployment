import pandas as pd

def data_import(file_path):
    '''
    Importing the data from "./data/raw_data.csv"
    I will try later on from the url from 
    repo immo-eliza-scraping-Python_Pricers("https://raw.githubusercontent.com/bear-revels/immo-eliza-scraping-Python_Pricers/main/data/all_property_details.csv")

    Returns:
    A Full DataFrame containing the raw_material data from previous project.

    '''
    df_raw = pd.read_csv(file_path)

    #because the index will give some error when doing OneHot, I remove the index for now
    df_raw.to_csv(file_path, index = False)

    return df_raw


