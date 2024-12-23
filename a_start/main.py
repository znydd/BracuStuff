import heapq

input_file = open("input_file.txt", 'r')

h = dict()
graph = dict()

for i in input_file:

    tmp = i.strip().split()
    parent = tmp[0]
    h[parent] = float(tmp[1])
    tmp = tmp[2:]
    graph[parent] = [(tmp[i], float(tmp[i+1])) for i in range(0, len(tmp), 2)]

# ** Graph **
print(h)
print(graph)
for i in graph:
    print(f"{i}: {graph[i]}", end="\n")


visited = set()
pq = []
heapq.heapify(pq)
start_node = input("Start node: ")
end_node = "Bucharest" # keeping it same as it is the goal and heurisic for other goal was not provided

start = (h[start_node], 0, [start_node], start_node) # {f(n) score}, {total dist from start}, {Path}, {node}  
heapq.heappush(pq, start)

res_tuple = None

while len(pq)>0:
    smallest_score = heapq.heappop(pq)
    # print(smallest_score)
    parent = smallest_score[3]
    if parent == end_node:
        res_tuple = smallest_score
        break

    if parent not in visited:
        visited.add(parent)

        for children in graph[parent]: # iterate on the list of child nodes eg: [('Zerind', 75.0), ('Timisoara', 118.0), ('Sibiu', 140.0)]
            child_node = children[0]
            child_node_dist = children[1] # distance from parent node
            if child_node not in visited:
                fn = smallest_score[1]+ child_node_dist + h[child_node]     # g(n) = smallest_score[1]+ child_node_dist
                child_path = (fn, child_node_dist+smallest_score[1], smallest_score[2]+[child_node], child_node)
                heapq.heappush(pq, child_path)

if res_tuple:
    res = "Path: "
    for item in res_tuple[2]:
        res+=f"{item}->"
    res = res[:len(res)-2]
    res+=f"\nTotal distance: {res_tuple[1]} km"
    print(res)
else:
    print("NO PATH FOUND")


# ** Jonayed Kader Nabil **