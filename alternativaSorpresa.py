import os

# comienza el script
rutaArchivo = "./audio/sorpresa.mp3"    # ruta del archivo de audio
os.system('mpg123 {rutaArchivo}')
# playsound(rutaArchivo)  # reproduce audio del archivo que encuentre.
print("Fin del programa")
