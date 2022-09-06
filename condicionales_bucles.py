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