import os

# comienza el script
rutaArchivo = "./audio/audioSorpresa.mp3"    # ruta del archivo de audio
os.system('mpg123 ./audio/audioSorpresa.mp3')
# playsound(rutaArchivo)  # reproduce audio del archivo que encuentre.
print("Fin del programa")
