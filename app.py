import streamlit as st
from dijkstra import dijkstra  # senin verdiğin algoritmayı buraya koyduğunu varsayıyorum

class Graph:
    def __init__(self):
        self.vertices = set()
        self.adjacency_list = {}
        self.source = None

    def add_edge(self, u, v, w):
        self.vertices.update([u, v])
        if u not in self.adjacency_list:
            self.adjacency_list[u] = {}
        self.adjacency_list[u][v] = w

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def insert(self, priority, value):
        self.elements.append((priority, value))

    def remove(self):
        self.elements.sort()
        return self.elements.pop(0)

    def sort(self):
        return sorted(self.elements)

    @property
    def length(self):
        return len(self.elements)

st.title("Dijkstra's Algorithm Simulator")

st.sidebar.header("Graph Inputs")
graph = Graph()

u = st.sidebar.text_input("Start node")
v = st.sidebar.text_input("End node")
w = st.sidebar.number_input("Weight", min_value=1, value=1)

if st.sidebar.button("Add Edge"):
    graph.add_edge(u, v, w)
    st.sidebar.success(f"Edge added: {u} → {v} ({w})")

source = st.sidebar.text_input("Source Node")
if source:
    graph.source = source

if st.button("Run Dijkstra"):
    queue = PriorityQueue()
    dist, prev, steps = dijkstra(graph, queue)

    st.subheader("Final Distances")
    st.write(dist)

    st.subheader("Previous Nodes")
    st.write(prev)

    st.subheader("Steps")
    for i, step in enumerate(steps):
        st.write(f"### Step {i+1}"

