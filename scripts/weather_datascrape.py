import pandas as pd
import numpy as np
import datetime as dt


def preprocess(hourly_data):

    # get the hourly weather report type
    df = hourly_data.loc[hourly_data['REPORT_TYPE'] == 'FM-15', :]

    # Extract the unscaled values for each column
    df.loc[:,'WND'] = (df['WND'].apply(lambda x: int(x.split(',')[-2])/10)
                                .replace(999.9, np.nan))
    
    df.loc[:,'TMP'] = (df['TMP'].apply(lambda x: int(x.split(',')[0])/10)
                                .replace(999.9, np.nan))
    
    df.loc[:,'DEW'] = (df['DEW'].apply(lambda x: int(x.split(',')[0])/10)
                                .replace(999.9, np.nan))
    
    df.loc[:,'SLP'] = (df['SLP'].apply(lambda x: int(x.split(',')[0])/10)
                                .replace(9999.9, np.nan))
    
    # Impute missing data using data from an hour before
    df.ffill(inplace=True)

    # Filter data to period between 2021-10 to 2022-04
    processed_data = df[(df['DATE'] >= '2023-07-01') & (df['DATE'] < '2024-01-01')]
    
    # Extract date and hour from datetime column
    processed_data.loc[:,'date'] = pd.to_datetime(df['DATE'])
    processed_data.loc[:,'hour'] = processed_data['date'].dt.hour
    processed_data.loc[:,'date'] = processed_data['date'].dt.date
    
    processed_data.rename({'WND':'wnd',
                           'TMP':'tmp',
                           'DEW':'dew',
                           'SLP':'atm'},
                           axis=1,
                           inplace=True)

    # Group by date and calculate daily averages
    daily_weather_df = processed_data.groupby('date').agg({
        'wnd': 'mean',   # Average wind speed
        'tmp': 'mean',   # Average temperature
        'dew': 'mean',   # Average dew point
        'atm': 'mean'    # Average atmospheric pressure
    }).reset_index()
    
    return daily_weather_df[['date', 'wnd', 'tmp', 'dew', 'atm']]

hourly_data = pd.read_csv('https://www.ncei.noaa.gov/data/global-hourly/access/2023/72505394728.csv')
preprocess(hourly_data)
