def get_negative_nonnegative_lists(L):

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)

    return (neg, nonneg)
