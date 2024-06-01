import tkinter as tk
from tkinter import simpledialog, messagebox
import heapq

def dijkstra(graph, source):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[source] = 0
    parent = {vertex: None for vertex in graph}
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        if current_distance > distance[u]:
            continue

        for neighbor, weight in graph[u].items():
            distance_via_u = current_distance + weight

            if distance_via_u < distance[neighbor]:
                distance[neighbor] = distance_via_u
                parent[neighbor] = u
                heapq.heappush(priority_queue, (distance_via_u, neighbor))

    return distance, parent

def shortest_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]

def input_graph():
    graph = {}
    num_nodes = int(simpledialog.askstring("Input", "Ingrese el número de nodos en el grafo:"))
    for _ in range(num_nodes):
        node = simpledialog.askstring("Input", "Ingrese el nombre del nodo:")
        graph[node] = {}
        num_edges = int(simpledialog.askstring("Input", f"Ingrese el número de aristas para el nodo {node}:"))
        for _ in range(num_edges):
            neighbor_weight = simpledialog.askstring("Input", "Ingrese el vecino y el peso de la arista (formato: vecino peso):")
            neighbor, weight = neighbor_weight.split()
            graph[node][neighbor] = int(weight)
    return graph

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    messagebox.showinfo("Información", "Definición del grafo:")
    graph = input_graph()

    source = simpledialog.askstring("Input", "Ingrese el nodo de origen:")
    target = simpledialog.askstring("Input", "Ingrese el nodo de destino:")
    
    distance, parent = dijkstra(graph, source)
    path = shortest_path(parent, target)
    
    result_distance = f"Distancia más corta desde {source} a {target}: {distance[target]}"
    result_path = f"Camino más corto desde {source} a {target}: {' -> '.join(path)}"
    
    messagebox.showinfo("Resultados", f"{result_distance}\n{result_path}")
    root.destroy()

if __name__ == "__main__":
    main()
