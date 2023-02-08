## This script downloads the clip model for embeddings service.

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('clip-ViT-L-14')
model.save('embeddings/app/clip-ViT-L-14.model')