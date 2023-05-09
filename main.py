import random
import networkx as nx
import matplotlib.pyplot as plt


def generate_graph(num_nodes, edge_probability):
    graph = nx.Graph()
    nodes = range(num_nodes)
    graph.add_nodes_from(nodes)
    # Go through each node and make based on probability
    for node1 in nodes:
        for node2 in nodes:
            if node1 != node2 and random.random() < edge_probability:
                graph.add_edge(node1, node2)

    return graph


def greedy_vert_cover(graph):
    vertexes = set()
    # loop until graph is empty
    while graph.edges:
        max_deg = max(graph, key=graph.degree)
        vertexes.add(max_deg)
        # adj = set(graph.neighbors(max_deg))
        # for points in adj:
        #     graph.remove_edge(max_deg, points)
        graph.remove_node(max_deg)
    return vertexes


def approximation_vertex_cover(graph):
    vertexes = set()
    while graph.edges:
        max_disjoint = nx.algorithms.matching.maximal_matching(graph)  # find max disjoint path
        for u, v in max_disjoint:  # iterate through the set and add vertexes to solution
            if u not in vertexes and v not in vertexes:
                vertexes.add(u)
                vertexes.add(v)
        graph.remove_edges_from(max_disjoint)  # remove edges from graph

    return vertexes


num_nodes = 500
probability = 0.005
gen_graph = generate_graph(num_nodes, probability)
gen_graph_copy = gen_graph.copy()
pos = nx.spring_layout(gen_graph, 42)
nx.draw(gen_graph, pos, with_labels=False, node_size=6)
plt.show()
cover_set = greedy_vert_cover(gen_graph)
cover_set2 = approximation_vertex_cover(gen_graph_copy)
print("Number of nodes for complete coverage via greedy heuristic " + str(len(cover_set)))
print("Number of nodes for complete coverage via the 2-approximation " + str(len(cover_set2)))
