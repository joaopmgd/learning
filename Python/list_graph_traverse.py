# Input:
# For a testcase, first line contains number of edges and
# next line contains N pairs of integers (X and Y each) where X Y means an edge from X to Y.
 
# Output:
# For each testcase, print the nodes while doing DFS starting from node 1.
 
# Example:
# Input:
# 4
# (1 2) (1 3) (1 4) (3 5)
 
# Output:
# 1 2 3 5 4

def create_graph(values):
    graph = dict()
    index = 0
    while index < len(values)-1:

        if values[index] in graph:
            graph[values[index]].append(values[index+1])
        else:
            graph[values[index]] = [values[index+1]]
        index+=2

    return graph

visited = []

def traverse(first, graph):
    print(first)
    visited.append(first)
    
    if first in graph:
        node = graph[first]
        for value in node:
            if value not in visited:
                traverse(value, graph)

input_value = [1, 2, 1, 3, 1, 4, 3, 5]
graph = create_graph(input_value)
traverse(input_value[0], graph)