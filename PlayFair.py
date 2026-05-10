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
            pares.append("1" + texto[i])
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
                    i+=1
                    continue
                if i==len(palabra)-1:
                    i+=1
                    continue
                if i==len(palabra)-2:
                    i+=1
                    continue
                if palabra[i-1] == palabra[i+1]:
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
