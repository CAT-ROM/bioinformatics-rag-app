import streamlit as st
import openai
import numpy as np
import pandas as pd
from PIL import Image
from retrieval_pipeline import retrieve_relevant_docs
from generation_module import generate_answer

# Load API key from secrets.toml
openai.api_key = st.secrets["general"]["openai_api_key"]

# Load data
df = pd.read_csv("data/bioinfo_tools_metadata.csv")
text_embeddings = np.load("embeddings/text_embeddings.npy")
image_embeddings = np.load("embeddings/image_embeddings.npy")

# App UI
st.set_page_config(page_title="🔬 Bioinformatics Visual Assistant", layout="wide")
st.title("🔬 Bioinformatics Visual Assistant")
st.markdown("Ask questions about bioinformatics tools and get AI-powered, context-rich answers based on text and image data.")

st.sidebar.markdown("🧰 **Available Tools**")
st.sidebar.dataframe(df[["ToolName", "Category"]])

# User query
query = st.text_input("💬 Ask a question about a tool (e.g., 'Is GATK good for variant calling?')")

if query:
    # Retrieve top relevant docs and images
    retrieved_texts, retrieved_images = retrieve_relevant_docs(query, df, text_embeddings, image_embeddings)

    # Show retrieved results
    st.markdown("### 📄 Retrieved Documents")
    for i, text in enumerate(retrieved_texts):
        st.markdown(f"**Document {i+1}:** {text}")

    st.markdown("### 🖼️ Related Images")
    for img_path in retrieved_images:
        try:
            img = Image.open(img_path)
            st.image(img, caption=img_path)
        except:
            st.write(f"(Could not load image: {img_path})")

    # Generate answer
    st.markdown("### 🤖 Answer")
    answer = generate_answer(query, retrieved_texts)
    st.success(answer)
