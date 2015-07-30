# Laboratorio-de-datos

El Laboratorio de Datos es el repositorio de datasets y API proporcionados por
las entidades participantes en la segunda edición de HackCDMX.

Este repositorio contiene una extensión del portal de datos [CKAN](http://ckan.org/).

## Instalación

Este repositorio provee dos formas para que puedas crear tu propia instancia del
Laboratorio de datos.

### Instalar extensión

Haciendo uso del metodo tradicional, necesitas tener ya instalado CKAN, junto con
los serviciós que de el depende como el la base de datos (Postgres).
Te recomendamos que consultes la documentación de CKAN para su
[instalación](http://docs.ckan.org/en/latest/maintaining/installing/index.html).

Ya teniendo CKAN instalado solo necesitas clonar este repositorio en tu sistema.

```
$ git clone https://github.com/LabPLC/Laboratorio-de-datos.git
```

Ingresa a la carpeta que acaba de ser creada e instala esta extensión en el sistema.

```
$ cd Laboratorio-de-datos
$ python setup.py develop
```

Ahora agrega a tu archivo de configuración de CKAN, el nombre de la extensión
que acabamos de instalar.
Si tienes dudas este archivo tiene terminación `.ini`.

```
ckan.plugins = ckanext-labplc
```

Ahora solo tienes que iniciar la instancia de CKAN o si lo tienes configurado con un
servidor apache, debes reiniar el servicio.

```
# service restart apache2
```

### Datacats

Esta opción depende de un sistema llamado docker. Datacats hace uso intensivo de
contenedores para aislar cada componente que require CKAN.

Debes tener instalado docker y pertenecer al grupo de docker.

Despues para la instalación de datacats, se require ejectuar el siguiente comando:

```
$ pip install datacats
$ datacats pull
```

Este ultimo comando obtiene las dependencias y al mismo CKAN.
Ya que tenemos todos los recursos creemos un proyecto y agreguemos nuestra
extensión.

```
$ datacats create labdatos
$ cd labdatos
$ git clone https://github.com/LabPLC/Laboratorio-de-datos.git
```

Editemos el archivo `development.ini` y agreguemos nuestra extensión a la lista
de plugins.

```
ckan.plugins = ckanext-labplc
```

Despues de esto solo necesitas ejectuar:

```
$ datacats install
$ datacats open
```

El cual abrira el navegador prefeinido en nuestro sistema con la pagina de una
nueva instancia del laboratorio de datos.

## Contribuye

Este proyecto esta abierto a la comunidad. Si deseas colaborar puedes hacerlo reportando errores, dando ideas o haciendo solicitudes en la sección de issues.

Si cuentas con codigo por favor crea un pull requests, dando un titulo conciso del aporte y una descripción de los elementos a modificar, asi como tus motivaciones. Si es algun aporte que involucre cambios visuales por favor enlaza una imagen de los cambios en la descripción.

## Licencia
