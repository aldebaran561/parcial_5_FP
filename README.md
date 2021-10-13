# parcial 5 de Fundamentos de Programación

### PResentado por: Víctor Agudelo
### Correo electrónico: vmanuel.agudelo@udea.edu.co

En el presente repositorio se encuentra una posible aproximación al parcial #5 propuesto en la materia Fundamentos de Programación de la Universidad de Antioquia durante el
semestre 2021-I.

Dicho parcial se basa en dos (2) puntos del taller de Estructuras Repetitivas

- [Punto 88](#punto88)
- [Punto 89](#punto89)

## Punto 88 <a name="punto88"></a>

Un teorema afirma que:

> *La probabilidad de que un entero elegido al azar sea libre de cuadrados es:*
<div align="center">
  <img src="https://latex.codecogs.com/svg.image?\frac{6}{\pi&space;^{2}}">
 </div>

> Realice una simulación para estimar el valor teórico de la probabilidad enunciando en el teorema de ![equation][1]. Suponga que los enteros positivos son finitos ![equation][2]
  con *N* muy "grande"
 
 ### Solución:
 
 Para la solución del ejercicio se realizó una aproximación en Python, la cual se puede encontrar en ![Ejercicio_88.py][4], utilizando la fórmula de sumas de Riemann generada para
 ejercicios anteriores, teniendo en cuenta que, una aproximación teórica al ejercicio es:
 
 <div align="center">
  <img src="https://latex.codecogs.com/svg.image?\frac{1}{\sum_{1}^{n}=&space;\frac{1}{n^{2}}}=&space;\frac{1}{\frac{\pi&space;^{2}}{6}}&space;=&space;\frac{6}{\pi&space;^{2}}">
 </div>
 
 Por lo tanto, utilizando algunos conceptos básicos de programación orientada a objetos, se crea un objeto ```Calculadora_Libre_Cuadrados``` enfocada en una única tarea de 
 realizar los respectivos cálculos que pide el ejercicio. Paso siguiente, se crea un objeto ```Impresora```, cuyo objetivo es imprimir los resultados de la calculadora, 
 los cuales son inyectados mediante inyección de dependencias
 
 ## Punto 88 <a name="punto89"></a>
 
 > Se elige al azar un entero ![equation][3] con *N* := 100 y deseamos estudiar *A* := {*n* es primo}
 
 ### Solución:
 
Para la solución del ejercicio se realizó una aproximación en Python, la cual se puede encontrar en ![Ejercicio_89.py][5] y se establecen dos objetos, la ```Calculadora_Perfectos```
que permite verificar el total de números perfectos en para un rango determinado y calcular la probabilidad de elegir uno de ellos. El segundo objeto ```Impresora``` permite
imprimir los resultados obtenidos en la calculadora mediante inyección de dependencias.

**Nota:** para este ejercicio se sabe que existen 4 números perfectos menores a 10000: 6, 28, 426 y 8128. Teniendo en cuenta que el siguiente número perfecto es 33550336, 
el ejercicio se corrió solo para los primeros 10000 datos, dado el rendimiento de la máquina por las Big-O notations que se utilizaron en el código.

[1]: https://latex.codecogs.com/svg.image?\6/\pi^{2}
[2]: https://latex.codecogs.com/svg.image?\mathbb{Z}^{&plus;}&space;=&space;\left\{&space;1,2,...,N\right\}
[3]: https://latex.codecogs.com/svg.image?n\in\Omega:=\left\{&space;1,2,...,N\right\}
[4]: https://github.com/aldebaran561/parcial_5_FP/blob/master/Ejercicio_88.py
[5]: https://github.com/aldebaran561/parcial_5_FP/blob/master/Ejercicio_89.py
