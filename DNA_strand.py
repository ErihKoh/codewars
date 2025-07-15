def DNA_strand(dna: str):
    dna_list = []
    for d in dna:
        if d == 'T':
            dna_list.append('A')
        elif d == 'A':
            dna_list.append('T')
        elif d == 'C':
            dna_list.append('G')
        elif d == 'G':
            dna_list.append('C')
    return ''.join(dna_list)


def DNA_strand_1(dna):
    reference = {"A": "T",
                 "T": "A",
                 "C": "G",
                 "G": "C"
                 }
    return "".join([reference[x] for x in dna])


if __name__ == '__main__':
    dna = 'ATTGC'
    print(DNA_strand(dna))
