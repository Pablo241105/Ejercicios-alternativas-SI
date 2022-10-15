base=0
exponente=0
base=(int)(input("Di la base: "))
exponente=(int)(input("Di el exponente: "))
if (exponente>0):
    print("Esta es la potencia: ",base**exponente)
if(exponente==0):
    print("El resultado es 1")
if(exponente<0):
    print("Este es el resultado: ",1/base**exponente*1)
