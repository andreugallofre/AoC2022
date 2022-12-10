from utils import parse_input
from day10 import problem

def main():
    in_lines = parse_input.pi("day10/input.txt")
    print(problem.part_one(in_lines))
    print(problem.part_two(in_lines))

if __name__ == "__main__":
    main()
