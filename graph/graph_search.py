## BREADTH FIRST SEARCH
def bfs(graph, first_node):
    """Breadh first search iterative
    
    Parameters
    ----------
    graph: dictionary of nodes
        {node: list of adjacent nodes, ...}
    first_node: initial node to start the search
    
    Return
    ------
    output: output of search as a list of nodes"""
    # data structures
    queue = []
    visited = set()
    output = []

    # first node
    current = first_node
    queue.append(current)
    visited.add(current)
    output.append(current)

    # graph search
    while queue:
        # get first node in queue
        current = queue.pop(0)

        for node in graph[current]:
            if not node in visited:
                queue.append(node)
                visited.add(node)
                output.append(node)

    return output

## DEPTH FIRST SEARCH
def dfs(graph, first_node):
    """Depth first search iterative
    
    Parameters
    ----------
    graph: dictionary of nodes
        {node: list of adjacent nodes, ...}
    first_node: initial node to start the search
    
    Return
    ------
    output: output of search as a list of nodes"""
    # data structures
    stack = []
    visited = set()
    output = []

    # first node
    current = first_node
    stack.append(current)

    while stack:
        # last node in stack
        current = stack.pop()

        # graph search
        if not current in visited:
            visited.add(current)
            output.append(current)

        # add adjacent nodes to stack
        for node in graph[current]:
            if not node in visited:
                stack.append(node)

    return output