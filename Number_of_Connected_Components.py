  class Solution:
      def countComponents(self, n: int, edges: List[List[int]]) -> int:
          # create adjacency list
          adj_list = [[] for _ in range(n)]
          for n1, n2 in edges:
              adj_list[n1].append(n2)
              adj_list[n2].append(n1)
  
          count = 0

          # keep track of visited nodes in set
          seen = set()
          queue = collections.deque()
          
          for i in range(n):
              if i not in seen:
                  queue.append(i)
                  seen.add(i)
                  count += 1
                  self.bfs(adj_list, queue, seen)
          return count
  
      # apply bfs
      def bfs(self, adj_list, queue, seen):
          while queue:
              node = queue.popleft()
              for neighbour in adj_list[node]:
                  if neighbour not in seen:
                      seen.add(neighbour)
                      queue.append(neighbour)
