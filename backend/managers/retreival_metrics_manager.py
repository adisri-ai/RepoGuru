class RetrievalMetricsManager:

    def __init__(self):

        self.scores = []

    def add_score(
        self,
        score: float
    ):

        self.scores.append(score)

    def get_average_score(
        self
    ):

        if not self.scores:
            return 0

        return (
            sum(self.scores)
            /
            len(self.scores)
        )

    def reset(self):

        self.scores.clear()