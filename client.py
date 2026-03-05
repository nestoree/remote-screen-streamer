import socket
import cv2
import numpy as np
import pyautogui
import pickle
import struct
import time

def start_mobile_stream(server_ip='192.168.x.x', port=8080):   # Modifica esto con la IP de tu maquina server.py
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, port))

            while True:
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                
                result, frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
                data = pickle.dumps(frame)
        
                size = struct.pack("L", len(data))
                client_socket.sendall(size + data)
                
        except (ConnectionResetError, ConnectionRefusedError, BrokenPipeError):
            print("PC desconectado. Reintentando en 5 segundos...")
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            break

start_mobile_stream('192.168.x.x') # Modifica esto con la IP de tu maquina server.py
