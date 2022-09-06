#Condicionales
x = 2
if x > 10:  #los dos putnos marcan donde comienzan las instrucciones.
    print("Mayor a 10")
else:
    print("Menor a 10")

if x < 10:
    print("Menor a 10")
elif x > 25: #elif pregunta por una segunda condicional 
    print("Mayor a 25")
else:
    print("Número entre 20 y 25")

y = 2
if (y < 5 and x > 10): # al ser dos condicionales deben estar en ()
    print("Y menor a 5, X mayor a 10")
else:
    print("Alguna de las condicionales no se cumplió")

if (y < 5 or x > 10): #or una u otra de las condiciones se cumple
    print("Alguna de las dos condicionales SI se cumplió")
else:
    print("Ninguna de las condicionales se cumplió")

if x < 5: #se puede tener solo una condicion, si no se cumple simplemente no se ejecuta
    print("Menor a 5")

i = 10
if(i > 5 and i % 2 == 0 and i % 5 == 0):  #mayor a 5, multiplo de 2 y multiplo de 5 
    print("Se cumple con las 3 condicionales")

#Bucles o Ciclos
for i in range(5): #bucle que comienza en 0 hasta el 4 (uno menos del número en range)
    print(i) #imprime 0 1 2 3 4 

print('--------------------')
for j in range(1, 5): #range comienza en 1 y termina en 4
    print(j)#valor de j se declara dentro de la variable

print('--------------------')

for k in range(0, 10, 2): #primero es comienzo, segundo donde termina, tercero cada cuanto avanza
    print(k)

#Se puede recorrer un texto
string = "Buenos días"
for letra in string: #por cada letra que existe en string se imprime una letra, el espacio tambien lo reconoce como letra
    print(letra)

# array =['A', 'B', 'C', 'D']
#for(var i=0; i<array.lenght; i++){
#    console.log(array[i])
#}
#for elemento in array: #recorrer una lista
#    print(elemento)

#total = 0
#gasto = 10
#total= 0 + 10 = 10
#gasto = 20
#total = 10 + 20 = 30
#gasto = 30
#total = 30 + 30 = 60
#gasto = 10
#total= 60 + 10 = 70


gastos = [10, 20, 30, 10]
total = 0
for gasto in gastos:
    total += gasto

print(total)

array =['A', 'B', 'C', 'D']
for i in range(0, len(array)): #para saber el indice o posicion del arreglo
    print(i, array[i])

diccionario = {"nombre": "Elena", "apellido": "De Troya", "edad":31}
for llave in diccionario:
    print(llave, diccionario[llave])

y = 0
while y < 3:
    print(y)
    y += 1  #aumenta en 1 la y 
else:
    print("Sentencia else final")

num = 1
while num < 15:
    print(num)
    num+=2
else: 
    print("Ya no entra al ciclo porque el número es",num)

