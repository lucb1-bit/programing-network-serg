import socket
import random

class NumberGuesser:
    def __init__(self):
        # Selecciona un número aleatorio entre 1 y 100
        self.secret_number = random.randint(1, 100)
        # Inicializa la lista de intentos hechos por el jugador
        self.attempts = []

    def guess(self, number):
        # Añadimos el intento actual a la lista
        self.attempts.append(number)
        x = len(self.attempts)  # Total de intentos realizados

        if number == self.secret_number:
            return f"You won after {x} attempts"
        elif number > self.secret_number:
            return "Lower"
        else:
            return "Higher"


def run_server():
    # Configuración del servidor de Sockets
    HOST = '127.0.0.1'  # Localhost
    PORT = 9999  # Puerto para el juego

    # Creamos el socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))# conectamos el socket al puerto
    server_socket.listen(1) # escucha el socket al puerto

    print(f"[SERVER] Game Server is running on {HOST}:{PORT}. Waiting for a player...")

    while True:
        # Aceptamos la conexión del jugador
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Player connected from {client_address}")

        # Instanciamos la clase que controla el juego de ESTE jugador
        game = NumberGuesser()
        # Línea de depuración opcional (por si quieres saber el número en la consola del servidor)
        print(f"[SERVER] Secret number generated for this game: {game.secret_number}")

        try:
            while True:
                # Recibimos el número del cliente (en bytes) y lo decodificamos
                data = client_socket.recv(1024).decode('utf-8')# recivimos del cliente
                if not data:
                    break  # Si el cliente se desconecta abruptamente, salimos del bucle

                try:
                    player_guess = int(data)
                    # Ejecutamos el método guess de nuestra clase
                    hint = game.guess(player_guess)

                    # Enviamos la respuesta de vuelta al jugador
                    client_socket.sendall(hint.encode('utf-8'))

                    # Si el mensaje contiene "You won", el juego para este cliente ha terminado
                    if "You won" in hint:
                        print(f"[SERVER] Player {client_address} guessed correctly. Ending game.")
                        break
                except ValueError:
                    client_socket.sendall("Error: Please send a valid integer.".encode('utf-8'))

        except Exception as e:
            print(f"[SERVER] An error occurred with player {client_address}: {e}")
        finally:
            # Cerramos la conexión con el cliente de forma segura
            client_socket.close()
            print(f"[SERVER] Connection closed with {client_address}. Ready for a new game.")


if __name__ == "__main__":
    run_server()