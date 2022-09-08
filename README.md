# SGC (Sistema de Gestión de Calificaciones)

## Instalación

### Ambiente virtual

Para instalar el proyecto (desde cero), lo primero que hay que realizar es crear un ambiente virtual (virtual environment). Esto es como un pequeño pc dentro del sistema y se hace con el fin de que lo que se va a trabajar e instalar no cause interferencias. Para crear este ambiente se debe ir al directorio donde se quiera trabajar y ejecutar el siguiente comando:

`python -m venv nombreDelAmbienteVirtual`

Por defecto el nombre del ambiente virtual es **env**, asi que el comando sería:

`python -m venv env`

### Instalar Django

Una vez se ha completado con éxito se puede instalar Django, pero se hará dentro del ambiente virtual, para ello primero hay que poner a correr el ambiente virtual, para ello se ejecuta el siguiente comando (desde la carpeta donde se creó el ambiente virtual):

`source nombreDelAmbienteVirtual/Scripts/activate`

Dado que en este ejemplo el ambiente virtual se llamó **env**, entonces el comando sería:

`source env/Scripts/activate`

Si el ambiente virtual está activo debe verse un (env) encima del nombre del directorio. Para instalar Django se ejecuta el siguiente comando:

`pip install django`

**Nota: Para que lo de pip funcione hay que tener instalado Python 3.4 o superior (o instalarlo por aparte).**

## Levantar el servidor

El programa corre en un servidor, así que para que el programa corra es necesario hacer que el servidor entre en funcionamiento (esto se conoce como levantar el servidor). En Django el servidor se levanta así (este comando se tiene que ejecutar desde el mismo directorio donde esté el archivo manage.py, en este caso está dentro de la carpeta de sgc, así que hay qu ubicarse en ese directorio para correrlo):

`python manage.py runserver`

## Visualizar el proyecto

Una vez se tiene corriendo el servidor se puede entrar al navegar e ingresar a la página *http://localhost:8000/login/*. Por ahora esta es la única página que está sirviendo y está limpia. La idea es ir construyendo con HTML puro.

Sandra ya tiene algo más avanzado, pero lo quise limpiar lo más posible para que se haga desde lo más básico y corra en cualquier IDE sin problema. 