import streamlit as st
import sys
import subprocess

# Function to install package if not present
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing matplotlib and install if needed
try:
    import matplotlib.pyplot as plt
except ImportError:
    install("matplotlib")
    import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.animation as animation
import io

# Function to create the animation
def create_animation():
    # Create a graph
    G = nx.erdos_renyi_graph(15, 0.2)
    pos = nx.circular_layout(G)

    # Initialize plot
    fig, ax = plt.subplots()
    ax.set_axis_off()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    # Initialize nodes and edges
    nodes = nx.draw_networkx_nodes(G, pos, ax=ax, node_size=200, node_color="blue")
    edges = nx.draw_networkx_edges(G, pos, ax=ax)

    def update(num):
        ax.clear()
        ax.set_axis_off()
        nx.draw_networkx_nodes(G, pos, ax=ax, node_size=200, node_color="blue")
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=list(G.edges())[:num], edge_color="black")

    ani = animation.FuncAnimation(fig, update, frames=len(G.edges()), interval=200, repeat=True)

    # Save animation to a byte buffer
    buf = io.BytesIO()
    ani.save(buf, format='gif')
    buf.seek(0)
    return buf

# Streamlit app
st.title("Network Animation: Connected Dots")

# Create and display the animation
animation_buffer = create_animation()
st.image(animation_buffer, format='gif')
