class Seq:

    def __init__(self, bases=None):
        if bases == None:
            self.bases = "NULL"
            print(" NULL sequence created!")
        else:
            isvalid = self.is_valid(bases)
            if isvalid == True:
                self.bases = bases
                print("New sequence created!")
            elif isvalid == False:
                self.bases = "Invalid Sequence"
                print("INCORRECT Sequence detected")

    def __str__(self):
        return self.bases

    def len(self):
        if (self.bases == "NULL") or (self.bases == "Invalid Sequence"):
            return 0
        else:
            return len(self.bases)

    def is_valid(self, bases):
        valid_bases = {'A', 'C', 'G', 'T'}
        for b in bases:
            if b not in valid_bases:
                return False
        return True

def count_base(self, base)