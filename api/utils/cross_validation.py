from sklearn.model_selection import cross_val_score, KFold
import numpy as np

from utils.model_for_linear_regression import model_LR
from utils.train import train_model

df_conc_test, df_conc_train,y_train, y_test = train_model()

# Define the number of folds for cross-validation
num_folds = 5

#cross-validation strategy
kf = KFold(n_splits=num_folds, shuffle=True, random_state=None)  # Set random_state if you want reproducible results

# Perform
scores = cross_val_score(model_LR, df_conc_train, y_train, cv=kf, scoring='neg_mean_squared_error')

# Convert scores to positive values
mse_scores = -scores

# Calculate mean and standard deviation of MSE scores
mean_mse = np.mean(mse_scores)
std_mse = np.std(mse_scores)

# Print the mean and standard deviation of MSE scores
print("Mean MSE:", mean_mse)
print("Standard Deviation of MSE:", std_mse)