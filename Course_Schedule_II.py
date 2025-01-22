class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        prereqNum = [0] * numCourses

        for course, prereq in prerequisites:
            courses[prereq].append(course)
            prereqNum[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if prereqNum[course] == 0:
                queue.append(course)
        
        topOrder = []
        while queue:
            curr = queue.popleft()
            topOrder.append(curr)

            for prereq in courses[curr]:
                prereqNum[prereq] -= 1
                if prereqNum[prereq] == 0:
                    queue.append(prereq)

        if len(topOrder) == numCourses:
            return topOrder
        else:
            return []
