# Calculadora de derivadas en Python sin bibliotecas externas.

def guardar_procedimiento(archivo, contenido):
    """
    Guarda el procedimiento en un archivo de texto.
    """
    with open(archivo, 'a') as file:
        file.write(contenido + '\n')


def separar_terminos(funcion):
    """
    Separa los términos de una función polinómica en una lista.
    Asume que los términos están separados por '+' o '-'.
    """
    funcion = funcion.replace(" ", "")
    terminos = []
    i = 0
    while i < len(funcion):
        if funcion[i] in "+-":
            terminos.append(funcion[i])
            i += 1
        else:
            j = i
            while j < len(funcion) and funcion[j] not in "+-":
                j += 1
            terminos.append(funcion[i:j])
            i = j
    return terminos


def obtener_coef_exp(termino):
    """
    Obtiene el coeficiente y el exponente de un término del tipo ax^n.
    Si el término no tiene exponente o coeficiente, asume los valores por defecto.
    """
    if "x^" in termino:
        coef, exp = termino.split("x^")
        coef = int(coef) if coef else 1
        exp = int(exp)
    elif "x" in termino:
        coef = int(termino.replace("x", "")) if termino.replace("x", "") else 1
        exp = 1
    else:
        coef = int(termino)
        exp = 0
    return coef, exp


def derivar_termino(termino, archivo_procedimiento):
    """
    Deriva un término monomial y guarda el procedimiento en un archivo.
    """
    coef, exp = obtener_coef_exp(termino)
    if exp == 0:
        guardar_procedimiento(archivo_procedimiento, f"Derivada de una constante: {termino} -> 0")
        return "0"
    
    nuevo_coef = coef * exp
    nuevo_exp = exp - 1
    if nuevo_exp == 0:
        derivada = str(nuevo_coef)
    elif nuevo_exp == 1:
        derivada = f"{nuevo_coef}x"
    else:
        derivada = f"{nuevo_coef}x^{nuevo_exp}"
    
    guardar_procedimiento(archivo_procedimiento, f"Derivada de {termino}: {derivada}")
    return derivada


def derivar_funcion(funcion, archivo_procedimiento):
    """
    Deriva una función polinómica completa y guarda el procedimiento.
    """
    terminos = separar_terminos(funcion)
    derivada = [derivar_termino(t, archivo_procedimiento) for t in terminos if t not in "+-"]
    return " + ".join(derivada)


def derivar_producto(funcion1, funcion2, archivo_procedimiento):
    """
    Aplica la regla del producto a dos funciones y guarda el procedimiento.
    """
    derivada1 = derivar_funcion(funcion1, archivo_procedimiento)
    derivada2 = derivar_funcion(funcion2, archivo_procedimiento)
    
    guardar_procedimiento(archivo_procedimiento, f"Regla del producto aplicada a: ({funcion1}) * ({funcion2})")
    return f"({derivada1}) * ({funcion2}) + ({funcion1}) * ({derivada2})"


def derivar_cociente(funcion1, funcion2, archivo_procedimiento):
    """
    Aplica la regla del cociente a dos funciones y guarda el procedimiento.
    """
    derivada1 = derivar_funcion(funcion1, archivo_procedimiento)
    derivada2 = derivar_funcion(funcion2, archivo_procedimiento)
    
    guardar_procedimiento(archivo_procedimiento, f"Regla del cociente aplicada a: ({funcion1}) / ({funcion2})")
    return f"(({derivada1}) * ({funcion2}) - ({funcion1}) * ({derivada2})) / ({funcion2})^2"


def detectar_tipo_funcion(funcion):
    """
    Detecta automáticamente si la función es un polinomio, un producto o un cociente.
    """
    if "*" in funcion:
        funciones = funcion.split("*")
        return "producto", funciones[0].strip(), funciones[1].strip()
    elif "/" in funcion:
        funciones = funcion.split("/")
        return "cociente", funciones[0].strip(), funciones[1].strip()
    else:
        return "polinomio", funcion, None


def calcular_derivada(funcion, archivo_procedimiento):
    """
    Calcula la derivada según el tipo de función y guarda el procedimiento.
    """
    tipo, funcion1, funcion2 = detectar_tipo_funcion(funcion)
    
    if tipo == "producto":
        return derivar_producto(funcion1, funcion2, archivo_procedimiento)
    
    elif tipo == "cociente":
        return derivar_cociente(funcion1, funcion2, archivo_procedimiento)
    
    else:
        return derivar_funcion(funcion1, archivo_procedimiento)


def mostrar_procedimiento(archivo_procedimiento):
    """
    Muestra el contenido del archivo donde se guardó el procedimiento.
    """
    try:
        with open(archivo_procedimiento, 'r') as file:
            procedimiento = file.read()
            print("\nProcedimiento:")
            print(procedimiento)
    except FileNotFoundError:
        print("No se encontró el archivo de procedimiento.")


def main():
    """
    Función principal que ejecuta la calculadora de derivadas.
    Guarda el procedimiento en un archivo y pregunta si se desea ver.
    """
    archivo_procedimiento = "procedimiento_derivada.txt"
    
    continuar = 's'
    while continuar == 's':
        # Limpiar el archivo de procedimiento al inicio de cada derivada
        open(archivo_procedimiento, 'w').close()
        
        funcion = input("Ingrese la función a derivar: ")
        derivada = calcular_derivada(funcion, archivo_procedimiento)
        print(f"Derivada: {derivada}")
        
        ver_procedimiento = input("¿Desea ver el procedimiento? (s/n): ").lower()
        if ver_procedimiento == 's':
            mostrar_procedimiento(archivo_procedimiento)
        
        continuar = input("¿Desea realizar otra derivada? (s/n): ").lower()


main()