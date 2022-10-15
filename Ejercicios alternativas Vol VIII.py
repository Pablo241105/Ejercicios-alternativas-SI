nota=0
edad=0
sexo=""

nota=(int)(input("Introduce la nota: "))
edad=(int)(input("Introduce la edad: "))
sexo=(input("Introduce el sexo:(Solo M o F): "))

if (nota>=5 and edad>=18 and sexo=="F"):
    print("Aceptada")
elif(nota>=5 and edad>=18 and sexo=="M"):
    print("Posible")
elif(nota<5 and edad<18 and sexo!="M"or"F"):
    print("No aceptado")