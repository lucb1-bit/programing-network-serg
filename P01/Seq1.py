from fileinput import filename


class Seq:

    def __init__(self, bases=None):
        if bases == None:
            self.bases = "NULL"
            print("NULL sequence created!")
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

    def countB(self):
        bases_dict = {'A':0, 'C':0, 'T':0, 'G':0}
        if self.bases == "NULL" or self.bases == "Invalid Sequence":
            bases_dict = {'A':0, 'C':0, 'T':0, 'G':0}
        else:
            for b in self.bases:
                if b in bases_dict:
                    bases_dict[b] += 1
        return bases_dict

    def reverse(self):
        reverse = ""
        if self.bases == "NULL" or self.bases == "Invalid Sequence":
            return self.bases
        else:
            reverse = ""
            for b in self.bases:
                reverse = b + reverse
            return reverse


    def seq_complement(self):
        base_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        replaced_seq = ""
        if self.bases == "NULL" or self.bases == "Invalid Sequence":
            return self.bases
        else:
            for b in self.bases:
                if b in base_dict:
                    replaced_seq += base_dict[b]
            return replaced_seq

    def seq_read_fasta(self,filename):
        filename = open(filename, "r")
        lines = filename.readlines()
        filename.close()

        seq_lines = lines[1:]
        sequence = ""
        for line in seq_lines:
            sequence += line.strip()
        self.bases = sequence


    def most_freq(self):
        freq = self.countB()
        most_dict = {}
        most = 0
        for f in freq:
            if freq[f] > most:
                most = freq[f]
                bs = f
                most_dict = {bs: most}
            elif freq[f] == most:
                most_dict[f] = most
        return "Most frequent base: ", most_dict