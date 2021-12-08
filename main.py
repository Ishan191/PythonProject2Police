import pandas as pd
data = pd.read_csv(r"C:\Users\Ishan\Documents\PythonPractice\Project2PoliceDatasets\PoliceData.csv")
data.isnull().sum()
data.drop(columns = 'country_name', inplace = True) # Removing completely empty country name column
data[data.violation == "Speeding"].driver_gender.value_counts() # Which gender has more violations
data.groupby('driver_gender').search_conducted.sum()
data.search_conducted.value_counts() # Searching true number of search conducted
data.stop_duration.value_counts()
data['stop_duration']= data['stop_duration'].map( {'0-15 Min' : 7.5 , '16-30 Min' : 24 ,'30+ Min' : 45 })
data['stop_duration'].mean() # Mean of stop duration
data.groupby('violation').driver_age.describe() # Age distribution of each violation
