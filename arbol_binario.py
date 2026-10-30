#Demostración funcional de un árbol binario.


def crear_nodo(dato):
    return {"dato": dato, "izquierdo": None, "derecho": None}


def _es_nodo(nodo):
    return (
        isinstance(nodo, dict)
        and "dato" in nodo
        and "izquierdo" in nodo
        and "derecho" in nodo
    )


def _nodos_alcanzables(raiz):
    if raiz is None:
        return []
    if not _es_nodo(raiz):
        raise ValueError("La raíz debe ser un nodo válido o None.")

    nodos = []
    pendientes = [raiz]
    visitados = set()

    while pendientes:
        nodo = pendientes.pop()
        if not _es_nodo(nodo):
            raise ValueError("El árbol contiene una referencia a un nodo inválido.")
        if id(nodo) in visitados:
            raise ValueError("La estructura contiene ciclos o nodos compartidos.")
        visitados.add(id(nodo))
        nodos.append(nodo)

        if nodo["derecho"] is not None:
            pendientes.append(nodo["derecho"])
        if nodo["izquierdo"] is not None:
            pendientes.append(nodo["izquierdo"])

    return nodos


def enlazar_hijo(padre, hijo, lado):
    if not _es_nodo(padre):
        raise ValueError("El padre debe ser un nodo válido.")
    if not _es_nodo(hijo):
        raise ValueError("El hijo debe ser un nodo válido.")
    if lado not in ("izquierdo", "derecho"):
        raise ValueError("El lado debe ser 'izquierdo' o 'derecho'.")
    if padre[lado] is not None:
        raise ValueError(f"El hijo {lado} ya está ocupado.")

    nodos_existentes = _nodos_alcanzables(padre)
    nodos_candidatos = _nodos_alcanzables(hijo)
    if {id(nodo) for nodo in nodos_existentes}.intersection(
        id(nodo) for nodo in nodos_candidatos
    ):
        raise ValueError("El enlace produciría un ciclo o compartiría nodos.")

    padre[lado] = hijo


def recorrer_preorden(raiz):
    if raiz is None:
        return []
    if not _es_nodo(raiz):
        raise ValueError("La raíz debe ser un nodo válido o None.")

    return (
        [raiz["dato"]]
        + recorrer_preorden(raiz["izquierdo"])
        + recorrer_preorden(raiz["derecho"])
    )


def identificar_hojas(raiz):
    return [
        nodo["dato"]
        for nodo in _nodos_alcanzables(raiz)
        if nodo["izquierdo"] is None and nodo["derecho"] is None
    ]


def identificar_nodos_internos(raiz):
    return [
        nodo["dato"]
        for nodo in _nodos_alcanzables(raiz)
        if nodo["izquierdo"] is not None or nodo["derecho"] is not None
    ]


def obtener_relaciones(raiz):
    relaciones = []
    for nodo in _nodos_alcanzables(raiz):
        for lado in ("izquierdo", "derecho"):
            hijo = nodo[lado]
            if hijo is not None:
                relaciones.append((nodo["dato"], lado, hijo["dato"]))
    return relaciones


def altura_arbol(raiz):
    """Devuelve la altura en aristas: -1 para vacío y 0 para un nodo."""
    if raiz is None:
        return -1
    if not _es_nodo(raiz):
        raise ValueError("La raíz debe ser un nodo válido o None.")
    return 1 + max(altura_arbol(raiz["izquierdo"]), altura_arbol(raiz["derecho"]))


def mostrar_arbol(raiz):
    if raiz is None:
        print("(árbol vacío)")
        return
    if not _es_nodo(raiz):
        raise ValueError("La raíz debe ser un nodo válido o None.")

    print(raiz["dato"])
    _mostrar_descendientes(raiz, "")


def _mostrar_descendientes(nodo, prefijo):
    hijos = [
        (lado, nodo[lado])
        for lado in ("izquierdo", "derecho")
        if nodo[lado] is not None
    ]
    for indice, (lado, hijo) in enumerate(hijos):
        es_ultimo = indice == len(hijos) - 1
        conector = "`-- " if es_ultimo else "|-- "
        print(f"{prefijo}{conector}{lado}: {hijo['dato']}")
        nuevo_prefijo = prefijo + ("    " if es_ultimo else "|   ")
        _mostrar_descendientes(hijo, nuevo_prefijo)


def construir_ejemplo():
    raiz = crear_nodo("A")
    nodo_b = crear_nodo("B")
    nodo_c = crear_nodo("C")
    nodo_d = crear_nodo("D")
    nodo_e = crear_nodo("E")
    nodo_f = crear_nodo("F")
    nodo_g = crear_nodo("G")

    enlazar_hijo(raiz, nodo_b, "izquierdo")
    enlazar_hijo(raiz, nodo_c, "derecho")
    enlazar_hijo(nodo_b, nodo_d, "izquierdo")
    enlazar_hijo(nodo_b, nodo_e, "derecho")
    enlazar_hijo(nodo_c, nodo_f, "derecho")
    enlazar_hijo(nodo_f, nodo_g, "izquierdo")
    return raiz


def main():
    raiz = construir_ejemplo()

    print("Representación del árbol:")
    mostrar_arbol(raiz)
    print(f"\nRaíz: {raiz['dato']}")
    print(f"Nodos en preorden: {recorrer_preorden(raiz)}")
    print(f"Nodos internos: {identificar_nodos_internos(raiz)}")
    print(f"Hojas: {identificar_hojas(raiz)}")
    print(f"Altura (en aristas): {altura_arbol(raiz)}")
    print("\nRelaciones padre-hijo:")
    for padre, lado, hijo in obtener_relaciones(raiz):
        print(f"{padre} --{lado}--> {hijo}")


if __name__ == "__main__":
    main()
