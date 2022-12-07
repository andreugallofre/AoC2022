def aux_func_p1(problem_input: list) -> int:
    score = 0
    for element in problem_input:
        fig = convert_figure(element[2])
        score += score_round(element[0], fig)
    return score

def aux_func_p2(problem_input: list) -> int:
    score = 0
    for element in problem_input:
        fig = calculate_figure(element[0], element[2])
        score += score_round(element[0], fig)
    return score


def convert_figure(move: str) -> str:
    move = "A" if move == "X" else "B" if move == "Y" else "C"
    return move


def score_round(opo: str, move: str)-> int:
    if move == opo:
        return ord(move) - ord('A')+1+3
    if move == "A" and opo == "C" or move == "B" and opo == "A":
        return ord(move) - ord('A')+1+6
    if move == "C" and opo == "B":
        return ord(move) - ord('A')+1+6

    return ord(move) - ord('A')+1


def calculate_figure(opo: str, res: str):
    if opo == "A":
        fig = "B" if res == "Z" else "A" if res == "Y" else "C"
    elif opo == "B":
        fig = "C" if res == "Z" else "B" if res == "Y" else "A"
    else:
        fig = "A" if res == "Z" else "C" if res == "Y" else "B"

    return fig


def part_one(problem_input: list) -> int:
    game_score = aux_func_p1(problem_input)
    return game_score


def part_two(problem_input: list) -> int:
    game_score = aux_func_p2(problem_input)
    return game_score
