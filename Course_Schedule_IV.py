class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isReachable = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            isReachable[u][v] = True
        
        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    if isReachable[j][i] and isReachable[i][k]:
                        isReachable[j][k] = True
        
        res = []
        for u, v, in queries:
            res.append(isReachable[u][v])

        return res
