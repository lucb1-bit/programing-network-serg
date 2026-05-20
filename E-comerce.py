import termcolor


# ==========================================
# PASO 1, 2 Y 3: CLASE PRODUCTO
# ==========================================
class Product:
    # Paso 1: Atributo de clase con valor por defecto
    name = "Tomato"

    # Paso 2: Constructor para inicializar los atributos de instancia
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Paso 3: Método de objeto para formatear la información
    def get_information(self):
        return f"Product: {self.name} | Price: {self.price}"


# ==========================================
# PASO 4: CLASE CLIENTE (BASE)
# ==========================================
class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []  # Lista vacía que actuará como carrito de la compra

    def add_to_cart(self, product_object):
        # Añade el objeto Producto a la lista del carrito
        self.cart.append(product_object)

    def compute_total(self):
        # Suma el precio de todos los objetos Producto que haya en el carrito
        total = 0
        for i in self.cart:
            total += i.price
        return total


# ==========================================
# PASO 5: CLASE CLIENTE VIP (HERENCIA Y POLIMORFISMO)
# ==========================================
# Al poner (Client) entre paréntesis, VIPClient hereda todos sus atributos y métodos
class VIPClient(Client):
    def __init__(self, name, email, discount):
        # super().__init__ llama al constructor del padre (Client) para no repetir código
        super().__init__(name, email)
        self.discount = discount  # Atributo extra exclusivo del cliente VIP (ej: 20)

    # POLIMORFISMO: Reescribimos el método compute_total para aplicar el descuento
    def compute_total(self):
        # Calculamos primero el total normal usando el método del padre
        total_original = super().compute_total()
        # Aplicamos la fórmula del descuento matemático: Total * (1 - Desc/100)
        total_con_descuento = total_original * (1 - self.discount / 100)
        # Lo convertimos a entero o flotante según necesitemos (el output espera 1032)
        return int(total_con_descuento)


# ==========================================
# PROGRAMA PRINCIPAL (DEMOSTRACIÓN DE TODOS LOS PASOS)
# ==========================================
if __name__ == "__main__":
    print("--- PASO 2 & 3: Creación y visualización de productos ---")
    # Instanciamos los tres productos exigidos
    p1 = Product("Laptop", 1200)
    p2 = Product("Chair", 90)
    p3 = Product("Scarf", 24)

    # Probamos el método del paso 3
    print(p1.get_information())
    print(p2.get_information())
    print(p3.get_information())
    print("-" * 50)

    print("--- PASO 4 & 5: Simulación del E-Commerce ---")
    # Alice es una cliente VIP con un 20% de descuento (Paso 5)
    alice = VIPClient("Alice", "alice@email.com", discount=20)
    # Paul es un cliente normal de toda la vida (Paso 4)
    paul = Client("Paul", "paul@email.com")

    # Llenamos el carrito de Alice (Laptop + Chair = 1290 -> Con 20% de desc = 1032)
    alice.add_to_cart(p1)
    alice.add_to_cart(p2)

    # Llenamos el carrito de Paul (Chair + Scarf = 90 + 24 = 114)
    paul.add_to_cart(p2)
    paul.add_to_cart(p3)

    # Mostramos los resultados finales por terminal tal y como los pide el enunciado
    termcolor.cprint(f"Customer (VIP): {alice.name}", "yellow", attrs=["bold"])
    print(f"Total to pay: {alice.compute_total()}")

    termcolor.cprint(f"Customer: {paul.name}", "cyan", attrs=["bold"])
    print(f"Total to pay: {paul.compute_total()}")