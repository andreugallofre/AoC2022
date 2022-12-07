def solve(problem_input: str, number: int) -> int:
    for i in range(0, len(problem_input)):
        if len(set(problem_input[i:i+number])) == number:
            return i+number

    return 0


def part_one(problem_input: list) -> int:
    res = solve(problem_input[0], 4)
    return res


def part_two(problem_input: list) -> int:
    res = solve(problem_input[0], 14)
    return res
