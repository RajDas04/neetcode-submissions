class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for counter in s:
            if counter in closeToOpen:
                if stk and stk[-1] == closeToOpen[counter]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(counter)
        return False if stk else True