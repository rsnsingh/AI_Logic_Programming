mca_graph = {'A': ['B', 'C'], 'B':['D','E'], 'C':['F','G'], 'D':[], 'E':[],'F':[],'G':[]}

def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        print(" Stack ")
        print(stack)
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

            if node == goal:
                print(" Goal Reached "+node)
                return
            for n1 in graph[node]:
                if n1 not in visited:
                    stack.append(n1)
                    print(" Visit " + n1,graph[node])

dfs(mca_graph,'A','E')

