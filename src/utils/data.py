class EvaluationDataGenerator:
    def __init__(self):
        pass
    
    def generate_evaluation_data(self, description, scenarios):
        # Placeholder: Implement logic to generate evaluation data
        evaluation_data = [{"scenario": scenario, "expected_output": "Expected output for " + scenario} for scenario in scenarios]
        return evaluation_data

# Example usage
if __name__ == "__main__":
    edg = EvaluationDataGenerator()
    description = "A system to generate prompts for various scenarios"
    scenarios = ["scenario 1", "scenario 2"]
    evaluation_data = edg.generate_evaluation_data(description, scenarios)
    for data in evaluation_data:
        print(data)
