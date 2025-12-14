import time
from itertools import combinations
from graph_generation import Graph


def brute_force(graph):
    best_combination = ([], float("inf"))
    stop = False
    for size in range(0, graph.nodes + 1):
        for nodes_group in combinations(range(0, graph.nodes), size):
            cost = 0
            for node in nodes_group:
                cost += graph.nodes_weight[node]
            
            if cost > best_combination[1]:
                continue

            for edges in graph.edges:
                if not (edges[0] in nodes_group or edges[1] in nodes_group):
                    stop = True
                    break
            
            if stop:
                stop = False
                continue
            best_combination = (nodes_group, cost)
    return best_combination


def brute_force_manage(data):
    for graph_dict in data["small"]:
        graph = Graph.from_dict(graph_dict)
        start_time = time.time()
        best_combination = brute_force(graph)
        end_time = time.time()
        print(f"For the graph with {graph.nodes} nodes, the best combination of ", end="")
        print(f"vertices is {best_combination[0]} at a cost {best_combination[1]}")
            