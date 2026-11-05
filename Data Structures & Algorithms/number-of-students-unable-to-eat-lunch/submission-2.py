class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        q = deque(students)
        n = res
        for sandwich in sandwiches:
            cnt = 0
            while cnt < res and q[0] != sandwich:
                cur = q.popleft()
                q.append(cur)
                cnt += 1
            if q[0] == sandwich:
                n -= 1
                q.popleft()
            else:
                break
        return n