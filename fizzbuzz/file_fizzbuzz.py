from fizzbuzz import fizzbuzz
resultados= [] 
def procesar_archivo():
	with open("numeros.txt",encoding = "utf-8") as archivo:
		for linea in archivo:
			numero = int(linea)
			resultados.append(fizzbuzz(numero))
		return resultados

print(procesar_archivo())