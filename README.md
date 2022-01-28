# API_RestCRUD

> API REST creada con Django y Django Rest Framework para manipulación de Clentes/Factura/Productos
> Autenticación JWT

## Instrucciones

``` bash
# Iniciamos el entorno virtual y lo activamos

python3 -m venv venv
. venv/bin/activate

# Dentro de env clonamos el repositorio
git clone git@github.com:IrvinAlexanders/API_RestCRUD.git

# Ahora instalamos los paquetes que utilizaremos con sus respectivas versiones con el siguiente comando

pip install -r requirements.txt

# Creamos las migraciones

python manage.py makemigrations

# Y aplicamos las migraciones

python manage.py migrate

# Django trae por dafault el puerto 8000, corremos nestra api con el siguiente programa

python manage.py runserver

# Para frenar el programa utilizamos ctrl + c

```


