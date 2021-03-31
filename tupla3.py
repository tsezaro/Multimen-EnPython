""" Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: 
(nombre, dni, destino). Ejemplo:
[("Manuel Juarez", 19823451, "Liverpool"), 
 ("Silvana Paredes", 22709128, "Buenos Aires"),
("Rosa Ortiz", 15123978, "Glasgow"), 
 ("Luciana Hernandez", 38981374, "Lisboa")
] 
Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: 
[("Buenos Aires", "Argentina"), 
("Glasgow", "Escocia"), 
("Lisboa", "Portugal"), 
("Londres", "Inglaterra"), 
("Madrid", "España")
] 
Hacer un programa que permita al usuario realizar las siguientes operaciones:
-Agregar pasajeros a la lista de viajeros.
-Agregar ciudades a la lista de ciudades.
-Dado el DNI de un pasajero, emitir a qué ciudad y país viaja.
-Dado un país, mostrar cuántos pasajeros viajan a ese país.
-Salir del programa.
"""

pasajeros = [("Manuel Juarez", 3, "Londres"),
 ("Silvana Paredes", 22709128, "Buenos Aires"),
("Rosa Ortiz", 15123978, "Glasgow"),
 ("Luciana Hernandez", 38981374, "Lisboa")
] 

destinos = [("Buenos Aires", "Argentina"),
("Glasgow", "Escocia"),
("Lisboa", "Portugal"),
("Londres", "Inglaterra"),
("Madrid", "España")
] 
#-------------------------------------------------------------------
continuar = True

while continuar:


    print("\n\t\tINGRESE LA OPCION DESEADA\n")
    print("\tIngrese 1) si desea cargar un nuevo pasajero.")
    print("\tIngrese 2) si desea cargar una nueva ciudad de destino.")
    print("\tIngrese 3) si desea buscar un destino por dni de pasajero.")
    print("\tIngrese 4) si desea saber cuantos pasajeros viajan a un destino.")
    print("\tIngrese 5) Si desea ver los pasajeros y destinos.")
    print("\tIngrese 0) si desea salir del programa.")

    try:
      op = int(input(""))
    except ValueError:
      print("Error, la opcion tiene que ser numerica.")
      continue

    if op == 1:
          nombre = input("ingrese el nombre del pasajero a agregar: ")
          dni = int(input("ingrese el dni del pasajero: "))
          destino_pasajero = input("ingrese la cuidad de destino del pasajero: ")
          tuplaPasajeros = (nombre,dni,destino_pasajero)
          pasajeros.append(tuplaPasajeros)
    elif op == 2:
          ciudad = input("ingrese una ciudad: ")
          pais = input("ingrese el pais: ")
          tuplaDestino = (ciudad, pais)
          destinos.append(tuplaDestino)  
    elif op == 3:
          dni_a_buscar = int(input("ingrese un dni a busacar: "))
          existe_dni = False
          for pasajero in pasajeros:
                if dni_a_buscar == pasajero[1]:
                    print("el pasajero con dni",dni_a_buscar, " tiene destino de su pasajero es: " , pasajero[2])
                    existe_dni = True
                    ciudadABuscar = pasajero[2]
                    for destino in destinos:
                          if ciudadABuscar == destino[0]:
                                print("la ciudad " , ciudadABuscar ," queda en el pais ", destino[1])
                             
          if not existe_dni:
            print("no hubo match con el dni encontrado.")      
    elif op == 4:
          destino_a_buscar = input("ingrese el destino a buscar: ")
          contador_pasajeros = 0
          bandero_destino = False
          for pasajero in pasajeros:
                if pasajero[2] == destino_a_buscar:
                      contadorPasajeros += 1
                      bandera_destino = True

          if bandera_destino:
            print("la cantidad de pasajeros a viajar a su destino es: " , contadorPasajeros)
          else:
            print("no hubo coincidencia con su destino a buscar")  
    elif op == 5:
        print("\n\n")
        print(pasajeros)
        print("\n\n")
        print(destinos)
        print("\n\n")
    elif op == 0:
          print("Gracias por usar nuestro programa !")
          continuar = False
          
    else:
          print("opcion incorrecta, porfavor vuelva a ingresarla")