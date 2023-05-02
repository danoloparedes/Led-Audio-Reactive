# Led-Audio-Reactive
Repositorio personal en donde facilita la instalación de todas las dependencias y configuraciones para las leds que reaccionan con audio. Esto tanto para las leds para escritorio (control por web), quincho y demases.

## Requisitos Previos
Antes de comenzar con la instalación, es fundamental asegurarse de que la Raspberry Pi esté correctamente iniciada, ya sea a través de SSH o mediante periféricos. Además, es necesario contar con una conexión a internet estable para proceder con los siguientes pasos.

A continuación, se detallan los pasos para preparar el entorno:

1. Actualizar e instalar paquetes necesarios ejecutando los siguientes comandos en la terminal:
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip
```
Estos comandos actualizarán los paquetes existentes y permitirán la instalación de pip3, el gestor de paquetes de Python. Puedes verificar la instalación exitosa de pip3 con el siguiente comando:
```
pip3 --version
```
2. (Opcional)  Se recomienda crear un entorno virtual para aislar las dependencias y configuraciones de este proyecto. Para crear y activar el entorno virtual, ejecuta los siguientes comandos:
```
python3 -m venv venv
source myenv/bin/activate (Linux/MacOS)
myenv\Scripts\activate (Windows)
```
Esto creará un entorno virtual llamado "venv" y lo activará en tu terminal.

3.A continuación, es necesario instalar la librería que permite el manejo de los LEDs. Puedes elegir entre dos opciones:

Opción 1: Instalación manual de las librerías ejecutando los siguientes comandos:
```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install –force-reinstall adafruit-blinka
```

Opción 2 (En desarrollo): Instalación de los requerimientos a través del archivo requirements.txt utilizando el siguiente comando:
```
pip install -r requirements.txt
```
## Configuraciones previas
Antes de utilizar los LEDs audio-reactivos, es necesario realizar algunas configuraciones previas, como configurar el dispositivo de audio predeterminado en la Raspberry Pi. A continuación, se detallan los pasos:

1. Crear el archivo asound.conf ejecutando el siguiente comando en la terminal:
```
sudo nano /etc/asound.conf
```
Esto abrirá el editor de texto nano con un archivo nuevo.
2. En el archivo asound.conf, copia y pega el siguiente contenido:
```
pcm.!default {
    type hw
    card 1
}
ctl.!default {
    type hw
    card 1
}
```
3. Guarda los cambios y cierra el editor de texto.
4. Luego, edita el archivo alsa.conf ejecutando el siguiente comando en la terminal:
```
sudo nano /usr/share/alsa/alsa.conf
```
5. Busca las dos líneas que contienen:
```
defaults.ctl.card 0
defaults.pcm.card 0
```
6. Reemplaza esas líneas con las siguientes:
```
defaults.ctl.card 1
defaults.pcm.card 1

```
7. Guarda los cambios y cierra el editor de texto.

Estas configuraciones permitirán que el dispositivo de audio USB sea reconocido como el dispositivo de audio predeterminado en tu Raspberry Pi.

Recuerda reiniciar tu Raspberry Pi después de realizar estas configuraciones para que los cambios surtan efecto.
