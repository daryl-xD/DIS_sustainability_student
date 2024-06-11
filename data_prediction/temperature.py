import pandas as pd

# Create a list to hold the date and mean temperature for each sheet
data = []

# Calculate mean temperature for each sheet 
# iterate over the years from 2018 to 2024
for year in range(2018, 2025):
    # iterate over the months from January (1) to December (12)
    for month in range(1, 13):

        # stop after April 2024
        # TODO: write your code here

        # format the sheet name as "YYYYMM"
        # TODO: write your code here

        try:
            # read the Excel file with each sheet_name (from 201801 to 202404) into a DataFrame
            df_weather = pd.read_excel("store/input/Weather_Data_Newton_2018_to_2024.xlsx", sheet_name=sheet_name)

            # convert the 'Mean Temperature (°C)' column to numeric, coercing errors to NaN
            df_weather['Mean Temperature (°C)'] = # TODO: write your code here

            # calculate the mean temperature for the current sheet (current month)
            mean_temp = # TODO: write your code here

            # append the date, and mean temperature to the list
            data.append({'date': f"{year}-{month:02d}", 'temperature': mean_temp})

        except Exception as e:
            # print an error message if the sheet could not be processed
            print(f"Failed to process {sheet_name}: {e}")

# convert the list of dictionaries to a DataFrame
df_temperature = # TODO: write your code here

# save the dataframe and export it in excel file with specified path 
output_file_path = 'store/predict/temperature_data.xlsx'
df_temperature.to_excel(output_file_path, index=False)
