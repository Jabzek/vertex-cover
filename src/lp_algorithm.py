import time
import pulp
from graph_generation import Graph

def ilp_algorithm(graph):
    problem = pulp






def ilp_algorithm_manage(data):
    for size in ["small", "medium", "big"]:
        for graph_dict in data[size]:
            graph = Graph.from_dict(graph_dict)
            start_time = time.time()
            ilp_algorithm(graph)
            end_time = time.time()
            print()