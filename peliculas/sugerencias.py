print("=====================================\n")
print("      sugerencias de pelìculas       \n")
print("=====================================\n")
def sacar_tildes(texto):
    texto=texto.lower()
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for con_tilde, sin_tilde in reemplazos.items():
        texto = texto.replace(con_tilde, sin_tilde)
    return texto
usuario=input("Buen dìa, cùal es tu nombre? ")
print("¿Què quieres ver hoy, "+usuario+"?")
Peliculas = [
    {"nombre": "Rapidos y furiosos", "genero": "Acción", "estreno": 2001, "rating": 6.8},
    {"nombre": "Troya", "genero": "Acción", "estreno": 2004, "rating": 7.3},
    {"nombre": "Terminator 2", "genero": "Acción", "estreno": 1991, "rating": 8.6},
    {"nombre": "¿Y dónde está el piloto?", "genero": "Comedia", "estreno": 1980, "rating": 7.7},
    {"nombre": "¿Què pasò ayer?", "genero": "Comedia", "estreno": 2009, "rating": 7.7},
    {"nombre": "Sherk", "genero": "Comedia", "estreno": 2001, "rating": 7.8},
    {"nombre": "El padrino", "genero": "Drama", "estreno": 1972, "rating": 9.2},
    {"nombre": "El rey león", "genero": "Animación", "estreno": 1994, "rating": 8.5},
]
print("---- GÉNEROS-----")
print("Acción")
print("Comedia")
print("Drama")
print("Animación")
genero_favorito=input("¿Que genero te gusta? ")
rating_minimo=float(input("¿Cúal es tu rating mínimo? "))
encontrar= False
print ("Buscando Péliculas del Género: " +genero_favorito)
for Pelicula in Peliculas:
    if sacar_tildes(Pelicula["genero"])==sacar_tildes(genero_favorito) and Pelicula["rating"]>=rating_minimo:
        print(f'{Pelicula["nombre"]} - {Pelicula["estreno"]} - {Pelicula["rating"]}')
        encontrar=True
if not encontrar:
    print("No se ha encontrado ninguna película con ese rating.")

