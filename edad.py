# Crear una aplciación que nos ayude a ver si una persona es mayor de edad

def calculator(edad):
    if(edad>18):
        msg = "Mayor de edad"
    else:
        msg = "Menor de edad"
    return msg

def main():
    edad = int(input("Ingrese su edad: "))
    msg = calculator(edad)
    print(msg)

if __name__=="__main__":
    main()

    #gjvbjhlbhjlbhjlbhjl