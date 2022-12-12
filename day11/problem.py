import re

class Monkey:

    def __init__(self, starting_items: list, operation: str, test: int, true_con: int, false_con: int):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.true_con = true_con
        self.false_con = false_con
        self.inspected_items = 0


    def process_operation(self, item: int) -> int:
        operation_tokens = self.operation
        first_op = 0
        second_op = 0

        ops = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,}

        if operation_tokens[0] == "old":
            first_op = item
        else:
            first_op = int(operation_tokens[0])
        if operation_tokens[2] == "old":
            second_op = item
        else:
            second_op = int(operation_tokens[2])

        return ops[operation_tokens[1]](first_op, second_op)


    def process_round(self, round2=False) -> list:
        items = []
        for item in self.items:
            if round2:
                # Mod least common multiple of input Monkeys
                worry = int(self.process_operation(int(item))%9699690)
            else:
                worry = int(self.process_operation(int(item))/3)

            if worry%self.test == 0:
                items.append((worry, self.true_con))
            else:
                items.append((worry, self.false_con))

            self.inspected_items += 1

        self.items = []
        return items


def parse_monkey(monkey_input: list) -> Monkey:
    starting_items = re.findall('[0-9]+', monkey_input[1])
    operation = monkey_input[2].strip().split(" new = ")[1].split(" ")
    test = int(re.findall('[0-9]+', monkey_input[3])[0])
    true_con = int(re.findall('[0-9]+', monkey_input[4])[0])
    false_con = int(re.findall('[0-9]+', monkey_input[5])[0])
    return Monkey(starting_items, operation, test, true_con, false_con)


def part_one(problem_input: list) -> int:
    monkeys = []
    for i in range(0, len(problem_input), 7):
        monkeys.append(parse_monkey(problem_input[i:i+7]))

    for i in range(20):
        for monkey in monkeys:
            changes = monkey.process_round()
            for change in changes:
                monkeys[change[1]].items.append(change[0])

    res = []
    for monkey in monkeys:
        res.append(monkey.inspected_items)

    res.sort(reverse=True)
    result = res[0]*res[1]

    return result


def part_two(problem_input: list) -> None:
    monkeys = []
    for i in range(0, len(problem_input), 7):
        monkeys.append(parse_monkey(problem_input[i:i+7]))

    for i in range(10000):
        for monkey in monkeys:
            changes = monkey.process_round(True)
            for change in changes:
                monkeys[change[1]].items.append(change[0])

    res = []
    for monkey in monkeys:
        res.append(monkey.inspected_items)

    res.sort(reverse=True)
    result = res[0]*res[1]

    return result