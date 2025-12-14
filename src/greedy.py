import time
from graph_generation import Graph


def greedy(graph):
    node_degree = []

    for el in graph.n_list:
        l_len = len(el)
        node_degree.append(l_len)
    
    





def greedy_manage(data):
    for size in ["small", "medium", "big"]:
        for graph_dict in data[size]:
            graph = Graph.from_dict(graph_dict)
            start_time = time.time()
            best_combination = greedy(graph)
            end_time = time.time()
            print(f"For the graph with {graph.nodes} nodes, the best combination of ", end="")
            print(f"vertices is {best_combination[0]} at a cost {best_combination[1]}")