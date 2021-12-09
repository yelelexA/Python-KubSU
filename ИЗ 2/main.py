# 9
# alexei peter_1
# anna peter_1
# elizabeth peter_1
# peter_2 alexei
# peter_3 anna
# paul_1 peter_3
# alexander_1 paul_1
# nicholaus_1 paul_1

def height(man):
    if man not in family_tree:
        return 0
    else:
        return 1 + height(family_tree[man])

def LCA(child1,child2):
    h1 = height(child1)
    h2 = height(child2)

    while h1 != h2:
        if h1 > h2:
            child1 = family_tree[child1]
            h1 -= 1
        else:
            child2 = family_tree[child2]
            h2 -= 1

    while child1 != child2:
        child1 = family_tree[child1]
        child2 = family_tree[child2]

    return child1

family_tree = dict()
n = int(input())

for i in range(n - 1):
    child, parent = input().split()
    family_tree[child] = parent

child1, child2 = input("\nВведите два потомка через пробел:").split()
print("\nНаименьший общий предок (Lowest common ancestor - LCA):",LCA(child1,child2))

