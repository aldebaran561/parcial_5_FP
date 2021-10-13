class Calculadora_Perfectos:
    def __init__(self, experimentos):
        self.experimentos = experimentos

    def numeros_perfectos(self):
        total_perfectos = 0
        for numero in range(1, self.experimentos):
            aux_suma = 0
            for aux_numero in range(1, numero):
                if numero % aux_numero == 0:
                    aux_suma += aux_numero
            if aux_suma == numero:
                total_perfectos += 1
        return total_perfectos

    def probabilidad(self):
        return self.numeros_perfectos() / self.experimentos

class Impresora:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def __str__(self):
        return f'''
la probabilidad de encontrar un número perfecto en {self.calculadora.experimentos} experimentos
es {self.calculadora.probabilidad()}, toda vez que en el rango dado solo se 
encuentran {self.calculadora.numeros_perfectos()} números perfectos, lo cual se aproxima
al teorema de Kanold, que establece que P(A) es = 0 a medida que los experimentos son más grandes
'''

if __name__ == '__main__':
    calculadora1 = Calculadora_Perfectos(10000)
    impresora1 = Impresora(calculadora1)
    print(impresora1)
