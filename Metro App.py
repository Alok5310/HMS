import networkx as nx
import matplotlib.pyplot as plt

def create_metro_graph():
    G = nx.Graph()
    
    # Real Delhi Metro station names
    stations = ["Rajiv Chowk", "Kashmere Gate", "Chandni Chowk", "New Delhi", 
                "AIIMS", "Hauz Khas", "Saket", "Botanical Garden"]
    G.add_nodes_from(stations)
    
    # Routes between stations with distances (km) and estimated time (minutes)
    edges = [
        ("Rajiv Chowk", "Kashmere Gate", {"distance": 6, "time": 9}),
        ("Kashmere Gate", "Chandni Chowk", {"distance": 2, "time": 3}),
        ("Chandni Chowk", "New Delhi", {"distance": 1, "time": 2}),
        ("New Delhi", "AIIMS", {"distance": 8, "time": 12}),
        ("AIIMS", "Hauz Khas", {"distance": 3, "time": 4}),
        ("Hauz Khas", "Saket", {"distance": 4, "time": 6}),
        ("Saket", "Botanical Garden", {"distance": 7, "time": 10}),
        ("Rajiv Chowk", "New Delhi", {"distance": 2, "time": 3}),
        ("Kashmere Gate", "AIIMS", {"distance": 10, "time": 15}),
        ("Chandni Chowk", "Hauz Khas", {"distance": 5, "time": 7}),
        ("New Delhi", "Saket", {"distance": 6, "time": 9})
    ]
    
    for u, v, data in edges:
        G.add_edge(u, v, **data)
    
    return G

def visualize_metro_graph(G, shortest_distance_path=[], shortest_time_path=[]):
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(12, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    
    edge_labels = { (u, v): f"{G[u][v]['distance']} km, {G[u][v]['time']} min" for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    if shortest_distance_path:
        path_edges = list(zip(shortest_distance_path, shortest_distance_path[1:]))
        nx.draw(G, pos, edgelist=path_edges, edge_color='red', width=3, label="Shortest Distance Path")
    
    if shortest_time_path:
        path_edges_time = list(zip(shortest_time_path, shortest_time_path[1:]))
        nx.draw(G, pos, edgelist=path_edges_time, edge_color='blue', width=3, label="Shortest Time Path")
    
    plt.legend(["Shortest Distance Path (Red)", "Shortest Time Path (Blue)"])
    plt.title("Delhi Metro Map with Distance & Time")
    plt.show()

def find_shortest_path(G, start, end, weight="distance"):
    return nx.dijkstra_path(G, start, end, weight=weight), nx.dijkstra_path_length(G, start, end, weight=weight)

if __name__ == "__main__":
    metro_graph = create_metro_graph()
    
    print("Available Metro Stations: ", list(metro_graph.nodes))
    start_station = input("Enter the source station: ").strip()
    end_station = input("Enter the destination station: ").strip()
    
    if start_station in metro_graph and end_station in metro_graph:
        # Find shortest path based on distance
        path_distance, length_distance = find_shortest_path(metro_graph, start_station, end_station, weight="distance")
        
        # Find shortest path based on time
        path_time, length_time = find_shortest_path(metro_graph, start_station, end_station, weight="time")
        
        print(f"Shortest path (Distance) from {start_station} to {end_station}: {path_distance} ({length_distance} km)")
        print(f"Shortest path (Time) from {start_station} to {end_station}: {path_time} ({length_time} min)")
        
        visualize_metro_graph(metro_graph, shortest_distance_path=path_distance, shortest_time_path=path_time)
    else:
        print("Invalid station names. Please enter correct station names.")
