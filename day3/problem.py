def repeated_elements(problem_input: list) -> int:
    score = 0
    for line in problem_input:
        score += calculate_error(line)

    return score


def repeated_elements2(problem_input: list) -> int:
    score = 0
    chunks = [problem_input[x:x+3] for x in range(0, len(problem_input), 3)]
    for chunk in chunks:
        score += calculate_error2(chunk)

    return score


def calculate_error2(elves: list) -> int:
    duplicated = list(set(elves[0])&set(elves[1])&set(elves[2]))[0]

    if duplicated.islower():
        return ord(duplicated)-ord('a')+1

    return ord(duplicated)-ord('A')+27


def calculate_error(line: str) -> int:
    elements = len(line)-1
    pocket_a = [*line[0:int(elements/2)]]
    pocket_b = [*line[int(elements/2):len(line)-1]]

    duplicated = list(set(pocket_a)&set(pocket_b))[0]

    if duplicated.islower():
        return ord(duplicated)-ord('a')+1

    return ord(duplicated)-ord('A')+27


def part_one(problem_input: list) -> int:
    res = repeated_elements(problem_input)
    return res


def part_two(problem_input: list) -> int:
    res = repeated_elements2(problem_input)
    return res
