import PyPDF2
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List
import os
import logging

logger = logging.getLogger(__name__)

class DocumentRagService:
    def __init__(self, pdf_path: str = None):
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatIP(384)  # MiniLM dimension
        self.documents = []
        self.pdf_path = pdf_path or "hr_policies.pdf"
        
        if os.path.exists(self.pdf_path):
            self._load_pdf()
    
    def _load_pdf(self):
        try:
            logger.info(f"Loading pdf from: {self.pdf_path}")
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                text_chunks = []
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    # Split into chunks with overlap
                    chunks = [text[i:i+500] for i in range(0, len(text), 400)]
                    text_chunks.extend(chunks)
                
                logger.info(f"Document loaded and split into {len(text_chunks)} segments")
                
                # Generate embeddings
                embeddings = self.embedding_model.encode(text_chunks)
                
                # Add to FAISS index
                self.index.add(embeddings.astype('float32'))
                self.documents = text_chunks
                
        except Exception as e:
            logger.error(f"Exception loading PDF: {e}")
            raise RuntimeError(f"Loading pdf failed: {e}")
    
    def retrieve_context(self, query: str, max_results: int = 3) -> str:
        logger.info(f"RAG Query {query} | Retrieving Top Chunks {max_results}")
        
        if self.index.ntotal == 0:
            return "No documents loaded"
        
        query_embedding = self.embedding_model.encode([query])
        scores, indices = self.index.search(query_embedding.astype('float32'), max_results)
        
        context_chunks = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.documents):
                context_chunks.append(self.documents[idx])
        
        context = "\n\n".join(context_chunks)
        context_length = len(context)
        context_tokens = context_length // 4
        
        logger.info(f"RAG Retrieved: {len(context_chunks)} chunks | {context_length} chars | ~{context_tokens} tokens")
        
        return context
    
    def get_sources(self, query: str, max_results: int = 3) -> List[str]:
        if self.index.ntotal == 0:
            return ["No documents loaded"]
        
        query_embedding = self.embedding_model.encode([query])
        scores, indices = self.index.search(query_embedding.astype('float32'), max_results)
        
        sources = []
        for i, score in enumerate(scores[0]):
            sources.append(f"Document (score: {score:.2f})")
        
        return sources