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

    def count_base(self,bases):
        A, C, T, G = 0,0,0,0
        if bases == "NULL" or bases == "Invalid Sequence":
            A,C,T,G = 0,0,0,0
        else:
            for b in self.bases:
                if b == "A":
                    A += 1
                elif b == "C":
                    C += 1
                elif b == "T":
                    T += 1
                elif b == "G":
                    G += 1
        return "A:", A, "C:", C, "T:", T, "G:", G

    def count(self):
        bases_dict = {'A':0, 'C':0, 'T':0, 'G':0}
        if self.bases == "NULL" or self.bases == "Invalid Sequence":
            bases_dict = {'A':0, 'C':0, 'T':0, 'G':0}
        else:
            for b in self.bases:
                if b in bases_dict:
                    bases_dict[b] += 1
        return bases_dict