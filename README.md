# 📱 Remote Screen Streamer (Python)
Este proyecto permite transmitir la pantalla de un dispositivo remoto (como una VM) a un PC central mediante Sockets. El servidor permite visualizar la transmisión en tiempo real y entrar/salir del modo visualización sin interrumpir la conexión del cliente.

## 🚀 Características

- Conexión Persistente: El cliente intenta reconectar automáticamente si el servidor se apaga.
- Control de Sesión: El servidor permite dejar de ver la pantalla (liberando recursos) mientras el cliente sigue activo en segundo plano.
- Optimización: Uso de compresión JPEG para reducir la latencia en redes locales.

## 🛠️ Instalación
1. Requisitos del Sistema
Asegúrate de tener Python 3.10 o superior.

2. Dependencias (PC y Cliente)
Debido a cambios recientes en las librerías, es crítico instalar las versiones compatibles para evitar errores de **numpy**:

```
pip uninstall numpy -y
pip install "numpy<2" opencv-python mss pillow
```

Nota: Si estás en Linux/Kali, instala también:
**sudo apt install scrot xsel xclip libpng-dev**

## 📦 Estructura del Proyecto

**servidor.py**
Es el nodo central que recibe las imágenes.
- Ejecuta el script.
- Espera a que el cliente se conecte.
- Usa el menú interactivo para ver la pantalla (Opción 1) o volver al menú (q).

**client.py**
Es el emisor.
- Edita la línea **start_mobile_stream('TU_IP_LOCAL')** con la IP de tu PC.
- Ejecuta el script. Se mantendrá transmitiendo hasta que lo detengas manualmente.

## 📋 Instrucciones de Uso
Obtén tu IP Local: En la terminal de tu PC (Servidor), escribe ipconfig (Windows) o ifconfig (Linux) y busca tu dirección IPv4 (ej. 192.168.0.12).
Configura el Cliente: Pega esa IP en el archivo client.py.

Ejecuta el Servidor:

```
python servidor.py
```

Ejecuta el Cliente:

```
python client.py
```

## 🛠️ Tecnologías Usadas
Python 3
OpenCV: Procesamiento de imagen.
MSS / PyAutoGUI: Captura de pantalla.
Sockets: Comunicación TCP/IP.
