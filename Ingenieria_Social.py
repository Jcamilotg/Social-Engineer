import itertools
import random

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Red="\033[1;31m"

print(" "+ Red + "______________________________________________________________________________")
print(" |  " +Blue  +"███─█──█─████─███─█──█─███─███─████─███─████────███─████─████─███─████─█──"+ Grey +"|")
print(" |  " +Blue  +"─█──██─█─█────█───██─█──█──█───█──█──█──█──█────█───█──█─█──█──█──█──█─█──"+ Grey +"|")
print(" |  " +Blue  +"─█──█─██─█─██─███─█─██──█──███─████──█──████────███─█──█─█─────█──████─█──"+ Grey +"|")
print(" |  " +Blue  +"─█──█──█─█──█─█───█──█──█──█───█─█───█──█──█──────█─█──█─█──█──█──█──█─█──"+ Grey +"|")
print(" |  " +Blue  +"███─█──█─████─███─█──█─███─███─█─█──███─█──█────███─████─████─███─█──█─███"+ Grey +"|")
print(" "+ Red + "______________________________________________________________________________")
print(" "+ Red + "")
print(" "+ Blue + "Este software creado con fines educativos y evaluar que tu contraseña sea segura")



print(Green + '''Debes tener información completa del Objetivo para esto, como:"
              
              [1]_[Nombres Completos, del objetivo, sea empresa u persona,  hijos o familiares cercanos]
              [2]_[Fechas de nacimiento o fechas importantes]
              [3]_[Nombres de mascotas, palabras claves o objetos de valor]
              [4]_[Numeros de Documento ID, o de suerte]''')

# Función para obtener datos del usuario
def obtener_datos():
    print("\n\nIntroduce los datos para generar la wordlist personalizada:\n\n")
    nombres = input("Nombre del objetivo, sea empresa o persona sus hijos o familia cercana (separados por comas) ejemplo: Juan,perez,restrepo,gomez,laura,pepa,ramirez: \n").split(",")
    fechas = input("Fechas importantes, cumpleaños (separadas por comas, ej. ,días,meses,años) ejemplo: 22,12,1985,17,01,1963: \n").split(",")
    palabras_clave = input("Palabras claves (mascotas, hobbies, etc., separadas por comas): ejemplo: firulais,blondi,roky: \n").split(",")
    num_id = input("Numeros de identificacion o de suerte (separadas por comas): ejemplo: 01234567,765432,123456,98765322: \n").split(",")

    # Limpiar espacios extra
    nombres = [n.strip() for n in nombres]
    fechas = [f.strip() for f in fechas]
    palabras_clave = [p.strip() for p in palabras_clave]
    num_id = [i.strip() for i in num_id]
    simbolos = ["@","#","*","!","|","&","/","=","?",".","%","+","","-","_","¡"]

    return nombres, fechas, palabras_clave, simbolos, num_id


# Generar combinaciones
def generar_combinaciones(datos, longitud_min=6, longitud_max=15):
    wordlist = set()
    for longitud in range(longitud_min, longitud_max + 1):
        for combinacion in itertools.permutations(datos, 4):
        #for combinacion in itertools.product(datos, repeat=longitud):
            posible = "".join(combinacion)
            if longitud_min <= len(posible) <= longitud_max:
                wordlist.add(posible)
    return wordlist

# Nueva función para obtener iniciales del nombre
def obtener_iniciales(nombre):
    return ''.join([parte[0].upper() for parte in nombre.split()])

# Nueva función para generar contraseñas con iniciales, ID y caracteres especiales
def generar_contraseñas_con_iniciales(nombres, ids, simbolos):
    wordlist = set()
    for nombre in nombres:
        iniciales = obtener_iniciales(nombre)
        for id_usuario in ids:
            for simbolo_inicio in simbolos:
                for simbolo_final in simbolos:
                    # Crear combinaciones con iniciales, ID y símbolos
                    contraseña = f"{id_usuario}{simbolo_inicio}{iniciales}{simbolo_final}"
                    wordlist.add(contraseña)
    return wordlist

# Función para generar contraseñas avanzadas con un formato específico
def generar_contraseña_formato_especifico(ids, nombres, simbolos):
    wordlist = set()
    for id_usuario in ids:
        for nombre in nombres:
            iniciales = obtener_iniciales(nombre)
            secuencia = nombre[1:3].lower()  # Ejemplo: tomar las dos primeras letras del apellido
            for _ in range(1500):
                simbolo_inicio = random.choice(simbolos)
                simbolo_final = random.choice(simbolos)
                # Formato: [ID][Símbolo][Iniciales][Secuencia][Símbolo]
                contraseña = f"{id_usuario}{simbolo_inicio}{iniciales}{secuencia}{simbolo_final}"
                wordlist.add(contraseña)
    return wordlist

# Función para obtener primera letra
# Función para obtener las iniciales de un nombre compuesto
def obtener_pri_iniciales(nombre):
    # Tomar la primera letra de cada parte del nombre y convertirla a mayúsculas
    pri_iniciales = ''.join([parte[0] for parte in nombre if parte])  # Filtrar partes vacías y tomar la inicial
    return pri_iniciales
def generar_contraseña_prim_ini(ids, nombres, simbolos):
    wordlist = set()
    for id_usuario in ids:
        for nombre in nombres:
            iniciales = obtener_pri_iniciales(nombres)
            secuencia = nombre[1:1].lower()  # Ejemplo: tomar las dos primeras letras del apellido
            for _ in range(1500):
                simbolo_inicio = random.choice(simbolos)
                simbolo_final = random.choice(simbolos)
                #simbolos_aleatorios = ''.join(random.choices(simbolos, k=4))  # Genera 4 símbolos aleatorios
                contraseña = f"{id_usuario}{simbolo_inicio}{iniciales}{secuencia}{simbolo_final}"
                #contraseña = f"{id_usuario}{simbolos_aleatorios}{iniciales}{secuencia}{simbolos_aleatorios}"
                wordlist.add(contraseña)
    return wordlist

def generar_contraseña_ini_princ(ids, nombres, simbolos):
    wordlist = set()
    for id_usuario in ids:
        for nombre in nombres:
            iniciales = obtener_pri_iniciales(nombres)
            secuencia = nombre[1:1].lower()  # Ejemplo: tomar las dos primeras letras del apellido
            for _ in range(1500):
                simbolo_inicio = random.choice(simbolos)
                simbolo_final = random.choice(simbolos)
                contraseña = f"{iniciales}{id_usuario}{simbolo_inicio}{secuencia}{simbolo_final}"
                wordlist.add(contraseña)
    return wordlist

def nombre_palabra_simbolo(palabras, nombres, simbolos):
    wordlist = set()
    for simbolo in simbolos:
        for nombre in nombres:
            for palabra in palabras:
                contraseña = f"{nombre}{palabra}{simbolo}"
                wordlist.add(contraseña)
    return wordlist
def guardar_listas(fechas, nombres, palabras_clave, num_id):
    # Usar un conjunto para evitar duplicados
    wordlist = set()
    iniciales = obtener_pri_iniciales(nombres)
    # Agregar datos individuales
    for nombre in nombres:
        wordlist.add(nombre)

    for fecha in fechas:
        wordlist.add(fecha)

    for palabra in palabras_clave:
        wordlist.add(palabra)

    for num in num_id:
        wordlist.add(num)

    # Generar combinaciones

    for nombre in nombres:
        for fecha in fechas:
            wordlist.add(f"{nombre}{fecha}")

        for palabra in palabras_clave:
            wordlist.add(f"{nombre}{palabra}")

        for num in num_id:
            wordlist.add(f"{nombre}{num}")

#com iniciales
        for fecha in fechas:
            wordlist.add(f"{iniciales}{fecha}")

        for fecha in fechas:
            wordlist.add(f"{fecha}{iniciales}")


        for palabra in palabras_clave:
            wordlist.add(f"{iniciales}{palabra}")

        for palabra in palabras_clave:
            wordlist.add(f"{palabra}{iniciales}")

        for num in num_id:
            wordlist.add(f"{iniciales}{num}")
        for num in num_id:
            wordlist.add(f"{num}{iniciales}")
##################################################################

    for palabra in palabras_clave:
        for fecha in fechas:
            wordlist.add(f"{palabra}{fecha}")

        for num in num_id:
            wordlist.add(f"{palabra}{num}")

    for fecha in fechas:
        for num in num_id:
            wordlist.add(f"{fecha}{num}")



    return wordlist

#dos primeras iniciales:
def generar_2prim_ini(ids, nombres, simbolos):
    wordlist = set()
    for id_usuario in ids:
        for nombre in nombres:
            iniciales = obtener_pri_iniciales(nombres)
            inicial1 = iniciales[0]
            inicial2 = iniciales[1]
            secuencia = nombre[1:1].lower()  # Ejemplo: tomar las dos primeras letras del apellido
            for _ in range(1500):
                simbolo_inicio = random.choice(simbolos)
                simbolo_final = random.choice(simbolos)
                contraseña = f"{inicial1}{inicial2}{id_usuario}{simbolo_inicio}{secuencia}{simbolo_final}"
                wordlist.add(contraseña)
    return wordlist

def generar_2prim_fin(ids, nombres, simbolos):
    wordlist = set()
    for id_usuario in ids:
        for nombre in nombres:
            iniciales = obtener_pri_iniciales(nombres)
            inicial1 = iniciales[0]
            inicial2 = iniciales[1]
            secuencia = nombre[1:1].lower()  # Ejemplo: tomar las dos primeras letras del apellido
            for _ in range(1500):
                simbolo_inicio = random.choice(simbolos)
                simbolo_final = random.choice(simbolos)
                contraseña = f"{id_usuario}{simbolo_inicio}{secuencia}{simbolo_final}{inicial1}{inicial2}"
                wordlist.add(contraseña)
    return wordlist


def nombre_simbolo_fecha(fechas, nombres, simbolos):
    wordlist = set()
    for simbolo in simbolos:
        for nombre in nombres:
            for _ in range(1500):  # Puedes ajustar el número de combinaciones
                simbolo_inicio = random.choice(simbolos)
                simbolo_intermedio = random.choice(simbolos)
                simbolo_final = random.choice(simbolos)

                # Seleccionar 3 elementos únicos de `fechas`
                fecha_comb = random.sample(fechas, 3)  # Selecciona 3 elementos diferentes

                contraseña = f"{nombre}{simbolo_inicio}{fecha_comb[0]}{simbolo_intermedio}{fecha_comb[1]}{simbolo_final}{fecha_comb[2]}"
                wordlist.add(contraseña)
    return wordlist
# Nueva función para generar números aleatorios de 4 dígitos basados en fechas

# Programa principal
def main():
    nombres, fechas, palabras_clave, simbolos, num_id = obtener_datos()
    datos = nombres + fechas + palabras_clave + simbolos + num_id

#LLamando las funciones
    combinaciones = generar_combinaciones(datos)
    contraseñas_iniciales = generar_contraseñas_con_iniciales(nombres, num_id, simbolos)
    contraseñas_formato = generar_contraseña_formato_especifico(num_id, nombres, simbolos)
    contraseñas_pri_ini = generar_contraseña_prim_ini(num_id, nombres, simbolos)
    contraseñas_ini_primero = generar_contraseña_ini_princ(num_id, nombres, simbolos)
    contraseñas_listas = guardar_listas(fechas, nombres, palabras_clave, num_id)
    contraseña_nompalsim = nombre_palabra_simbolo(palabras_clave, nombres, simbolos)
    contraseña_2primini = generar_2prim_ini(num_id, nombres, simbolos)
    contraseña_2prifin = generar_2prim_fin(num_id, nombres, simbolos)
    contraseña_nomsimfech = nombre_simbolo_fecha(fechas, nombres, simbolos)

    # Unir ambas listas de contraseñas
    wordlist = combinaciones.union(
    contraseñas_iniciales,
        contraseñas_formato,
        contraseñas_pri_ini,
        contraseñas_ini_primero,
        contraseñas_listas,
        contraseña_nompalsim,
        contraseña_2primini,
        contraseña_2prifin,
        contraseña_nomsimfech
                                   )


    # Guardar en archivo
    with open(f"{nombres}wordlist.txt", "w") as archivo:
        for palabra in sorted(wordlist):
            archivo.write(palabra + "\n")

        # Mostrar el total de contraseñas generadas
    #total_combinaciones = len(combinaciones)
    #total_iniciales = len(contraseñas_iniciales)
    #total_formato = len(contraseñas_formato)
    #total_pri_ini = len(contraseñas_pri_ini)
    #total_ini_primero = len(contraseñas_ini_primero)
    #total_con_listas = len(contraseñas_listas)
    #total_nompalsim = len(contraseña_nompalsim)
    total_wordlist = len(wordlist)


    print(f"\nGenerando combinaciones de contraseñas...\n")
    print(" "+ Blue +f"Total de contraseñas: {total_wordlist}.")
    print(" "+ Red +f"Guardada como {nombres}'wordlist.txt'. Puedes usarla como herramientas de auditoría.")

if __name__ == "__main__":
    main()
