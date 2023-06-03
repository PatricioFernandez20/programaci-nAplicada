
# Importar la libreria json para trabajar con archivos json, en este caso sensores.json 
import json

 
with open("sensores.json") as file: # Se abre el archivo sensores.json 
    # El contenido de sensores.json se almacenara en la variable información, json.load convierte un archivo json en un objeto de python
    informacion = json.load(file)
# En este paso se obtiene la lista de sensores, en la cual se encuentran todos los sensores en el archivo json
sensores = informacion["Sensores"]

# con print se imprime las opciones que tendrá el usuario a disposición a elegir.
print("Seleccione una opción:")
print("1.- Mostrar Temperatura máxima.:")
print("2.- Mostrar Temperatura mínima.:")

# Con input el usuario interactua, eligiendo asi alguna de las opciones que imprimen anteriormente. guardando la informacion en una variable 
respuestausuario = input()


# Al momento que el usuario opta por la opcion 1 se muestran la temperaturas maximas de las distintas localidades. 
if respuestausuario == "1":
    print("Temperaturas máximas:\n")
    # Con for leera y comparara los datos de todos los sensores, que se encuentran en el archivo sensores.json 
    for Hosts in sensores: 
        # Se extraen los valores de la clave equipo del archivo sensores.json, y lo guarda en la variable equipo
        equipo = Hosts["equipo"]
       
        # Se hace lo mismo que en el paso anterior, en el cual de el archivo sensores.json se extraen valores.
        Localidad = Hosts["sector"] 
      
       # Con max() se obtiene el dia con mayor temp y se almacena dentro de dia_max_temp
        dia_max_temp = max(Hosts["dias"], key=Hosts["dias"].get) 
        
        #Se obtiene los dias con mayor temperatura almacenandolo en temperatura_max
        temperatura_max = Hosts["dias"][dia_max_temp]  

        #se imprimen los valores, agregando °C para que los valores salgan en formato de temperatura
        print(f"{Localidad}: {dia_max_temp} {temperatura_max}°C")

# Si el usuario interactua con un numero 2 se imprimirá las temp minimas
elif respuestausuario == "2": 
    #Imprime lo mismo que sucede con las temperaturas maximas, pero aca en minimas. 
    print("Temperaturas mínimas:\n")
    for sensor in sensores:
        equipo = sensor["equipo"]
        localidad = sensor["sector"]
        dia_min_temp = min(sensor["dias"], key=sensor["dias"].get)
        temperatura_min = sensor["dias"][dia_min_temp]
        print(f"{localidad}: {dia_min_temp} {temperatura_min}°C")
else: # con else al no ingresar una opción valida imprimirá un mensaje de error
    print("Esta opción es invalida, ingrese una opción valida")
    cara_triste = '''
  .-""""""-.
.'          '.
|   o    o   |
|     ><     |
|  .- -- -.  |
'            '
  '-......-'
'''

    print(cara_triste)
