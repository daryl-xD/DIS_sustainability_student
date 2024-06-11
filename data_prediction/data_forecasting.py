import pandas as pd
from data_prediction.prediction import predict_chronos
from data_prediction.prediction import predict_lgbm

# load the training data
df_building = pd.read_excel("store/predict/train_data.xlsx")

# predict energy and water using lgbm model by calling 'predict_lgbm' function
df_lgbm =  # TODO: write your code here

output_file_path = 'store/output/clean_data_lgbm.xlsx'
# save the LightGBM predictions to an Excel file without the index
# TODO: write your code here

# predict energy and water using chronos by calling 'predict_chronos' function
df_chronos = # TODO: write your code here

output_file_path = 'store/output/clean_data_chronos.xlsx'
# save the Chronos predictions to an Excel file without the index
# TODO: write your code here