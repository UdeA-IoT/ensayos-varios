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

