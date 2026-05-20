import socket
import termcolor

def run_player():
    HOST = '127.0.0.1'
    PORT = 9999

    # Creamos el socket TCP para el cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectamos al servidor del juego
        client_socket.connect((HOST, PORT))
        print("==================================================")
        termcolor.cprint(" Connected to the Guess the Number Game Server!", "cyan", attrs=["bold"])
        print("==================================================")
        print("Guess a number between 1 and 100.\n")

        while True:
            # Pedimos el número al usuario por consola
            user_input = input("Enter your guess: ").strip()

            if not user_input:
                continue

            # Enviamos el número al servidor
            client_socket.sendall(user_input.encode('utf-8'))

            # Recibimos la pista o respuesta del servidor
            response = client_socket.recv(1024).decode('utf-8')

            # Analizamos la respuesta para pintarla de colores interactivos
            if "You won" in response:
                termcolor.cprint(f"\n🎉 {response} 🎉", "green", attrs=["bold", "blink"])
                break  # El juego ha terminado, salimos del bucle
            elif response == "Higher":
                termcolor.cprint(f"📈 Hint: {response}! (Try a larger number)", "yellow")
            elif response == "Lower":
                termcolor.cprint(f"📉 Hint: {response}! (Try a smaller number)", "blue")
            else:
                # Por si llega el mensaje de error de formato del servidor
                termcolor.cprint(response, "red")

    except ConnectionRefusedError:
        termcolor.cprint("[ERROR] Could not connect to the server. Is Game.py running?", "red", attrs=["bold"])
    except Exception as e:
        termcolor.cprint(f"[ERROR] An unexpected error occurred: {e}", "red")
    finally:
        # Cerramos el socket del cliente al terminar
        client_socket.close()
        print("\nThank you for playing! Connection closed.")

if __name__ == "__main__":
    run_player()