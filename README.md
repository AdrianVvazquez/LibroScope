# Biblioteca de libros en Python

Este proyecto proporciona una biblioteca digital simple que permite contar la cantidad de veces que aparece un personaje en una página específica de un libro almacenado en una base de datos.

## Estructura del Proyecto

### 1. `LibraryDatabase`
Clase que maneja la base de datos de libros. Sus principales métodos incluyen:

- `getAllBookTitles()`: Devuelve una lista de todos los títulos de libros disponibles.
- `getBookByName(bookName)`: Obtiene el contenido de un libro por su nombre.
- `getBookCharacters(book)`: Devuelve los personajes principales de un libro.

### 2. `Library`
Clase que interactúa con la base de datos y permite contar personajes en páginas específicas de los libros.

- `countCharacters(book, character)`: Cuenta cuántas veces aparece un personaje en una página del libro.
- `getBookPageCharactersCount(bookName, page)`: Cuenta la aparición de cada personaje en una página específica de un libro.
- `getAllBookCharactersCount(bookName)`: Función en desarrollo para contar personajes en todo el libro.

### 3. Funciones auxiliares
- `validatePageInput(bookPage)`: Valida la entrada del número de página para evitar errores de ejecución.

## Cómo ejecutar el código

1. Asegúrate de tener Python instalado en tu sistema.
2. Guarda el archivo con extensión `.py`.
3. Ejecuta el script en la terminal usando:

   ```sh
   python nombre_del_archivo.py