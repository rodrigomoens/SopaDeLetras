import random
import string
def menúInicio():
    """Imprime la bienvenida al juego, solicita el nombre de usuario y lo retorna"""
    cadena = "Bienvenido a la Sopa De Letras del Mundial de Qatar 2022"
    cadena = f"{cadena:^150}"  # la cadena se centra en 150 espacios
    print("\n")
    print("="*150)  # el = se imprime 150 veces
    print(cadena)
    print("="*150)  # el = se imprime 150 veces
    print("\n")
    usuarios = []
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    print("Desea confirmar que", nombre_usuario, "sea su nombre usuario?")
    confirmar = input("Escriba Si / No: ")
    # si al confirmar, el usuario ingresa cualquier cosa que no sea si o no, le solicita nuevamente el nombre de usuario
    while confirmar.lower() != "si":
        if confirmar.lower() != "no":
            print("ERROR AL CONFIRMAR EL NOMBRE DE USUARIO")
            nombre_usuario = input("Reingrese su nombre de usuario: ")
            print("Desea confirmar que", nombre_usuario, "sea su nombre de usuario?")
            confirmar = input("Escriba Si / No: ")
        else:
            nombre_usuario = input("Reingrese su nombre de usuario: ")
            print("Desea confirmar que", nombre_usuario, "sea su nombre de usuario?:")
            confirmar = input("Escriba Si / No: ")
    print("CONFIRMADO, será direccionado al MENÚ PRINCIPAL")
    usuarios.append(nombre_usuario)
    return nombre_usuario

def menuPrincipal(nombre_usuario):
    """Imprime el menú principal, solicita el menú deseado y lo retorna."""
    cadena1 = str(nombre_usuario)+", estás en el MENÚ PRINCIPAL"
    cadena2 = cadena1.center(50, "-")# la cadena se centra en 50 espacios
    print("\n\n")
    detalle = "-" * 50
    print(detalle)  # el - se imprime 50 veces
    print(cadena2)
    print("1) JUGAR")
    print("2) INSTRUCCIONES")
    print("3) HISTORIAL DE PARTIDAS")
    print("4) CRÉDITOS")
    print("5) SALIR")
    print(detalle)  # el - se imprime 50 veces
    menu_seleccionado = input("Ingresá el numero correspondiente para cada acción que desee: ")
    # VUELVE A PEDIR LOS DATOS POR SI LO INGRESADO NO ES DIGITO O ESTA FUERA DE RANGO
    # si el usuario ingresa cualquier cosa que no sea un numero y que ese numero no sea entre 1 y 4, le solicita nuevamente el ingreso de un numero. el isdigit() funciona porque el numero ingresado sigue siendo un STRING
    while menu_seleccionado.isdigit() == False or int(menu_seleccionado) < 1 or int(menu_seleccionado) > 5:
        menu_seleccionado = input("ERROR. Reingresá el numero correspondiente para cada acción que desee: ")
    menu_seleccionado = int(menu_seleccionado)  # de string pasa a int
    return menu_seleccionado

def menuJugar(nombre_usuario):
    """Imprime el menú jugar, solicita una dificultad o volver al menu principal y devuelve el orden de la matriz y la dificultad elegida por el usuario"""
    ordenDeMatriz = 0
    cadena1 = str(nombre_usuario)+", estás en el MENÚ JUGAR"
    cadena2 = cadena1.center(50, "-")
    print("\n\n")
    detalle = "-" * 50
    print(detalle)
    print(cadena2)
    print(" 1) FÁCIL")
    print(" 2) INTERMEDIO")
    print(" 3) DIFICIL")
    print(" 4) Volver al MENÚ PRINCIPAL")
    print("-"*50)
    dificultad = input("Seleccione la dificultad en la que desea jugar o si desea volver al menu principal: ")
    # si el usuario ingresa cualquier cosa que no sea un numero y que ese numero no sea entre 1 y 4, le solicita nuevamente el ingreso de un numero. el isdigit() funciona porque el numero ingresado sigue siendo un STRING
    while dificultad.isdigit() == False or int(dificultad) < 1 or int(dificultad) > 4:
        dificultad = input("ERROR. Reingresá el numero correspondiente para cada acción que desee: ")
    dificultad = int(dificultad)
    # Segun la dificultad elegida la matriz va a ser de un orden u otro.
    if dificultad == 1:
        ordenDeMatriz = 20
    elif dificultad == 2:
        ordenDeMatriz = 25
    elif dificultad == 3:
        ordenDeMatriz = 30
    else:
        ordenDeMatriz = 0
    return dificultad, ordenDeMatriz

def obtenciondepaises():
    paises = []
    pais = ""
    try:
        archivo = open("paises.txt", "rt")
    except IOError:
        print("Error, no se pudo abrir el archivo")
    else:
        try:
            linea = archivo.readline()
            while linea:
                lista = linea.split(" ")
                """print(lista)"""
                for i in range(len(lista)):
                    pais = pais + lista[i]
                pais = pais.upper()
                if "\n" in pais:
                    pais = pais[:len(pais) - 1]
                paises.append(pais)
                pais = ""
                linea = archivo.readline()
        finally:
            archivo.close()
    """print(paises)"""
    return paises

"""def seleccionarPalabras():
    Selecciona 8 palabras al azar sin que se repitan y las retorna en un conjunto
    archivoPaises = open("paises.txt", "rt")
    listaPalabras = archivoPaises.readline()  # LEO UNA LINEA
    palabrasAInsertar = set()
    while listaPalabras:  # Mientras que linea contenga un valor, se imprime el archivo linea a linea
        listaPalabras = listaPalabras.split(" ")
        while len(palabrasAInsertar) < 8:
            palabra = random.choice(listaPalabras)
            # Agrega la palabra elegida al conjunto palabrasAInsertar
            palabrasAInsertar.add(palabra)
        listaPalabras = archivoPaises.readline()    
    palabrasAInsertar = list(palabrasAInsertar)
    print(palabrasAInsertar)
    archivoPaises.close()
    
        
      # ES UN CONJUNTO
    cantPalabrasAInsertar = 8
    # LAS PALABRAS SON ELEGIDAS DE LA LISTA ListaPalabras ALEATORIAMENTE  Y NO SE REPITEN GRACIAS  A QUE LAS PALABRAS INSERTADAS SE GUARDAN EN UN CONJUNTO (EL CONJUNTO NO GUARDA ELEMENTOS DUPLICADOS)
    # while len(palabrasAInsertar) < cantPalabrasAInsertar:
    #     palabra = random.choice(listaPalabras)
    #     # Agrega la palabra elegida al conjunto palabrasAInsertar
    #     palabrasAInsertar.add(palabra
    #Luego lo pasamos a lista
    return palabrasAInsertar"""

def creaciondesopa(sopa, filas = 30, columnas = 30):
    """Crea la sopa"""
    for f in range(filas):
        sopa.append([])
        for c in range(columnas):
            if f == 0:
                sopa[f].append(c)
            elif c == 0:
                sopa[f].append(f)
            else:
                sopa[f].append("-")

def impresiondesopa(sopa):
    """Imprime la sopa"""
    filas = len(sopa)
    columnas = len(sopa[0])
    for f in range(filas):
        for c in range(columnas):
            if f == 0 :
                if c < 9:
                    print(sopa[f][c], end="  ")
                else:
                    print(sopa[f][c], end=" ")
            elif c == 0:
                if f < 10:
                    print(sopa[f][c], end="  ")
                else:
                    print(sopa[f][c], end=" ")
            else:
                print(sopa[f][c], end= "  ")
        print()
    print()

def paiselegido(paises):
    """Selecciona un pais de la lista"""
    minimo = 0
    maximo = len(paises) - 1
    """print("Intenta pasar una novena vez")"""
    posicion = random.randint(minimo, maximo)
    pais = paises[posicion]
    paises.pop(posicion)
    return pais

def filaaleatoria1(sopa):
    """Devuelve una fila aleatoria"""
    minimo = 1
    maximo = len(sopa) - 1
    fila = random.randint(minimo, maximo)
    return fila

def espacios1(sopa, fila, pais):
    """Devuelve los espacios disponibles que hay en la fila seleccionada y en el que pueda
       entrar el pais seleccionado"""
    largo = 0
    inicial = 0
    final = 0
    nuevo = True
    disponibles = ()
    columnas = len(sopa[fila])
    for c in range(columnas):
        if nuevo == True:
            if sopa[fila][c] == "-":
                inicial = c
                largo = largo + 1
                nuevo = False
        else:
            if sopa[fila][c] == "-":
                largo = largo + 1
                if c == columnas - 1 and largo >= len(pais):
                    final = c
                    disponible = (largo, inicial, final)
                    disponibles = disponibles + (disponible,)
            else:
                if largo >= len(pais):
                    final = c - 1
                    disponible = (largo, inicial, final)
                    disponibles = disponibles + (disponible,)
                largo = 0
                inicial = 0
                final = 0
                nuevo = True
    """print(disponibles)"""
    return disponibles

def espacioelegido(disponibles):
    """Elige al azar uno de los espacios disponibles"""
    minimo = 0
    maximo = len(disponibles) - 1
    elegido = random.randint(minimo, maximo)
    espacio = disponibles[elegido]
    return espacio

def columnaaleatoria1(espacio, pais):
    """Elige una posicion entre todas las disponibles para colocar el pais en la sopa"""
    minimo = espacio[1]
    columnalimite = espacio[2] - len(pais) + 1
    columna = random.randint(minimo, columnalimite)
    return columna

def ubicaciondepalabra1(sopa, pais, fila, columna):
    """Ubica la palabra en la lista"""
    posicion = columna
    for i in range(len(pais)):
        sopa[fila][posicion] = pais[i]
        posicion = posicion + 1

def procedimiento1(sopa, paises, diccionario):
    """Ubica al pais en caso de que la fila no sea vacia"""
    fila = filaaleatoria1(sopa)
    pais = paiselegido(paises)
    disponibles = espacios1(sopa, fila, pais)
    while len(disponibles) == 0:
        fila = filaaleatoria1(sopa)
        disponibles = espacios1(sopa, fila, pais)
    espacio = espacioelegido(disponibles)
    columna = columnaaleatoria1(espacio, pais)
    ultimacolumna = columna + len(pais) - 1
    diccionario[pais] = [fila, fila, columna, ultimacolumna]
    ubicaciondepalabra1(sopa, pais, fila, columna)

def columnaaleatoria2(sopa):
    """Devuelve una fila aleatoria"""
    minimo = 1
    maximo = len(sopa) - 1
    columna = random.randint(minimo, maximo)
    return columna

def espacios2(sopa, columna, pais):
    """Devuelve los espacios disponibles que hay en la fila seleccionada y en el que pueda
       entrar el pais seleccionado"""
    largo = 0
    inicial = 0
    final = 0
    nuevo = True
    disponibles = ()
    filas = len(sopa)
    for f in range(filas):
        if nuevo == True:
            if sopa[f][columna] == "-":
                inicial = f
                largo = largo + 1
                nuevo = False
        else:
            if sopa[f][columna] == "-":
                largo = largo + 1
                if f == filas - 1 and largo >= len(pais):
                    final = f
                    disponible = (largo, inicial, final)
                    disponibles = disponibles + (disponible,)
            else:
                if largo >= len(pais):
                    final = f - 1
                    disponible = (largo, inicial, final)
                    disponibles = disponibles + (disponible,)
                largo = 0
                inicial = 0
                final = 0
                nuevo = True
    """print(disponibles)"""
    return disponibles

def filaaleatoria2(espacio, pais):
    """Elige una posicion entre todas las disponibles para colocar el pais en la sopa"""
    minimo = espacio[1]
    filalimite = espacio[2] - len(pais) + 1
    fila = random.randint(minimo, filalimite)
    return fila

def ubicaciondepalabra2(sopa, pais, columna, fila):
    """Ubica la palabra en la lista"""
    posicion = fila
    for i in range(len(pais)):
        sopa[posicion][columna] = pais[i]
        posicion = posicion + 1

def procedimiento2(sopa, paises, diccionario):
    """Ubica al pais en caso de que la fila no sea vacia"""
    columna = columnaaleatoria2(sopa)
    pais = paiselegido(paises)
    disponibles = espacios2(sopa, columna, pais)
    while len(disponibles) == 0:
        columna = columnaaleatoria2(sopa)
        disponibles = espacios2(sopa, columna, pais)
    espacio = espacioelegido(disponibles)
    """if espacio[0] == len(pais):
        columna = espacio[1]
    else:
        columna = columnaaleatoria2(espacio, pais)"""
    fila = filaaleatoria2(espacio, pais)
    ultimafila = fila + len(pais) - 1
    diccionario[pais] = [fila, ultimafila, columna, columna]
    ubicaciondepalabra2(sopa, pais, columna, fila)
    
def rellenodesopa(sopa):
    """Esta funcion no es muy recomendada pero la use para probar el juego"""
    filas = len(sopa)
    columnas = len(sopa[0])
    for f in range(filas):
        for c in range(columnas):
            if sopa[f][c] == "-":
                sopa[f][c] = string.ascii_uppercase[random.randint(0,24)]

def procedimiento(sopa, paises, diccionario):
    contador = 4
    while contador != 0:
        procedimiento1(sopa, paises, diccionario)
        procedimiento2(sopa, paises, diccionario)
        contador = contador - 1

def informaciondeprogreso(progreso, paisesencontrados, paises):
    paisesHalladosCadena = ""
    print(paisesHalladosCadena)
    print(paisesencontrados)
    for pais in paisesencontrados:  # TRANSFORMO LA LISTA EN UNA CADENA ASI SE IMPRIME MEJOR A LA VISTA
        paisesHalladosCadena = paisesHalladosCadena + pais + ", "
    print(progreso)
    progresoPorcentual = (progreso * 100) // len(paises)
    print("Tu progreso es", progresoPorcentual, "%")
    primeraparte = "Las palabras encontradas son: "
    oracion = primeraparte + paisesHalladosCadena
    print(oracion)

def chequearEstadoDePartida(progreso, paisesencontrados, finalizarPartida, paises, totalpaises = 20):
    """Verifica si la partida continúa o finaliza según el usuario encuentre todas las palabras o decida abandonar la partida. Rertona el estado de la partida y, en caso de que haya finalizado, el diccionario resumen."""
    estadoDeLaPartida = ""
    palabrasHalladasCadena = ""
    if progreso == totalpaises:
        finalizarPartida = True
        print("\n-----------------------------------\n"
              "¡HAS ENCONTRADO TODAS LAS PALABRAS!\n"
              "-----------------------------------\n")
    # CHEQUEA SI SE ESCRIBE CORRECTAMENTE EL SI O EL NO
    else:  # entra aca si la partida no finalizo
        # solicito al usuario si desea continuar jugando o quiere finalizar la partida
        while estadoDeLaPartida.lower() != "no" and estadoDeLaPartida.lower() != "si":
            estadoDeLaPartida = input("Continuar partida? Si / No: ")
        if estadoDeLaPartida.lower() == "no":
            finalizarPartida = True
    if finalizarPartida == True:  # CONDICION SI EL USUARIO NO QUISO CONTINUAR LA PARTIDA o YA GANO, MUESTRA EL RESUMEN
        print("\n\n---> Partida finalizada <---")
        print("\n\n--------------------------------------------------------------------------------------------------------------------------------------")
        print("---> RESUMEN <---")
        informaciondeprogreso(progreso, paisesencontrados, paises)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
    return finalizarPartida

def revisiondeespacios(pais):
    sinespacios = ""
    auxiliar = pais.split(" ")
    for i in auxiliar:
        sinespacios = sinespacios + i
    return sinespacios

def hallarPalabras(sopa, paises, progreso, paisesencontrados, diccionario):
    """Realiza la búsqueda de palabras en la sopa de letras dependiendo de los datos ingresados por el jugador. Retorna el progreso de la partida y las palabras halladas hasta el momento"""
    palabraHallada = ""
    confirmar = ""
    while confirmar.lower() != "si":  # hasta que el usuario confirme el ingreso de datos de fila y columna no se sale de este bucle
        confirmar = ""
        # Verifico que el usuario, al tratar de hallar las palabras, ingrese sólo numeros y no letras. Ademas que no ingrese la fila 0 y columna 0 porque estan reservadas para la guia
        comienzoFila = input("Fila en donde empieza la palabra? ")
        while comienzoFila.isdigit() == False or int(comienzoFila) < 0:
            print("ERROR. REINGRESE NUEVAMENTE")
            # se deja que sea de tipo string para verificar que ingrese solo numeros
            comienzoFila = input("Fila en donde empieza la palabra? ")
        # Lo paso a entero para poder usarlo en la ubicacion de la palabra
        comienzoFila = int(comienzoFila)
        comienzoColumna = input("Columna en donde empieza la palabra? ")
        while comienzoColumna.isdigit() == False or int(comienzoColumna) < 0:
            print("ERROR. REINGRESE NUEVAMENTE")
            comienzoColumna = input("Columna en donde empieza la palabra? ")
        comienzoColumna = int(comienzoColumna)
        finalFila = input("Fila en donde termina la palabra? ")
        while finalFila.isdigit() == False or int(finalFila) < 0:
            print("ERROR. REINGRESE NUEVAMENTE")
            finalFila = input("Fila en donde termina la palabra? ")
        finalFila = int(finalFila)
        finalColumna = input("Columna en donde termina la palabra? ")
        while finalColumna.isdigit() == False or int(finalColumna) == 0:
            print("ERROR. REINGRESE NUEVAMENTE")
            finalColumna = input("Columna en donde termina la palabra? ")
        finalColumna = int(finalColumna)
        pais = input("Pais al cual se refiere?: ")
        if " " in pais:
            pais = revisiondeespacios(pais)
        pais = pais.upper()
        while pais.isalpha() == False:
            pais = input("Ese pais no existe, por favor ingrese uno existente: ")
            if " " in pais:
                pais = revisiondeespacios(pais)
            pais = pais.upper()
        print()
        # C
        print(pais, "comienza en", comienzoFila, comienzoColumna, "y termina en", finalFila, finalColumna)
        confirmar = input("CONFIRMAR? Si / No:")
        """confirmar = input(pais, "comienza en", comienzoFila, comienzoColumna, "y termina en", finalFila, finalColumna, "CONFIRMAR? Si / No:")"""
        while confirmar.lower() != "no" and confirmar.lower() != "si":
            print("Se recibio una respuesta no esperada")
            print(pais, "comienza en", comienzoFila, comienzoColumna, "y termina en", finalFila, finalColumna)
            confirmar = input("CONFIRMAR? Si / No:")               
    if pais.upper() in diccionario:
        if diccionario[pais.upper()] == [comienzoFila, finalFila, comienzoColumna, finalColumna]:
            if pais.upper() not in paisesencontrados:  # Si la palabra no se halló anteriormente entra a esta condicion
                print("CORRECTO, has encontrado a", pais)
                paisesencontrados.append(pais.upper())
                progreso += 1
            else:
                print("Ese pais ya fue encontrado anteriormente")
        else:
            print("La palabra no se hallo correctamente, por favor vuelva a intentarlo")
    else:
        print("La palabra no se hallo correctamente, por favor vuelva a intentarlo")
    return progreso

def menuInstrucciones(nombreDeUsuario):
    """Imprime las instrucciones del juego."""
    cadena = str(nombreDeUsuario)+", estás en el MENÚ INSTRUCCIONES"
    cadena = cadena.center(120, "-")
    print("\n\n")
    print("-"*120)
    print(cadena, "\n")
    # Gracias a la triple comilla simple, la variable instrucciones mantiene este formato al imprimirse
    intrucciones = '''Las instrucciones para jugar son las siguientes: 

    1) Debes ingresar la fila y la columna en donde se encuentra la LETRA que COMIENZA la palabra. 

    2) Cada vez que ingrese los datos anteriores, se le preguntará si confirma el ingreso

    3) Cada vez que realice una búsqueda de palabra, se le preguntará si desea continuar jugando

    4) Puede jugar hasta 3 modos de dificultad:
        a. Fácil: Están en vertical y horizontal. La sopa de letras es de 20x20.
        b. Intermedio: Están en vertical y horizontal. La sopa de letras es de 25x25
        c. Difícil: La sopa de letras es de 25x25.

    5) En el menú HISTORIAL, encontrará todos los datos relevantes de las partidas que se jugaron anteriormente en toda 
       la historia de la sopa de letras.
    
    6) Última instrucción, diviértase!'''
    print(intrucciones)
    cadena = "---> Será direccionado al MENÚ PRINCIPAL <---"
    cadena = f"{cadena:^119}"
    print("-"*120)
    print(cadena)

def menuCreditos(nombreDeUsuario):
    """Imprime el menú creditos"""
    cadena = str(nombreDeUsuario)+", estás en el MENÚ CRÉDITOS"
    cadena = f"{cadena:^50}"
    print("\n\n")
    print("-"*50)
    print(cadena, "\n")
    diccionarioCreditos = {
        "GRUPO:": "5",
        "1157720": "Pistolesi, Lucas ",
        "1141870": "Huentelaf, Mauricio",
        "1160200": "Petruchi, Gian",
        "1158518": "Moens, Rodrigo",
        "1135716": "Del Piano, Bautista "
    }
    for palabra in diccionarioCreditos:
        # IMPRIME EL DICCIONARIO, primero la clave, luego el valor
        print(palabra, diccionarioCreditos[palabra])
    print("-"*50)
    cadena = "---> Será direccionado al MENÚ PRINCIPAL <---"
    cadena = f"{cadena:^50}"
    print(cadena)

def informedecierre():
    cadena = "El juego de la SOPA DE LETRAS se ha cerrado exitosamente"
    cadena = f"{cadena:^150}"
    print("\n")
    print("="*150)
    print(cadena)
    print("="*150)
    print("\n")

def main():
    diccionario = {}
    sopa = []
    paisesencontrados = []
    progreso = 0
    finalizarPartida = False
    nombre_usuario = menúInicio()
    menu_seleccionado = menuPrincipal(nombre_usuario)
    while 1:
        if menu_seleccionado == 1:
            dificultad, ordenDeMatriz = menuJugar(nombre_usuario)
            if dificultad < 4:
                creaciondesopa(sopa, ordenDeMatriz, ordenDeMatriz)
                paises = obtenciondepaises()
                """print(paises)"""
                procedimiento(sopa, paises, diccionario)
                rellenodesopa(sopa)
                while finalizarPartida == False:
                    impresiondesopa(sopa)
                    progreso = hallarPalabras(sopa, paises, progreso, paisesencontrados, diccionario)
                    informaciondeprogreso(progreso, paisesencontrados, paises)
                    finalizarPartida = chequearEstadoDePartida(progreso, paisesencontrados, finalizarPartida, paises)
            elif menuseleccionado == 2:
                menuInstrucciones(nombre_usuario)
            elif menuPrincipalSeleccionado == 4:
                menuCreditos(nombre_usuario)
            elif menuPrincipalSeleccionado == 5:
                break


    
main()
"""Les comento los cambios que hice:
   Modularice el programa principal y puse todo adentro de un main
   Cambie todo el algoritmo con respecto a la creacion de la sopa, seleccion de palabras y ubicacion de las palabras en la sopa
   Cambie algunas logicas en la interaccion con el usuario debido a que en algunos casos no devolvia lo que tenia que devolver
   Cambie la forma en que se revisa si los datos que envio el usuario estan bien, repetidos o mal
   Lo demas esta tal como lo hicieron ustedes"""
