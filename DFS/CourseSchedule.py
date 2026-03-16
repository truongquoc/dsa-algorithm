from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = set()
        rec_stack = set()
        def is_cycle_detect(course):
            visited.add(course)
            rec_stack.add(course)

            for c in graph[course]:
                if c not in visited:
                    if is_cycle_detect(c):
                        return True
                elif c in rec_stack:
                    return True
            
            rec_stack.remove(course)
            return False
        for i in range(numCourses):
            if i not in visited:
                if is_cycle_detect(i):
                    return False
        
        return True
        
        