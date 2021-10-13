import math


class Calculadora_Libre_Cuadrados:
    def __init__(self, numero):
        self.numero = numero

    def zeta(self):
        sumatoria = 0

        for valor in range(1, self.numero + 1):
            sumatoria += 1 / (valor ** 2)

        return round(sumatoria, 5)

    def probabilidad_libre_cuadrados(self):
        return round(1 / self.zeta(), 5)

    def valor_teorico(self):
        return round(6 / (math.pi ** 2), 5)

    def comparacion_teorica(self):
        valor_teorico = self.valor_teorico()
        diferencia = abs(valor_teorico - self.probabilidad_libre_cuadrados())
        return round(diferencia, 5)


class Impresora:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def __str__(self):
        return f'''
la probabilidad de que un entero elegido al azar sea libre de cuadrado es {self.calculadora.probabilidad_libre_cuadrados()},
la diferencia absoluta entre el resultado de {self.calculadora.numero} y el valor teórico {self.calculadora.valor_teorico()} es {self.calculadora.comparacion_teorica()}
        '''


if __name__ == '__main__':
    calculadora1 = Calculadora_Libre_Cuadrados(10000)
    impresora1 = Impresora(calculadora1)
    print(impresora1)
