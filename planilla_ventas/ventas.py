#pip install pandas
#pip install openpyxl
import pandas as pd
import matplotlib.pyplot as plt 
nombre_planilla=input("Ingrese el nombre de la planilla: ")
ventas=pd.read_excel(nombre_planilla, sheet_name="Ventas")
#print(ventas)
#print(ventas.describe())
#print(ventas["Precio_Unitario"])
ventas["Facturación"]=ventas["Precio_Unitario"]*ventas["Unidades"]
#print(ventas["Facturación"])
print(f"\n=== Totales de {nombre_planilla} ===")
print(f"Unidades Vendidas:{ventas["Unidades"].sum()}")
print(f"Total Vendido: ${ventas["Facturación"].sum()}")
negocios=pd.read_excel(nombre_planilla,sheet_name="Negocios")
ventas=ventas.merge(negocios, on="Negocio", how="left")
#print(ventas)
print(f"\n=== Facturación por barrio {nombre_planilla} ===")
por_barrio=ventas.groupby("Barrio")["Facturación"].sum()
print(por_barrio.to_frame())
plt.pie(por_barrio, labels=por_barrio.index, autopct="%1.1f%%")
plt.show()
