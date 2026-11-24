class BrowserHistory:

    def __init__(self, homepage: str):
        self.bHistory = [homepage]
        self.fHistory = []

    def visit(self, url: str) -> None:
        self.bHistory.append(url)
        self.fHistory = []

    def back(self, steps: int) -> str:
        while steps and len(self.bHistory) > 1:
            self.fHistory.append(self.bHistory.pop())
            steps -= 1
        return self.bHistory[-1]

    def forward(self, steps: int) -> str:
        while steps and self.fHistory:
            self.bHistory.append(self.fHistory.pop())
            steps -= 1
        return self.bHistory[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)