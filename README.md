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


## 4.   Connect db
Connect to the database throught DBeaver or any database client with the following credentials or configure your credentials and after run 'python manage.py makemigrations' and 'python manage.py migrate'
```text
NAME: "ecommerce"
USER: "daimer"
PASSWORD: "Redes1212"
HOST: "localhost"
PORT: "5433"
```
After that execute the following script


# Notas
Los archivos independientes de los módulos se ubican en /filemanager (archivos transversales como imagenes, css, fuentes y demás), la carpeta /media es para los archivos que se suben por la applicacion y dependen de cada módulo.
. 

# API para guardar las consultas realizadas de productos

Para guardar los registros de los productos mas buscados filtrarlos por esta api ya sea con los siguientes ejemplos
GET  http://127.0.0.1:8000/api/productsSearch/?id=&name=PANTALON&price=&discount=&country=&price__gt=&price__lt=&discount__gt=&discount__lt=&country__id=
GET /api/productsSearch/?search=camisa
# API de documentación de filtros de productos

ingresa a la siguiente api y encontrara toda la documentación relacionad 
http://127.0.0.1:8000/api/productsSearch/


# API de productos más buscados
http://localhost:8000/api/productsTop/

# API para guardar imagenes de productos

http://localhost:8000/api/images/


# API de documentación general del proyecto

en la siguientes apis encontrara una documentación general de todo el proyecto
http://127.0.0.1:8000/api/swagger/
http://127.0.0.1:8000/api/swagger/
http://127.0.0.1:8000/api/redoc/


# install pip
python3 -m pip install --upgrade pip

# config and install virtualenv

pip3 install virtualenv

virtualenv bombink

source bombink/bin/activate

pip install -r requirements.txt
# run environment with 

source bombink/bin/activate


# run dockerfile
docker build -t bombink .

docker run -p 8000:8000 bombink

-> docker ls

