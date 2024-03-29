from .preprocessing_input_client import clean_select_data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

import pandas as pd

def train_model():
    """
    Train a linear regression model.

    Parameters:
    - X_train: DataFrame containing the features for training.
    - y_train: Series containing the target variable for training.

    Returns:
    - model: Trained linear regression model.
    """
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
    #converting output into a DataFrame
    transformed_X_df_train = pd.DataFrame(transformed_X_train, columns=one_hot.get_feature_names_out(['Province']))
    #add transfromed_X_df to the original df
    df_conc_train = pd.concat([X_train.reset_index(), transformed_X_df_train], axis=1).drop("Province", axis=1)

    transformed_X_test = one_hot.transform(X_test[['Province']])
    #converting output into a DataFrame
    transformed_X_df_test = pd.DataFrame(transformed_X_test, columns=one_hot.get_feature_names_out(['Province']))
    #add transfromed_X_df to the original df
    df_conc_test = pd.concat([X_test.reset_index(), transformed_X_df_test], axis=1).drop("Province", axis=1)

    return df_conc_test, df_conc_train,y_train, y_test
