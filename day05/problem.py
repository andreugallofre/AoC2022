import re

def parse_problem_input(problem_input: list) -> list:
    no_element = int(len(problem_input[0])/4)
    stacks = [[] for _ in range(no_element)]

    for line in problem_input:
        for i in range(no_element):
            if line.startswith(" 1"):
                for i in range(no_element):
                    stacks[i].reverse()
                return stacks
            if line[i*4:i*4+4].strip():
                stacks[i].append(line[i*4+1:i*4+2])

    return stacks


def parse_moves(problem_input: list) -> list:
    moves = []
    for line in problem_input:
        if line.startswith("move"):
            nums = re.findall('[0-9]+', line)
            moves.append({"quantity": int(nums[0]) , "from": int(nums[1])-1, "to": int(nums[2])-1})
    return moves


def solve_stack(stacks: list, moves: list, problem2: bool = False) -> str:
    for move in moves:
        aux_stack = []
        for _ in range(move["quantity"]):
            aux_stack.append(stacks[move["from"]].pop())

        if problem2:
            aux_stack.reverse()
        stacks[move["to"]].extend(aux_stack)

    res = ""
    for stack in stacks:
        res += stack[-1]

    return res


def part_one(problem_input: list) -> int:
    stacks = parse_problem_input(problem_input)
    moves = parse_moves(problem_input)

    res = solve_stack(stacks, moves)

    return res


def part_two(problem_input: list) -> int:
    stacks = parse_problem_input(problem_input)
    moves = parse_moves(problem_input)

    res = solve_stack(stacks, moves, True)
    return res
