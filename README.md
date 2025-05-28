# 🔬 Multimodal RAG for Knowledge-Aware Bioinformatics Visual Assistant

This repository contains the implementation of a **Multimodal Retrieval-Augmented Generation (RAG)** system that answers user queries about **bioinformatics tools** using both **textual** and **visual** context. Built as part of the **AIMS-DTU Research Internship Round 2**, this project demonstrates how LLMs can be combined with domain-specific multimodal retrieval to power intelligent assistants.

---

## 🧠 Project Objective

Develop an AI-powered assistant that can:
- Ingest and index textual and image-based knowledge about bioinformatics tools
- Retrieve relevant multimodal context (descriptions, reviews, and tool figures)
- Generate grounded, insightful, and natural language responses to user questions

---

## 📦 Dataset

A custom dataset was curated covering **50+ bioinformatics tools**, each with:
- 🧾 **Metadata**: Tool name, function, publication info, category (e.g., genome assembly, variant calling)
- 💬 **Textual Documents**: Descriptions, use-cases, reviews, user questions, and best practices
- 🖼️ **Images**: Logos, screenshots, diagrams, flowcharts

> **Note:** Data collected from official documentation, publications, online tutorials, and tool repositories.

---

## 🧰 Features

- 💬 Ask natural-language questions like:
  - *"Is GATK good for variant calling?"*
  - *"What tools are used for single-cell RNA-seq analysis?"*
- 📥 Retrieves context from embedded documents and images
- 🧠 Generates intelligent answers using OpenAI GPT-4
- 🌐 Streamlit interface for local interaction and testing

---

## 🧱 Architecture

1. **Data Ingestion**
   - Tools, metadata, descriptions, and images collected and organized
2. **Embedding Generation**
   - Textual documents: Embedded using OpenAI or HuggingFace models
   - Images: Embedded using CLIP or similar vision models
3. **Vector Store**
   - FAISS used for similarity-based retrieval across modalities
4. **Retrieval Pipeline**
   - Query embedding → Multimodal document search → Top-k context
5. **Answer Generation**
   - Retrieved context + user query → Prompted into LLM for final answer

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bioinfo-rag-assistant.git
cd bioinfo-rag-assistant
