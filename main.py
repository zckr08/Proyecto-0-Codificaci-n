import funciones as f

def main():
    """
    Este es el programa principal de todos los métodos de cifrado.
    Aquí se encuentra la interfaz con el usuario, se invocan el resto de funciones y se chequean restricciones.
    Entradas: Ninguna
    Salidas: Lo que eliga el usuario
    Restricciones: Entradas deben str y restricciones cambian dependiendo la función que sea invocada.
    """
    f.limpiarPantalla()
    print(" ______  ______  ______  ______  ______  ______  ______ \n| |__| || |__| || |__| || |__| || |__| || |__| || |__| |\n|  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |\n|______||______||______||______||______||______||______|\n ______                                          ______ \n| |__| |              ¡BIENVENIDO!              | |__| |\n|  ()  |  CON ESTE PROGRAMA PUEDES CODIFICAR O  |  ()  |\n|______|   DECODIFICAR MENSAJES CON DISTINTOS   |______|\n ______          METODOS DECODIFICACION          ______ \n| |__| |                                        | |__| |\n|  ()  |      CREADO POR JOSE O. Y ZACK R.      |  ()  |\n|______|                                        |______|\n ______  ______  ______  ______  ______  ______  ______ \n| |__| || |__| || |__| || |__| || |__| || |__| || |__| |\n|  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |\n|______||______||______||______||______||______||______|")
    continuar = 1
    while continuar == 1:
        try:
            print("\nElige un método de cifrado:\n1. Cifrado César\n2. Cifrado monoalfabético con palabra clave\n3. Cifrado Vigenère\n4. Cifrado PlayFair modificado\n5. Cifrado Rail Fence\n6. Escítala\n")
            seleccionMetodo = int(input("Para seleccionar elige el número del cifrado (1 a 6): \n"))
            while seleccionMetodo > 6 or seleccionMetodo < 1:
                seleccionMetodo = int(input("La selección tiene que hacerse con un número y debe ser un valor entre 1 y 6, intente de nuevo: "))
            seleccionOpcion = int(input("Eliga 1 para Codificar o 2 para Decodificar: "))
            while seleccionOpcion not in (1,2):
                seleccionOpcion = int(input("La selección debe ser un número uno para codificar o un número dos para decodificar, intente de nuevo: "))

            if seleccionMetodo == 1:
                texto = str(input("Digite el texto que quiere cifrar: "))
                while f.validarTexto(texto) == False:
                    texto = str(input("El texto no es válido, debe contener únicamente letras y espacios. Intente de nuevo: "))
                desplazamiento = int(input("Digite el desplazamiento: "))
                if seleccionOpcion == 1:
                    textoCod = f.cesarCod(texto, desplazamiento)
                    print("El texto codificado con cifrado César es: " + textoCod)
                elif seleccionOpcion == 2:
                    textoDec = f.cesarDec(texto, desplazamiento)
                    print("El texto decodificado es: " + textoDec)

            elif seleccionMetodo == 2:
                texto = str(input("Digite el texto que quiere cifrar: "))
                while f.validarTexto(texto) == False:
                    texto = str(input("El texto no es válido, intente de nuevo: "))
                palabra = str(input("Digite la palabra clave: "))
                while f.validarPalabra(palabra) == False:
                    palabra = str(input("La palabra clave no es válida, intente de nuevo: "))
                if seleccionOpcion == 1:
                    textoCod = f.monoCod(texto, palabra)
                    print("El texto codificado con cifrado monoalfabético es: " + textoCod)
                elif seleccionOpcion == 2:
                    textoDec = f.monoDec(texto, palabra)
                    print("El texto decodificado es: " + textoDec)

            elif seleccionMetodo == 3:
                texto = str(input("Digite el texto que quiere cifrar: "))
                while f.validarTexto(texto) == False:
                    texto = str(input("El texto no es válido, intente de nuevo: "))
                palabra = str(input("Digite la palabra clave: "))
                while f.validarPalabra(palabra) == False:
                    palabra = str(input("La palabra clave no es válida, intente de nuevo: "))
                if seleccionOpcion == 1:
                    textoCod = f.vigenereCod(texto, palabra)
                    print("El texto codificado con cifrado Vigenère es: " + textoCod)
                elif seleccionOpcion == 2:
                    textoDec = f.vigenereDec(texto, palabra)
                    print("El texto decodificado es: " + textoDec)

            elif seleccionMetodo == 4:
                texto = str(input("Digite el texto que quiere cifrar: "))
                while f.validarTexto(texto) == False:
                    texto = str(input("El texto no es válido, intente de nuevo: "))
                palabra = str(input("Digite la palabra clave: "))
                while f.validarTexto(palabra) == False:
                    palabra = str(input("La palabra clave no es válida, intente de nuevo: "))
                if seleccionOpcion == 1:
                    textoCod = f.PlayFairCod(texto, palabra)
                    print("El texto codificado con cifrado PlayFair es: " + textoCod)
                elif seleccionOpcion == 2:
                    textoDec = f.PlayFairDec(texto, palabra)
                    print("El texto decodificado es: " + textoDec)

            elif seleccionMetodo == 5:
                texto = str(input("Digite el texto que quiere cifrar: "))
                if seleccionOpcion == 1:
                    textoCod = f.railfenceCod(texto)
                    print("El texto codificado con cifrado Rail Fence es: " + textoCod)
                elif seleccionOpcion == 2:
                    textoDec = f.railfenceDec(texto)
                    print("El texto decodificado es: " + textoDec)

            elif seleccionMetodo == 6:
                texto = str(input("Digite el texto que quiere cifrar: "))
                V = int(input("Digite la cantidad de letras por vuelta: "))
                while V < 1:
                    V = int(input("El número no es válido, intente de nuevo: "))
                if seleccionOpcion == 1:
                    textoCod = f.escitalaCod(texto, V)
                    print("El texto codificado con Escítala es: " + textoCod)
                elif seleccionOpcion == 2:
                    textoDec = f.escitalaDec(texto, V)
                    print("El texto decodificado es: " + textoDec)

            continuar = int(input("¿Desea seguir utilizando el programa? 1 = Continuar  2 = Terminar: "))
            
            while continuar > 2 or continuar < 1:
                continuar = int(input("La selección debe ser 1 para continuar o 2 para terminar, intente de nuevo: "))
        
        except Exception as e:
            print("Error:", e)
    print("Gracias por usar el programa, hasta luego!")



main()