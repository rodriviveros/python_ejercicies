
def parimpar(num):
 
    if num % 1 != 0:
        return "Decimal"
    if num == 0:
        return "Cero"
    if num % 2 == 0:
        return "Par"
    return "Impar" 

def lista_par_impar(lista_nums):
    lista_resultados = []
    for numero in lista_nums:
        lista_resultados.append(parimpar(numero))
    return lista_resultados

print(lista_par_impar([2,5,7,13,8,9,25]))