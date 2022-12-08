def parse_problem_input(problem_input: list):

    columns = [[] for i in range(len(problem_input[0]) - 1)]
    rows = []
    for i, line in enumerate(problem_input):
        line = line[:-1]
        rows.append([*line])
        for j in range(len(line)):
            columns[j].append(line[j])

    return rows, columns


def calculate_visible_trees(rows: list, columns: list) -> int:
    res = len(rows) * 4 - 4  # External trees

    # Internal trees
    for i in range(1, len(rows) - 1):
        for j in range(1, len(columns) - 1):
            right = rows[i][0:j]
            left = rows[i][j + 1 : :]
            top = columns[j][0:i]
            down = columns[j][i + 1 : :]

            if (
                max(right) < rows[i][j]
                or max(left) < rows[i][j]
                or max(top) < rows[i][j]
                or max(down) < rows[i][j]
            ):
                res += 1

    return res


def check_offending_tree(neighbors: list, current_tree: str, reverse: bool) -> int:
    if reverse:
        neighbors.reverse()

    for i, element in enumerate(neighbors):
        if element >= current_tree:
            return i + 1

    return 0


def calculate_best_location(rows: list, columns: list) -> int:
    res = 0

    # Internal trees
    for i in range(1, len(rows) - 1):
        for j in range(1, len(columns) - 1):
            right = rows[i][0:j]
            left = rows[i][j + 1 : :]
            top = columns[j][0:i]
            down = columns[j][i + 1 : :]

            current_tree = rows[i][j]

            if max(right) < rows[i][j]:
                r_mult = len(right)
            else:
                r_mult = check_offending_tree(right, current_tree, True)
            if max(left) < rows[i][j]:
                l_mult = len(left)
            else:
                l_mult = check_offending_tree(left, current_tree, False)
            if max(top) < rows[i][j]:
                u_mult = len(top)
            else:
                u_mult = check_offending_tree(top, current_tree, True)
            if max(down) < rows[i][j]:
                d_mult = len(down)
            else:
                d_mult = check_offending_tree(down, current_tree, False)

            res = max(res, r_mult * l_mult * u_mult * d_mult)

    return res


def part_one(problem_input: list) -> int:
    rows, columns = parse_problem_input(problem_input)
    res = calculate_visible_trees(rows, columns)
    return res


def part_two(problem_input: list) -> int:
    rows, columns = parse_problem_input(problem_input)
    res = calculate_best_location(rows, columns)
    return res
