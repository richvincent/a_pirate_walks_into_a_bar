def answer(numbers):
    try:
        startPosition = numbers.index(0)
    except ValueError:
        startPosition = numbers.index(min(numbers))

    loop = []
    backHome = False
    nextPosition = startPosition + 1

    if len(numbers) == 2:
        return 2
    else:
        while backHome is False:
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

                if nextPosition == startPosition:
                    if len(loop) == 1:
                        return 2
                    else:
                        return len(loop)
