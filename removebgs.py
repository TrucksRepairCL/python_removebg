import os
from rembg import remove
from PIL import Image
import io

# Directorios de entrada y salida
input_dir = 'input_images'  # Cambia esto al directorio con las imágenes de entrada
output_dir = 'output_images'  # Cambia esto al directorio de salida para las imágenes sin fondo

# Crear directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Procesar todas las imágenes en el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filtra por extensiones de imagen
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Leer la imagen
        with open(input_path, 'rb') as input_file:
            input_image = input_file.read()

        # Eliminar el fondo
        output_image = remove(input_image)

        # Guardar la imagen sin fondo
        with open(output_path, 'wb') as output_file:
            output_file.write(output_image)

        print(f'Imagen procesada: {filename}')

print('Proceso terminado.')
