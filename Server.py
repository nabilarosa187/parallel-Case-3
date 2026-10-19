import socket
import time

HOST = "127.0.0.1"
PORT = 5000


def timestamp():
    return time.strftime("%H:%M:%S")


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))

    server_socket.listen(5)
    print(f"[{timestamp()}] Server berjalan di {HOST}:{PORT}. Menunggu klien...")

    try:
        
        while True:
            
            conn, addr = server_socket.accept()
            print(f"[{timestamp()}] Klien terhubung dari {addr}")

            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    message = data.decode("utf-8")
                    print(f"[{timestamp()}] Pesan dari {addr}: {message}")

                    conn.sendall("Message received".encode("utf-8"))
            except ConnectionResetError:
                print(f"[{timestamp()}] Koneksi {addr} terputus tiba-tiba.")
            finally:
                
                conn.close()
                print(f"[{timestamp()}] Koneksi dengan {addr} ditutup.\n")
    except KeyboardInterrupt:
        print("\nServer dihentikan (Ctrl+C).")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()