def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item into the last position.

    Precondition: len(L) >= 1
    '''

    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item

def shift_right(L):

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item
    

def count_adjacent_repeats(s):
    '''(str) -> int

    Return the number of occurences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats

