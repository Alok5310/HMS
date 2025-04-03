import networkx as nx
import matplotlib.pyplot as plt

def create_metro_graph():
    G = nx.Graph()
    
    # Adding metro stations as nodes
    stations = ["A", "B", "C", "D", "E", "F", "G", "H"]
    G.add_nodes_from(stations)
    
    # Adding edges (routes between stations) with weights (distance/time)
    edges = [
        ("A", "B", 2), ("B", "C", 3), ("C", "D", 1),
        ("D", "E", 4), ("E", "F", 2), ("F", "G", 3), ("G", "H", 1),
        ("A", "D", 5), ("B", "E", 6), ("C", "F", 4), ("D", "G", 7)
    ]
    G.add_weighted_edges_from(edges)
    
    return G

def visualize_metro_graph(G, shortest_path=[]):
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw(G, pos, edgelist=path_edges, edge_color='red', width=3)
    
    plt.title("Metro Map Visualization")
    plt.show()

def find_shortest_path(G, start, end):
    shortest_path = nx.dijkstra_path(G, start, end, weight='weight')
    path_length = nx.dijkstra_path_length(G, start, end, weight='weight')
    return shortest_path, path_length

if __name__ == "__main__":
    metro_graph = create_metro_graph()
    start_station = "A"
    end_station = "G"
    
    path, length = find_shortest_path(metro_graph, start_station, end_station)
    print(f"Shortest path from {start_station} to {end_station}: {path} (Distance: {length})")
    
    visualize_metro_graph(metro_graph, shortest_path=path)
