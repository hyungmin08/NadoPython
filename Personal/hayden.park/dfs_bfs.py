my_graph = {
    '1':['2','3'],
    '2':['1','4','5'],
    '3':['1','6'],
    '4':['2'],
    '5':['2','7'],
    '6':['3'],
    '7':['5']
}

def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)
    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    
    print ('dfs - ',visited)

dfs(my_graph,'2')


def bfs(graph, start_node):
    visited=list()
    queue=list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    print ('bfs - ', visited)

bfs(my_graph, '2')