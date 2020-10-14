def conversion(cadenadenumeros):
    try:
        var1 = int(cadenadenumeros, 16)
        var2 = str(var1)
        print("El numero en Decimal es: ", var2)
    except ValueError:
        print("solo se pueden meter numeron enteros y letras (Hexadecimal)")

    return 

cadenadenumeros = input("Ingresa el valor Hexadecimal: ")
(conversion(cadenadenumeros))
