import math, copy


def calc_tail_pos(head: list, tail: list) -> None:
    distance = math.dist(head, tail)
    if distance >= 2:
        if head[0] == tail[0]:
            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1
        elif head[1] == tail[1]:
            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1

        elif head[0] > tail[0] and head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1

        elif head[0] > tail[0] and head[1] < tail[1]:
            tail[0] += 1
            tail[1] -= 1

        elif head[0] < tail[0] and head[1] > tail[1]:
            tail[0] -= 1
            tail[1] += 1

        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -= 1
            tail[1] -= 1

    return tail


def update_tails(rope: list, visited: list) -> None:
    for i in range(1, len(rope)):
        rope[i] = calc_tail_pos(rope[i - 1], rope[i])
        visited[i-1].append(tuple(rope[i]))


def calculate_movements(problem_input: list, visited: list) -> list:
    rope = [[0, 0],[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

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
