# Led-Audio-Reactive
Repositorio personal en donde facilita la instalación de todas las dependencias y configuraciones para las leds que reaccionan con audio. Esto tanto para las leds para escritorio (control por web), quincho y demases.

## Requisitos Previos
Después de iniciar la Raspberry Pi, ya sea a través de SSH o mediante periféricos, es esencial asegurarse de estar conectado a internet antes de proceder con los siguientes pasos de instalación.

Escribir en el terminar los siguientes comandos.
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip
```
Con esto estara instalado el comando pip. Se puede revisar si se instalo correctamente con el siguiente comando.
```
pip3 --version
```
Opcionalmente, se recomienda crear un entorno virtual
```
python3 -m venv venv
```
Esto creará un entorno virtual llamado "myenv" en el directorio actual. Los entornos virtuales son una forma de aislar las dependencias y configuraciones de un proyecto del resto del sistema.

Para activar el entorno escriba lo siguiente
```
source myenv/bin/activate (Linux/MacOS)
myenv\Scripts\activate (Windows)
```

Luego es necesario instalar la libreria encargada del manejo de las leds. 
Opcion 1:Escribir estos comandos en la terminal
```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install –force-reinstall adafruit-blinka
```

Opcion 2 (Desarrollandose): instalar los requerimientos a traves del requirement.txt
```
pip install -r requirements.txt
```
## Configuraciones previas
