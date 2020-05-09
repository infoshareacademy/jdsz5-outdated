
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
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

            
def description(x):
    return dfs[x].describe()


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


# Wykresy

def boxplot(df, categorical, numerical):
    try:
        if not df.dtypes[numerical] in ('float', 'int'):
            raise TypeError('Trzecia zmienna powinna byc numeryczna')

        if not df.dtypes[categorical] == 'object':
            raise TypeError('Druga zmienna powinna byc kategoryczna')

        if not isinstance(df, pd.DataFrame):
            raise TypeError('Pierwsza zmienna powinna byc data framem')

        df.pivot(columns=categorical, values=numerical).plot.box()

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)


def time_plot(df, data_col, dates_col, **kwargs):
    try:
        start = kwargs.get('start', None)
        end = kwargs.get('end', None)

        if start == None and end != None:
            df = df[df[dates_col] <= end]

        elif end == None and start != None:
            df = df[df[dates_col] >= start]

        elif start == None and end == None:
            df = df
        else:
            df = df[(df[dates_col] >= start) & (df[dates_col] <= end)]

        df.groupby(dates_col)[data_col].count().cumsum().plot()

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)


def line_plot(df, index, columns, values, aggfunc='count'):
    try:
        return df.pivot_table(index=index, columns=columns, values=values, aggfunc=aggfunc).plot()

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)


def bar_plot(df, columns, values, aggfunc='count'):
    try:
        return df.pivot_table(columns=columns, values=values, aggfunc=aggfunc).plot.bar()

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)


# Funkcja przeksztalcania roku w aktualny wiek
def obliczanie_wieku(df, column):
    try:
        data = np.array(df[column].dropna().values)
        f = lambda x: pd.datetime.now().year - x
        wiek = f(data)

        return wiek

    except TypeError:
        print('Dane powinny byc rokiem urodzenia')

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)

# Obliczanie przedzialow ufnosci
def przedzialy_ufnosci_srednia(data, confidence):
    try:
        data = 1.0 * data
        n = len(data)
        mean = np.mean(data)
        sterr = st.sem(data)
        h = sterr * st.t.ppf((1 + confidence) / 2.0, n - 1)
        return f'Srednia: {mean}. Przedzialy ufnosci: {mean - h}, {mean + h}'

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)
        
# test porównania wariancji
def porownaj_wariancje(x,y, z='trimmed'):
    
    if x is y:
        print('Należy wybrać dwie różne kolumny.')
        
    else:
        
        try:
            st.levene(x, y, center='trimmed')