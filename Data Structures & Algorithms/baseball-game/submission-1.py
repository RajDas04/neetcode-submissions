class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, total = [], 0
        for i in operations:
            if i == "C":
                total -= record.pop()
            else:
                if i == "+":
                    score = record[-1] + record[-2]
                elif i == "D":
                    score = record[-1] * 2
                else:
                    score = int(i)
                record.append(score)
                total += score
        return total