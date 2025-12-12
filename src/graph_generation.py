import random
import itertools

class Graph:
    def __init__(self, n):
        self.nodes = n
        self.nodes_weight = []
        self.edges = []

    def add_edge(self, tuple_):
        self.edges.append(tuple_)

    def add_weight(self, weight):
        self.nodes_weight.append(weight)


def draw_edges(graph):
    nodes = graph.nodes
    edges = itertools.combinations(range(nodes), 2)


def draw_weight(graph):
    nodes = graph.nodes
    for _ in range(nodes):
        w = random.randint(1, 100)
        graph.add_weight(w)


def generation():
    graphs = {"small":((18, 60), (19, 50), (20, 20), (21, 70), (22, 40)),
              "medium": ((40, 70), (60, 50), (80, 20), (90, 60), (100, 30)),
               "big": ((150, 50), (200, 30), (250, 20), (300, 15), (350, 10))}
    
    for size in ("small", "medium", "big"):
        for tuple_ in graphs[size]:
            nodes = tuple_[0]
            saturation = tuple_[1]
            all_edges = nodes * (nodes - 1) // 2
            number_of_edges = saturation * all_edges // 100 
            graph = Graph(nodes)
            draw_edges(number_of_edges, graph)
            draw_weight(graph)