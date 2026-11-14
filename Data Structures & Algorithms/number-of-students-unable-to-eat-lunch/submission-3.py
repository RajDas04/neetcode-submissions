class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        counter = Counter(students)
        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                counter[sandwich] -= 1
                res -= 1
            else:
                break
        return res