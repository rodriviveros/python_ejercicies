def main():
    ARCHIVO="empleados.txt"
    print("-"*80)
    total=0.0
    cantidad=0
    print("Acreditación de sueldos")
    print("-"*80)
    with open(ARCHIVO,"r", encoding="utf-8") as archivo:
        for linea in archivo:
            empleado= linea.strip()
            legajo,nombre,cbu,salario=empleado.split(";")
            salario=float(salario)
            print(f"Se transfirió al cbu {cbu} el monto de ${salario}")
            total+=salario
            cantidad+=1
            print("-"*80)
    print(f"se transfirió en total ${total} a {cantidad} empleados"+"\n")

if __name__ == "__main__":
    main()