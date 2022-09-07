#Función es un bloque de código que nombramos y que podemos ejecutar las veces que queramos, siempre y cuando se llame. (def para definir función)
def hola():  #def "nombrefuncion"():
    print("Hola a todos!")

hola() 

def sumatoria(a,b):
    suma = a+b
    print(suma) #solo hace la impresión en la pantalla

sumatoria(1,2) #envio los valores en () a=1 b=2

#Función con valor de retorno, regresa algo
def sumatoriaReturn(a,b): #a=3 b=4
    suma= a+b #suma = 3 + 4 = 7
    return suma #regresa 7



sum = sumatoriaReturn(3,4)  #sum = 7
print("La sumatoria recibida fue:",sum)
sum -= 1
print("Restándole 1 es:",sum)

#Reto 1 - crear una función llamada sumatoriaArray(arreglo) y regrese la sumatoria de todos lo elementos del arreglo 

#arreglo = [2, 3, 4, 5]
#total = 0
#num = 2
#total = 0 + 2 = 2

#num = 3
#total= 2 + 3 = 5

#num = 4
#total = 5 + 4 = 9

#num = 5
#total= 9 + 5 = 14

#RETURN 14
def sumatoriaArray(arreglo):
    total = 0

    for num in arreglo:
        total += num

    return total

total_sumatoria = sumatoriaArray([2, 3, 4, 5]) #total_sumatoria = 14
print(total_sumatoria)

#RETO 2: Crear una función que reciba un arreglo y que regrese el premedio de los elementos del arreglo.
#array = [1,2,3]
#sum = 0
#num = 1
#sum = 0 + 1 = 1

#num = 2
#sum = 1 + 2 = 3

#num = 3
#sum = 3 + 3 = 6

#cant_promedio = 6/3 = 2 

#RETURN 2

def promedio(array):
    sum = 0

    for num in array:
        sum += num

    cant_promedio = sum/len(array)

    return cant_promedio


total_promedio = promedio([1,2,3]) # total_promedio = 2

print(total_promedio)

#RETO 3: Crear una función que reciba un arreglo que sume solo los números postitivos.

def sumPositivos(array):
    sum = 0

    for num in array:
        if num > 0:  #solo suma 1 + 2 + 3, porque son positivos.
            sum += num

    return sum

total_suma = sumPositivos ([1,2,3, -1]) #Solo suma positivos 
print(total_suma)