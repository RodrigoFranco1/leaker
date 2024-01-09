
![DALL·E 2023-12-04 14 49 03 - Create a bold and dynamic image for a cybersecurity tool named 'Leaker'  The image should feature an abstract digital avatar, not a human or a known c](https://github.com/RodrigoFranco1/leaker.py/assets/115948997/edcf6e2d-6a04-457f-977d-9fad5e8564c2)
# Leaker

Este script en Python permite realizar búsquedas en la API de DeHashed, facilitando la obtención de información relacionada con filtraciones de datos, cuentas comprometidas y más.

## Características

- Búsqueda por diferentes campos como email, nombre de usuario, IP, entre otros.
- Posibilidad de buscar en todos los campos disponibles.
- Paginación automática para recorrer todos los resultados.
- Soporte para búsqueda a partir de una lista de términos.

## Requisitos

- Python 3
- Biblioteca `requests`

## Instalación

Clone el repositorio a su máquina local:

https://github.com/RodrigoFranco1/leaker.py.git

Instale las dependencias necesarias (en este caso, `requests`):

pip install requests


## Uso

El script se puede ejecutar desde la línea de comandos. Aquí hay algunos ejemplos de cómo usarlo:

```bash
# Buscar por email
python leaker.py --email tu_correo@ejemplo.com --search email -t "usuario@ejemplo.com"

# Buscar por nombre de usuario
python leaker.py --email tu_correo@ejemplo.com --search username -t "nombreusuario"

# Buscar por dirección IP
python leaker.py --email tu_correo@ejemplo.com --search ip_address -t "192.168.1.1"

# Buscar por dominio
python leaker.py --email tu_correo@ejemplo.com --search domain -t "ejemplo.com"

# Buscar en todos los campos
python leaker.py --email tu_correo@ejemplo.com --search all -t "termino_de_busqueda"

# Buscar utilizando una lista de términos
python leaker.py --email tu_correo@ejemplo.com --search all -l "lista.txt"
Reemplace tu_correo@ejemplo.com con su correo electrónico registrado en DeHashed.

Configuración
Puede configurar la clave API de DeHashed directamente en el script:
API_KEY = 'tu_clave_api'

#############################################################################################################

# Buscar utilizando una lista de términos
python leaker.py --email tu_correo@ejemplo.com --search all -l "lista.txt"
Reemplace tu_correo@ejemplo.com con su correo electrónico registrado en DeHashed.


Contribuciones
Las contribuciones son siempre bienvenidas. Por favor, lea el archivo CONTRIBUTING.md para detalles sobre nuestro código de conducta, y el proceso para enviarnos pull requests.
