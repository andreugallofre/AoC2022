def calculate_movements(problem_input: list) -> list:
    actions = [0]
    for line in problem_input:
        tokens = line.split(" ")
        if tokens[0] == "addx":
            actions.append(0)
            actions.append(int(tokens[1]))
        else:
            actions.append(0)

    return actions


def cycle_result(actions: list) -> int:
    regx = 1
    res = []
    cycles = [20, 60, 100, 140, 180, 220]

    for i in range(240):
        regx += int(actions[i])
        if i + 1 in cycles:
            res.append(regx * (i + 1))

    return sum(res)


def crt_visualization(actions: list) -> None:
    regx = 1

    for i in range(6):
        for j in range(1, 41):
            pos = i * 40 + j
            if regx <= j < regx + 3:
                print("#", end="")
            else:
                print(".", end="")
            regx += int(actions[pos])

        print()


def part_one(problem_input: list) -> int:
    actions = calculate_movements(problem_input)
    res = cycle_result(actions)
    return res


def part_two(problem_input: list) -> None:
    actions = calculate_movements(problem_input)
    crt_visualization(actions)
