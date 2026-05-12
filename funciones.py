###########################################################
#Esta sección va a contener algunas funciones recurrentes,# 
# algunas de interfaz de usuario y otras que se se        #
#utilizan en otras funciones.                             #
###########################################################

def limpiarPantalla():
    """
    Esta subrutina se encarga únicamente de limpiar la pantalla.
    Entradas: Ninguna
    Salidas: Pantalla limpia
    Restricciones: Ninguna
    """
    print("\n" * 40)

def prepararTexto(texto):
    """Esta función va a preparar texto para que puedan ser procesados correctamente.
       Entradas: texto = string
       Salidas: texto preparado = string
       Restricciones: texto debe ser un string
    """
    if type(texto) != str:
        raise Exception("Debe ingresar un string")
    texto = texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    return texto

def validarTexto(texto):
    """Esta es una función booleana que va a recibir un texto y va a verificar si contiene
       únicamente letras y espacios.
       Entradas: texto = String.
       Salidas: True si el solo contiene letras y espacios.
                False en caso contrario.
       Restricciones: Texto debe ser un string. 
    """
    if type(texto) != str:
        raise Exception("Debe ingresar un string")
    texto = prepararTexto(texto)
    for caracter in texto:
        if caracter not in ("abcdefghijklmnñopqrstuvwxyz "):
            return False
    return True

def validarPalabra(texto):
    """Esta es una función booleana que va a recibir un texto y va a verificar si contiene
       únicamente letras.
       Entradas: texto = String.
       Salidas: True si el solo contiene letras y espacios.
                False en caso contrario.
       Restricciones: texto debe ser un string. 
    """
    if type(texto) != str:
        raise Exception("Debe ingresar un string")
    texto = prepararTexto(texto)
    for caracter in texto:
        if caracter not in ("abcdefghijklmnñopqrstuvwxyz"):
            return False
    return True

def nuevoAbecedario(palabra):
    """Esta funcion tiene como objetivo crear un nuevo orden del abecedario a partir de una palabra clave.
       Entradas: palabra = string de solo letras y espacios.
       Salidas: una lista con el alfabeto original y el alfabeto modificado.
       Restricciones: palabra debe de ser un string que solo contenga espacios o letras.
    """
    if validarPalabra(palabra) != True or type(palabra) != str:
        raise Exception("Error: La palabra clave solo debe contener letras.")
    palabra = prepararTexto(palabra)
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    alfabetoNuevo = alfabeto.copy()
    palabraF = ""
    palabra = palabra.lower()
    for letra in palabra:
         if letra not in palabraF:
              palabraF = palabraF+letra
    for caracter in palabraF:
        alfabetoNuevo.remove(caracter)
    for caracter in palabraF:
        alfabetoNuevo.insert((palabraF.index(caracter)),caracter)
    alfabetos = [alfabeto,alfabetoNuevo]
    return alfabetos

def matrizPlayFair(clave):
    """
    Esta función es la encargada de crear la matriz para el metodo PlayFair.
    Elimina las letras repetidas en la palabra clave y luego forma la matriz
    Entradas: La palabra Clave
    Salidas: Matriz lista para codificar
    Restricciones: Ninguna
    """
    claveLista = ""
    for letra in clave:
        if letra not in claveLista:
            claveLista += letra
    lista = [letra for letra in claveLista]
    for letra in "abcdefghijklmnñopqrstuvwxyz123":
        if letra not in lista:
            lista.append(letra)
    indice = 0
    matriz = []
    for fila in range(6):
        L = []
        for columna in range(5):
            L.append(lista[indice])
            indice += 1
        matriz.append(L)
    return matriz
    
def separarTextoPlayFair(texto):
    """
    Esta función separa el texto original en grupos de dos letras
    para poder codificarlo a PlayFair. Remplaza dos letras iguales juntas por un 1.
    Ejemplo: mississippi -> mi, s1, si, s1, is, si, p1, pi
    Entradas: El texto que quiere ser codificado.
    Salidas: Texto separado
    Restricciones: ninguna.
    """
    texto = texto.lower().strip()
    pares = []
    i = 0
    procesar = []
    while i < len(texto):
        procesar.append(texto[i])
        if i+1 < len(texto) and texto[i]==texto[i+1]:
            procesar.append("1")
        i+=1
    texto="".join(procesar)
    i=0
    while i < len(texto):
        if i == len(texto)-1:
            pares.append(texto[i] + "1")
            i += 1
        else:
            letra1 = texto[i]
            letra2 = texto[i+1]
            if letra1 == letra2:
                pares.append("1" + letra2)
                i += 1
            else:
                pares.append(letra1 + letra2)
                i += 2
    return pares

def parCod_PlayFair(matriz, letra1, letra2):
    """
    Esta función se encarga de codificar los pares de letras necesarias para completar la codificación de la palabra.
    Entradas: matriz, letra1, letra2
    Salidas: pares de letras codificados.
    Restricciones: Ninguna.
    """
    fila1, col1 = posicionPlayFair(matriz, letra1)
    fila2, col2 = posicionPlayFair(matriz, letra2)
    if fila1 == fila2:
        nueva1 = matriz[fila1][(col1 + 1) % 5]
        nueva2 = matriz[fila2][(col2 + 1) % 5]
    elif col1 == col2:
        nueva1 = matriz[(fila1+1)%6][col1]
        nueva2 = matriz[(fila2+1)%6][col2]
    else:
         nueva1=matriz[fila1][col2]
         nueva2=matriz[fila2][col1]
    return nueva1 + nueva2

def posicionPlayFair(matriz, letra):
    """
    Esta función encuentra la posición de los pares codificados en la matriz
    Entradas: La matriz y la letra que se desea identificar
    Salidas: posición de pares en la matriz
    Restricciones: Ninguna
    """
    for fila in range(6):
        for columna in range(5):
            if matriz[fila][columna] == letra:
                return fila, columna

def parDec_PlayFair(matriz, letra1, letra2):
    """
    Esta función se encarga de decodificar los pares de letras para devolver el par original.
    Entradas: Las dos letras que tiene que descodificarse y la matriz
    Salidas: El par de letras en su estado original.
    Restricciones: Ninguna
    """
    fila1, col1 = posicionPlayFair(matriz, letra1)
    fila2, col2 = posicionPlayFair(matriz, letra2)
    if fila1 == fila2:
        nueva1 = matriz[fila1][(col1 - 1) % 5]
        nueva2 = matriz[fila2][(col2 - 1) % 5]
    elif col1 == col2:
        nueva1 = matriz[(fila1 - 1) % 6][col1]
        nueva2 = matriz[(fila2 - 1) % 6][col2]
    else:
        nueva1 = matriz[fila1][col2]
        nueva2 = matriz[fila2][col1]
    return nueva1 + nueva2

def quitarNum(texto):
    """
    Esta subrutina elimina los números del texto decodificado en caso de que tuviera.
    Entradas: El texto decodifcado
    Salidas: El texto en su forma original sin los números del PlayFair
    Restricciones: Ninguna
    """
    palabras = texto.split()
    textoFinal = ""
    for palabra in palabras:
        palabraLimpia = ""
        i = 0
        while i < len(palabra):
            letra = palabra[i]
            if letra == "1":
                if i == 0:
                    i += 1
                    continue
                if i == len(palabra) - 1:
                    i += 1
                    continue
                if i == len(palabra) - 2:
                    palabraLimpia += palabra[i + 1]
                    i += 2
                    continue
                if i + 1 < len(palabra) and palabra[i - 1] == palabra[i + 1]:
                    i += 1
                    continue
            palabraLimpia += letra
            i += 1
        textoFinal += palabraLimpia + " "
    return textoFinal.strip()
    
def separarParesPlayFair(texto):
    """
    Esta función separa los pares de letras codificados para decodificarlos.
    Entradas: Texto
    Salidas: las letras en grupos pares
    Restricciones: ninguna
    """
    #Uso esta para decodificar porque con separarTextoPlayFair si detecta una letra repetida en la palabra codificada le pone un 1 que queda en el resultado final
    pares = []
    i = 0
    while i < len(texto):
        pares.append(texto[i] + texto[i+1])
        i += 2
    return pares


#########################################################
#A partir de aquí van a ir las funciones de codificación#
#########################################################

def cesarCod(texto, desplazamiento):
    """Esta función es la encargada de realizar la codificación tipo Cesar a partir de un texto y un desplazamiento
       Entradas: Texto = String que solo contenga letras y espacios.
                 Desplazamiento = Int 
       Salidas:  Texto codificado = String
       Restricciones: Texto solo puede contener letras y espacios
                      Desplazamiento debe de ser un valor entero
    """
    if validarTexto(texto) != True or type(texto) != str:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if type(desplazamiento) != int:
        raise Exception("Error: El valor del desplazamiento tiene que ser un número entero.") 
    texto = prepararTexto(texto)
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    textoCod = ""
    for caracter in texto:
            if caracter != " ":
                posicion = ((alfabeto.index(caracter))+desplazamiento)%27
                textoCod = textoCod+alfabeto[posicion]
            else:
                textoCod = textoCod+caracter
    return textoCod

def cesarDec(texto, desplazamiento):
    """Esta función es la encargada de realizar la decodificación tipo Cesar a partir de un texto y un desplazamiento
       Entradas: Texto = String que solo contenga letras y espacios.
                 Desplazamiento = Int 
       Salidas:  Texto codificado = String
       Restricciones: Texto solo puede contener letras y espacios
                      Desplazamiento debe de ser un valor entero
    """
    if validarTexto(texto) != True or type(texto) != str:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if type(desplazamiento) != int:
        raise Exception("Error: El valor del desplazamiento tiene que ser un número entero.") 
    texto = prepararTexto(texto)
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    textoDec = ""
    for caracter in texto:
        if caracter != " ":
            posicion = ((alfabeto.index(caracter))-desplazamiento)%27
            textoDec = textoDec + alfabeto[posicion]
        else:
            textoDec = textoDec + caracter
    return textoDec


def monoCod(texto, palabra):
    """Esta función se va a encargar de realizar una codificación tipo Mono alfabetico a partir de una palabra clave.
       Entradas: texto = string con letras y espacios.
                 palabra = string con letras.
       Salidas: texto codificado = string.
       Restricciones: texto debe ser un string unicamente con letras y espacios.
                      palabra debe ser un string unicamente con letras.  
    """
    if validarTexto(texto) != True or type(texto) != str:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if validarPalabra(palabra) != True or type(palabra) != str:
        raise Exception("Error: La palabra clave solo debe contener letras.")
    alfabeto = nuevoAbecedario(palabra)[0]
    alfabetoNuevo = nuevoAbecedario(palabra)[1]
    texto = prepararTexto(texto)
    textoCod = ""
    for caracter in texto:
         if caracter not in alfabetoNuevo:
            textoCod = textoCod + caracter
         else:
            textoCod = textoCod + alfabetoNuevo[alfabeto.index(caracter)]
    return textoCod

def monoDec(texto, palabra):
    """Esta función se va a encargar de realizar una decodificación tipo Mono alfabetico a partir de una palabra clave.
       Entradas: texto = string con letras y espacios.
                 palabra = string con letras.
       Salidas: texto decodificado = string.
       Restricciones: texto debe ser un string unicamente con letras y espacios.
                      palabra debe ser un string unicamente con letras.  
    """
    if validarTexto(texto) != True or type(texto) != str:
        raise Exception("Error: El texto solo debe contener letras y espacios.")
    if validarPalabra(palabra) != True or type(palabra) != str:
        raise Exception("Error: La palabra clave solo debe contener letras.")
    alfabeto = nuevoAbecedario(palabra)[0]
    alfabetoNuevo = nuevoAbecedario(palabra)[1]
    texto = prepararTexto(texto)
    textoDec = ""
    for caracter in texto:
         if caracter not in alfabeto:
            textoDec = textoDec + caracter
         else:
            textoDec = textoDec + alfabeto[alfabetoNuevo.index(caracter)]
    return textoDec

def vigenereCod(texto, palabra):
    """Esta función se va a encargar de realizar una codificación tipo Vigenere.
       Entradas: texto = string con letras y espacios.
                 palabra = string con letras.
       Salidas: texto codificado = string.
       Restricciones: texto debe ser un string unicamente con letras y espacios.
                      palabra debe ser un string unicamente con letras.  
    """
    if validarTexto(texto) != True or type(texto) != str:
        raise Exception("Error: Debe ingresar un texot válida que solo contenga letras y espacios.")
    if validarPalabra(palabra) != True or type(texto) != str:
        raise Exception("Error: Debe ingresar una palabra válida que solo contenga letras.")
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    palabra = prepararTexto(palabra)
    texto = prepararTexto(texto)
    textoCod = ""
    contador = 0
    for i in texto:
            if i not in alfabeto:
                textoCod = textoCod+i
            else:
                posicion = (alfabeto.index(i)+(alfabeto.index((palabra[(contador%len(palabra))]))))%27
                textoCod = textoCod+alfabeto[posicion]
                contador += 1
    return textoCod

def vigenereDec(texto, palabra):
    """Esta función se va a encargar de realizar una decodificación tipo Vigenere.
       Entradas: texto = string con letras y espacios.
                 palabra = string con letras.
       Salidas: texto decodificado = string.
       Restricciones: texto debe ser un string unicamente con letras y espacios.
                      palabra debe ser un string unicamente con letras.  
    """
    if validarTexto(texto) != True:
        raise Exception("Error: Debe ingresar un texot válida que solo contenga letras y espacios.")
    if validarPalabra(palabra) != True:
        raise Exception("Error: Debe ingresar una palabra válida que solo contenga letras.")
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    palabra = prepararTexto(palabra)
    texto = prepararTexto(texto)
    textoDec = ""
    contador = 0
    for i in texto:
            if i not in alfabeto:
                textoDec = textoDec+i
            else:
                posicion = (alfabeto.index(i)-(alfabeto.index((palabra[(contador%len(palabra))]))))%27
                textoDec = textoDec+alfabeto[posicion]
                contador += 1
    return(textoDec)

def PlayFairCod(texto, clave):
    """
    Esta función codifica una palabra usando el metodo PlayFait modificado.
    Entradas: Texto a codificar. Palabra Clave
    Salidas: Texto del usuario codificado con PlayFair
    Restricciones: Texto debe ser string.
    """
    palabras = texto.split()
    textoCod = ""
    texto = texto.lower().strip()
    matriz = matrizPlayFair(clave)
    pares = separarTextoPlayFair(texto)
    for palabra in palabras:
        pares = separarTextoPlayFair(palabra)
        for par in pares:
            letra1=par[0]
            letra2=par[1]
            textoCod += parCod_PlayFair(matriz, letra1, letra2)
        textoCod += " "
    return textoCod.strip()

print(PlayFairCod("guitarras guardadas en el placard", "profundizaste"))

def PlayFairDec(textoCod, clave):
    """
    Esta función se encarga de decodificar un mensaje codifico con PlayFair.
    Entradas: El texto Codificado y la palabra Clave
    Salidas: El texto codificado pasa a ser texto normal.
    Restricciones: TextoCod y clave deben ser str.
    """     
    palabras=textoCod.split()
    textoDec=""
    matriz=matrizPlayFair(clave)
    for palabra in palabras:
        pares=separarParesPlayFair(palabra)
        for par in pares:
            textoDec += parDec_PlayFair(matriz, par[0], par[1])
        textoDec+=" "
    textoDec = textoDec.strip()
    return quitarNum(textoDec)

print(PlayFairCod("lpdeduyonc lpduininxe si cj ugclduyi", "profundizaste"))

def railfenceCod(texto):
    """Esta función se va a encargar de codificar un texto siguiendo un patron de zigzag y algunos añadidos.
       Entradas: texto = string
       Salidas: texto codificado = string
       Restricciones = texto tiene que ser string
       """
    if type(texto) != str:
        raise Exception("Error: Debe ingresar un string.")
    textoCodificado = ""
    if len(texto) % 4 != 0:
        texto = texto+" "*(4-(len(texto)%4))
    texto = texto.replace(" ", "-")
    texto = list(texto)
    for caracter in texto[0::4]:
        textoCodificado = textoCodificado+caracter
    for caracter in texto[1::2]:
        textoCodificado = textoCodificado+caracter
    for caracter in texto[2::4]:
        textoCodificado = textoCodificado+caracter
    docker1 = list(textoCodificado)
    docker2 = []
    while docker1 != []:
        for i in range(0,5):
            if docker1 != []:
                docker2.append(docker1.pop(0))
        if docker1 != []:
            docker2.append(" ")
    textoCodificado = ""
    for i in docker2:
        textoCodificado = textoCodificado+i         
    return textoCodificado
    
def railfenceDec(texto):
    """Esta función se va a encargar de decodificar un texto siguiendo un patron de zigzag y algunos añadidos.
       Entradas: texto = string
       Salidas: texto decodificado = string
       Restricciones = texto tiene que ser string
    """
    if type(texto) != str:
        raise Exception("Error: Debe ingresar un string.")
    textoDecodificado = ""
    fila1 = []
    fila2 = []
    fila3 = []
    docker1 = list(texto)
    docker2 = []
    while docker1 != []:
        for i in range(0,5):
            if docker1 != []:
                docker2.append(docker1.pop(0))
        if docker1 != []:
            docker1.remove(" ")
    texto = ""
    for i in docker2:
        texto = texto+i
    texto = list(texto)
    for caracter in texto[0:int((len(texto)/4)):]:
        fila1.append(caracter)
    for caracter in texto[int((len(texto)/4)):int((len(texto)/4)*3):]:
        fila2.append(caracter)
    for caracter in texto[int((len(texto)/4)*3)::]:
        fila3.append(caracter)
    while fila2 != []:
        textoDecodificado = textoDecodificado + fila1.pop(0)
        textoDecodificado = textoDecodificado + fila2.pop(0)
        textoDecodificado = textoDecodificado + fila3.pop(0)
        textoDecodificado = textoDecodificado + fila2.pop(0) 
    textoDecodificado = textoDecodificado.replace("-", " ")
    docker1 = list(textoDecodificado)
    while docker1[-1] == " ":
        docker1.pop(-1)
    textoDecodificado = ""
    for i in docker1:
        textoDecodificado = textoDecodificado+i
    return textoDecodificado

def escitalaCod(texto, V):
    """
    Esta función se encarga de codificar una palabra mediente el método de Escítala.
    Entradas: El texto a codificar y la cantidad de letras que caben en una vuelta (V).
    Salidas: El texto pasado a Escítala.
    Restricciones: El texto debe ser un str y V un número entero positivo.
    """
    if type(texto) != str:
        raise Exception("Error: Debe ingresar un string.")
    if type(V) != int or V < 1:
        raise Exception("Error: Debe ingresar un número entero positivo")
    textoCod=""
    if len(texto) % V != 0:
        texto = texto + " " * (V - (len(texto) % V))
    texto = texto.replace(" ", "-")
    filas = len(texto) // V
    for fila in range(V):
        for columna in range(filas):
            textoCod = textoCod + texto[columna * V + fila]
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
    if type(textoCod) != str:
        raise Exception("Error: Debe ingresar un string.")
    if type(V) != int or V < 1:
        raise Exception("Error: Debe ingresar un número entero positivo")
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