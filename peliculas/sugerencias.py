print("=====================================\n")
print("      sugerencias de pelìculas       \n")
print("=====================================\n")
usuario=input("Buen dìa, cùal es tu nombre? ")
print("¿Què querès ver hoy, "+usuario+"?")
Peliculas = [
    {"nombre": "Rapidos y furiosos", "genero": "Acción", "estreno": 2001, "rating": 6.8},
    {"nombre": "Troya", "genero": "Acción", "estreno": 2004, "rating": 7.3},
    {"nombre": "Terminator 2", "genero": "Acción", "estreno": 1991, "rating": 8.6},
    {"nombre": "¿Y dónde está el piloto?", "genero": "Comedia", "estreno": 1980, "rating": 7.7},
    {"nombre": "¿Què pasò ayer?", "genero": "Comedia", "estreno": 2009, "rating": 7.7},
    {"nombre": "Sherk", "genero": "Comedia", "estreno": 2001, "rating": 7.8}
]
print("---- GÉNEROS-----")
print("Acción")
print("Comedia")
genero_favorito=input("¿Que genero te gusta? ")
print ("Buscando Péliculas del Género: " +genero_favorito)
for Pelicula in Peliculas:
    if Pelicula["genero"]==genero_favorito:
        print(Pelicula["nombre"])
