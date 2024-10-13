# Calculadora de derivadas
Hacer una calculadora de derivadas en Python sin utilizar bibliotecas matemáticas externas es el objetivo. Crear una herramienta que permita calcular derivadas de funciones matemáticas básicas mediante la aplicación de lógica y programación. La calculadora estará diseñada para manejar las reglas de derivación fundamentales, como la derivada de una constante, la derivada de una potencia, la regla del producto, la regla del cociente, la derivada de una raíz de cualquier índice y la regla de la cadena. Este proyecto es importante porque, además de reforzar el entendimiento de los conceptos básicos del cálculo diferencial, fomenta el desarrollo de habilidades de programación. Al evitar el uso de bibliotecas preexistentes, se obliga a una comprensión más profunda y a una aplicación directa de las matemáticas dentro del código. Esto no solo es un excelente ejercicio para mostrar los conocimientos adquiridos, y también permite que se use como base para futuras modificaciones del proyecto, como el manejo de funciones más complejas o la resolución de ecuaciones diferenciales.

Este proyecto consiste en el desarrollo de una calculadora de derivadas en Python que puede derivar funciones polinómicas, productos y cocientes de manera automática. El enfoque principal de este proyecto es ofrecer una herramienta que no solo entregue el resultado simplificado de una derivada, sino que además permita guardar y mostrar el procedimiento paso a paso que llevó a dicho resultado.

El procedimiento de derivación se almacena en un archivo de texto, lo que ofrece al usuario la opción de revisar cómo se aplicaron las reglas de derivación (como la regla del producto y la regla del cociente) en cada parte de la función. Esto es útil tanto para fines educativos como para comprender cómo se llega a la solución final de la derivada.

## Formulas basicas:
Derivada de una constante: 𝑑/𝑑𝑥(𝑐)=0   
Derivada de una potencia: 𝑑/𝑑𝑥(𝑥^𝑛)=𝑛𝑥^(𝑛−1)  
Regla del poducto: 𝑑/𝑑𝑥(𝑢𝑣)=𝑢′𝑣+𝑢𝑣′  
Regla del cociente: 𝑑/𝑑𝑥(𝑢/𝑣)=(𝑢′𝑣−𝑢𝑣′)/𝑣^2  
Regla de la cadena: 𝑑/𝑑𝑥(𝑓(𝑔(𝑥)))=𝑓′(𝑔(𝑥))⋅𝑔′(𝑥)

## contexto
Una calculadora de derivadas es una herramienta diseñada para calcular la derivada de funciones matemáticas de forma rápida y precisa. Estas calculadoras suelen estar disponibles en línea o como aplicaciones y permiten a los usuarios ingresar una función, que puede incluir polinomios, funciones trigonométricas, exponenciales, logarítmicas, y más. Una vez ingresada la función, la calculadora procesa la información y aplica las reglas de derivación para proporcionar la derivada correspondiente. Algunas de estas calculadoras también ofrecen funcionalidades adicionales, como la posibilidad de calcular derivadas parciales, derivadas sucesivas, o incluso mostrar el proceso paso a paso de cómo se llega al resultado. Además, algunas versiones avanzadas permiten graficar la función original junto con su derivada, lo que facilita la visualización del comportamiento de la función en diferentes puntos. Estas herramientas son particularmente útiles en contextos educativos, donde los estudiantes pueden verificar sus respuestas y comprender mejor los conceptos de cálculo diferencial, así como en entornos profesionales donde se requiere rapidez y precisión en los cálculos matemáticos.

## Algoritmo
Este programa calcula derivadas de funciones polinómicas, productos y cocientes de manera automática y guarda el procedimiento en un archivo. 

1. El usuario ingresa una función algebraica en formato de texto. La función puede ser un polinomio, un producto de dos funciones o un cociente de dos funciones.

2. El programa analiza la función ingresada para detectar automáticamente si es un polinomio, un producto o un cociente. No es necesario que el usuario especifique el tipo de función.

3. Según el tipo de función detectado:
   - Si la función es un polinomio **( 8x^2 - 3x )**, el programa separa cada término, deriva individualmente cada uno, y guarda el procedimiento paso a paso en un archivo llamado **procedimiento_derivada.txt**.
   - Si la función es un producto **( 3x * 8x^2 )**, el programa aplica la **regla del producto**: 
     𝑑/𝑑𝑥(𝑢𝑣)=𝑢′𝑣+𝑢𝑣′
     Deriva las dos funciones involucradas y guarda los pasos en el archivo de procedimiento.
   - Si la función es un cociente **( ( 3x+1 )/( 8x^2 - 3x ) )**, el programa aplica la **regla del cociente**:
     𝑑/𝑑𝑥(𝑢/𝑣)=(𝑢′𝑣−𝑢𝑣′)/𝑣^2
     Deriva el numerador y el denominador, y guarda el procedimiento en el archivo.

4. Después de derivar la función, el programa muestra en pantalla el resultado final de la derivada en su forma más simplificada.

5. A continuación, el programa pregunta al usuario si desea ver el procedimiento completo que se siguió para llegar al resultado. Si el usuario elige ver el procedimiento, el programa abre el archivo **procedimiento_derivada.txt** y muestra en pantalla los pasos guardados.

6. El programa pregunta si el usuario desea realizar otra derivada. Si el usuario responde que sí, el programa vuelve al paso 1, donde se solicita una nueva función para derivar. Si el usuario responde que no, el programa finaliza.

---

### Entradas

- Función algebraica (polinomio, producto o cociente) introducida en formato de texto.
- Opción del usuario para ver el procedimiento (**s/n**).
- Opción del usuario para realizar otra derivada (**s/n**).

### Proceso

El programa detecta automáticamente el tipo de función (polinomio, producto o cociente), deriva cada parte correspondiente y guarda cada paso del procedimiento en un archivo de texto. Luego, muestra el resultado simplificado al usuario y le pregunta si desea ver el procedimiento completo.

### Salida

- Derivada simplificada de la función ingresada.
- Procedimiento guardado en el archivo **procedimiento_derivada.txt** que puede ser mostrado al usuario si lo solicita.

