import sys
sys.tracebacklimit=0
# graph = [
#     [(1,3), (2,6)],
#     [(3,4)],
#     [(3,2), (4,3)],
#     [(4,1)],
#     []
# ]

N = int(input())
graph = [[] for _ in range(N)]
for k in range(N):
    p = int(input())
    for _ in range(p):
        i, d = [int(inp) for inp in input().split()]
        graph[k].append((i, d))
        

def dijkstra(nodes:list[tuple[int, int]]) -> int:
    min_dists = [0] + [float('inf')] * (len(nodes) - 1)
    travelled_paths = ["0"] + [None] * (len(nodes) - 1)
    visited = [False] * len(nodes)
    
    def visit(node:int):
        for road in nodes[node]:
            neighbour_node, distance = road
            if min_dists[neighbour_node] > distance + min_dists[node]:
                min_dists[neighbour_node] = distance + min_dists[node]
                travelled_paths[neighbour_node] = travelled_paths[node] + " " + str(neighbour_node)
    
    def find_min():
        min = float('inf')
        min_index = -1
        for i in range(len(min_dists)):
            if min_dists[i] < min and not visited[i]:
                min = min_dists[i]
                min_index = i
        return min_index
    
    for _ in range(len(nodes)):
        min_index = find_min()
        visit(min_index)
        visited[min_index] = True
        
    
    return min_dists[-1], travelled_paths[-1]

min_dist, path = dijkstra(graph)
print(min_dist)
print(path)

