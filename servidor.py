import socket
import cv2
import pickle
import struct

def run_server(port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Servidor iniciado. Esperando conexión por el puerto {port}...")

    conn, addr = server_socket.accept()
    print(f"Móvil conectado desde: {addr}")

    while True:
        print("\n--- MENÚ DE CONTROL ---")
        print("1. Ver pantalla")
        print("2. Salir")
        print("3. Cerrar todo")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            data = b""
            payload_size = struct.calcsize("L")
            print("Presiona 'q' para dejar de ver la pantalla.")
            
            try:
                while True:
                    while len(data) < payload_size:
                        data += conn.recv(4096)
                    
                    packed_msg_size = data[:payload_size]
                    data = data[payload_size:]
                    msg_size = struct.unpack("L", packed_msg_size)[0]
                    
                    while len(data) < msg_size:
                        data += conn.recv(4096)
                    
                    frame_data = data[:msg_size]
                    data = data[msg_size:]
                    
                    frame = pickle.loads(frame_data)
                    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                    
                    cv2.imshow('Streaming Movil', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        break
            except Exception as e:
                print(f"Conexión interrumpida: {e}")
                break

        elif opcion == '2':
            cv2.destroyAllWindows()
            print("Has salido de la visualización.")
            
        elif opcion == '3':
            conn.close()
            break

run_server()
