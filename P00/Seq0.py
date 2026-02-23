def seq_ping():
    print("OK")

def seq_read_fasta(file):
    file = open(file, "r")
    lines = file.readlines()
    file.close()

    seq_lines = lines[1:]
    sequence = ""
    for line in seq_lines:
        sequence += line.strip()

    return sequence

def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    count = 0

    for l in seq:
        if l == base:
            count += 1

    return count


def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    for l in seq:
        if l in d:
            d[l] += 1
    return d


def seq_reverse(seq, n):
    fragment = seq[:n]
    reverse = ""
    for base in fragment:
        reverse = base + reverse
    return reverse


def seq_complement(seq):
    base_dict = {'A': 'T','T': 'A','C': 'G','G': 'C'}
    replaced_seq = ""
    for base in seq:
        if base in base_dict:
            replaced_seq += base_dict[base]
    return replaced_seq


def most_freq(seq):
    freq = seq_count(seq)
    most_dict = {}
    most = 0
    for f in freq:
        if freq[f] > most:
            most = freq[f]
            bs = f
            most_dict = {bs:most}
        elif freq[f] == most:
            most_dict[f] = most
    return most_dict

    return most, l
