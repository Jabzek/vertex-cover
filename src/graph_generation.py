import random
from pathlib import Path
from dataclasses import dataclass, field, asdict
import json

@dataclass
class Graph:
    nodes: int
    size: str
    nodes_weight: list[int] = field(default_factory=list)
    edges: list[list[int, int]] = field(default_factory=list)

    def add_edge(self, tuple_):
        self.edges.append(tuple_)

    def add_weight(self, weight):
        self.nodes_weight.append(weight)

    def data_to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, dict_):
        pass



def draw_edges(graph, number_of_edges):
    nodes = graph.nodes
    i = 0

    while i < number_of_edges:
        a = random.randrange(0, nodes)
        b = random.randrange(0, nodes)

        if a == b:
            continue
        elif a > b:
            a, b = b, a

        if [a, b] not in graph.edges:
            graph.add_edge([a, b])
            i += 1


def draw_weight(graph):
    nodes = graph.nodes
    for _ in range(nodes):
        w = random.randint(1, 100)
        graph.add_weight(w)


def save_to_json(new_data, data_file, size):
    if data_file.exists():
        with open(data_file, "r") as f:
            data = json.load(f)
    else:
        data = {"small": [],
                "medium": [],
                "big": []}
    
    data[size].append(new_data)

    with open(data_file, "w") as f:
        json.dump(data, f, indent=2)


def data_generator(file_name):
    graphs = {"small":((18, 60), (19, 50), (20, 20), (21, 70), (22, 40)),
              "medium": ((40, 70), (60, 50), (80, 20), (90, 60), (100, 30)),
               "big": ((150, 50), (200, 30), (250, 20), (300, 15), (350, 10))}

    main_folder = Path(__file__).resolve().parent.parent
    data_folder = main_folder / "data"
    data_folder.mkdir(exist_ok=True)
    data_file = data_folder / file_name
    
    if data_file.exists():
        data_file.unlink()

    for size in ("small", "medium", "big"):
        for tuple_ in graphs[size]:
            nodes = tuple_[0]
            saturation = tuple_[1]
            
            all_edges = nodes * (nodes - 1) // 2
            number_of_edges = saturation * all_edges // 100 
            graph = Graph(nodes, size)
            
            draw_edges(graph, number_of_edges)
            draw_weight(graph)
            new_data = graph.data_to_dict()
            save_to_json(new_data, data_file, size)


