def count_bases(seq):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0, }

    for base in seq:
        if base in bases:
            bases[base] +=1
    return bases


if __name__ =="__main__":
    seq= input("Enter a sequence").upper()
    print("Total length:",len(seq))

    result = count_bases(seq)

    for base,count in bases.items():
        print(f'{base}: {count}')