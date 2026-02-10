seq= input("Enter a sequence").upper()

def counter(seq):
    a,c,t,g=0,0,0,0
    for i in seq:
        if i == "A":
            a += 1
        if i == "C":
            c += 1
        if i == "T":
            t += 1
        if i == "G":
            g += 1
    return a,c,t,g

a,c,t,g = counter(seq)
print("Total length:",len(seq))
print("A:",a)
print("C:",c)
print("T:",t)
print("G:",g)

