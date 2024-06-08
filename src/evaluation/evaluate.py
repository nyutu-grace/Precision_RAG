from sentence_transformers import SentenceTransformer, util
import numpy as np

class PromptEvaluator:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def evaluate_prompts(self, description, prompts):
        description_embedding = self.model.encode(description)
        prompt_embeddings = self.model.encode(prompts)
        scores = [util.pytorch_cos_sim(description_embedding, prompt_embedding).item() for prompt_embedding in prompt_embeddings]
        return scores

# Example usage
if __name__ == "__main__":
    description = "A system to generate prompts for various scenarios"
    prompts = ["Generate scenarios for a prompt system", "Create a system for generating prompts"]
    evaluator = PromptEvaluator()
    scores = evaluator.evaluate_prompts(description, prompts)
    for prompt, score in zip(prompts, scores):
        print(f"Prompt: {prompt}, Score: {score}")