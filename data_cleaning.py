import pandas as pd
import datetime
from utility.functions import calculate_working_days

# read the excel file and store its contents in a dataframe
df_basic = pd.read_excel("store/input/basic_data.xlsx")

# set the "code" column as the index of the dataframe for easier retrieve rows by index
# TODO: write your code here

# convert dataframe to dictionary with the index as key and the row data as value 
# easy access to row data by using the "code" as key
data_basic = # TODO: complete the code

# initialize an empty dictionary and set the variable as dataframe_building
# TODO: write your code here

# iterate through each item in data_basic for easier retrieval of relevant details
# "codes" as key and "details" as value 
for ___  , ___ in ___: # TODO: complete the code

    # Retrieve the value associated with the current "codes" key from data_basic
    data_building = # TODO: complete the code

    # specifies the sheet name to read and skip the first 11 rows to get the data needed 
    df_building = pd.read_excel("store/input/singland mock.xlsx", sheet_name=data_building['tab']) # TODO: complete the code

    # only keep columns that have value from df_building
    df_building = # TODO: complete the code
    
    # rename the columns
    df_building.columns = ["date", "energy", "water", "working_day"]

    # convert the DataFrame to a dictionary
    z = # TODO: complete the code

    # initialize an empty list to store row indices to drop
    row_to_drop = # TODO: complete the code

    # iterate through the items of the "date" column in the dictionary
    # check if the value is not an instance of datetime.datetime
    # if not, append the row index to the row_to_drop list
    # TODO: write your code here
        

    # drop the rows from the dataframe whose indices are in row_to_drop
    df_building = # TODO: complete the code

    # drop na/missing value based on energy and water from df_building
    # to ensure the data used for analysis is complete and accurate
    # TODO: write your code here

    # reset df_building index by dropping the old index
    # TODO: write your code here

    # calculate working days within each month. Exclude every Saturday, Sunday, and public holiday
    # use the function 'calculate_working_days' which import from utility 
    df_building = # TODO: complete the code

    # create a codes column to store the sheetname
    # TODO: write your code here

    # store df_building to dataframe_building with the respective sheetname
    dataframe_building[data_building['tab']] = df_building

# combine all DataFrames into a single DataFrame 
# making all the data easier to manage and manipulate
# TODO: write your code here

output_file_path = 'store/output/clean_data.xlsx'
# Save the combined DataFrame to an Excel file with the path given
# TODO: write your code here
