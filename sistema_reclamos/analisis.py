import csv
import matplotlib.pyplot as plt 
from collections import Counter 
categorias_reclamos=[]

with open("reclamos.csv","r",encoding="utf-8",newline="") as archivo:
    lector=csv.DictReader(archivo,delimiter=",")
    for fila in lector:
        categorias_reclamos.append(fila["categoria"])
conteo=Counter(categorias_reclamos)
#print(conteo)
barras=plt.bar(conteo.keys(), conteo.values(),color="#9BDFEB", edgecolor="#EBA79B")
plt.bar_label(barras, fontsize=11, weight="bold", padding=3)
plt.title("Cantidad de Reclamos por Categoría", fontsize=14, weight="bold", fontfamily="Comic Sans MS")
plt.xlabel("Categoría")
plt.ylabel("Cantidad")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()


