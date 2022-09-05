# para ejecutar: py nombre_de_archivo.py     -     python nombre_de_archivo.py

#Booleans
boolean = True #true or false   ( "nombre" = valor)

#Numerales
num = 10
fl = 10.34
#parseInt() el texto lo convertia en entero - .round para redondear
nuevo_float = float(num)
nuevo_entero = int(fl)

print(nuevo_float)
print(nuevo_entero)

import random #importamos una librería llamada random
num_aleatorio = random.randint(2, 5)   #número aleatorio entre 2 y 5 

print(num_aleatorio)

#Cadenas o textos o strings
string = "ABCDEFG"
nombre = "Elena"
apodo = "elenita"
print("Este es el alfabeto",string) #la coma en automatico agrega un espacio
print("Este es el alfabeto "+string) #si se hace con signo + se debe agregar el espacio 
print("Este es un numero",10)
#print("Este es un numero"+10) #no se puede utilizar signo mas para concatenar dos tipos de variables distintas.
print("Este es un numero "+str(10)) #str(10) es como tener "10"
print(f"Este es el alfabeto {string}")
print("Les presento a",nombre,",le pueden llamar'", apodo,"'")
print(f"Les presento a {nombre}, le pueden llamar '{apodo}'")

#metodos que nos pueden servir
string2 = "hola mundo! soy Roxany y hoy es 5 de Septiembre" 
print(string2.title()) #primera letra de cada palabra será en mayuscula
print(string2.upper()) #todas las letras en mayúscula
print(string2.lower()) # todas las letras en minuscula
print(string2.count('oy')) #regresa cuantos 'oy' hay en la cadena
string3 = "Elena!Juana!Pablo!Pedro"
print(string3.split('!')) #enlista y divide la cadena por cada ! que hay
print(string2.find('Roxany')) #devuelve donde comienza 'Roxany'. si devuele -1 es porque no lo encontro CASE SENSITIVE

#Tupla - muy parecida a una lista, pero no se puede modificar su valor. pueden tener mas d eun tipo de dato
tupla = ("ABC",10,10.3,False)
print(tupla[2])

#Listas / array / arreglo
lista_vacia = []
lista_llena = ["Hugo","Paco","Luis"] # 0-Hugo 1-Paco 2-Luis
print(lista_llena[1])
lista_llena[2] = "Donald"
print(lista_llena)
lista_llena.pop() #elimina el último elemento de la lista
print(lista_llena)
lista_llena.pop(0) #elimina el elemento de la posisicon en ()
print(lista_llena)
lista_llena.append("Mickey") #agrega in dato al final de la lista
print(lista_llena)

lista_mix = ["Texto1","Texto2",1,False,["Lista1","Lista2"]] #se pueden guardar distintos tipos de valores

lista_nombres = ["Elena", "Juana", "Pedro"]
nuevo_lista = lista_llena + lista_nombres
print(nuevo_lista)

#DICCIONARIOS -> objetos java script
diccionario_vacio = {}
diccionario = {"nombre": "Elena", "edad":30, "soltera":False, "hobbies":["leer","comer","ver tele"]}
diccionario['estatura'] = 1.67
print(diccionario)
diccionario.pop('estatura') #se elimina la propiedad
print(diccionario)
edad = diccionario.pop('edad') #eliminamos de diccionario la propiedad y el valor queda asignado en la variable
print(diccionario)

lista_alumnas = [
    {"nombre":"Elena", "apellido":"De Troya", "id":123, "cursos":["Fundamentos de la Web", "Pyhton"]},
    {"nombre":"Juana", "apellido":"De Arco", "id":234, "cursos":["Fundamentos de la Web", "Pyhton","MERN"]},
    {"nombre":"Pedro", "apellido":"Páramo", "id":345, "cursos":["Fundamentos de la Web", "Pyhton","MERN","Java"]}
]
lista_alumnas[2]["cursos"].pop(2)  #borra MERN de Pedro 
from pprint import pprint #libreria que hace impresionas mas ordenadas
print(lista_alumnas)
