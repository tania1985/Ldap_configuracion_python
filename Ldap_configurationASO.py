#!/urs/bin/env python3
import os.path
import os
import re
"""
La biblioteca re (Regular Expressions): Esta biblioteca proporciona funciones de expresiones regulares.
Se utiliza para buscar patrones específicos dentro de los archivos, como encontrar texto dentro de los
corchetes.
"""


# Usaremos está función para pedir variables al usuario
def pedirValor(mensaje):
    valor = input(mensaje)
    return valor

# Usaremos está función para crear los ficheros que usaremos para la configuración de Ldap
"""
os.path.isfile: Se utiliza para verificar si una ruta especificada apunta a un archivo existe
"""
def creacionficheros():
    if os.path.isfile('crear_ou.ldif') is False:
        creacion_fichero = ('touch crear_ou.ldif')
        os.system(creacion_fichero)

    if os.path.isfile('crear_grupos.ldif') is False:
        creacion_fichero = ('touch crear_grupos.ldif')
        os.system(creacion_fichero)

    if os.path.isfile('crear_usuarios.ldif') is False:
        creacion_fichero = ('touch crear_usuarios.ldif')
        os.system(creacion_fichero)

    if os.path.isfile('gid.txt') is False:
        creacion_fichero = ('touch gid.txt')
        os.system(creacion_fichero)

    if os.path.isfile('Nombres_ou.txt') is False:
        creacion_fichero = ('touch Nombres_ou.txt')
        os.system(creacion_fichero)

    if os.path.isfile('Nombres_grupos.txt') is False:
        creacion_fichero = ('touch Nombres_grupos.txt')
        os.system(creacion_fichero)

    if os.path.isfile('Nombres_usuarios.txt') is False:
        creacion_fichero = ('touch Nombres_usuarios.txt')
        os.system(creacion_fichero)

    if os.path.isfile('grupos_ou.txt') is False:
        creacion_fichero = ('touch grupos_ou.txt')
        os.system(creacion_fichero)

    if os.path.isfile('OU_grupo.txt') is False:
        creacion_fichero = ('touch OU_grupo.txt')
        os.system(creacion_fichero)

#Usaremos está función para encontrar determinadas palabras dentro de los archivos que voy a crear
"""
En esta función buscará palabras que encuentren entre dos puntos en un string, lo usaré para enconntrar
palabras en distintos ficheros. En caso de encontrar devolverá True en caso contrario False.
"""
def encontrar_basico(texto, palabra):

    busqueda = "." + " " + palabra + " " + "."
    if busqueda in texto:
        return True
    else:
        return False

#Usaremos esta función para encontrar determinadas palabras dentro de los archivos
# que estén entre corchetes y si se encuentrá devuelve "True"
"""

"""
def encontrar_corchetes(texto, palabra):

    res = re.findall(r'\[.*?\]', texto)

    palabro = "[" + palabra + "]"

    if palabro in res:
        return True
    else:
        return False

#Usaremos esta función para encontrar frases que empiecen determinadas palabras dentro de los archivos
# y saque esas frases por pantalla
def encontrar_primera_print(texto, palabra):

    lineas_empiezan = []

    for linea in texto.split('\n'):
        if linea.startswith(palabra):
            lineas_empiezan.append(linea)

    for linea in lineas_empiezan:
        print(linea)

#Usaremos esta función para encontrar determinadasfrases que empiecen por
#Una palabra determinada y contengan otra palabra dentro de un archivo
# y si se cumplen dichas condiciones devuelve "True"
def encontrar_principio_existe(texto, palabra, palabra2):
    lineas = texto.split("\n")

    palabro = "(" + palabra2 + ")"

    for linea in lineas:
        if linea.startswith(palabra) and palabro in linea:
            return True
    return False

#Usaremos esta funcion para comprobar que no hay varaibles ni puntos dentro de una variables
#Ya que este codigo no lo permite
def comprueba_espacios_puntos(variable):
    if ' ' in variable or '.' in variable or '(' in variable or ')' in variable \
            or '[' in variable or ']' in variable:
        return True
    else:
        return False

#Usaremos esta función para crear un fichero que contendrá el nombre del dominio de nuestro servidor
def CrearDominio():
    prueba = os.path.isfile('dominio.txt')
    if prueba is False:
        dominio = (pedirValor("\033[95mCual es el nombre de tu dominio (ej. Tania.castelao):\033[0m\n"))
        lista = dominio.split(".")
        f = open("dominio.txt", "a")
        f.write(dominio)
        f.close()

#Usaremos esta función para crear un fichero que contendrá el nombre del administrador de nuestro servidor
def CrearAdmin():
    prueba = os.path.isfile('admin.txt')
    if prueba is False:
        administrador = (pedirValor("\033[95mCual es el nombre de tu administrador (ej. admin):\033[0m\n"))
        f = open("admin.txt", "a")
        f.write(administrador)
        f.close()

#Usaremos esta función para crear un fichero que contendrá la contraseña de nuestro servidor
def CrearContra():
    prueba = os.path.isfile('contra.txt')
    if prueba is False:
        contrasena = (pedirValor("\033[95mCual la contraseña de tu dominio (ej. Prueba-123):\033[0m\n"))
        f = open("contra.txt", "a")
        f.write(contrasena)
        f.close()

#Usaremos esta función para leer el fichero que contiene
#la lista con la OU creadas y sacar su contenido por pantalla
def listarou():
    print("\033[95mLista de Unidades organizativas:\033[0m")

    with open("Nombres_ou.txt") as file:
        lines = [line.rstrip() for line in file]

    count = 0

    for line in lines:
        count += 1
        print("{}{}".format(count, line.strip()))

#Usaremos esta función para leer el fichero que contiene
#la lista con los grupos creados y sacar su contenido por pantalla
def listagrupo():
    print("\n\033[95mLista de los grupos:\033[0m")

    with open("Nombres_grupos.txt") as file:
        lines = [line.rstrip() for line in file]

    count = 0

    for line in lines:
        count += 1
        print("{}{}".format(count, line.strip()))

#Usaremos esta función para leer el fichero que contiene
#la lista con los usuarios creados y sacar su contenido por pantalla
def listausuarios():
    print("\n\033[95mLista de los usuarios:\033[0m")

    with open("Nombres_usuarios.txt") as file:
        lines = [line.rstrip() for line in file]

    count = 0

    for line in lines:
        count += 1
        print("{}{}".format(count, line.strip()))

#Usaremos esta función para leer el fichero que contiene
#la lista con los usuarios creados y la unidad organizativa en que se encuentran
# y sacar su contenido por pantalla
def listargrupos_ou():
    print("\n\033[95mLista de unidades organizativas con grupos:\033[0m")

    with open("grupos_ou.txt") as file:
        lines = [line.rstrip() for line in file]

    count = 0

    for line in lines:
        count += 1
        print("{}{}".format(count, line.strip()))

#Usaremos esta función para crear el fichero .ldif que usaremos para crear las unidades organizativas
def CrearOu():

    unidad_o = (pedirValor("\n\033[95mQue nombre quieres darle a la unidad organizativa:\033[0m\n"))
    if comprueba_espacios_puntos(unidad_o):
        print("\033[31mLas unidades organizativas no pueden contener \033[0mespacios\033[31m, ni "
              "\033[0mpuntos\033[31m, ni \033[0mparentesis\033[31m "
              "si quieres separar palabras utiliza '_'\033[0m")
    else:
        #Comprobamos que el nombre del ou dado no existe en nuestro servidor
        with open('Nombres_ou.txt') as file:
            contents = file.read()

        if encontrar_basico(contents, unidad_o) is False:

            # Escribimos los datos dentro del fichero
            f = open("crear_ou.ldif", "a")
            f.write("dn: ou=" + str(unidad_o) + ",dc=" + str(lista[0]) + ",dc=" + str(lista[1]) + "\n"
                    "objectClass: organizationalunit\n"
                    "objectClass: top\n"
                    "ou:" + str(unidad_o) + "\n")
            f.close()

            #Guardamos el nombre del OU creado dentro de este fichero para hacer comprobaciones
            f = open("Nombres_ou.txt", "a")
            f.write("." + " " + str(unidad_o) + " " + "." + "\n")
            f.close()
        else:
            print("\n\033[31mYa hay una unidad organizativa con ese nombre, escoge otro nombre\033[0m")
            listarou()
            CrearOu()

        #El comando siguiente cargará la unidad organizativa en nuestro servidor
        cargaOU= ("ldapadd -f crear_ou.ldif -D cn=" + str(administrador) + ",dc=" + str(lista[0])
                  + ",dc=" + str(lista[1]) + " -w " + str(contrasena))
        os.system (cargaOU)

        #Al acabar borro los datos del fichero y lo dejo en blanco de nuevo
        with open('crear_ou.ldif', 'w') as fichero:
            fichero.write('')

#Usaremos esta función para crear el fichero .ldif que usaremos para crear los grupos
def Creargrupo():

    #Creo un bucle que no se rompa hasta que el usuario escriba el nombre de una OU existente
    loop= False
    while not loop:
        listarou()
        unidad_2 = (pedirValor("\n\033[95mEn que unidad organizativa quieres crearlo:\033[0m\n"))

        with open('Nombres_ou.txt') as file:
            contents = file.read()
            if encontrar_basico(contents, unidad_2) is True:
                loop= True
            else:
                print('\033[31mEsa unidad organizativa no existe\033[0m')

    #Creo un bucle que no se rompa hasta que el usuario escriba el nombre de un grupo que no exista
    loop2= False
    while not loop2:
        grupo = (pedirValor("\033[95mQue nombre quieres darle a tu grupo:\033[0m\n"))
        if comprueba_espacios_puntos(grupo):
            print("\033[31mLas unidades organizativas no pueden contener \033[0mespacios\033[31m, ni "
                  "\033[0mpuntos\033[31m, ni \033[0mparentesis\033[31m "
                  "si quieres separar palabras utiliza '_'\033[0m")
        else:
            with open('Nombres_grupos.txt') as file:
                contents = file.read()

            #Si el nombre de el grupo es encontrado comienza la configuración del fichero
            if encontrar_basico(contents, grupo) is False:

                # Empiezo dando 500 de numero 'gid' al primer usuario y
                # si ya existe un grupo con ese número le doy el 501 y así sucesivamente
                gid = 500
                loop3= False
                while not loop3:
                    with open('gid.txt') as file:
                        contents = file.read()
                    if encontrar_basico(contents, str(gid)) is True:
                        gid= gid + 1
                    else:
                        #Guardo los datos de los gid ya dados en un documento
                        f = open("gid.txt", "a")
                        f.write("." + " " + str(gid) + " " + "." "\n")
                        f.close()
                        loop3= True

                # Escribimos los datos dentro del fichero
                f = open("crear_grupos.ldif", "a")
                f.write("dn: cn="+ str(grupo) +",ou="+ str(unidad_2) +",dc="+ str(lista[0]) +",dc="+ str(lista[1]) +"\n"
                        "objectClass: top\n"
                        "objectClass: posixGroup\n"
                        "gidnumber:"+ str(gid) + "\n")
                f.close()

                # Guardamos el nombre del grupo creado dentro de este fichero para hacer comprobaciones
                f= open ("Nombres_grupos.txt", "a")
                f.write( "." + " " + str(grupo) + " " + "." "\n")
                f.close()

                # Guardamos el nombre del (grupo+OU) creado dentro de este fichero para hacer comprobaciones
                f = open("grupos_ou.txt", "a")
                f.write(". " + "Ou: [" + str(unidad_2) + "], Grupo: (" + str(grupo) + ")\n")
                f.close()

                # Guardamos el nombre del (Ou+grupo) creado dentro de este fichero para hacer comprobaciones
                f = open("OU_grupo.txt", "a")
                f.write(str(unidad_2) + ", Grupo: (" + str(grupo) + ")\n")
                f.close()

                loop2 = True

            else:
                print("\033[31mError Ya hay un grupo con ese nombre, escoge otro nombre\033[0m")
                listagrupo()
                print("-------------------------------------------------- ")

            #El comando siguiente cargará el grupo en nuestro servidor
            cargaGrupo= ("ldapadd -f crear_grupos.ldif -x -D cn=" + str(administrador) + ",dc=" + str(lista[0])
                      + ",dc=" + str(lista[1]) + " -w " + str(contrasena))
            os.system (cargaGrupo)

            #Al acabar borro los datos del fichero y lo dejo en blanco de nuevo
            with open('crear_grupos.ldif', 'w') as fichero:
                fichero.write('')

#Usaremos esta función para crear el fichero .ldif que usaremos para crear los usuarios
def CrearUsuarios():

    usuario = (pedirValor("\033[95mQue nombre quieres darle al usuario\033[0m\n"))

    if comprueba_espacios_puntos(usuario):
        print("\033[31mLas unidades organizativas no pueden contener \033[0mespacios\033[31m, ni "
              "\033[0mpuntos\033[31m, ni \033[0mparentesis\033[31m "
              "si quieres separar palabras utiliza '_'\033[0m")
    else:
        #Compruebo que el nombre de usuario dado no existe en nuestro servidor
        with open('Nombres_usuarios.txt') as file:
            contents = file.read()
        if encontrar_basico(contents, usuario) is False:
            apellido = (pedirValor("\033[95mCual es el apellido del usuario\033[0m\n"))
            display = (pedirValor("\033[95mElige un nombre de display\033[0m\n"))

            # Creo un bucle que no se rompa hasta que el usuario escriba el nombre de una OU existente
            loop = False
            while not loop:
                listargrupos_ou()
                unidad_3 = (pedirValor("\n\033[95mEn que unidad organizativa quieres crearlo:\033[0m\n"))

                with open('grupos_ou.txt') as file:
                    contents = file.read()

                if encontrar_corchetes(contents, unidad_3) is True:
                    loop = True

                else:
                    print('\033[31mEsa unidad organizativa no existe\033[0m')

            # Creo un bucle que no se rompa hasta que el usuario escriba
            # el nombre de un grupo que exista dentro de esa unidad
            loop4 = False
            while not loop4:
                with open('OU_grupo.txt') as file:
                    contents = file.read()

                encontrar_primera_print(contents, unidad_3)
                grupo_2 = (pedirValor("\n\033[95mEn que grupo quieres crearlo:\033[0m\n"))

                with open('OU_grupo.txt') as file:
                    contents = file.read()

                if encontrar_principio_existe(contents , unidad_3, grupo_2) is True:

                    # Escribimos los datos dentro del fichero
                    f = open("crear_usuarios.ldif", "a")
                    f.write("dn: uid=" + str(usuario) + ",cn=" + str(grupo_2) + ",ou="
                            + str(unidad_3) + ",dc=" + str(
                        lista[0]) + ",dc=" + str(lista[1]) + "\n"
                        "objectClass: inetOrgPerson\n"
                        "uid:" + str(usuario) + "\n"
                        "cn:" + str(grupo_2) + "\n"
                        "sn:" + str(apellido) + "\n"
                        "displayName:" + str(display) + "\n")
                    f.close()

                    # Guardamos el nombre del usuario creado dentro de este fichero para hacer comprobaciones
                    f = open("Nombres_usuarios.txt", "a")
                    f.write("." + " " + str(usuario) + " " + "." "\n")
                    f.close()
                    loop4 = True

                else:
                    print("\033[31mEse grupo no existe en la Unidad organizativa\033[0m")
        else:
            listausuarios()
            print("Ese usuario ya existe escoge otro")

        #El comando siguiente cargará el grupo en nuestro servidor
        cargaUsuario= ("ldapadd -f crear_usuarios.ldif -x -D cn=" + str(administrador) + ",dc=" + str(lista[0])
                  + ",dc=" + str(lista[1]) + " -w " + str(contrasena))
        os.system (cargaUsuario)

        #Al acabar borro los datos del fichero y lo dejo en blanco de nuevo
        with open('crear_usuarios.ldif', 'w') as fichero:
            fichero.write('')

#Creamos un bucle para el menu

isSalir = False
while not isSalir:

    #Creamos los ficheros en caso de que no existan
    creacionficheros()
    CrearDominio()
    CrearAdmin()
    CrearContra()

    #Sacamos los datos que necesitamos de los ficheros y los guardamos en variables
    with open('dominio.txt') as file:
        Domain = file.read()
    lista = Domain.split(".")

    with open('admin.txt') as file:
        administrador = file.read()

    with open('contra.txt') as file:
        contrasena = file.read()

    #Informamos al usuario de las opciones de uso
    Opciones = (pedirValor("------------------------------- "
                           "\n\033[36mQue quieres hacer:\n"
                           "1. Crear una unidad organizativa\n"
                           "2. Crear un grupo\n"
                           "3. Crear un usuario\n"
                           "4. Listar Unidades organizativas, Grupos y Usuarios\n"
                           "5. Cambiar Dominio, Administrador y Contraseña guardados\n"
                           "6. Salir\033[0m\n"))

    if (Opciones == "1"):

        CrearOu()

    elif (Opciones == "2"):

        #Comprobamos que hay OU creadas
        if (os.stat("Nombres_ou.txt").st_size == 0):
            print("\033[31mNo hay unidades organizativas creadas, crea una antes de crear un grupo\033[0m")
        else:
            Creargrupo()

    elif (Opciones == "3"):

        #Comprobamos que hay grupos creados
        if (os.stat("Nombres_grupos.txt").st_size == 0):
            print("\033[31mNo hay grupos creados, crea uno antes de crear un usuario\033[0m")
        else:
            CrearUsuarios()

    elif (Opciones == "4"):

        listarou()
        listagrupo()
        listausuarios()
        listargrupos_ou()

    elif (Opciones == "5"):

        from os import remove
        remove("dominio.txt")
        remove("admin.txt")
        remove("contra.txt")

    elif (Opciones == "6"):

        isSalir = True
        print("Saliendo ...")
