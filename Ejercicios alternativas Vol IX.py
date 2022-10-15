vNumeros=[]

numero1=0
numero2=0
numero3=0



numero1=(int)(input("Di un numero: "))
numero2=(int)(input("Di otro numero: "))
numero3=(int)(input("Di el ultimo numero: "))

vNumeros.insert(0,numero1)
vNumeros.insert(1,numero2)
vNumeros.insert(2,numero3)

vNumeros.sort(reverse=False)

print("Ya estan ordenados",vNumeros)

