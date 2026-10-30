import contextlib
import io

from arbol_binario import (
    altura_arbol,
    construir_ejemplo,
    crear_nodo,
    enlazar_hijo,
    identificar_hojas,
    identificar_nodos_internos,
    mostrar_arbol,
    obtener_relaciones,
    recorrer_preorden,
)


def debe_lanzar_value_error(funcion, *args):
    try:
        funcion(*args)
    except ValueError:
        return
    raise AssertionError("Se esperaba un ValueError.")


def probar_arbol_vacio():
    assert recorrer_preorden(None) == []
    assert identificar_hojas(None) == []
    assert identificar_nodos_internos(None) == []
    assert obtener_relaciones(None) == []
    assert altura_arbol(None) == -1

    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        mostrar_arbol(None)
    assert "árbol vacío" in salida.getvalue()


def probar_arbol_con_un_nodo():
    raiz = crear_nodo("A")
    assert recorrer_preorden(raiz) == ["A"]
    assert identificar_hojas(raiz) == ["A"]
    assert identificar_nodos_internos(raiz) == []
    assert altura_arbol(raiz) == 0


def probar_arbol_con_varios_nodos():
    raiz = construir_ejemplo()
    assert raiz["dato"] == "A"
    assert recorrer_preorden(raiz) == ["A", "B", "D", "E", "C", "F", "G"]
    assert identificar_nodos_internos(raiz) == ["A", "B", "C", "F"]
    assert identificar_hojas(raiz) == ["D", "E", "G"]
    assert altura_arbol(raiz) == 3
    assert obtener_relaciones(raiz) == [
        ("A", "izquierdo", "B"),
        ("A", "derecho", "C"),
        ("B", "izquierdo", "D"),
        ("B", "derecho", "E"),
        ("C", "derecho", "F"),
        ("F", "izquierdo", "G"),
    ]

    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        mostrar_arbol(raiz)
    assert "izquierdo: B" in salida.getvalue()
    assert "derecho: C" in salida.getvalue()


def probar_nodo_con_un_solo_hijo():
    raiz = crear_nodo("A")
    enlazar_hijo(raiz, crear_nodo("B"), "izquierdo")
    assert identificar_hojas(raiz) == ["B"]
    assert altura_arbol(raiz) == 1

    otra_raiz = crear_nodo("C")
    enlazar_hijo(otra_raiz, crear_nodo("D"), "derecho")
    assert identificar_hojas(otra_raiz) == ["D"]
    assert recorrer_preorden(otra_raiz) == ["C", "D"]


def probar_enlaces_invalidos():
    raiz = crear_nodo("A")
    hijo = crear_nodo("B")
    enlazar_hijo(raiz, hijo, "izquierdo")

    debe_lanzar_value_error(enlazar_hijo, raiz, crear_nodo("C"), "izquierdo")
    debe_lanzar_value_error(enlazar_hijo, raiz, crear_nodo("C"), "centro")
    debe_lanzar_value_error(enlazar_hijo, hijo, raiz, "derecho")
    debe_lanzar_value_error(enlazar_hijo, raiz, None, "derecho")


def ejecutar_pruebas():
    pruebas = [
        probar_arbol_vacio,
        probar_arbol_con_un_nodo,
        probar_arbol_con_varios_nodos,
        probar_nodo_con_un_solo_hijo,
        probar_enlaces_invalidos,
    ]
    for prueba in pruebas:
        prueba()
        print(f"OK: {prueba.__name__}")
    print(f"\n{len(pruebas)} pruebas superadas.")


if __name__ == "__main__":
    ejecutar_pruebas()
