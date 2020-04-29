
# JDSZ5-Outdated projekt python
# Data Science for COVID-19 (DS4C)
## DS4C: Data Science for COVID-19 in South Korea
## ANALIZA EPIDEMII KORONA WIRUSA W KOREI POŁUDNIOWEJ

## Opis
Aplikacja pozwala nam na wyświetlenie statystyki opisowej, rysowanie histogramów i dystrybuant wybranej kolumny z dostępnych zbiorów danych. Następnie przeprowadzenie testów zbieżności rozkładu wybranej funkcji do rozkładu narmalnego oraz porównania wariancji wybranych funkcji, pozwalający na porównanie przebiegu epidemi wśród osób różnych płci i w różych prowincjach Koreii Południowej. Ostatnią funkcjonalnością aplikacji jest przeprowadzenie testu Monte-Carlo, który pozwoli porównać średnią zachorowalność dla osób w różnych grupach wiekowych.

## Użycie 
Właściwą aplikacją jest notebook app.ipynb
```python
print(Datasets())
```
ypisze nam dostępne do analizy zbiory danych - Po pobraniu zbioru za pomocą funkcji ```import_data ```, będziemy mogli ...

## Pakiety
```
pandas==0.24.2
matplotlib==3.0.3
```

## link bazy:
https://www.kaggle.com/kimjihoo/coronavirusdataset