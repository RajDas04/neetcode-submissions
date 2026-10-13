class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "}":"{", "]":"["}
        stack = []
        if len(s) % 2:
            return False
        else:
            for c in s:
                if c in brackets:
                    if not stack or stack.pop() != brackets[c]:
                        return False
                else:
                    stack.append(c)
        return not stack