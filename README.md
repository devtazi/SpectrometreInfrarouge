# Spectromètre Infrarouge

Ce projet permet de calculer la thermicité à partir d’un fichier CSV contenant des mesures spectrométriques.

## Fonction principale

Le script Python lit un fichier CSV contenant deux colonnes :
- `nombre d'onde` : la fréquence (en cm⁻¹)
- `transmission` : le pourcentage de transmission

La fonction `mesureThermicite` :
1. Lit le fichier CSV.
2. Convertit les données en format numérique.
3. Filtre les valeurs de `nombre d'onde` entre 770 et 1430.
4. Calcule l’aire sous la courbe de transmission.
5. Calcule l’aire au-dessus de la courbe et le ratio par rapport à l’aire totale.
6. Affiche les résultats.

## Utilisation

Placez votre fichier CSV (exemple : `fichierSpectrometre.csv`) dans le dossier du projet, puis lancez :

```bash
python main.py
```

## Dépendances

- pandas
- numpy

Installez-les avec :

```bash
pip install pandas numpy
```

## Exemple de fichier CSV

```
770;85
800;83
...
1430;90
```

## Résultat

Le script affiche :
- L’aire au-dessus de la courbe
- Le ratio aire/aire totale

