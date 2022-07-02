def factura():

    fact = float(input("Ingrese el monto de la factura: "))
    iva = 0.21

    total = print("El total de la factura mas el iva es de: ", fact + fact * iva)
    return total

print(factura())