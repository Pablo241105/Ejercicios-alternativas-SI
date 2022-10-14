usuSecreto="juan"
passSecreto="12"
usuario = input("Dime tu usuario: ")
password= input("Dime tu contraseña: ")

while (usuSecreto!=usuario or passSecreto!=password) :
 if(usuSecreto!=usuario) :
    print("Error en el ususario") 
    usuario = input("Dime tu usuario: ")
 elif (passSecreto!=password):
    print("Error en la contraseña") 
    usuario = input("Dime tu contraseña: ")

print("Usuario y password correcto")



