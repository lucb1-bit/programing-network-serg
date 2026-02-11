dna = "ATGCGATCGATCGATCGATCGA"

def count_atc(seq):
    i = 0
    counter = 0
    while i < (len(seq)-3):
        if (seq[i] == "A") and (seq[i+1] == "T") and (seq[i+2] == "C"):
            counter +=1
        i +=1
    return counter

def replacement(seq):
    arn = seq.replace("T","U")
    return arn



print("The total length of the string",len(dna))
print("The first 5 characters",dna[0:5])
print("The last 3 characters",dna[-3:])
print("The string converted to lowercase",dna.lower())
print("the substring ""ATC"" appears",count_atc(dna) ,"times")
print("DNA to RNA transcription is:", replacement(dna))