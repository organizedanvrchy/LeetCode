from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        
        # Step 1: Map emails to names and union emails within the same account
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                uf.add(email)
                email_to_name[email] = name
                uf.union(account[1], email)  # Union all emails in this account
        
        # Step 2: Group emails by their root
        email_groups = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            email_groups[root].append(email)
        
        # Step 3: Format the result
        result = []
        for group in email_groups.values():
            result.append([email_to_name[group[0]]] + sorted(group))
        
        return result
