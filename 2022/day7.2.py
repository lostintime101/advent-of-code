with open("day7_input.txt", "r") as lines:

    directory = {"/": {"children": [], "parent": None, "weights": []}}


    def get_fullname(name, parent):
        return f"{parent if parent != '/' else ''}/{name}"


    def add_directory(name, parent, directory):
        fullname = get_fullname(name, parent)
        directory[fullname] = {"children": [], "parent": parent, "weights": []}
        directory[parent]["children"].append(fullname)


    for idx, line in enumerate(lines):
        if "$ cd" in line:
            target = line.split()[-1]
            if target == "..":
                cwd = directory[cwd]["parent"]
            elif target == "/":
                cwd = "/"
            else:
                cwd = get_fullname(target, cwd)
        if line[0] != "$":
            metadata, name = line.split()
            if metadata == "dir":
                if name not in directory:
                    add_directory(name, cwd, directory)
            else:
                directory[cwd]["weights"].append(int(metadata))
    weights = {}


    def calculate_weights(node):
        if node not in weights:
            weights[node] = sum(directory[node]["weights"]) + sum(
                calculate_weights(node) for node in directory[node]["children"]
            )
        return weights[node]

    calculate_weights("/")
    print(sum(weight for weight in weights.values() if weight <= 100_000))

    to_free = weights["/"] - 40_000_000
    print(to_free, "to_free")
    print(min(weight for weight in weights.values() if weight >= to_free))