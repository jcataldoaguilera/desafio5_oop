# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-18
# RLAB-23-02-09-0044-2
#

# Liberias
from usuario import Usuario
import json
import datetime

# Variables
instancias = []

# Desarollo
with open('usuarios.txt') as users:
    linea = users.readline()
    while linea:
        try:
            user = json.loads(linea)
            instancias.append(
                Usuario(user.get("nombre"), user.get("apellido"), user.get("email"), user.get("genero"))
                )
            linea = users.readline()
        except Exception as e:
            with open('errors.log','a+') as log_file:
                log_file.write(f"{datetime.datetime.now()} Error: {e}\n")
            log_file.close()
            exit(e)

# Prueba
for i in range(len(instancias)):
    print(instancias[i].email)