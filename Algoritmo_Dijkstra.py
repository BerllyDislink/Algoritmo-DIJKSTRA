import tkinter as tk
from tkinter import simpledialog, messagebox
import heapq

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, prompt=""):
        self.prompt = prompt
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text=self.prompt).grid(row=0, column=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)
        self.geometry("400x100")  # Ajusta el tamaño del diálogo
        return self.entry

    def apply(self):
        self.result = self.entry.get()

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
    num_nodes = int(CustomDialog(root, title="# Nodos", prompt="Ingrese el número de nodos en el grafo:").result)
    for _ in range(num_nodes):
        node = CustomDialog(root, title="Nombre del Nodo", prompt="Ingrese el nombre del nodo:").result
        graph[node] = {}
        num_edges = int(CustomDialog(root, title=f"# Aristas para {node}", prompt=f"Ingrese el número de aristas para el nodo {node}:").result)
        for _ in range(num_edges):
            neighbor_weight = CustomDialog(root, title="Nodo Vecino y su peso", prompt="Ingrese el vecino y el peso de la arista (formato: nodo vecino peso):").result
            neighbor, weight = neighbor_weight.split()
            graph[node][neighbor] = int(weight)
    return graph

def main():
    global root
    root = tk.Tk()
    root.geometry("400x300")  # Cambia el tamaño de la ventana principal
    root.withdraw()  # Oculta la ventana principal

    messagebox.showinfo("Información", "Definición del grafo:")
    graph = input_graph()

    source = CustomDialog(root, title="Origen", prompt="Ingrese el nodo de origen:").result
    target = CustomDialog(root, title="Destino", prompt="Ingrese el nodo de destino:").result
    
    distance, parent = dijkstra(graph, source)
    path = shortest_path(parent, target)
    
    result_distance = f"Distancia más corta desde {source} a {target}: {distance[target]}"
    result_path = f"Camino más corto desde {source} a {target}: {' -> '.join(path)}"
    
    messagebox.showinfo("Resultados", f"{result_distance}\n{result_path}")
    root.destroy()

if __name__ == "__main__":
    main()
