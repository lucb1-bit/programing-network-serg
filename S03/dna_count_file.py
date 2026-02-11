from dna_count_2form import count_bases

#lines= ["AGTACACTGGT","ACCAGTGTACT","ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG "]
#print("Total length:",len())

if __name__ == "__main__":
#option 1
    f = open("dna.txt","r")
    lines = f.readlines()
    f.close()

#option 2
    with open("dna.txt","r") as f:
        lines = f.readlines()


    total_number = 0
    bases = {"A":0,"C":0,"T":0,"G":0,}


    for sequence in lines:
        sequence= sequence.strip() #Remove spaces and newline characters at the end of the string
        total_number += len(sequence)
        result = count_bases(sequence)
        for key in result:
            bases[key] += result[key]

    print("Total number of bases:",total_number)

    for base,count in bases.items():
        print(f'{base}: {count}')