
# JDSZ5-Outdated projekt machine learning
# House Prices: Advanced Regression Techniques
## Predict sales prices and practice feature engineering, RFs, and gradient boosting

## Opis
Aplikacja pozwala nam na przewidywanie cen mieszkań w Ames in Iowa. wybrane metryki sukcesu modeli to mse (średni błąd kwadratowy) oraz R2 (statystykę wyjaśniającą za ile zmienności odpowiadają dane).

Na początku przygotowano bazę do analiz (data cleaning i wrangling), potem przygotowano zmienne do analiz (Feature Engineering).
Następnie przeprowadzona zastała analiza wartości odstających i normalizacja danych do celu analiz. Póżniej stowrzono i przetestowano następujące modele: regresji liniowej i logistycznej, drzew decyzyjnych i lasów losowych, support vector machine (svm), k-next neighbours (knn) oraz xgboost Do każdego z nich dobrano hiperparametry i wybrano najbardziej optymalne. Ostatecznie wybrano najbardziej optymalny model i poprzez przetestowanie skuteczności najbardziej obiecujących modeli na danych testowych.

## Użycie 
Właściwą aplikacją jest notebook app.ipynb
```python```

Pozwala ona na zapoznanie się zbarą danych poprzez wizualizacj poszczególych kolumn...

Przetestowane modele:

- regresja liniowa i logistyczna
- drzewo decyzyjne
- random forest
- svm(r)
- knn
- xgboost

## Pakiety
```
pandas==0.24.2
matplotlib==3.0.3
xgboost==1.0.2
sklearn==0.23

```

## link bazy:
https://www.kaggle.com/c/house-prices-advanced-regression-techniques