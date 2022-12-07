def pi(filename: str) -> list:
    print(filename)
    with open(filename, "r") as f:
        return f.readlines()