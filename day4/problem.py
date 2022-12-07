from interval import interval

def aux_func_p1(problem_input: list) -> int:
    score = 0
    for element in problem_input:
        intervals = parse_line(element)
        if intervals[0] in intervals[1] or intervals[1] in intervals[0]:
            score += 1
    return score


def aux_func_p2(problem_input: list) -> int:
    score = 0
    for element in problem_input:
        intervals = parse_line(element)
        if intervals[0] & intervals[1]:
            score += 1
    return score


def parse_line(line: str) -> list:
    intervals = []
    for element in line.split(","):
        intervals.append(
                interval[int(element[0:element.index("-")]),
                int(element[element.index("-")+1::])]
                )
    return intervals


def part_one(problem_input: list) -> int:
    game_score = aux_func_p1(problem_input)
    return game_score


def part_two(problem_input: list) -> int:
    game_score = aux_func_p2(problem_input)
    return game_score
