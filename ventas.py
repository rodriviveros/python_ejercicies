ARCHIVO="ventas.txt"
def cargar_ventas():
    try:
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            tipo = input("Tipo de madera : ")
            precio = int(input("Precio : "))
            fecha=input("Fecha de la venta: ")
            cliente=input("Clientes: ")
            entrega=input("¿Cúal es el método de entrega? (retira en el aserradero / envío a domicilio): ")
            if entrega == "envio a domicilio":
                envio_domicilio=input("Ingrese la dirección de envío: ")
            archivo.write(f"{tipo}\t${precio}\t{fecha}\t{cliente}\t{entrega}\t{envio_domicilio} \n")
    except PermissionError:
        print("Error con los permisos.")
    except OSError as error:
        print(f"Problema con el archivo usando el SO: {error}")






def main():
    seguir="s"
    while(seguir=="s"):
        cargar_ventas()
        seguir=input("¿Necesita registrar otra venta? (s/n): ").lower()
    






if __name__ == "__main__":
    main()