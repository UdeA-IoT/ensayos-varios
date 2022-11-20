# Ejemplo 1

Aplicación de Hola mundo usando flask en linea de comandos.

* **Configuración del entorno de trabajo**: solo se hace una vez despues de descargadas totas las fuentes necesarias:

  ```bash
  cd example1
  python3 -m venv env
  source env/bin/activate   # venv\Scripts\activate (windows)
  pip3 install -r requirements.txt
  ```

* **Despues de configurar el entorno**: Cada vez que se vaya a trabajar en el ejemplo, es necesario activar el entorno virtual.
  
  ```bash
  source env/bin/activate # venv\Scripts\activate (windows)
  ```

* **Ejecución de la aplicación**: Despues de activar el entorno virtual puede correr la aplicación. 
  
  ```bash
  export FLASK_APP="hello.py" # Windows (pwsh)> $env:FLASK_APP="hello.py"
                              # Windows (cmd)> set FLASK_APP="hello.py"
  
  flask run 
  ```

* **Desactivar el entorno virtual**: Cuando se va a dejar de trabajar en el entorno virtual.
  
  ```bash
  dactivate # Funciona tambien en windows
  ```




## Enlaces de utilidad

* [Environment Variables in Windows/macOS/Linux](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html#:~:text=2.2%20Set%2FUnset%2FChange%20an,it%20to%20an%20empty%20string.)
* [about_Environment_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3)
