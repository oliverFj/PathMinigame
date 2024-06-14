class Score:
    def __init__(self):
        self.score = 0

    def reset(self):
        self.score = 0

    def increment(self, points=1):
        self.score += points

    def get_score(self):
        return self.score
