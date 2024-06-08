import random

class MonteCarloMatchmaking:
    def __init__(self):
        pass
    
    def match_prompts(self, prompts):
        random.shuffle(prompts)
        matches = [(prompts[i], prompts[i + 1]) for i in range(0, len(prompts) - 1, 2)]
        return matches

class ELORatingSystem:
    def __init__(self, k=32):
        self.k = k
        self.ratings = {}

    def get_rating(self, prompt):
        return self.ratings.get(prompt, 1500)
    
    def update_ratings(self, prompt1, prompt2, result):
        r1 = self.get_rating(prompt1)
        r2 = self.get_rating(prompt2)
        e1 = 1 / (1 + 10 ** ((r2 - r1) / 400))
        e2 = 1 / (1 + 10 ** ((r1 - r2) / 400))
        if result == 1:
            r1_new = r1 + self.k * (1 - e1)
            r2_new = r2 + self.k * (0 - e2)
        else:
            r1_new = r1 + self.k * (0 - e1)
            r2_new = r2 + self.k * (1 - e2)
        self.ratings[prompt1] = r1_new
        self.ratings[prompt2] = r2_new

# Example usage
if __name__ == "__main__":
    mcm = MonteCarloMatchmaking()
    prompts = ["Prompt 1", "Prompt 2", "Prompt 3", "Prompt 4"]
    matches = mcm.match_prompts(prompts)
    for match in matches:
        print(match)

    elo = ELORatingSystem()
    elo.update_ratings("Prompt 1", "Prompt 2", 1)
    elo.update_ratings("Prompt 3", "Prompt 4", 0)
    print(elo.ratings)
