import tkinter as tk
from tkinter import simpledialog, messagebox
import heapq

def dijkstra(graph, source):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[source] = 0
    parent = {vertex: None for vertex in graph}
    priority_queue = [(0, source)]

    print("Initial distances:", distance)
    print("Initial parents:", parent)
    print("Initial priority queue:", priority_queue)

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)
        print("\nPopped from priority queue:", (current_distance, u))

        print(f"Checking if current distance {current_distance} is greater than known distance {distance[u]}")
        if current_distance > distance[u]:
            print(f"Current distance {current_distance} is greater than known distance {distance[u]}")
            continue

        for neighbor, weight in graph[u].items():
            distance_via_u = current_distance + weight
            print(f"Checking neighbor {neighbor} with edge weight {weight}")
            print(f"Distance via {u} to {neighbor}: {distance_via_u}")

            if distance_via_u < distance[neighbor]:
                distance[neighbor] = distance_via_u
                parent[neighbor] = u
                heapq.heappush(priority_queue, (distance_via_u, neighbor))
                print(f"Updated distance for {neighbor}: {distance_via_u}")
                print(f"Updated parent for {neighbor}: {u}")
                print(f"Priority queue updated with: {(distance_via_u, neighbor)}")

    print("\nFinal distances:", distance)
    print("Final parents:", parent)
    return distance, parent

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source = 'A'
dijkstra(graph, source)
