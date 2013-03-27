def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return len(dna1) > len(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    i = 0

    for char in dna:
        if char == nucleotide:
            i = i + 1
    return i
    


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna2 in dna1


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if DNA sequence dna does not contain any characters
    other than 'A', 'T', 'C' and 'G'.

    >>> is_valid_sequence('ATTCGA')
    True
    >>> is_valid_sequence('ATTFHGA')
    False
    >>> is_valid_sequence('aaTTGA')
    False
    '''
    i = 0
    for char in dna:
        if char in 'ATCG':
            i = i + 0
        else:
            i = i + 1
    return i == 0


def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str

    Return the DNA sequence obtained by inserting DNA sequence dna2 into
    DNA sequence dna1 at the specified index in dna1.

    Precondition: index is a valid index within dna1.

    >>> insert_sequence('ATTA', 'GG', 2)
    'ATGGTA'
    >>> insert_sequence('AAAAAAAA', 'GTGT', 4)
    'AAAAGTGTAAAA'
    '''
    i = dna1
    t = dna2
    return i[:index] + t + i[index:]


def get_complement(nucleotide):
    ''' (str) -> str

    Return the complement of the specified nucleotide.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('C')
    'G'
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'


def get_complementary_sequence(dna):
    ''' (str) -> str

    Return the complementary DNA sequence for the DNA sequence dna.

    >>> get_complementary_sequence('ATTA')
    'TAAT'
    >>> get_complementary_sequence('GCCGTA')
    'CGGCAT'
    '''
    i = ''
    for char in dna:
        i = i + get_complement(char)
    return i
    

