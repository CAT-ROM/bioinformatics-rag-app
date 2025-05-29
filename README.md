# 🔬 Multimodal RAG for Knowledge-Aware Bioinformatics Visual Assistant

This repository contains the implementation of a **Multimodal Retrieval-Augmented Generation (RAG)** system that answers user queries about **bioinformatics tools** using both **textual** and **visual** context. Built as part of the **AIMS-DTU Research Internship Round 2**, this project demonstrates how LLMs can be combined with domain-specific multimodal retrieval to power intelligent assistants.

## 📁 Project Structure

```
bioinfo-rag-assistant/
├── data/                     # Collected tool data (CSV, JSON, images)
├── embeddings/               # Precomputed text and image embeddings
├── bioinfo_rag_app.py        # Streamlit frontend interface
├── retrieval_pipeline.py     # Logic for retrieving relevant multimodal documents
├── generation_module.py      # GPT-based answer generation from context
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 📌 Objective

To build a **Multimodal RAG system** that can:
- Accept a natural language query about a bioinformatics tool.
- Retrieve **textual** (descriptions, reviews, metadata) and **visual** (logos, screenshots) context.
- Use an **LLM (GPT-4)** to generate a grounded, context-aware answer.

## 📦 Dataset

You can collect your own data or refer to the sample metadata CSV under `data/` which includes:
- Tool Name, Category, Description
- Associated Logos or Illustrations (saved as image files in `data/`)

## ⚙️ How It Works

1. **Frontend**:
   - `bioinfo_rag_app.py` renders the interface via Streamlit.
   - Allows users to input a query and view answers with supporting content.

2. **Retrieval**:
   - `retrieval_pipeline.py` loads text/image embeddings and performs similarity search using FAISS.

3. **Answer Generation**:
   - `generation_module.py` constructs the prompt and queries the OpenAI API to generate an answer.

## 💬 Sample Queries

Try asking:
- “Is GATK good for variant calling?”
- “What are the best RNA-Seq analysis tools?”
- “Does Bowtie2 support metagenomic data?”

## ✅ Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your `secrets.toml`:
```toml
# .streamlit/secrets.toml
[general]
openai_api_key = "your-api-key-here"
```

3. Run the app:
```bash
streamlit run bioinfo_rag_app.py
```

## ✨ Credits

For AIMS-DTU Research Intern Round 2 - Multimodal RAG Track.
