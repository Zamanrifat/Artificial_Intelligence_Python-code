List = [0, 4, 2, 5, 10, 3, 11, 4]
def bfs(graph, start, goal):
    if start == goal:
        print([start])
        return

    queue = deque([start])
    parent = {}
    parent[start] = start

    while queue:
        currNode = queue.popleft()
        for neighbor in graph[currNode]:
            if neighbor == goal:
                parent[neighbor] = currNode
                print_path(parent, neighbor, start)
                return
            if neighbor not in parent:
                parent[neighbor] = currNode
                queue.append(neighbor)
    print("No path found.")


def print_path(parent, goal, start):
    path = [goal]
    while goal != start:
        goal = parent[goal]
        path.insert(0, goal)
    print(path)


if __name__ == '__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['C', 'D']),
             'C': set(['E']),
             'D': set(['F']),
             'E': set(['D']),
             'F': set(['F'])}

    bfs(graph, 'A', 'F')

print(List[0])
print(List[1])
print(List[2])
print(List[3])
print(List[4])
print(List[5])
print(List[6])
print(List[7])
print(List[8])