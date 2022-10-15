usuSecreto = "pepe"
passSecreto = "asdasd"

usuario = input("Dime tu ususario: ")
contraseña = input("Dime tu contraseña: ")

while (usuSecreto!=usuario or passSecreto!=contraseña):
    if (usuSecreto!=usuario):
        print("Error en el usuario")
        usuario = input("Dime tu ususario: ")
    elif (passSecreto!=contraseña):
        print("Error en el password")
        password = input("Dime tu contraseña: ")
    


print("Usuario y password correcto")