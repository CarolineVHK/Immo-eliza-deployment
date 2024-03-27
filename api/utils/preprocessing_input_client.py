import pandas as pd
import numpy as np
import json
# from .import_data import data_import
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import OneHotEncoder

#class Preprocessing:

def preproces_json(input):
    #same columns as the trained data:
    order_col = ['LivingArea', 'Province', 'BedroomCount', 'PropertySubType']
    #creating dataframe to work with model: with input data the json-file from web.
    df_input = pd.DataFrame([input], columns=order_col)

    # # File path where you want to save the JSON file
    # file_path = "data_from_input_api.json"
    # # Convert Python dictionary to JSON string
    # json_string = json.dumps(input, indent=4)
    # # Write JSON string to a file
    # with open(file_path, "w") as json_file:
    #     json_file.write(json_string)
    # print("JSON file saved successfully.")

    return df_input

def preprocessing_input(df_input):
    '''if one column is missing, need to add others and place a 0 as a value for:
    Province_Antwerp, Province_Brussels ,Province_East Flanders ,Province_Flemish Brabant,Province_Hainaut ,
    Province_Liege ,Province_Limburg ,Province_Luxembourg,Province_Namur ,Province_Walloon Brabant,
    Province_West Flanders
    '''
    list_province = ["Province_Antwerp", "Province_Brussels" , "Province_East Flanders", "Province_Flemish Brabant",
                     "Province_Hainaut", "Province_Liege", "Province_Limburg", "Province_Luxembourg", 
                     "Province_Namur", "Province_Walloon Brabant", "Province_West Flanders"]
    #df province with value 1:
    df_provinces = pd.DataFrame(0, index=[0], columns=list_province)

    #handling column 'Province'
    #copy original
    df_change = df_input.copy()
    for province in df_input['Province'].unique():
        #create column 'Province_{province}' =1 
        df_province = df_input['Province'] == province
        df_change[f'Province_{province.replace(" ", "_")}'] = df_province.astype(int)
        print(type(df_change),type(df_province))
        print(type(province), province.replace(" ", "_"))
    # Drop the original "Province" and "PropertySubType" column
    df_change.drop(columns=['Province','PropertySubType'], inplace=True) #return: df_change    LivingArea  BedroomCount  Province_Brussels
                                                                                        #0         200             4                  1

    #concat 2 df:!!  'Province_{province}' =1  needs to stay 1!!
    df_conc = pd.concat([df_change, df_provinces], axis=1)
    #print("df_conc",df_conc)
    return df_conc #--> return df_conc    LivingArea  BedroomCount  Province_Brussels  ...  Province_Namur  Province_Walloon Brabant  Province_West Flanders
                                #0         200             4                  1  ...               0                         0                       0
                                #[1 rows x 14 columns]

#testing:
input = {
  "LivingArea": 200,
  "Province": "Brussels",
  "BedroomCount": 2,
  "PropertySubType": "HOUSE"
}


# Preprocess JSON input
df_input = preproces_json(input)

# Perform one-hot encoding
df_output = preprocessing_input(df_input)

print(df_output)





def clean_select_data(file_path):
    """
    Preprocess the data.

    Parameters:
    - df_raw: DataFrame containing the raw data.

    Returns:
    - df: DataFrame containing the preprocessed data.
    """
        
    df_raw = data_import(file_path)
    #selecting only the data for houses
    df = df_raw[df_raw['PropertySubType'] == 'HOUSE']
    #For the model I only want to work with the variable with the best correlation (Price-LivingArea-BedroomCount):
    df = df[['Price', 'LivingArea','Province','BedroomCount','PropertySubType']]
    #removing the rows with empty Prices and LivingArea
    df.dropna(subset=['Price', 'LivingArea'], inplace=True)
    #removing index from df because otherwise it gives NaN-values becaus after cleaning, indexes are non exsistent
    df.reset_index(drop=True, inplace=True) 
    #log10 from np on price: reduce effect from outliers
    df['Price'] = np.log10(df['Price'])

    #saving the new dataFrame:
    #path for the CSV file
    output_file_path = "./data/preprocessed_data.csv"
    # Save df to CSV file
    df.to_csv(output_file_path, index=False)

    return df

def encoding(new_data):
    df = clean_select_data('./data/raw_data.csv')
    #split the data
    #1. defining X (without the target-variable) and y (=target-value):
    X = df.drop(columns=['Price','PropertySubType'], axis=1)
    y = df['Price']
    #2. create the training and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  #training with 20% of the dataset

    #dealing with categorical data for'Province': turn categories into numbers:
    one_hot = OneHotEncoder(handle_unknown = "ignore", sparse_output=False)
    transformed_X_train = one_hot.fit_transform(X_train[['Province']])

    transformed_X_new_data = one_hot.transform(new_data[['Province']])
    transformed_X_new_data = pd.DataFrame(transformed_X_new_data, columns=one_hot.get_feature_names_out(['Province']))
    #add transfromed_X_df to the original df
    df_conc_new_data = pd.concat([new_data.reset_index(), transformed_X_new_data], axis=1).drop(["Province","Price","PropertySubType"], axis=1)

    return df_conc_new_data

