"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Eliminacion de columnas innecesarias
    df = df.drop(columns=["Unnamed: 0"])

    # Unificar '-' y '_' como ' '
    df = df.replace("-", " ").replace("_", " ")
    
    # Convertir mayusculas a minusculas
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

    # Limpieza de fecha_de_beneficio
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).fillna(
        pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    )

    # Limpieza columna monto_del_credito
    df["monto_del_credito"] = (df.monto_del_credito
                            .str.replace("$", "")
                            .str.strip()
                            .str.replace(",", "")
                            .str.replace(r'\.\w+', '', regex=True)
                            .astype(int))

    # Cambio de tipo de dato de comuna_ciudadano
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # Limpiza de datos duplicados y nulos
    df = df.drop_duplicates().dropna()

    print(df)
    return df

clean_data()