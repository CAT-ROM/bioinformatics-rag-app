import os
import csv
import random
import requests

# Create folders
os.makedirs("bioinfo_dataset/documents", exist_ok=True)
os.makedirs("bioinfo_dataset/images", exist_ok=True)

# Sample tool names
tools = [
    "BLAST", "GATK", "Bowtie", "BWA", "HISAT2", "FastQC", "Trimmomatic", "SPAdes",
    "Cufflinks", "TopHat", "Samtools", "Picard", "STAR", "MAFFT", "ClustalW",
    "Bioconductor", "DESeq2", "EdgeR", "IGV", "CNVkit", "MEGA", "Galaxy", "Snippy",
    "HMMER", "Phylip", "RAxML", "Pilon", "LoFreq", "bcftools", "Plink", "Geneious",
    "SOAPdenovo", "SnpEff", "TIGRFAMs", "MUSCLE", "Annovar", "FastTree", "Kallisto",
    "Salmon", "BEDTools", "GSEA", "OrthoFinder", "Infernal", "Kraken", "Kaiju",
    "MetaPhlAn", "QIIME", "RDP", "SILVA", "GTDB-Tk"
]

# Dummy content
desc = "This tool is widely used for genomic analysis and supports high-throughput data processing."
review = "Users have found this tool to be effective in variant calling and aligning short reads."
faq = "Q: Is this tool suitable for RNA-seq? A: Yes, it supports transcriptomic analysis."

# Download a placeholder image
def download_placeholder_image(tool, idx):
    url = "https://via.placeholder.com/150"
    image_path = f"bioinfo_dataset/images/{tool}_{idx}.png"
    with open(image_path, "wb") as f:
        f.write(requests.get(url).content)

# Write metadata CSV
with open("bioinfo_dataset/tools.csv", "w", newline="") as csvfile:
    fieldnames = ["Tool", "Category", "SpecFile1", "SpecFile2", "SpecFile3", "Image1", "Image2"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for tool in tools:
        doc1 = f"{tool}_doc1.txt"
        doc2 = f"{tool}_doc2.txt"
        doc3 = f"{tool}_doc3.txt"

        # Write dummy docs
        with open(f"bioinfo_dataset/documents/{doc1}", "w") as f: f.write(desc)
        with open(f"bioinfo_dataset/documents/{doc2}", "w") as f: f.write(review)
        with open(f"bioinfo_dataset/documents/{doc3}", "w") as f: f.write(faq)

        # Download 1–2 images
        download_placeholder_image(tool, 1)
        if random.random() > 0.5:
            download_placeholder_image(tool, 2)
            img2 = f"{tool}_2.png"
        else:
            img2 = ""

        writer.writerow({
            "Tool": tool,
            "Category": random.choice(["Genomics", "Transcriptomics", "Metagenomics", "Alignment", "Phylogenetics"]),
            "SpecFile1": doc1,
            "SpecFile2": doc2,
            "SpecFile3": doc3,
            "Image1": f"{tool}_1.png",
            "Image2": img2
        })
