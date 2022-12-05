from random import choice
import os, time

lista_paises = ["Argentina", "Brasil", "Colombia", "Venezuela", 
            "Japon", "Puerto Rico", "Nueva Zelanda", "Estados Unidos"]

lista_huesos = ["Femur", "Meta carpo", "Radio", "Cubito", 
            "Meta tarso", "Astragalo", "Calcaneo", "Etmoides", "Esfenoides"]

diccionario_tematicas = {"paises": lista_paises, "huesos del cuerpo humano": lista_huesos}


#obtener una palabra al azar de la lista de paises
def obtener_palabra(lista):
    item = choice(lista)
    return item.upper()

#reemplazar letras por un caracter
def esconder_palabra(palabra):
    lista_secreta = []
    for i in palabra:
        if i != " ":
            lista_secreta.append("_")
        else:
            lista_secreta.append(" ")
    return lista_secreta


#funcion para limpiar (borrar-refrescar) pantalla
def limpiar_pantalla():
    #os.name - nos dice el sistema operativo
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#muestra las vidas y progreso de la palabra secreta
def estado_juego(vidas, letras_usuario, palabra_secreta):
    print("Intentos disponibles: ", vidas)
    if letras_usuario != "":
        print("Letras utilizadas: ", letras_usuario)

    secreto = " ".join(palabra_secreta)
    print(secreto)

def opcion_tematica():
    lista_elementos = []
    for clave in diccionario_tematicas.keys():
        lista_elementos.append(clave)
    while True:
        limpiar_pantalla()
        print("Elija entre las siguientes Tematicas:")
        for i in range(len(lista_elementos)):
            print(f"{i + 1} {lista_elementos[i]}")
        try:
            opcion = int(input(": "))
            if opcion > 0 and opcion <= len(lista_elementos):
                #return opcion - 1
                return diccionario_tematicas[lista_elementos[opcion - 1]]
            #diccionario_tematicas[lista_elementos[opcion - 1]]
            #print(diccionario_tematicas[lista_elementos[opcion - 1]])
            else:
                #print("Opcion no valida.")
                print("\033[;31m"+"Opcion NO valida"+"\033[;37m")
                time.sleep(1)
        except:
            #print("Opcion no valida.")
            print("\033[;31m"+"Solamente numeros"+"\033[;37m")
            time.sleep(1)



def iniciar_juego():
    vidas = 7
    juego_terminado = False
    letras_usuario = ""

    lista_opcion_usuario = opcion_tematica()

    palabra_original = obtener_palabra(lista_opcion_usuario)

    palabra_secreta = esconder_palabra(palabra_original)

    lista_palabra_original = list(palabra_original)

    #ciclo de juego
    while vidas >= 1 and not juego_terminado:
        limpiar_pantalla()

        estado_juego(vidas, letras_usuario, palabra_secreta)

        if lista_palabra_original == palabra_secreta:
            #print("Felicitaciones!! Adivinaste")
            juego_terminado = True
            continue

        #pedir letra al usuario
        letra_usuario = input("Ingrese letra o palabra: ").upper()

        if len(letra_usuario) > 1:
            print('cantidad letras ingresadas: ', len(letra_usuario))
            lista_letras_usuario = list(letra_usuario)
            print(lista_letras_usuario)
            if lista_letras_usuario == lista_palabra_original:
                palabra_secreta = lista_letras_usuario
                juego_terminado = True
            else:
                vidas -= 3
                if vidas <= 0:
                    vidas = 0
            continue
        

        #comparar letra  
        if letra_usuario in palabra_original:
            for i in range(len(lista_palabra_original)):
                if lista_palabra_original[i] == letra_usuario:
                    palabra_secreta[i] = letra_usuario
            
            
        else:
            if letra_usuario in letras_usuario:
                print("\033[;31m"+f"Ya se utilizo la letra {letra_usuario}"+"\033[;37m")
                #pausar por un momento
                time.sleep(1)
            else:
                
                letras_usuario += letra_usuario
                vidas -= 1

    #fin ciclo
    limpiar_pantalla()
    estado_juego(vidas, letras_usuario, palabra_secreta)
    if vidas <= 0:
        print(f"Perdiste, la palabra era {palabra_original}")
    elif juego_terminado:
        print("Felicitaciones! adivinaste")
        

    


eleccion = ""
while eleccion != "N":
    iniciar_juego()
    eleccion = input("""Presione enter para juegar de nuevo\npresione n/N para salir: """).upper()