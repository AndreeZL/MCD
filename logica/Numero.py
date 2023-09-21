class NumeroNegativoException(Exception):
    pass
class Numero():
    def calcular_mcd(a, b):
        """Calcula el MCD usando el algoritmo de Euclides."""
        while b:
            a, b = b, a % b
        return a

    def main(self):
        while True:
            try:
                num1 = int(input("Introduce el primer número natural: "))

                if num1 < 0:
                    raise NumeroNegativoException("Por favor, introduce un número natural (no negativo).")

                num2 = int(input("Introduce el segundo número natural: "))

                if num2 < 0:
                    raise NumeroNegativoException("Por favor, introduce un número natural (no negativo).")

                resultado = Numero.calcular_mcd(num1, num2)
                print(f"El Máximo Común Divisor de {num1} y {num2} es {resultado}")
                break

            except NumeroNegativoException as err:
                print(err)