import socket

HOST = "127.0.0.1"
PORT = 5000


def main():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        
        client_socket.connect((HOST, PORT))
        print(f"Terhubung ke server {HOST}:{PORT}")
        print("Ketik pesan lalu tekan Enter. Ketik 'exit' untuk keluar.\n")

        
        while True:
            message = input("Anda: ")

            if message.lower() == "exit":
                break
            if not message.strip():
                continue

            
            client_socket.sendall(message.encode("utf-8"))

            
            response = client_socket.recv(1024)
            if not response:
                print("Server menutup koneksi.")
                break
            print(f"Server: {response.decode('utf-8')}")

    except ConnectionRefusedError:
        print("Gagal terhubung. Pastikan server.py sudah dijalankan.")
    except (ConnectionResetError, BrokenPipeError):
        print("Koneksi ke server terputus.")
    finally:
        
        client_socket.close()
        print("Koneksi ditutup.")


if __name__ == "__main__":
    main()