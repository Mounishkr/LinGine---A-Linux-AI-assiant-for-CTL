# app.py
import streamlit as st
import torch
from sentence_transformers import SentenceTransformer
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle

# Load models and data
@st.cache_resource
def load_models():
    model = SentenceTransformer('linux_command_model')
    command_embeddings = torch.load('command_embeddings.pt')
    df = pd.read_pickle('command_data.pkl')
    with open('command_nn_model.pkl', 'rb') as f:
        nbrs = pickle.load(f)
    return model, command_embeddings, df, nbrs

model, command_embeddings, df, nbrs = load_models()

# Streamlit UI
st.title("Linux Command AI Assistant")
st.write("Ask about Linux commands and get relevant suggestions")

user_input = st.text_input("What do you want to do?", "")

if user_input:
    # Encode user input
    input_embedding = model.encode(user_input, convert_to_tensor=True).cpu().numpy().reshape(1, -1)
    
    # Find nearest commands
    distances, indices = nbrs.kneighbors(input_embedding)
    
    # Display results
    st.subheader("Top matching Linux commands:")
    for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
        command = df.iloc[idx]['command']
        desc = df.iloc[idx]['description']
        category = df.iloc[idx]['category']
        
        st.write(f"### {i+1}. `{command}`")
        st.write(f"**Category**: {category}")
        st.write(f"**Description**: {desc}")
        st.write(f"**Relevance score**: {1-dist:.2f}")
        st.write("---")

# To run: streamlit run app.py