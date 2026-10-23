dominio = input("Indica el dominio del país que queres conocer: ")
def obtener_pais():
    paises = {"ar":"Argentina", "br":"Brasil", "uy":"Uruguay", "cl":"Chile", "es":"España"}
    print(paises[dominio])
paises= {"mx":"Mexico","ec":"Ecuador","fr":"Francia","py":"Paraguay"}
obtener_pais()