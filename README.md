# Descripción
Se le solicita crear un script Python que permita crear instancias de usuario a partir de los
datos entregados en el archivo usuarios.txt, y almacene cada instancia creada en una lista.
Cada línea del archivo usuario.txt contiene un texto en estructura json, donde cada clave
corresponde al nombre de un atributo de Usuario, y su valor asociado corresponde al valor
que debe tener en dicho atributo cada instancia de usuario creada.
Se le solicita además que se maneje las posibles excepciones en cada intento de leer los
datos de un usuario y crear una instancia a partir de ellos. En caso de que se produzca una
excepción, se debe añadir a un archivo error.log.
Se le proporciona el archivo usuario.py que contiene la definición de la clase usuario, y el
archivo usuarios.txt que contiene los datos de los usuarios a ser creados.