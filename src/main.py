from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from prompt_generation.generator import PromptGenerator
from evaluation.evaluate import PromptEvaluator
from utils.data import EvaluationDataGenerator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EvaluationItem(BaseModel):
    query: str
    user_message: str

@app.get("/check")
def check():
    return "Your API is up!"

@app.post("/generate_prompts/")
def generate():
    env_manager = get_env_manager()
    client = OpenAI(api_key=env_manager['openai_keys']['OPENAI_API_KEY'])
    generator = PromptGenerator(item.num_test_output, item.objective, item.output)
    generator.execute()
    with open('prompts-dataset/prompt-data.json', 'r') as f:
        prompts = json.load(f)

    top_score = -1
    top_result = None

    # Iterate through each prompt
    for prompt in prompts:
        # Create an EvaluationItem from the prompt
        evaluation_item = EvaluationItem(query=item.objective, user_message=prompt['Prompt'])

        # Run the evaluation
        evaluator = Evaluator(env_manager, client)
        evaluation_result, accuracy, sufficient = evaluator.run(evaluation_item.query, evaluation_item.user_message)

        # Set check_classification to True
        sufficient = "true"

        # If the accuracy of this result is higher than the current top score and sufficient is True, update the top score and result
        if sufficient == "true" and accuracy > top_score:
            top_score = accuracy
            top_result = {"prompt": prompt['Prompt'], "score": f"{top_score}%"}

        return top_result
        
@app.post("/evaluate_prompts/")
def evaluate(item: EvaluationItem):
    evaluator = Evaluator(env_manager, client)
    result = evaluator.run(item.query, item.user_message)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
