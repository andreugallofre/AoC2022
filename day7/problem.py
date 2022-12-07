from anytree import Node, RenderTree, Resolver, PreOrderIter


def parse_problem_input(problem_input: list) -> Node:
    dir_tree = Node("/", type="dir", size=0)
    parent = dir_tree

    for line in problem_input[1::]:
        line =  line.strip()
        if line.startswith("$ ls"):
            continue
        if line.startswith("$ cd"):
            if line == "$ cd ..":
                parent = parent.parent
            else:
                tokens = line.split(" ")
                resolver = Resolver("name")
                parent = resolver.get(parent, tokens[2])
        elif line.startswith("dir"):
            Node(line[4:], parent=parent, type="dir", size=0)
        else:
            elements = line.split(" ")
            Node(elements[1], parent=parent, type="file", size=elements[0])

    return dir_tree


def calc_dir_size(node: Node) -> int:
    dir_size = 0
    for tree_node in PreOrderIter(node):
        if tree_node.type == "file":
            dir_size += int(tree_node.size)

    return dir_size



def part_one(problem_input: list) -> int:
    dir_tree = parse_problem_input(problem_input)
    res = 0
    for node in PreOrderIter(dir_tree):
        if node.type == "dir":
            size = calc_dir_size(node)
            if size <= 100000:
                res += size

    # Tree visualization
    for pre, _, node in RenderTree(dir_tree):
        print(f"{pre}{node.name} {node.type} {node.size}")

    return res


def part_two(problem_input: list) -> int:
    dir_tree = parse_problem_input(problem_input)
    res_size = 70000000
    need_size = 30000000
    used_size = calc_dir_size(dir_tree)
    free_space = res_size - used_size

    print(used_size, free_space)

    for node in PreOrderIter(dir_tree):
        if node.type == "dir":
            size = calc_dir_size(node)
            if size + free_space > need_size and size < res_size:
                res_size = size

    return res_size
