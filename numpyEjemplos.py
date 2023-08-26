import numpy as np
#Los numpy son multi dimensionales
#LOS ARRAY SOLO YIENEN QUE TENER UN TIPO DE DATO
lista =[1, 2, 3, 4]
n1 = np.array(lista) #Numpy. array: Tiene capacidades que la lista no tiene
print(n1)
print(type(n1))
print(n1*2)

cali = [[100, 85, 90],
        [70, 50, 60],
        [80, 100, 70]]

cn=np.array((cali))
print(cn.mean())
print(cn.mean(axis=0)) #Por columna
print(cn.mean(axis=1)) #Por renglon
#sin axis son todos los numeros

print(cn.ndim) #Numero de dimensiones
print(cn.shape)#Tupla con la cantidad de elementos por dimension
print(cn.size) #Num datos en total
print(cn.dtype) #Tipo de dato

print(cn[0, 1]) #Para poder acceder   #renglon, columna
print(cn.transpose())#Invertir el matriz

"""
    x + 2y = 1
    3x + 5y = 2
"""

ecuaciones = np.array([[1, 2],
              [3, 5]])

res= np.array([1, 2])

r=np.linalg.solve(ecuaciones, res)
print(r)



import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Pclass': [1, 2, 1, 3, 2, 1, 3, 2],
        'Age': [35, 22, 38, 26, 19, 42, 21, 30]}
df = pd.DataFrame(data)

# Utilizar groupby para crear grupos basados en la columna 'Pclass'
grupos = df.groupby('Age')

# Aplicar la función size() para contar el número de filas en cada grupo
conteo_por_clase = grupos.size()

# Mostrar el resultado
print(conteo_por_clase)
