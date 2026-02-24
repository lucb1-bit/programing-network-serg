# S06/e1.py
class Seq:
    def __init__(self, strbases):
        # Definimos las bases válidas
        valid_bases = ['A', 'C', 'G', 'T']
        is_valid = True

        # Comprobamos cada letra
        for base in strbases:
            if base not in valid_bases:
                is_valid = False
                break

        if is_valid:
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("ERROR!! INCORRECT Sequence detected")

    def __str__(self):
        return self.strbases


# Prueba
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")