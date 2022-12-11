def aux_func(problem_input: list) -> list:
    curr = 0
    elfs = []
    for elf in problem_input:
        elf = elf.strip()
        if elf:
            curr += int(elf)
        else:
            elfs.append(curr)
            curr = 0

    elfs.append(curr)

    return elfs


def part_one(problem_input: list) -> int:
    elfs = aux_func(problem_input)
    return max(elfs)


def part_two(problem_input: list) -> int:
    elfs = aux_func(problem_input)
    elfs.sort(reverse=True)
    return sum(elfs[:3])
