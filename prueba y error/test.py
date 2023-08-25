class Pensionista:
    def __init__(self, identificador, edad, gastos_mensuales):
        self.identificador = identificador
        self.edad = edad
        self.gastos_mensuales = gastos_mensuales

class GrupoPensionistas:
    def __init__(self, pensionistas):
        self.pensionistas = pensionistas

    def mediaGastos(self, identificador):
        for pensionista in self.pensionistas:
            if pensionista.identificador == identificador:
                return sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)
        return None

    def mediaEdad(self):
        edadTotal = 0
        for pensionista in self.pensionistas:
            edadTotal += pensionista.edad
        return edadTotal / len(self.pensionistas)

    def edadesExtremas(self):
        menorEdad = 999999999
        mayorEdad = 0
        for pensionista in self.pensionistas:
            if pensionista.edad < menorEdad:
                menorEdad = pensionista.edad
            if pensionista.edad > mayorEdad:
                mayorEdad = pensionista.edad
        return menorEdad, mayorEdad

    def sumaPromedio(self):
        suma = 0
        for pensionista in self.pensionistas:
            suma += sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)
        return suma

    def mediaMaxima(self):
        maxMedia = None
        maxPromedio = 0

        for pensionista in self.pensionistas:
            promedio_actual = sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)

            if promedio_actual > maxPromedio:
                maxPromedio = promedio_actual
                maxMedia = (pensionista.identificador, maxPromedio)

        return maxMedia

    def gastoPromedio(self):
        gasto_promedio = []
        for pensionista in self.pensionistas:
            gasto_promedio.append(sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales))
        return sorted(gasto_promedio)


pensionista1 = Pensionista('1111A', 68, [640, 589, 573])
pensionista2 = Pensionista('1222A', 72, [360, 550, 376])
pensionista3 = Pensionista('1333A', 75, [250, 960, 850])


grupo = GrupoPensionistas([pensionista1, pensionista2, pensionista3])


print(grupo.mediaGastos('1111A'))
print(grupo.mediaEdad())
print(grupo.edadesExtremas())
print(grupo.sumaPromedio())
print(grupo.mediaMaxima())
print(grupo.gastoPromedio())
