import pandas as pd 
import numpy as np

def mesureThermicite(fichier):
    """
    Calcule la thermicité à partir d'un fichier CSV contenant les colonnes
    'nombre d'onde' et 'transmission' (en %).
    Retourne (aireDessusLaCourbe, ratio).
    """
    try:
        df = pd.read_csv(fichier, sep=";")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

    df.columns = ["nombre d'onde", "transmission"] # attention la transmission est en %

    # Conversion des valeurs en float
    df["transmission"] = df["transmission"].astype(str).str.replace(",", ".")
    df["transmission"] = df["transmission"].astype(float)
    df["nombre d'onde"] = df["nombre d'onde"].astype(str).str.replace(",", ".")
    df["nombre d'onde"] = df["nombre d'onde"].astype(float)

    # Filtrage de la plage d'intérêt
    df_filtre = df[(df["nombre d'onde"]>= 770) & (df["nombre d'onde"]<= 1430)]

    if df_filtre.empty:
        print("Aucune donnée dans la plage spécifiée.")
        return None

    x = df_filtre["nombre d'onde"]
    y = df_filtre["transmission"] 

    aireSousLaCourbe = - np.trapz(y, x)
    aireTotale = 100 * (1430 - 770)
    aireDessusLaCourbe = aireTotale - aireSousLaCourbe

    print(f"Aire au-dessus de la courbe : {aireDessusLaCourbe:.2f}")
    print(f"Ratio aire/aire totale : {aireDessusLaCourbe/aireTotale:.4f}")

    return aireDessusLaCourbe, aireDessusLaCourbe/aireTotale

mesureThermicite("fichierSpectrometre.csv")


