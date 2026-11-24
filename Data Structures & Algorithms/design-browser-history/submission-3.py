class BrowserHistory:

    def __init__(self, homepage: str):
        self.history =[homepage]
        self.current = 0
        self.n = 1

    def visit(self, url: str) -> None:
        self.current += 1
        if self.current == len(self.history):
            self.history.append(url)
            self.n += 1
        else:
            self.history[self.current] = url
            self.n = 1 + self.current

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.n - 1, self.current + steps)
        return self.history[self.current]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)