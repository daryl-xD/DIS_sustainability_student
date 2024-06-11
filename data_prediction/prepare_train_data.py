import pandas as pd

# Load the the original dataset (clean_data) and temperature_data
df_building = pd.read_excel("store/predict/clean_data.xlsx")
df_temperature = pd.read_excel("store/predict/temperature_data.xlsx")

# make sure the 'date' columns for both dataframe is in datetime format
df_building['date'] = pd.to_datetime(df_building['date'], format='%Y-%m')  
df_temperature['date'] = pd.to_datetime(df_temperature['date'], format='%Y-%m')

# Merge the DataFrames on the 'date' column
df_building = # TODO: write your code here

# Extract unique codes from the 'code' column of df_building
unique_codes = # TODO: write your code here

# create a dictionary to assign a unique number to each unique code
# use a dictionary comprehension to map each unique code to a unique number
# enumerate over 'unique_codes' to get the index (i) and the code
# the index (i) is incremented by 1 to start the numbering from 1
code_number = {code: i + 1 for i, code in enumerate(unique_codes)}

# assign numbers to the 'code_number' column of df_building using the code_number dictionary
# map each value in the 'code' column of df_building to its corresponding number from the dictionary
df_building['code_number'] = # TODO: write your code here

# Save the modified DataFrame to an Excel file
output_file_path = 'store/predict/train_data.xlsx'
df_building.to_excel(output_file_path, sheet_name="Summary", index=False)