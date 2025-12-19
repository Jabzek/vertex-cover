import time
import pulp
from graph_generation import Graph

def ilp_algorithm(graph):
    problem = pulp.LpProblem("Vertex_cover", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("node", range(graph.nodes), cat=pulp.LpBinary)
    problem += pulp.lpSum([graph.nodes_weight[i] * x[i] for i in range(graph.nodes)])

    for edge in graph.edges:
        problem += x[edge[0]] + x[edge[1]] >= 1

    problem.solve(pulp.PULP_CBC_CMD(msg=0))

    final_nodes = []
    final_cost = pulp.value(problem.objective)

    for n in range(graph.nodes):
        if pulp.value(x[n]) == 1.0:
            final_nodes.append(n)
    
    return final_nodes, int(final_cost)


def lp_algorithm(graph):
    problem = pulp.LpProblem("Vertex_cover", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("node", range(graph.nodes), lowBound=0, upBound=1, cat=pulp.LpContinuous)
    problem += pulp.lpSum([graph.nodes_weight[i] * x[i] for i in range(graph.nodes)])
    
    for edge in graph.edges:
        problem += x[edge[0]] + x[edge[1]] >= 1

    problem.solve(pulp.PULP_CBC_CMD(msg=0))

    final_nodes = []
    final_cost = 0

    if pulp.LpStatus[problem.status] == "Optimal":
        for n in range(graph.nodes):
            val = pulp.value(x[n])        
            if val >= 0.5:
                final_nodes.append(n)
                final_cost += graph.nodes_weight[n]

    return final_nodes, final_cost


def lp_algorithms_manage(data, lp):
    if lp: 
        graphes = ["small", "medium", "big"]
    else:
        graphes = ["small", "medium"]

    for size in graphes:
        for graph_dict in data[size]:
            graph = Graph.from_dict(graph_dict)
            
            if lp:
                start_time = time.time()
                final_nodes, final_cost = lp_algorithm(graph)
            else:
                start_time = time.time()
                final_nodes, final_cost = ilp_algorithm(graph)
            end_time = time.time()
            
            print(f"For the graph with {graph.nodes} nodes, the best combination of ", end="")
            print(f"vertices is {sorted(final_nodes)} at a cost {final_cost}")

