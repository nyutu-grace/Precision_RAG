from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import torch
import os
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the tokenizer and model
model_name = "facebook/rag-sequence-nq"
tokenizer = RagTokenizer.from_pretrained(model_name)
retriever = RagRetriever.from_pretrained(model_name)
rag_model = RagSequenceForGeneration.from_pretrained(model_name, retriever=retriever)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"files/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"info": "File uploaded successfully", "filename": file.filename}

@app.post("/generate_prompts/")
async def generate_prompts(query: str = Form(...)):
    # Tokenize input
    inputs = tokenizer(query, return_tensors="pt")

    # Retrieve documents
    doc_ids = retriever(inputs.input_ids)

    # Generate response using RAG model
    outputs = rag_model.generate(input_ids=inputs.input_ids, context_input_ids=doc_ids['context_input_ids'])
    prompt = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"prompt": prompt}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
