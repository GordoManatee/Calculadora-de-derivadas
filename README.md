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
La función que se desea derivar (en formato algebraico), especificando los coeficientes y exponentes de cada término.

### Proceso: 
Pedir al usuario que ingrese la función que desea derivar.
Identificar cada término de la función ingresada, separando los coeficientes y exponentes correspondientes.
Aplicar la regla de derivación adecuada para cada término:
Si el término es una constante, su derivada será 0.
Si el término es de la forma 𝑎𝑥^𝑛, calcular la derivada utilizando la regla de la potencia
Si la función incluye multiplicaciones o divisiones, aplicar la regla del producto o del cociente según corresponda.
Si la función es una raíz, convertirla a su forma exponencial y aplicar la regla de la potencia.
Si la función es compuesta, aplicar la regla de la cadena.
Sumar todas las derivadas de los términos individuales para obtener la derivada total de la función original.
Formatear el resultado de manera que sea fácil de leer, ajustando signos y simplificando la expresión final si es necesario.

### Salida: 
La derivada de la función ingresada, presentada en formato algebraico simplificado.
