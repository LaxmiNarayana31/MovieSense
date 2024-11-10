# helpers.py
import os
import streamlit as st
from nbclient import NotebookClient
from nbformat import read

def generate_model_files():
    try:
        with open("notebook86c26b4f17.ipynb") as f:
            nb = read(f, as_version=4)
            client = NotebookClient(nb)
            client.execute()
    except Exception as e:
        st.error(f"Error generating model files: {e}")
        st.stop()
