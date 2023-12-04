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

git clone https://github.com/Rodrigofranco1/leaker.git

Instale las dependencias necesarias (en este caso, `requests`):

pip install requests

graphql

## Uso

El script se puede ejecutar desde la línea de comandos. Aquí hay algunos ejemplos de cómo usarlo:

```bash
# Buscar por email
python dehashed.py --email tu_correo@ejemplo.com --search email -t "usuario@ejemplo.com"

# Buscar por nombre de usuario
python dehashed.py --email tu_correo@ejemplo.com --search username -t "nombreusuario"

# Buscar por dirección IP
python dehashed.py --email tu_correo@ejemplo.com --search ip_address -t "192.168.1.1"

# Buscar por dominio
python dehashed.py --email tu_correo@ejemplo.com --search domain -t "ejemplo.com"

# Buscar en todos los campos
python dehashed.py --email tu_correo@ejemplo.com --search all -t "termino_de_busqueda"

# Buscar utilizando una lista de términos
python dehashed.py --email tu_correo@ejemplo.com --search all -l "lista.txt"
Reemplace tu_correo@ejemplo.com con su correo electrónico registrado en DeHashed.

Configuración
Puede configurar la clave API de DeHashed directamente en el script:

python
Copy code
API_KEY = 'tu_clave_api'
Contribuciones
Las contribuciones son siempre bienvenidas. Por favor, lea el archivo CONTRIBUTING.md para detalles sobre nuestro código de conducta, y el proceso para enviarnos pull requests.

Licencia
Este proyecto está licenciado bajo la Licencia MIT - vea el archivo LICENSE.md para más detalles.

markdown
Copy code

### Notas Adicionales:

- **Información Personalizada**: Reemplaza `https://github.com/tu_usuario/dehashed-script.git` con la URL real de tu repositorio.
- **Contribuciones y Licencia**: Si planeas aceptar contribuciones, sería bueno tener un archivo `CONTRIBUTING.md`. Similarmente, si eliges una licencia específica, incluye un archivo `LICENSE.md`.
- **Documentación Adicional**: Si el script tiene más opciones o capacidades, asegúrate de documentarlas en el `README.md`.
