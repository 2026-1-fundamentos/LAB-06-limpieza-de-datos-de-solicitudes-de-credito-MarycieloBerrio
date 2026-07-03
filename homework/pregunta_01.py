"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")

    df = df.drop(columns=["Unnamed: 0"])
    df = df.dropna()

    df["sexo"] = df["sexo"].str.lower().str.strip()
    df["tipo_de_emprendimiento"] = (
        df["tipo_de_emprendimiento"].str.lower().str.strip()
    )

    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ", regex=False)
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ", regex=False)
    df["idea_negocio"] = df["idea_negocio"].str.strip()
    df["idea_negocio"] = df["idea_negocio"].str.replace(r"\s+", " ", regex=True)

    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("_", " ", regex=False)
    df["barrio"] = df["barrio"].str.replace("-", " ", regex=False)
    df["barrio"] = df["barrio"].str.replace(r"\s+", " ", regex=True)

    df["estrato"] = df["estrato"].astype(int)
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    def parse_fecha(f):
        parts = f.split("/")
        if len(parts[0]) == 4:
            return f"{int(parts[2]):02d}/{int(parts[1]):02d}/{parts[0]}"
        else:
            return f"{int(parts[0]):02d}/{int(parts[1]):02d}/{parts[2]}"

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(parse_fecha)

    df["monto_del_credito"] = df["monto_del_credito"].astype(str)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(
        r"[\$,]", "", regex=True
    )
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(
        r"\.\d+$", "", regex=True
    )
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ", regex=False)
    df["línea_credito"] = df["línea_credito"].str.strip()
    df["línea_credito"] = df["línea_credito"].str.replace(r"\s+", " ", regex=True)

    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)
