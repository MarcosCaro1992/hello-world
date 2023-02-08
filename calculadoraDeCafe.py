cantTazas = int(input("Cuantas tazas te vas a hacer?"))

# conectar de acá para abajo con el botón
cantCafe = (cantTazas *250)/15

strCantTazas = str(cantTazas) 
strCantCafe = str(cantCafe) 


print ("Para hacer " + strCantTazas + " tazas de café, necesitas " + strCantCafe + " gr. de café.") 
