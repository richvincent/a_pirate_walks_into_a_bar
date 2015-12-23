def answer(numbers):
    try:
        startPosition = numbers.index(0)
    except ValueError:
        startPosition = numbers.index(min(numbers))

    loop = []
    nextPosition = startPosition + 1

    if len(numbers) <= 2:
        return 2
    else:
        while nextPosition != startPosition:
                try:
                    numbers[nextPosition]
                    try:
                        loop.index(numbers[nextPosition])
                    except ValueError:
                        if numbers[nextPosition] != 0:
                            loop.append(numbers[nextPosition])
                    nextPosition += 1

                except IndexError:
                    nextPosition = 0
        return len(loop)

assert (answer([1, 3, 0, 1]) == 2)
assert (answer([1, 0]) == 2)
assert (answer([1, 2, 1]) == 2)
