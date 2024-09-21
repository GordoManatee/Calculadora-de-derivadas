# Calculadora de derivadas en Python sin bibliotecas externas.

def derivada_monomio(coeficiente, exponente):
    """
    Calcula la derivada de un monomio de la forma coeficiente * x^exponente.
    Utiliza la regla de la potencia: d/dx [coef * x^n] = coef * n * x^(n-1).
    Entrada: coeficiente, exponente
    Salida: nuevo coeficiente y exponente del monomio derivado.
    """
    if exponente == 0:
        return 0, 0
    nuevo_coef = coeficiente * exponente
    nuevo_exp = exponente - 1
    return nuevo_coef, nuevo_exp


def mostrar_derivada(coeficiente, exponente):
    """
    Muestra la derivada de un monomio en forma legible.
    Entrada: coeficiente, exponente
    Salida: expresión de la derivada en forma de texto.
    """
    nuevo_coef, nuevo_exp = derivada_monomio(coeficiente, exponente)
    
    if nuevo_exp == 0:
        return f"Derivada: {nuevo_coef}"
    elif nuevo_exp == 1:
        return f"Derivada: {nuevo_coef}x"
    else:
        return f"Derivada: {nuevo_coef}x^{nuevo_exp}"


def pruebas():
    """
    Función de pruebas para mostrar el avance de la calculadora.
    Prueba la derivada de algunos monomios básicos usando ciclos for.
    """
    print("Pruebas de la calculadora de derivadas:")
    
    # Prueba 1: Derivada de 5x^3
    coeficiente = 5
    exponente = 3
    resultado = mostrar_derivada(coeficiente, exponente)
    print(f"Función: {coeficiente}x^{exponente} -> {resultado}")
    
    # Prueba 2: Derivada de 7x^2
    coeficiente = 7
    exponente = 2
    resultado = mostrar_derivada(coeficiente, exponente)
    print(f"Función: {coeficiente}x^{exponente} -> {resultado}")
    
    # Prueba 3: Derivada de 4x
    coeficiente = 4
    exponente = 1
    resultado = mostrar_derivada(coeficiente, exponente)
    print(f"Función: {coeficiente}x^{exponente} -> {resultado}")
    
    # Prueba 4: Derivada de una constante (10)
    coeficiente = 10
    exponente = 0
    resultado = mostrar_derivada(coeficiente, exponente)
    print(f"Función: {coeficiente} -> {resultado}")


def main():
    """
    Función principal que ejecuta la calculadora de derivadas.
    """
    print("Calculadora de derivadas")
    pruebas()
    
    continuar = 's'
    while continuar == 's':
        # Solicita al usuario el coeficiente y exponente
        print("Ingrese los datos para calcular la derivada del monomio.")
        coeficiente = float(input("Ingrese el coeficiente del monomio: "))
        exponente = int(input("Ingrese el exponente del monomio: "))
        
        # Muestra el resultado de la derivada
        resultado = mostrar_derivada(coeficiente, exponente)
        print(f"Función: {coeficiente}x^{exponente} {resultado}")
        
        # Pregunta si desea continuar
        continuar = input("¿Desea calcular otra derivada? (s/n): ")

    print("Saliendo...")
main()
