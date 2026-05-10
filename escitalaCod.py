def escitalaCod(texto, V):
    """
    Esta función se encarga de codificar una palabra mediente el método de Escítala.
    Entradas: El texto a codificar y la cantidad de letras que caben en una vuelta (V).
    Salidas: El texto pasado a Escítala.
    Restricciones: El texto debe ser un str y V un número entero positivo.
    """
    textoCod=""
    if len(texto) % V != 0:
        texto = texto + " " * (V - (len(texto) % V))
    texto = texto.replace(" ", "-")
    filas = len(texto) // V
    for fila in range(V):
        for columna in range(filas):
            textoCod+=texto[columna * V + fila]
    resultado = " "
    i = 0
    while i < len(textoCod):
        resultado = resultado + textoCod[i:i+5] + " "
        i += 5
    return resultado.strip()

def escitalaDec(textoCod, V):
    """
    Esta función decodifica un mensaje codificado con Escítala.
    Entradas: El texto codificado y la cantidad de letras por vuelta (v).
    Salidas: El texto original.
    Restricciones: el textoCod debe ser un string y V un número entero positivo.
    """
    texto = textoCod.replace(" ", "")
    filas = len(texto) // V
    resultado = [""] * len(texto)
    idx = 0
    for fila in range(V):
        for columna in range(filas):
            resultado[columna * V + fila] = texto[idx]
            idx += 1
    textoDeC = "".join(resultado)
    textoDeC = textoDeC.replace("-", " ")
    textoDeC = textoDeC.strip()
    return textoDeC
