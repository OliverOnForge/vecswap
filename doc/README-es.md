
# vecswap 📐

[View in English](../README.md)

**vecswap** es una biblioteca ligera de Python diseñada para la manipulación, transformación y filtrado eficiente de vectores (listas de enteros). Es ideal para proyectos que requieren operaciones geométricas simples, lógica de arreglos o limpieza de datos sin depender de librerías externas pesadas.

## 🚀 Instalación

Actualmente, puedes usar **vecswap** clonando el repositorio o copiando el archivo `tools.py` en tu directorio de trabajo:

```bash
git clone https://github.com/tu-usuario/vecswap.git
```

## 🛠️ Módulos y Funcionalidades

### 1\. Generadores (`Generators`)

Crea vectores rápidamente con valores predefinidos o aleatorios.

- **`generate_full_int(n, value)`**: Crea un vector de tamaño `n` lleno del entero `value`.
- **`generate_random_int(n, v_min, v_max)`**: Genera un vector con `n` enteros aleatorios entre `v_min` y `v_max`.
- **`generate_range_int(start, stop, step)`**: Genera una secuencia de enteros con un incremento definido.

### 2\. Operadores y Comparadores (`Operators & Comparators`)

Herramientas para comparar y combinar vectores.

- **`add_vectors` / `subtract_vectors`**: Suma y resta elemento a elemento (requiere vectores de igual longitud).
- **`interleave_from`**: Intercala un segundo vector en el primero a partir de un índice específico.
- **`matched_indices` / `mismatched_indices`**: Retorna una lista con las posiciones donde los valores coinciden o difieren.
- **`intersection` / `symmetric_difference`**: Operaciones lógicas para encontrar elementos comunes o únicos entre dos listas.

### 3\. Transformadores (`Transformers`)

Modifica los datos del vector manteniendo su tamaño original.

- **`normalize`**: Escala todos los valores del vector al rango numérico $[0.0, 1.0]$.
- **`reflect_vertical(vector, center)`**: Refleja cada valor verticalmente usando un "centro" como eje (fórmula: $2 \cdot \text{center} - \text{valor}$).
- **`fill_pattern(vector, value, n, m)`**: Sobrescribe el vector siguiendo un patrón: llena `n` elementos y salta `m` posiciones.

### 4\. Reordenamiento y Estructura (`Reordering`)

Cambia la disposición física de los elementos.

 - **`mirror`**: Invierte el orden completo del vector.
 - **`random_swap(vector, changes)`**: Intercambia posiciones aleatorias el número de veces indicado.
 - **`reflect_on_axis(vector, axis_index)`**: Intercambia elementos alrededor de un índice que actúa como pivote.

### 5\. Limitadores (`Limiters`)

Controla que los valores no excedan rangos específicos.

- **`clamp(vector, min_val, max_val)`**: Restringe todos los valores al rango especificado.
- **`limit_by_range(vector, center, offset)`**: Mantiene los valores dentro de un radio de distancia respecto a un valor central.

-----

## 🗺️ Roadmap
¿Tienes una idea para una nueva funcionalidad? > Si hay alguna operación de vectores que consideres esencial, no dudes en abrir un issue o contactarme vía GitHub.

- Visualización: Implementación de animaciones dinámicas para ilustrar el comportamiento de cada función de transformación y reordenamiento.
- Optimización: Mejora del rendimiento en operaciones de comparación para vectores de gran escala.

## 🤝 Contribuciones

¡Las colaboraciones son lo que hacen a la comunidad de código abierto un lugar increíble para aprender, inspirar y crear! Cualquier aportación que hagas será muy apreciada.

Para mantener la calidad del código y la coherencia del proyecto, por favor revisa nuestras guías detalladas antes de enviar un Pull Request:

👉 [Leer Guía de Contribución](CONTRIBUTING-es.md)

## 📃 Licencia

Este proyecto se distribuye bajo la lincencia MIT.

[MIT LICENCE](../LICENCE)

## 📬 Contacto

Puedes seguir el desarrollo del proyecto o contactarme para sugerencias en:

- **GitHub**: [OliverOnForge](https://github.com/OliverOnForge)

-----

### 🧪 Pruebas (Testing)

Para verificar que todo funcione correctamente, puedes ejecutar los tests unitarios desde la raíz del proyecto:

```bash
python3 -m unittest test/test.py
```
