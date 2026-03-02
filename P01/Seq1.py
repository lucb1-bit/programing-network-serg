class Seq:

    def __init__(self, bases):
        if self.is_valid(bases) == True:
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.bases

    def len(self):
        return len(self.bases)

    def is_valid(self, bases):
        valid_bases = {'A', 'C', 'G', 'T'}
        result = 0
        for b in bases:
            if b in valid_bases:
                result = 0
            else:
                result +=1

        if result == 0:
            return True
        else:
            return False



