# LINK to Question: https://leetcode.com/problems/task-scheduler/

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = Counter(tasks)

        maxTaskFreq = max(taskFreq.values())

        maxTaskCount = list(taskFreq.values()).count(maxTaskFreq)

        intervals = (maxTaskFreq - 1) * (n + 1) +  maxTaskCount

        return max(len(tasks), intervals)
