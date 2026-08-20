import pandas as pd

def verificar_calidad(df: pd.DataFrame, columnas: list, n_samples: int = 5):
    """
    Imprime la verificación de calidad de datos para cada Bloque.
    """
    print("\nMuestra de datos:")
    print(df[columnas].head(n_samples))
    print("\nConteo de nulos:")
    print(df[columnas].isnull().sum())
    print(f"\nTotal de filas en el DataFrame: {df.shape[0]}")
    print(f"Total de columnas en el DataFrame: {df.shape[1]}")