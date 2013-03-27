def egg_count(eggs):
    if eggs % 12 == 0:
        return False
    else:
        return True


def egg_count2(eggs):
    return not (eggs % 12 != 0)
