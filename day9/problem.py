import math


def calc_tail_pos(head: list, tail: list) -> None:
    distance = math.dist(head, tail)

    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]

    if distance >= 2:
        tail[0] += diff_x / abs(diff_x) if diff_x != 0 else 0
        tail[1] += diff_y / abs(diff_y) if diff_y != 0 else 0

    return tail


def update_tails(rope: list, visited: list) -> None:
    for i in range(1, len(rope)):
        rope[i] = calc_tail_pos(rope[i - 1], rope[i])
        visited[i - 1].append(tuple(rope[i]))


def calculate_movements(problem_input: list, visited: list) -> list:
    rope = [[0, 0] for _ in range(10)]

    for move in problem_input:
        mov = move.split(" ")
        positions = int(mov[1])
        if mov[0] == "R":
            for _ in range(positions):
                rope[0][1] += 1
                update_tails(rope, visited)

        if mov[0] == "L":
            for _ in range(positions):
                rope[0][1] -= 1
                update_tails(rope, visited)

        if mov[0] == "U":
            for _ in range(positions):
                rope[0][0] -= 1
                update_tails(rope, visited)

        if mov[0] == "D":
            for _ in range(positions):
                rope[0][0] += 1
                update_tails(rope, visited)


def part_one(problem_input: list) -> int:
    visited = [[] for _ in range(9)]
    calculate_movements(problem_input, visited)
    return len(set(visited[0]))


def part_two(problem_input: list) -> int:
    visited = [[] for _ in range(9)]
    calculate_movements(problem_input, visited)

    return len(set(visited[8]))
