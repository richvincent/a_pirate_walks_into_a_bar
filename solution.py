def answer(numbers):
    if isinstance(numbers, list):
        loop = list(set(numbers))
        if len(loop) < 5000:
            if len(loop) > 2:
                if loop[0] == 0:
                    return len(loop) - 1
            elif len(loop) == 2:
                return 2
        else:
            raise ValueError('Please no less than 2 and\
            no more than 5000 pirates')
    else:
        raise ValueError('Please supply a list')


assert (answer([1, 3, 0, 1]) == 2)
assert (answer([1, 0]) == 2)
assert (answer([1, 2, 1]) == 2)
