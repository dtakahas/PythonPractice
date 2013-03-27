def convert_to_celsius(fahrenheit):
    '''(number) -> float

    Return the number of celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    '''
    return (fahrenheit - 32) * 5 / 9
