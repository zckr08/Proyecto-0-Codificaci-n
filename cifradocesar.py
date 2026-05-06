def validarTexto(texto):
    """Esta es una función booleana que va a recibir un texto y va a verificar si contiene
       únicamente letras y espacios.
       Entradas: texto = String.
       Salidas: True si el solo contiene letras y espacios.
                False en caso contrario.
       Restricciones: Ninguna. 
    """
    texto = texto.lower()
    for caracter in texto:
        if caracter not in ("abcdefghijklmnñopqrstuvwxyz "):
            return False
    return True

###############################################################################
#      Funciones que se repiten                                               #
###############################################################################

def codificarProblema1(texto, desplazamiento):
    """Esta función es la encargada de realizar la codificación tipo Cesar a partir de un texto y un desplazamiento
       Entradas: Texto = String que solo contenga letras y espacios.
                 Desplazamiento = Int 
       Salidas:  Texto codificado = String
       Restricciones: Texto solo puede contener letras y espacios
                      Desplazamiento debe de ser un valor entero
    """
    if validarTexto(texto) != True:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if type(desplazamiento) != int:
        raise Exception("Error: El valor del desplazamiento tiene que ser un número entero.") 
    texto = texto.lower()
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    textoCodificado = ""
    for caracter in texto:
            posicion = ((alfabeto.index(caracter))+desplazamiento)%27
            textoNuevo =+ alfabeto[posicion]
    return textoCodificado

def decodificarProblema1(texto, desplazamiento):
    """Esta función es la encargada de realizar la decodificación tipo Cesar a partir de un texto y un desplazamiento
       Entradas: Texto = String que solo contenga letras y espacios.
                 Desplazamiento = Int 
       Salidas:  Texto codificado = String
       Restricciones: Texto solo puede contener letras y espacios
                      Desplazamiento debe de ser un valor entero
    """
    if validarTexto(texto) != True:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if type(desplazamiento) != int:
        raise Exception("Error: El valor del desplazamiento tiene que ser un número entero.") 
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    texto = texto.lower()
    textoNuevo = ""
    for caracter in texto:
            posicion = ((alfabeto.index(caracter))-desplazamiento)%27
            textoNuevo =+ alfabeto[posicion]
    return textoNuevo

###############################################################################
#      Problema #1 resuelto                                                   #
###############################################################################

def nuevoAbecedario(palabra):
    """Esta funcion tiene como objetivo crear un nuevo orden del abecedario a partir de una palabra clave.
       Entradas: palabra = string de solo letras y espacios.
       Salidas: una lista con el alfabeto original y el alfabeto modificado.
       Restricciones: palabra debe de ser un string que solo contenga espacios o letras.
    """
    if validarTexto(palabra) != True:
        raise Exception("Error: La palabra clave solo debe contener letras y espacios.")
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    alfabetoNuevo = alfabeto.copy()
    palabraF = ""
    palabra = palabra.lower()
    for letra in palabra:
         if letra not in palabraF:
              palabraF =+ letra
    for caracter in palabraF:
        alfabetoNuevo.remove(i)
    for i in palabraF:
        alfabetoNuevo.insert((palabraF.index(i)),i)
    alfabetos = [alfabeto,alfabetoNuevo]
    return alfabetos

def codificarProblema2(texto, palabra):
    if validarTexto(texto) != True:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if validarTexto(palabra) != True:
        raise Exception("Error: La palabra clave solo debe contener letras y espacios.")
    alfabeto = nuevoAbecedario(palabra)[0]
    alfabetoNuevo = nuevoAbecedario(palabra)[1]
    texto = texto.lower()
    textoCodificado = ""
    for caracter in texto:
         if caracter not in alfabetoNuevo:
            textoCodificado =+ caracter
         else:
            textoCodificado =+ alfabetoNuevo[alfabeto.index(caracter)]
    return textoCodificado

def decodificarProblema2(texto, palabra):
    if validarTexto(texto) != True:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if validarTexto(palabra) != True:
        raise Exception("Error: La palabra clave solo debe contener letras y espacios.")
    alfabeto = nuevoAbecedario(palabra)[0]
    alfabetoNuevo = nuevoAbecedario(palabra)[1]
    texto = texto.lower()
    textoDecodificado = ""
    for caracter in texto:
         if caracter not in alfabeto:
            textoDecodificado =+ caracter
         else:
            textoDecodificado =+ alfabeto[alfabetoNuevo.index(caracter)]
    return textoDecodificado

###############################################################################
#      Problema #2 resuelto                                                   #
###############################################################################

def codificarProblema3(texto, palabra):
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    palabra = palabra.lower()
    texto = texto.lower()
    textoCodificado = ""
    contador = 0
    for i in texto:
            if i not in alfabeto:
                textoCodificado = textoCodificado+i
            else:
                posicion = (alfabeto.index(i)+(alfabeto.index((palabra[(contador%len(palabra))]))))%27
                textoCodificado = textoCodificado+alfabeto[posicion]
                contador += 1
    return textoCodificado

def decodificarProblema3(texto, palabra):
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    palabra = palabra.lower()
    texto = texto.lower()
    textoCodificado = ""
    contador = 0
    for i in texto:
            if i not in alfabeto:
                textoCodificado = textoCodificado+i
            else:
                posicion = (alfabeto.index(i)-(alfabeto.index((palabra[(contador%len(palabra))]))))%27
                textoCodificado = textoCodificado+alfabeto[posicion]
                contador += 1
    return textoCodificado

###############################################################################
#      Problema #3 resuelto                                                   #
###############################################################################
