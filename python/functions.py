
import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np 
import scipy.stats as st



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

def description(df,column=None):

    try:
        
        if not column:
            column = df.columns[0]


        df[column].describe()

    except TypeError:
        print('Zmienne we wskazanej kolumnie muszą mieć charakter numeryczny.')
    

## Funkcja porównująca średnie

# zanim dodałem if - wskazując dwie te same kolumny dostawałem p-value = 0 czyli należałoby
# uznać, że średnie w między kolumnami się różnią :P 


def porownaj_srednie(x,y, a = 0.05):
    
    if x is y:
        print('Należy wybrać dwie różne kolumny.')
        
    else:
        
        try:
            mx = np.mean(x)
            my = np.mean(y)
            nx = len(x)
            ny = len(y)

            sx = np.std(x)
            sy = np.std(y)

            u = mx - my/np.sqrt(sx**2/nx + sy**2/ny)
            
            rozkladNormalny = st.norm()

            pvalue = rozkladNormalny.cdf(u)


            print('Wartość p-value {} jest {} niż wartość a {}'.format(pvalue, 'większa' if pvalue >a else 'mniejsza', a))

            if pvalue > a:
                  print('Nie ma podstaw do odrzucenia hipotezy zerowej')
            else:
                  print('Istnieją przesłanki do odrzucenia hipotezy zerowej na rzecz alternatywnej - średnia mx jest niższa od średniej my')


        except TypeError:
            print('Zmienne w podanych kolumnach muszą mieć charakter numeryczny')



            
        except:
            print('Wystąpił nieoczekiwany błąd')




##Test normalności rozkładu

def sprawdz_rozklad(x):
    #x.dropna(inplace=True) #konieczne jest usunięcie nanów by f-cja działała
    N = len(x)
    
    try:
        if N <= 100:
            #Test Shapiro-Wilka
            st.shapiro(x)
            test = st.shapiro(x)[0]
            pvalue = st.shapiro(x)[1]
            
            print('Statystyka testowa = {}, p-value = {}, wartość p-value jest {} od statystyki testowej'.format(test, pvalue, 'większa' if pvalue > test else 'mniejsza'))

            if pvalue > test:
                print('Wartość pvalue jest wyższa od statystyki testowej - można uznać, że próba podchodzi z rozkładu normalnego')

            else:
                print('Wartość pvalue jest niższa od statystyki testowej - nie można uznać, że próba pochodzi z rozkładu normalnego')

            
            
        else:
            #Test Kołomogowa-Smirnova
            #Ewentualnie zamiast rysowania tutaj wykresu można przywołać zdefiniowaną funkcję
                      
            
            x = np.array(x)
            x = x.reshape(N,)

            #plt.hist(x, bins = 25, edgecolor = 'black')
            
            mx = np.mean(x)
            sx = np.std(x)
            
            rozkladNormalny = st.norm(mx,sx)
            
            xsorted = np.sort(x)
            
            F = rozkladNormalny.cdf(xsorted)
            
            Fni = np.fromiter(range(1, N+1), dtype =int)/N
            
            #wykres dystrybuanty
            plt.plot(xsorted,F,color="black")
            plt.scatter(xsorted, Fni, color="red")
            plt.legend(["F(x)","Fni"])
            
            #obliczanie wartości
            rozkladKS = st.kstwobign()

            Dn = max(np.abs(F - Fni))
            stTest = np.sqrt(N)*Dn
            pvalue = 1 - rozkladKS.cdf(stTest)

            print('Dn = {}, p-value = {}, wartość p-value jest {} od Dn'.format(Dn, pvalue, 'większa' if pvalue > Dn else 'mniejsza'))

            if pvalue > Dn:
                print('Wartość pvalue jest wyższa od statystyki testowej Dn - można uznać, że próba podchodzi z rozkładu normalnego')

            else:
                print('Wartość pvalue jest niższa od statystyki Dn - nie można uznać, że próba pochodzi z rozkładu normalnego')


    except TypeError:
        print('Zmienne we wskazanej kolumnie muszą mieć charakter numeryczny.')

