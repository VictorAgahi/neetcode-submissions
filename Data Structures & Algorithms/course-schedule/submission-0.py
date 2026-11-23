from collections import defaultdict, deque


class Solution:

  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = defaultdict(list)

    in_degree = [0] * numCourses 

    for course, prereq in prerequisites:
      adj[prereq].append(course)
      in_degree[course] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited_courses = 0

    while queue:
      curr = queue.popleft()
      visited_courses += 1

      for next_course in adj[curr]:
        in_degree[next_course] -= 1
        if in_degree[next_course] == 0:
          queue.append(next_course)

    return visited_courses == numCourses