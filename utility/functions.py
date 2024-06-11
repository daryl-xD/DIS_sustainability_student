import pandas as pd

def calculate_working_days(dataframe):
    """
    Calculates the number of working days for each month in a DataFrame.
    Args: dataframe: A DataFrame with a 'month' column containing datetime objects.
    Returns: A DataFrame with the same index as the input DataFrame, containing a
    'working_days' column with the number of working days for each month.
    """
    # read the data for public holiday from the excel file 
    df_holiday = pd.read_excel("../MOM_PublicHoliday.xlsx")

    # create a column for the dataframe to store the calculated 'working_day' for each month by intializing the value as 0 
    # TODO: write your code here

    # iterate through the input dataframe to calculate the 'working_day' for each month
    # remove the public holidays from all the weekdays for each month of the year 
    for index, row in dataframe.iterrows():

        # retrieve the 'date' from the current row
        month = # TODO: write your code here

        # set the 'start_date' to the first day of the month extracted from 'month'
        start_date = # TODO: write your code here

        # calculate the 'end_date' as the last day of the same month
        end_date = # TODO: write your code here

        # create a list of weekdays (Monday to Friday) between 'start_date' and 'end_date'
        weekdays = # TODO: write your code here

        # filter out the public holidays from 'df_holiday' dataframe for the given month and year
        holidays = # TODO: write your code here

        # calculate the number of working days by subtracting the number of holidays from total weekdays
        working_days = # TODO: write your code here

        # assign the calculated 'working_days' to 'working_day' column for corresponding row 
        dataframe.at[index, 'working_day'] = working_days
    return dataframe

def calculate_carbon(row, variable, intensity):
    """
    Calculate the carbon emissions for a given row of data based on 'energy' and 'water'.
    Args:
    row: An object represents a row of dataframe that includes key like month, energy and water. 
    variable: A string as the type of variable to calculate emissions for 'energy' or 'water'.
    intensity: A dictionary with the value'grid_emission_factor' for energy and 'water_factor' for water.
    Returns: A float that calculated carbon emissions based on the input row, variable and intensity.
    """
    # extract year from the 'date' column of the row 
    year = # TODO: write your code here

    # select the appropriate emission factor from the intensity dict based on the specified variable and the year
    # 'variable' can be either 'energy' or 'water', and it determines which factor to use
    # calculate and return the carbon emissions for the specified variable by multiplying the value in the current row with the emission factor
    # TODO: write your code here

