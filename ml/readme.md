
# JDSZ5-Outdated projekt machine learning
# House Prices: Advanced Regression Techniques
## Predict sales prices and practice feature engineering, RFs, and gradient boosting

## Opis
Aplikacja pozwala nam na przewidywanie cen mieszkań w Ames in Iowa. Wybrane metryki sukcesu modeli to  R2 (statystykę wyjaśniającą za ile zmienności odpowiadają dane), mse (średni błąd kwadratowy) oraz średni błąd mierzony w procentach.

Na początku przygotowano bazę do analiz (data cleaning i wrangling), potem przygotowano zmienne do analiz (Feature Engineering).
Następnie przeprowadzona zastała analiza wartości odstających i normalizacja danych do celu analiz. Póżniej stowrzono i przetestowano następujące modele: regresji liniowej i logistycznej, drzew decyzyjnych i lasów losowych, support vector machine (svm), k-next neighbours (knn) oraz xgboost Do każdego z nich dobrano hiperparametry i wybrano najbardziej optymalne. Ostatecznie wybrano najbardziej optymalny model i poprzez przetestowanie skuteczności najbardziej obiecujących modeli na danych testowych.

## Użycie 
Właściwą aplikacją jest notebook app.ipynb
```python```

## Cel biznesowy:

Applikacja może stanowić pomoc zarówno dla podażowej cześci rynku nieruchomości mieszkaniowych: agencji nieruchomości i osób fizycznych chcących wycenić konkretną nieruchomość do sprzedarzy jak i dla cześci popytowej: gdyż powzoli na ocenę czy oferta sprzedaży jest korzystna, optymalna czy nie korzystna poprzez estymację jaka powinna być jej cena biorąc pod uwagę jej cechy.

## Przetestowane modele:

- regresja liniowa 
- drzewo decyzyjne
- random forest
- svm(r)
- knn
- xgboost

## Pakiety
```
pandas==0.24.2
numpy==1.12.1
matplotlib==3.0.3
xgboost==1.0.2
sklearn==0.23
seaborn==0.10.1

```

## link bazy:
https://www.kaggle.com/c/house-prices-advanced-regression-techniques