import pandas as pd

datos = {
    "nombres": [ "Maria", "Jose", "Juan"],
    "edad": [20, 19, 23],
    "promedio": [100, 60, 85]
}
df = pd.DataFrame(datos)
print(df)

csv=pd.read_csv("https://raw.githubusercontent.com/asalber/"
            "manual-python/master/datos/colesteroles.csv",
                sep =";", decimal=",")

print(csv)

print(csv.info())

print("\n\nDESCRIBE")
print(csv.describe())
print("\n\nHEAD")
print(csv.head())
print("\n\nTAIL")
print(csv.tail())
print("\n\nSAMPLE")
print(csv.sample(5))
print("\n\nATRUBUTOS")
print(csv.shape)  #Numero de renglones y columnas
print("\n\nSize")
print(csv.size)  #Numero total de datos
print("\n\nColumnas")
print(csv.columns) #NOMBRE DE TODAS LAS COLUMNAS
print("\n\nindices")
print(csv.index) #Nombres de los renglones
print("\n\n")
print(csv.dtypes)#Tipos de cada columna
print("\n\n")
print(csv[["edad", "colesterol"]])

print("\n\n")
print(csv.min())