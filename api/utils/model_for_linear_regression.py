from .train import train_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def model_LR():
    df_conc_test, df_conc_train, y_train, y_test = train_model()
    #choosing model:
    model = LinearRegression()
    model.fit(df_conc_train, y_train)

    # File path to save the model
    model_file_path = "./models/lin_regres_houses.pkl"
    # Save the model to disk
    joblib.dump(model, model_file_path)
    model = joblib.load('./models/lin_regres_houses.pkl')

    y_pred= model.predict(df_conc_test)
    # mse = mean_squared_error(y_test, y_pred)
    # print("Mean Sqaured Error for this model is: ", mse)
    print("Score from train-set = ", model.score(df_conc_train, y_train))
    print("Score from test-set = ", model.score(df_conc_test, y_test))

    return y_pred
