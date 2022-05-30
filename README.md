# ICPC-DATA-BASE-ADMIN
Aplicacion para la administracion de una base de datos de la competecia de programacion ICPC
#instalcion base de datos postgres
(*Este paso requiere que cuente con postgresql instalado en su equipo)
Debe descargar el proyecto.sql una vez descargado crea una base de datos con el nombre proyectofinal
posteriormente carga los datos del archivo proyecto.sql a la base de datos con el comando 

psql -U postgres -p 5432 proyectofinal < proyecto.sql

#Instalacion de la aplicacion
Para compilar la aplicacion necesitara usar python  e instalar usando el comando pip en la terminal 
de su sistema operativo, descargando las siguientes dependencias

pip install pysimplegui

y posteriormente 

pip install psycopg2 



una vez halla realizado las instalaciones previas debe de ir  al carpeta donde guardo el repositorio 
(la ubicacion debe contener la imagen logo.png para poder funcionar) y ejecutar el siguiente comando


python proyecto.py 



#Uso de la aplicacion 

Para usar la aplicaion solamente de click en el apartado al que quiere entrar, una vez dentro llene los campos 
respetando los tipos de datos de lo contrario las acciones que realize no se llevaran  a cabo.

*Los elementos del tipo fecha cuentan con un calendario para que seleccione la fecha, pero en caso de que guste
escribirla directamente debe seguir el siguiente formato aaaa/mm/dd(sin espacios) los numeros de un solo digito 
deben escribirse tal cual no es valido el uso de elementos del tipo 01,02,etc.
