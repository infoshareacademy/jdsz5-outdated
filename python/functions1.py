
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np 
import scipy.stats as st
from datetime import datetime

Datasets = {
    'current_dataset' : 'patient',
    'patient': {'path': 'data/PatientInfo.csv',
                'subset': ['sex', 'birth_year', 'age', 'country', 'confirmed_date', 'state'],
                'drop': ['global_num', 'disease', 'infection_order', 'infected_by', 'contact_number'],
                'name' : 'patient',
                'dates' : ['symptom_onset_date', 'confirmed_date', 'released_date'],
                'categorical' : ['sex', 'age', 'country', 'province', 'city', 'infection_case', 'state'],
                'count_col' : 'patient_id',
                'numerical': ['birth_year'],
                'counter' : ['birth_year','patient_id']
            },
    'region' : {'path' : 'data/Region.csv',
                'subset' : 'all',
                'drop' : 'all',
                'name' : 'region',
                'numerical' : ['elementary_school_count', 'kindergarten_count', 'university_count', 'academy_ratio', 'elderly_population_ratio', 'elderly_alone_ratio', 'nursing_home_count'],
                'categorical' : ['province', 'city' ],
                'count_col' : ['code'],
                'geo' : ['latitude', 'longitude'],
                'counter' : ['code']
    },
    'weather': {'path': 'data/Weather.csv',
               'subset': 'all',
               'drop': ['code','most_wind_direction'],
               'name': 'weather',
                'numerical' : ['min_temp','max_temp','precipitation','max_wind_speed', 'avg_temp', 'avg_relative_humidity'],
                'dates' : ['date'],
                'categorical': ['province', 'city']
               },
    'patient-region': { 'name' : 'patient-region',
                        'numerical' : ['birth_year', 'elementary_school_count', 'kindergarten_count', 'university_count', 'academy_ratio', 'elderly_population_ratio', 'elderly_alone_ratio', 'nursing_home_count'],
                        'categorical' : ['sex', 'age', 'country', 'province', 'city', 'infection_case', 'state'],
                        'count_col' : ['code', 'patient_id'],
                        'geo' : ['latitude', 'longitude'],
                        'counter' : ['code', 'birth_year','patient_id'],
                        'dates' : ['symptom_onset_date', 'confirmed_date', 'released_date']
    },
    'patient-weather': {'name' : 'patient-weather',
                        'numerical' : ['avg_temp', 'avg_relative_humidity', 'birth_year'],
                        'date' : ['date', 'symptom_onset_date', 'confirmed_date', 'released_date'],
                        'categorical' : ['sex', 'age', 'country', 'province', 'city', 'infection_case', 'state'],
                        'count_col' : ['patient_id'],
                        'counter' : ['birth_year','patient_id']


    }
}


# patient_region = pd.merge(patient, region, how='inner', on=['province', 'city'])
# patient_weather = pd.merge(patient, weather, how='inner', left_on=['confirmed_date', 'province'], right_on=['date', 'province'])

def set_current(dataset):
    Datasets['current_dataset'] = dataset['name']
    print(f'Obecnie pracujesz na tabeli {Datasets["current_dataset"]}')


def import_data():
    for dataset in Datasets:
        if dataset in ('patient', 'weather', 'region'):
            data = pd.read_csv(Datasets[dataset]['path'])
            if Datasets[dataset]['subset'] == 'all':
                data.dropna(how='all', inplace=True)
            else:
                data.dropna(subset=Datasets[dataset]['subset'], inplace=True)

            if Datasets[dataset]['drop'] == 'all':
                data.dropna(how='all')
            else:
                data.drop(columns=Datasets[dataset]['drop'], inplace=True)

            Datasets[dataset]['data'] = data
            print(f'Dataset {dataset} zostal zaimportowany')


def merge_data(dataset):
    if Datasets[dataset]['name'] != Datasets['current_dataset']:
        df1 = Datasets[Datasets['current_dataset']]['data']

        if Datasets['current_dataset'] == 'patient' and dataset == 'weather':
            df2 = Datasets['weather']['data']
            data = pd.merge(df1, df2, how='inner', left_on=['confirmed_date', 'province'],
                            right_on=['date', 'province'])
            name = 'patient-weather'
            Datasets['current_dataset'] = name
            Datasets[name]['data'] = data

        if Datasets['current_dataset'] == 'patient' and dataset == 'region':
            df2 = Datasets['region']['data']
            data = pd.merge(df1, df2, how='inner', on=['province', 'city'])
            name = 'patient-region'
            Datasets['current_dataset'] = name
            Datasets[name]['data'] = data

        if Datasets['current_dataset'] == 'weather' and dataset == 'patient':
            df2 = Datasets['weather']['data']
            data = pd.merge(df1, df2, how='inner', left_on=['confirmed_date', 'province'],
                            right_on=['date', 'province'])
            name = 'patient-weather'
            Datasets['current_dataset'] = name
            Datasets[name]['data'] = data

        if Datasets['current_dataset'] == 'region' and dataset == 'patient':
            df2 = Datasets['region']['data']
            data = pd.merge(df1, df2, how='inner', on=['province', 'city'])
            name = 'patient-region'
            Datasets['current_dataset'] = name
            Datasets[name]['data'] = data

        if Datasets['current_dataset'] == 'region' and dataset == 'weather':
            print('Nie mozna polaczyc tych datasetow')

        if Datasets['current_dataset'] == 'weather' and dataset == 'region':
            print('Nie mozna polaczyc tych datasetow')

        print('Datasety zostaly polaczone')

    else:
        print('Nie mozna polaczyc dwoch takich samych datasetow')


def show_current():
    print(f'Obecnie pracujesz na tabeli {Datasets["current_dataset"]}')


def describe_data():
    return Datasets[Datasets['current_dataset']]['data'].describe()


def head_data():
    return Datasets[Datasets['current_dataset']]['data'].head()

def show_columns():
    i = 1
    for column in Datasets[Datasets['current_dataset']]['data'].columns:
        print(f'{i}. {column}')
        i+=1


# Wykresy

def boxplot(categorical, numerical):
    df = Datasets[Datasets['current_dataset']]['data']
    try:
        if not df.dtypes[numerical] in ('float', 'int'):
            raise TypeError('Trzecia zmienna powinna byc numeryczna')

        if not df.dtypes[categorical] == 'object':
            raise TypeError('Druga zmienna powinna byc kategoryczna')

        if not isinstance(df, pd.DataFrame):
            raise TypeError('Pierwsza zmienna powinna byc data framem')

        df.pivot(columns=categorical, values=numerical).plot.box(figsize=(30, 20),fontsize=20)
        plt.tick_params(axis = 'both', which = 'major', labelsize = 24)
        plt.tick_params(axis = 'both', which = 'minor', labelsize = 16)
        plt.xlabel(categorical, fontsize=24);

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)


start_date = datetime(2020, 1, 15)
end_date = datetime(2020, 4, 15)

dates_range = pd.date_range(start_date, end_date, freq='D')

options = [(date.strftime(' %d %b %Y '), date) for date in dates_range]
index = (0, len(options) - 1)

selection_range_slider = widgets.SelectionRangeSlider(
    options=options,
    index=index,
    description='Dates',
    orientation='horizontal',
    layout={'width': '500px'}
)


def time_plot(data, dates, date_range):
    df = Datasets[Datasets['current_dataset']]['data']

    try:
        start = str(date_range[0])
        end = str(date_range[1])

        df = df[df[dates].between(start, end)]
        df.groupby(dates)[data].count().cumsum().plot.line(figsize=(30, 20),fontsize=20).legend(loc=2, prop={'size': 30})
        plt.tick_params(axis = 'both', which = 'major', labelsize = 24)
        plt.tick_params(axis = 'both', which = 'minor', labelsize = 16)
        plt.xlabel(dates, fontsize=24);

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)


def line_plot(dates, data, groupping):
    df = Datasets[Datasets['current_dataset']]['data']

    try:

        columns = df.pivot_table(index=dates, columns=groupping, values=data, aggfunc='count').count().sort_values(
            ascending=False).head(11).index
        df = df.pivot_table(index=dates, columns=groupping, values=data, aggfunc='count')[columns]
        df.plot.line(figsize=(30, 20), fontsize=20).legend(loc=2, prop={'size': 30})
        plt.tick_params(axis = 'both', which = 'major', labelsize = 24)
        plt.tick_params(axis = 'both', which = 'minor', labelsize = 16)
        plt.xlabel(dates, fontsize=24);

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)


def bar_plot(column, data):
    df = Datasets[Datasets['current_dataset']]['data']

    try:
        df.pivot_table(index=column, values=data, aggfunc='count').sort_values(by=data, ascending=False).head(10).plot.bar(figsize=(30, 20),fontsize=20).legend(loc=2, prop={'size': 30})
        plt.tick_params(axis = 'both', which = 'major', labelsize = 24)
        plt.tick_params(axis = 'both', which = 'minor', labelsize = 16)
        plt.xlabel(column, fontsize=24);

    except (KeyError, NameError):
        print('Niepoprawna nazwa zmiennej')

    except Exception as e:
        print(e)

def plot_hist(numerical):
    df = Datasets[Datasets['current_dataset']]['data']
    df[numerical].plot.hist(figsize=(30, 20),fontsize=20).legend(loc=2, prop={'size': 30})
    plt.tick_params(axis='both', which='major', labelsize=24)
    plt.tick_params(axis='both', which='minor', labelsize=16)
    plt.xlabel(numerical, fontsize=24);


def porownaj_srednie(a = 0.05):
    df = Datasets[Datasets['current_dataset']]['data']

    @interact
    def selectVariable(column1 = list(df.columns)):

        @interact
        def selectVariablevalue(var_column1 = list(df[column1].unique()),
                               var_column2 = list(df[column1].unique())):
            pass
            @interact
            def selectCounter(counter = Datasets[Datasets['current_dataset']]['counter']):
                sprawdz_rozklad1(df.loc[df[column1] == var_column1, counter])
                sprawdz_rozklad1(df.loc[df[column1] == var_column2, counter])
                
                try:
                    x = df.loc[df[column1] == var_column1, counter]
                    y = df.loc[df[column1] == var_column2, counter]
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
                          print('Istnieją przesłanki do odrzucenia hipotezy zerowej na rzecz alternatywnej - średnia pierwszej zmiennej jest niższa od średniej drugiej zmiennej')


                except TypeError:
                    print('Zmienne w podanych kolumnach muszą mieć charakter numeryczny')




                except:
                    print('Wystąpił nieoczekiwany błąd')



##Test normalności rozkładu wywolywany samodzielnie

def sprawdz_rozklad():
    df = Datasets[Datasets['current_dataset']]['data']
    @interact
    def test(column = list(df.select_dtypes('number').columns)):

        x= df[column]
        x.dropna(inplace=True) #konieczne jest usunięcie nanów by f-cja działała
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
                plt.show()

                #obliczanie wartości
                rozkladKS = st.kstwobign()

                Dn = max(np.abs(F - Fni))
                stTest = np.sqrt(N)*Dn
                pvalue = 1 - rozkladKS.cdf(stTest)

                print('\nDn = {}, p-value = {}, wartość p-value jest {} od Dn'.format(Dn, pvalue, 'większa' if pvalue > Dn else 'mniejsza'))

                if pvalue > Dn:
                    print('\nWartość pvalue jest wyższa od statystyki testowej Dn - można uznać, że próba podchodzi z rozkładu normalnego')

                else:
                    print('\nWartość pvalue jest niższa od statystyki Dn - nie można uznać, że próba pochodzi z rozkładu normalnego')


        except TypeError:
            print('Zmienne we wskazanej kolumnie muszą mieć charakter numeryczny.')
            
            
## Test normalnosci rozkladu wywolywany w funkcji porownaj_srednie            
def sprawdz_rozklad1(x):
    
    x.dropna(inplace=True) #konieczne jest usunięcie nanów by f-cja działała
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
            plt.show()

            #obliczanie wartości
            rozkladKS = st.kstwobign()

            Dn = max(np.abs(F - Fni))
            stTest = np.sqrt(N)*Dn
            pvalue = 1 - rozkladKS.cdf(stTest)

            print('\nDn = {}, p-value = {}, wartość p-value jest {} od Dn'.format(Dn, pvalue, 'większa' if pvalue > Dn else 'mniejsza'))

            if pvalue > Dn:
                print('\nWartość pvalue jest wyższa od statystyki testowej Dn - można uznać, że próba podchodzi z rozkładu normalnego')

            else:
                print('\nWartość pvalue jest niższa od statystyki Dn - nie można uznać, że próba pochodzi z rozkładu normalnego')


    except TypeError:
        print('Zmienne we wskazanej kolumnie muszą mieć charakter numeryczny.')





# Funkcja przeksztalcania roku w aktualny wiek
def obliczanie_wieku(column):
    df = Datasets[Datasets['current_dataset']]['data']

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
    df = Datasets[Datasets['current_dataset']]['data']
    try:
        data = df[data] * 1.0
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
       st.levene(x, y, center='trimmed')


def bootstrap_gender():
    patient = Datasets['patient']['data']
    x=np.array(patient.groupby(['sex', 'age']).count()['patient_id'].reset_index().loc[
                                    patient.groupby(['sex', 'age']).count()['patient_id'].reset_index()[
                                        'sex'] == 'male']['patient_id'])
    y=np.array(
    patient.groupby(['sex', 'age']).count()['patient_id'].reset_index().loc[
        patient.groupby(['sex', 'age']).count()['patient_id'].reset_index()['sex'] == 'female']['patient_id'])
    n=1000
    alpha=0.05
    pvalues = []

    for i in range(n):
        x_sample = np.random.choice(x, len(x), replace=True)
        y_sample = np.random.choice(y, len(y), replace=True)

        tst = st.ttest_ind(x_sample, y_sample)

        p = (tst.pvalue < alpha) * 1
        pvalues.append(p)

    print('Wynik testu istotny w {0} symulacji'.format("{:.1%}".format(np.mean(pvalues))))