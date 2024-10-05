# Calculadora de derivadas
Hacer una calculadora de derivadas en Python sin utilizar bibliotecas matemáticas externas es el objetivo. Crear una herramienta que permita calcular derivadas de funciones matemáticas básicas mediante la aplicación de lógica y programación. La calculadora estará diseñada para manejar las reglas de derivación fundamentales, como la derivada de una constante, la derivada de una potencia, la regla del producto, la regla del cociente, la derivada de una raíz de cualquier índice y la regla de la cadena. Este proyecto es importante porque, además de reforzar el entendimiento de los conceptos básicos del cálculo diferencial, fomenta el desarrollo de habilidades de programación. Al evitar el uso de bibliotecas preexistentes, se obliga a una comprensión más profunda y a una aplicación directa de las matemáticas dentro del código. Esto no solo es un excelente ejercicio para mostrar los conocimientos adquiridos, y también permite que se use como base para futuras modificaciones del proyecto, como el manejo de funciones más complejas o la resolución de ecuaciones diferenciales.

## Formulas basicas:
Derivada de una constante: 𝑑/𝑑𝑥(𝑐)=0   
Derivada de una potencia: 𝑑/𝑑𝑥(𝑥^𝑛)=𝑛𝑥^(𝑛−1)  
Regla del poducto: 𝑑/𝑑𝑥(𝑢𝑣)=𝑢′𝑣+𝑢𝑣′  
Regla del cociente: 𝑑/𝑑𝑥(𝑢/𝑣)=(𝑢′𝑣−𝑢𝑣′)/𝑣^2  
Regla de la cadena: 𝑑/𝑑𝑥(𝑓(𝑔(𝑥)))=𝑓′(𝑔(𝑥))⋅𝑔′(𝑥)

## contexto
Una calculadora de derivadas es una herramienta diseñada para calcular la derivada de funciones matemáticas de forma rápida y precisa. Estas calculadoras suelen estar disponibles en línea o como aplicaciones y permiten a los usuarios ingresar una función, que puede incluir polinomios, funciones trigonométricas, exponenciales, logarítmicas, y más. Una vez ingresada la función, la calculadora procesa la información y aplica las reglas de derivación para proporcionar la derivada correspondiente. Algunas de estas calculadoras también ofrecen funcionalidades adicionales, como la posibilidad de calcular derivadas parciales, derivadas sucesivas, o incluso mostrar el proceso paso a paso de cómo se llega al resultado. Además, algunas versiones avanzadas permiten graficar la función original junto con su derivada, lo que facilita la visualización del comportamiento de la función en diferentes puntos. Estas herramientas son particularmente útiles en contextos educativos, donde los estudiantes pueden verificar sus respuestas y comprender mejor los conceptos de cálculo diferencial, así como en entornos profesionales donde se requiere rapidez y precisión en los cálculos matemáticos.

## Algoritmo
### Entrada:

1. **Menú de Selección**: 
   - El programa presenta al usuario un menú con tres opciones:
     - 1: Derivada de un polinomio.
     - 2: Derivada de un producto.
     - 3: Derivada de un cociente.
   
2. **Elección del Usuario**:
   - El usuario selecciona el tipo de derivada que desea calcular ingresando el número correspondiente (1, 2 o 3).

3. **Ingreso de Funciones**:
   - Según la selección del usuario, el programa solicitará las siguientes entradas:
     - Si elige **1** (Polinomio): el usuario ingresa una función polinómica (por ejemplo: x^2 + 3x - 2).
     - Si elige **2** (Producto): el usuario ingresa dos funciones que están siendo multiplicadas (por ejemplo: 3x y 8x^3).
     - Si elige **3** (Cociente): el usuario ingresa el numerador y el denominador de la fracción (por ejemplo: x^3 + 1 y x^2 - 1).

### Proceso:

1. **Procesar la Derivada**:
   - Según la opción elegida por el usuario:
     - **Polinomio**: Se separan los términos de la función polinómica. Luego, cada término es derivado individualmente, y los resultados son combinados para formar la derivada final.
     - **Producto**: Se derivan ambas funciones por separado y se aplica la **regla del producto**: 
       𝑑/𝑑𝑥(𝑢𝑣)=𝑢′𝑣+𝑢𝑣′  
     - **Cociente**: Se derivan el numerador y el denominador y se aplica la **regla del cociente**: 
       𝑑/𝑑𝑥(𝑢/𝑣)=(𝑢′𝑣−𝑢𝑣′)/𝑣^2
   
2. **Mostrar el Resultado**:
   - El resultado de la derivada es mostrado en formato simplificado. El programa realiza las operaciones algebraicas necesarias para devolver la derivada de forma correcta.

3. **Ciclo de Continuación**:
   - El programa pregunta al usuario si desea realizar otro cálculo (**s** para continuar, **n** para salir). Si el usuario decide continuar, el programa regresa al menú inicial. De lo contrario, el programa finaliza.

### Salida:

- Dependiendo de la selección del usuario, las salidas pueden ser:
  - La derivada de un polinomio.
  - La derivada de un producto de dos funciones.
  - La derivada de un cociente de dos funciones.
  
- Después de calcular, se muestra el resultado en formato simplificado.
