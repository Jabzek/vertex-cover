import json
from graph_generation import Graph

def brute_force_manage(data_file):
    with open(data_file, "r") as f:
        data = json.load(f)

    for type in ["small", "medium", "big"]:
        for graph in data[type]:
            pass