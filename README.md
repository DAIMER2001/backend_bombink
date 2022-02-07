# Introduction 
Projecto base en Django para soportar los diferentes módulos de la plataforma Productos. 

# Antes de iniciar
## 1.	Instalación de herramientas
- Instalar conda: puede encontrar un instalador adecuado a su Sistema Operativo en https://repo.anaconda.com/archive/

## 2.	Después de Clonar
Una ves clonado este proyecto, debe crear un ambiente conda y activarlo, paso seguido instalar las dependencias python de ese ambiente 
- **conda create -n ecommerce python=3.9.7**
- **conda activate ecommerce**
- **pip install -r requirements.txt**

### \* Usuarios linux.
Se debe instalar un compilador antes de correr la línea pip, use **sudo apt install -y g++ autoconf libpq-dev python-dev**

## 3.	Iniciar entorno local
Levante django, **python manage.py runserver**

# Notas
Los archivos independientes de los módulos se ubican en /filemanager (archivos transversales como imagenes, css, fuentes y demás), la carpeta /media es para los archivos que se suben por la applicacion y dependen de cada módulo.

De no aparecer se debe de crear la carpeta /apps, en esta carpeta se ubican los módulos de viclass. 
