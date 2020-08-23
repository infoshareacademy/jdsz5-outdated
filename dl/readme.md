
# JDSZ5-Outdated projekt deep learning
# Flowers recognition
## The pictures are divided into five classes: daisy, tulip, rose, sunflower, dandelion.
## For each class there are about 800 photos. Photos are not high resolution, about 320x240 pixels. Photos are not reduced to a single size, they have different proportions!

## Opis
Sieć ma za zadanie klasyfikować zdjęcia kwiatów do jednej z 5 klas:
1) stokrotka
2) tulipan
3) róża
4) słonecznik
5) mniszek lekarski (mlecz)

## Użycie 

Właściwą aplikacją jest google colab
```python```

## Cel biznesowy:
Ta aplikacja jest to proof of concept rozwiązania, ktore mogłby pozwolić na usprawneinie pracy sortowni kwiatów. Innym zastosowaniem to aplikacja na smartfona pozwalająca rozpoznawać gatunek kwiatów.

## model:

Podczas pracy nad projektem spawdzono nastepujące modele: Xception, VGG16, Mobilenet v2, oraz przeprowadzono transfer learning Mobilenet v2 z wagami Imaginet.
Do tego zadanie najlepiej sprawdził się VGG16 dlatego wykonano dla niego dodatkowe kalibracje (fine tunning)

## Pakiety
```
pandas==0.24.2
numpy==1.12.1
matplotlib==3.0.3
seaborn==0.10.1
keras

```

## link bazy:
https://www.kaggle.com/alxmamaev/flowers-recognition
