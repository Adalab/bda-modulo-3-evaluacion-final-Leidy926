# Bienvenida a mis librerias-

# Funcion para exploracion básica del dataframe
def exploracion_basica(df):
    print(" Numero de filas y columnas\n:", df.shape)
    print(" Columnas:\n", df.columns.tolist())
    print("Tipos de datos:\n", df.dtypes)
    print("Primeras filas:\n", df.head())
    print("Últimas filas:\n", df.tail())
    df.info()

# Funcion para estadísticos principales de columnas
def estadisticos_principales_todas_columnas(df):
    display(df.describe().T)
    print(".............")
    display(df.describe(include="O").T)

# Funcion para explorar nulos

def revisar_nulos(df):
    print("Valores nulos por columna:")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0])

    print("Porcentaje de nulos por columna:")
    porcentaje_nulos = (nulos[nulos > 0] / df.shape[0]) * 100
    print(porcentaje_nulos.round(2).astype(str) + '%')

    print("Número de filas duplicadas:")
    print(df.duplicated().sum())


# Funcion para explorar nulos categoricos

def explorar_nulos_categoricos(df):
    df_cat = df.select_dtypes(include='object')

    print(f"Variables categóricas encontradas: {len(df_cat.columns)}\n")

    for col in df_cat.columns:
        nulos = df[col].isnull().sum()
        print(f" {col.upper()}")
        print(f"   - Nulos: {nulos}")
        print(f"   - Valores únicos (top 5):")
        display(df[col].value_counts().reset_index().head())

# Funcion para explorar frecuencia variables categoricas
def frecuencia_variables_categoricas (df):
    df_cat = df.select_dtypes(include='object')
    print(f"Variables categóricas encontradas: {len(df_cat.columns)}\n")
    for col in df_cat.columns:
        print(f"Los valores únicos para la columna: {col.upper()}")
        display(df[col].value_counts().reset_index().head())



# Funcion para imputar nulos
def imputar_nulos(df):
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].median())


# Funcion para hallar medidas centrales
def resumen_medidas_centrales(dataframe):
    print("=== MEDIA, MEDIANA Y MODA DE VARIABLES NUMÉRICAS ===")
    columnas_numericas = dataframe.select_dtypes(include='number')
    if columnas_numericas.empty:
        print("No hay columnas numéricas en el dataset.")
        return
    for nombre_columna in columnas_numericas.columns:
        print(f"\nColumna: {nombre_columna}")
        media = columnas_numericas[nombre_columna].mean()
        mediana = columnas_numericas[nombre_columna].median()
        moda = columnas_numericas[nombre_columna].mode()
        print(f"  Media: {media:.2f}")
        print(f"  Mediana: {mediana}")
        if len(moda) == 1:
            print(f"  Moda: {moda[0]}")
        else:
            print(f"  Moda (varias): {list(moda)}")
