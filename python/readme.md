
# JDSZ5-Outdated projekt python
# Data Science for COVID-19 (DS4C)
## DS4C: Data Science for COVID-19 in South Korea
## ANALIZA EPIDEMII KORONA WIRUSA W KOREI POŁUDNIOWEJ

## Opis
Aplikacja pozwala nam na wyświetlenie statystyki opisowej dostępnych baz, rysowanie histogramów, wykresów pudełkowych, wykresu liniowego dla wybranego przedzialu czasowego dla wybranej kolumny z dostępnych zbiorów danych. 
Następnie sprawdzany jest przedział ufności dla średniej wybranej kolumny. Aplikacja pozwala na przeprowadzenie testów zbieżności rozkładu wybranej funkcji do rozkładu narmalnego oraz porównania średnich wybranych funkcji, pozwalający na porównanie przebiegu epidemi wśród osób różnych płci i w różych prowincjach Koreii Południowej. Ostatnią funkcjonalnością aplikacji jest przeprowadzenie testu Monte-Carlo, który pozwoli porównanie średniej zachorowalność wśród osób różnych płci.

## Użycie 
Właściwą aplikacją jest notebook app.ipynb
```python
print(Datasets())
```
Wypisze nam dostępne do analizy zbiory danych - Po pobraniu zbioru za pomocą funkcji ```import_data```, będziemy mogli zaimportować dane. Za pomocą funkcji ```description``` opisać główne statystyki, ```przedzialy_ufnosci_srednia```  sprawdzić  przedział ufności dla średniej wybranej kolumny, ```porownaj_srednie``` porównanać średnie wybranych funkcji, ```boxplot```,```time_plot```,```line_plot```,```time_plot``` pozwolą na narysowanie odpowiednich wykresów. Funkcje ```sprawdz_rozklad```i ```poróbnaj średnie``` wywołują testy statystyczne odpowiednio zbieżności rozkładu wybranej funkcji do rozkładu narmalnego oraz porównania średnich wybranych funkcji. Za pomocą funkcji ```bootstrap``` można przeprowadzić Monte-Carlo, który pozwoli porównanie średniej zachorowalność wśród osób różnych płci.

## Pakiety
```
pandas==0.24.2
matplotlib==3.0.3
ipywidgets==7.5.1
```

## link bazy:
https://www.kaggle.com/kimjihoo/coronavirusdataset