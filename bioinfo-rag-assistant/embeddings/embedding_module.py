import os
import pandas as pd
import numpy as np
import torch
from PIL import Image
from sentence_transformers import SentenceTransformer
from torchvision import transforms, models

# Load models
text_model = SentenceTransformer("all-MiniLM-L6-v2")

# Image embedding model (pretrained ResNet)
image_model = models.resnet50(pretrained=True)
image_model = torch.nn.Sequential(*(list(image_model.children())[:-1]))  # Remove final layer
image_model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Compute text embeddings
def compute_text_embeddings(text_list):
    return text_model.encode(text_list, show_progress_bar=True)

# Compute image embedding
def compute_image_embedding(image_path):
    img = Image.open(image_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0)
    with torch.no_grad():
        features = image_model(img_tensor).squeeze().numpy()
    return features

# Example usage
def embed_all_data(csv_path, image_folder, output_path="embeddings"):
    os.makedirs(output_path, exist_ok=True)

    df = pd.read_csv(csv_path)

    # Text embeddings
    text_data = df["Description"].tolist()
    text_embeddings = compute_text_embeddings(text_data)
    np.save(os.path.join(output_path, "text_embeddings.npy"), text_embeddings)

    # Image embeddings
    image_embeddings = []
    for img_file in df["ImageFile"]:
        img_path = os.path.join(image_folder, img_file)
        if os.path.exists(img_path):
            emb = compute_image_embedding(img_path)
            image_embeddings.append(emb)
        else:
            image_embeddings.append(np.zeros(2048))  # Placeholder

    np.save(os.path.join(output_path, "image_embeddings.npy"), np.array(image_embeddings))
