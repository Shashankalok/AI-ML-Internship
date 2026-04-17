class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self, state):
        """
        Every agent must implement this method.
        It takes shared state and returns updated state.
        """
        raise NotImplementedError("Each agent must implement the run method")

    def log(self, message):
        print(f"[{self.name}] {message}")