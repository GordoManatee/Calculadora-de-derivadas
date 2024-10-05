def separar_terminos(funcion):
    """
    Separa los términos de una función polinómica en una lista.
    Entrada: funcion (cadena de texto que representa la función polinómica).
    Salida: lista de términos separados.
    """
    funcion = funcion.replace(" ", "")
    terminos = []
    i = 0
    while i < len(funcion):
        if funcion[i] == "+" or funcion[i] == "-":
            terminos.append(funcion[i])
            i += 1
        else:
            j = i
            while j < len(funcion) and funcion[j] not in "+-":
                j += 1
            terminos.append(funcion[i:j])
            i = j
    return terminos


def derivar_termino(termino):
    """
    Deriva un monomio del tipo ax^n o bx, devuelve la derivada del término.
    Entrada: termino (cadena de texto que representa un monomio).
    Salida: cadena de texto que representa la derivada del término.
    """
    if "x" not in termino:  # Caso de una constante
        return "0"
    
    if "^" in termino:
        coef, exponente = termino.split("x^")
        coef = int(coef) if coef != "" else 1
        exponente = int(exponente)
        nuevo_coef = coef * exponente
        nuevo_exp = exponente - 1
        if nuevo_exp == 0:
            return str(nuevo_coef)
        elif nuevo_exp == 1:
            return f"{nuevo_coef}x"
        else:
            return f"{nuevo_coef}x^{nuevo_exp}"
    
    elif "x" in termino:
        coef = termino.replace("x", "")
        coef = int(coef) if coef != "" else 1
        return str(coef)


def derivar_funcion(funcion):
    """
    Deriva una función polinómica completa.
    Entrada: funcion (cadena de texto que representa la función polinómica).
    Salida: cadena de texto que representa la derivada de la función.
    """
    terminos = separar_terminos(funcion)
    derivada = []
    
    for termino in terminos:
        if termino == "+" or termino == "-":
            derivada.append(termino)
        else:
            derivada.append(derivar_termino(termino))
    
    return " ".join(derivada)


def derivar_producto(funcion1, funcion2):
    """
    Deriva un producto de dos funciones f(x) * g(x).
    Aplicando la regla del producto: (f * g)' = f' * g + f * g'.
    Entrada: funcion1, funcion2 (cadenas de texto que representan dos funciones).
    Salida: derivada del producto simplificada.
    """
    derivada1 = derivar_funcion(funcion1)
    derivada2 = derivar_funcion(funcion2)
    
    return f"({derivada1}) * ({funcion2}) + ({funcion1}) * ({derivada2})"


def derivar_cociente(funcion1, funcion2):
    """
    Deriva un cociente de dos funciones f(x) / g(x).
    Aplicando la regla del cociente: (f/g)' = (f'g - fg') / g^2.
    Entrada: funcion1, funcion2 (cadenas de texto que representan dos funciones).
    Salida: derivada del cociente.
    """
    derivada1 = derivar_funcion(funcion1)
    derivada2 = derivar_funcion(funcion2)
    
    return f"(({derivada1}) * ({funcion2}) - ({funcion1}) * ({derivada2})) / ({funcion2})^2"


def obtener_opcion_menu():
    """
    Muestra el menú de opciones al usuario y devuelve la opción seleccionada.
    """
    print("\nSeleccione el tipo de derivada que desea calcular:")
    print("1. Derivada de un polinomio")
    print("2. Derivada de un producto")
    print("3. Derivada de un cociente")
    
    opcion = input("Ingrese el número de la opción: ")
    return opcion


def calcular_derivada():
    """
    Calcula la derivada según el tipo de operación seleccionado en el menú.
    """
    opcion = obtener_opcion_menu()
    
    if opcion == "1":
        # Derivada de un polinomio
        funcion = input("Ingrese la función polinómica a derivar (Ej: x^2 + 3x - 2): ")
        derivada = derivar_funcion(funcion)
        print(f"Derivada del polinomio: {derivada}")
    
    elif opcion == "2":
        # Derivada de un producto
        funcion1 = input("Ingrese la primera función (Ej: x^2 + 1): ")
        funcion2 = input("Ingrese la segunda función (Ej: x^3 - 2x): ")
        derivada = derivar_producto(funcion1, funcion2)
        print(f"Derivada del producto: {derivada}")
    
    elif opcion == "3":
        # Derivada de un cociente
        funcion1 = input("Ingrese la función del numerador (Ej: x^3 + 1): ")
        funcion2 = input("Ingrese la función del denominador (Ej: x^2 - 1): ")
        derivada = derivar_cociente(funcion1, funcion2)
        print(f"Derivada del cociente: {derivada}")
    
    else:
        print("Opción no válida. Intente de nuevo.")


def main():
    """
    Función principal que ejecuta la calculadora de derivadas con menú.
    """
    print("Bienvenido a la calculadora de derivadas")
    
    continuar = 's'
    while continuar == 's':
        calcular_derivada()
        continuar = input("¿Desea realizar otra derivada? (s/n): ").lower()


main()
