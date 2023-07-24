def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    

    print("Ahira introduce la operación")
    print("suma:1")
    seleccion=input("\nTu selección (1-4): ")

    if seleccion=='1':
        sum=sumar(num1,num2)
        print(f"La suma de los dos números es... {sum}")


if __name__ == "__main__":
    main()