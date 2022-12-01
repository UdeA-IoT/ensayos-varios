# Proyecto 1

## Descripción

Controlar de manera remota un led conectado a un arduino de manera serial

## Fases

### Fase 1

* **link**: [fase1](./fase1/README.md) 

### Fase 2

* **link**: [fase2](./fase2/README.md) 

### Fase 3

* **link**: [fase3](./fase3/README.md) 

### Fase 4

* **link**: [fase4](./fase4/README.md) 

### Fase 5

Integración y mejora.


# Enlaces 
1. [ESP32 Relay Web Server](https://learn.sparkfun.com/tutorials/esp32-relay-web-server/all)

<!--

# Ejemplo 1

## Antes de empezar

### Configuración del entorno de desarrollo
Una vez se descarge el repositorio es necesario ingresar al directorio en el que se aloja el proyecto ```example1``` y se configura el entorno de trabajo siguiendo los siguientes pasos:

  ```bash
  cd example1
  python3 -m venv env
  source env/bin/activate   # venv\Scripts\activate (windows)
  pip3 install -r requirements.txt
  pip3 freeze               # Lista de requerimientos instalados
  deactivate                # Salir del entorno virtual 
  ```
El procedimiento anterior solo es necesario realizarlo una sola vez en caso de no necesitar instalar mas cosas.  

## Trabajo en el proyecto

Cada vez que inicie el proyecto, siga los siguientes pasos:

1. **Activar el entorno virtual**: Lo cual se hace ejecutando el siguiente comando
  
  ```bash
  source env/bin/activate # venv\Scripts\activate (windows)
  ```

2. **Configure las variables de entorno**: Al ser un proyecto Flask, se recomienda que defina las siguientes variables de entorno. La siguiente tabla muestra los comandos para el caso para Linux y Windows:

   |Variable|Valor|Linux|Windows (pwsh)|Windows (cmd)|
   |---|---|---|---|---|
   |```FLASK_APP```|"main.py"|```export FLASK_APP="main.py"```<br>```echo $FLASK_APP```|```$env:FLASK_APP="main.py"```<br>```$env:FLASK_APP```|```set FLASK_APP="main.py"```<br>```echo %FLASK_APP%```|
   |```FLASK_DEBUG```|1|```export FLASK_APP="main.py"```<br>```echo $FLASK_APP```|```$env:FLASK_DEBUG=1``` <br>```$env:FLASK_DEBUG```|```set FLASK_DEBUG=1```<br>```echo %FLASK_DEBUG%```|
   
   Por ejemplo si se esta en una maquina linux, despues de haber iniciado el entorno, los comandos de configuración para las variables de entorno serian:
   
   ```bash
   export FLASK_APP="main.py" 
   echo $FLASK_APP
   export FLASK_DEBUG=1 
   echo $FLASK_DEBUG 
   ```

3. **Codifique, haga cambios y pruebe**: Despues de hacer los cambios en el archivo inicie el servidor (**Nota**: Si activa el debug con una vez que lo inicie hay pues los cambios en los programas se veran reflejados):
   
   * **Iniciar el servidor**: Para las pruebas.
     
     ```bash
     flask run
     ```

   * **Finalizar el servidor**: Cuando ya va a dejar de trabajar.
     
     ```bash
     CTRL+Z
     ```

4. **Desactivar el entorno virtual**: Para salir del entorno virtual se ejecuta el comando.
   
   ```bash
   dactivate # Funciona tambien en windows
   ```


## Enlaces de utilidad

* [Environment Variables in Windows/macOS/Linux](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html#:~:text=2.2%20Set%2FUnset%2FChange%20an,it%20to%20an%20empty%20string.)
* [about_Environment_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3)
* [jinja](https://jinja.palletsprojects.com/en/3.1.x/)
* [Example list of first words to use in a git commit title](https://gist.github.com/scmx/411f6fea4ee3832806720d536a7d5d8f)






## Ejemplo 1


Ejemplo ejecutando usando flask en un entorno virtual en python. [link](example1/README.md)

## Ejemplo 2

Ejemplo usando dockerizando el ejemplo uno. Pendiente.

## Referencias

1. https://midu.dev/buenas-practicas-escribir-commits-git/
2. https://udacity.github.io/git-styleguide/
3. https://www.conventionalcommits.org/en/v1.0.0/
4. https://github.com/fteem/git-semantic-commits
5. https://chiamakaikeanyi.dev/how-to-write-good-git-commit-messages/
6. https://github.com/elsewhencode/project-guidelines
7. https://www.datree.io/resources/github-best-practices
8. https://www.freecodecamp.org/news/git-best-practices-commits-and-code-reviews/
9. https://www.gitkraken.com/learn/git/best-practices/git-commit-message

-->