import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import time

# Function to create a graph and position nodes
def create_graph():
    G = nx.erdos_renyi_graph(15, 0.2)
    pos = nx.circular_layout(G)
    return G, pos

# Function to draw the network with a given number of edges
def draw_network(G, pos, num_edges):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=200, node_color="blue")
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=list(G.edges())[:num_edges], edge_color="black")
    return fig

# Streamlit app
st.title("Network Animation: Connected Dots")

# Create the graph
G, pos = create_graph()

# Number of edges to draw in each frame
num_edges = st.slider("Number of edges to draw:", 1, len(G.edges()), 1)

# Draw the network with the selected number of edges
fig = draw_network(G, pos, num_edges)
st.pyplot(fig)

# Animation loop (optional)
if st.button("Start Animation"):
    for i in range(len(G.edges())):
        fig = draw_network(G, pos, i + 1)
        st.pyplot(fig)
        time.sleep(0.2)
