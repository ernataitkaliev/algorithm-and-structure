# Task 17. Generate All Permutations
def permute(prefix, rest):
    if rest == "":
        print(prefix)
        return
    for i in range(len(rest)):
        permute(prefix + rest[i], rest[:i] + rest[i+1:])

permute("", "ABC")
