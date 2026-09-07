
print("=====================================\n")
print("      sugerencias de pelìculas       \n")
print("=====================================\n")
usuario=input("Buen dìa, cùal es tu nombre? ")
print("¿Què querès ver hoy, "+usuario+"?")
nombre_pelicula="Rapidos y furiosos"
genero_pelicula="Acciòn"
anio_pelicula=2001
rating_pelicula=6.8
nombre_pelicula2="Troya"
genero_pelicula2="Acciòn"
anio_pelicula2=2004
rating_pelicula2=7.3
nombre_pelicula3="Terminator 2"
genero_pelicula3="Acciòn"
anio_pelicula3=1991
rating_pelicula3=8.6
nombre_pelicula4="¿Y dónde está el piloto?"   
genero_pelicula4="Comedia"  
anio_pelicula4=1980 
rating_pelicula4=7.7 
nombre_pelicula5="¿Què pasò ayer?"
genero_pelicula5="Comedia"
anio_pelicula5=2009
rating_pelicula5=7.7
print("---- GÉNEROS-----")
print("Acción")
print("Comedia")
genero_favorito=input("¿Que genero te gusta? ")
print ("Buscando Péliculas del Género: " +genero_favorito)
if (genero_pelicula==genero_favorito):
	print(nombre_pelicula)
if (genero_pelicula2==genero_favorito):
  print(nombre_pelicula2)
if (genero_pelicula3==genero_favorito):
  print(nombre_pelicula3)
if (genero_pelicula4==genero_favorito):
	print(nombre_pelicula4)
if (genero_pelicula5==genero_favorito):
	print(nombre_pelicula5)
