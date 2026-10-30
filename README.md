# Árbol binario sin clases

Aplicación introductoria de consola para representar y recorrer un árbol binario
con diccionarios y funciones. No define clases.

## Requisitos

- Python 3.10 o posterior.
- No requiere instalar paquetes.

## Ejecutar la aplicación

```powershell
python arbol_binario.py
```

La aplicación muestra el árbol, su raíz, el recorrido en preorden, los nodos
internos, las hojas, la altura y las relaciones padre-hijo.

## Diagrama del ejemplo

```text
A
|-- izquierdo: B
|   |-- izquierdo: D
|   `-- derecho: E
`-- derecho: C
    `-- derecho: F
        `-- izquierdo: G
```

- Raíz: A.
- Nodos internos: A, B, C y F.
- Hojas: D, E y G.
- Altura: 3 aristas.
- Recorrido en preorden: A, B, D, E, C, F, G.

## Casos de prueba

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Árbol vacío | `None` | Sin nodos ni hojas; altura -1. |
| Un nodo | A | A es raíz y hoja; altura 0. |
| Varios niveles | Árbol del diagrama | Hojas D, E y G; altura 3. |
| Solo hijo izquierdo | A con hijo izquierdo B | B es hoja; altura 1. |
| Solo hijo derecho | C con hijo derecho D | D es hoja; preorden C, D. |
| Dos hijos | A con hijos B y C | B y C son hojas. |
| Enlace no válido | Lado incorrecto, enlace ocupado o ciclo | Se informa con `ValueError`. |

Ejecuta todas las pruebas con:

```powershell
python test_arbol_binario.py
```

## Representación

Cada nodo es un diccionario con las claves `dato`, `izquierdo` y `derecho`.
`crear_nodo` crea nodos y `enlazar_hijo` conecta cada padre con un hijo por el
lado indicado. Los recorridos y consultas aceptan `None` para representar un
árbol vacío. La altura se mide en aristas: un árbol vacío tiene altura -1 y un
árbol de un solo nodo tiene altura 0.
