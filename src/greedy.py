import time
from graph_generation import Graph

def greedy(graph):
    node_degree = []
    final_nodes = []
    final_cost = 0
    uncovered_edges = len(graph.edges)

    for el in graph.n_list:
        list_len = len(el)
        node_degree.append(list_len)
    
    while uncovered_edges:
        best_node = None
        best_price = float("inf")
        for idx in range(graph.nodes):
            if node_degree[idx] == 0:
                continue
            price = graph.nodes_weight[idx] / node_degree[idx]  

            if price < best_price:
                best_price = price
                best_node = idx         
        final_nodes.append(best_node)
        final_cost += graph.nodes_weight[best_node]
        uncovered_edges -= node_degree[best_node]
        node_degree[best_node] = 0

        for n in graph.n_list[best_node]:
            if node_degree[n] > 0:
                node_degree[n] -= 1
    return (final_nodes, final_cost)
        

def greedy_manage(data):
    for size in ["small", "medium", "big"]:
        for graph_dict in data[size]:
            graph = Graph.from_dict(graph_dict)
            start_time = time.time()
            best_combination = greedy(graph)
            end_time = time.time()
            print(f"For the graph with {graph.nodes} nodes, the best combination of ", end="")
            print(f"vertices is {sorted(best_combination[0])} at a cost {best_combination[1]}")