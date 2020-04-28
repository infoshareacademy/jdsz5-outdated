
import pandas as pd
from matplotlib import pyplot as plt 

class Datasets:
    patient = 'data/PatientInfo.csv'
    region = 'data/Region.csv'
    weather = 'data/Weather.csv'
    def __str__(self):
        return 'Dostępne datasety: patient, region, weather'

def import_data(path=Datasets.patient):
    data = pd.read_csv(path)
    return data

def import_data(path=Datasets.region):
    data = pd.read_csv(path)
    return data   

def import_data(path=Datasets.weather):
    data = pd.read_csv(path)
    return data 
    
def plot_hist(df,column=None):
    
    if not column:
        column = df.columns[0]
        
    plt.hist(df[column])
    plt.title(column)


