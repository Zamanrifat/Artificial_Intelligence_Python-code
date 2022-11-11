# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def __init__(self): 
    self.graph = dict()
    self.cost_dict=dict()
    self.final_dict=dict()

def addEdge(self,u,v,c):
    
    if u not in self.graph:
        qu = Q.PriorityQueue()
        self.graph.update({u:qu})

    self.graph[u].put(v)
    self.cost_dict.update({(u,v):c})
    
def tnode(self,n):
    self.visited = [False]*n


def UCS_util(self,s,visited,path,goal,value):

    path.append(s)
    
    visited[s]=True
    
    
    if goal==s:
        self.final_dict.update({tuple(path):value})
        return
    
   
    for i in self.graph[s].queue:
        if visited[i]==False:
           
            self.UCS_util(i,copy.deepcopy(visited),copy.deepcopy(path),goal,value + self.cost_dict[s,i])

def UCS(self, s,goal):
    self.visited[s] = True
    
    path=[s]
    
    for i in self.graph[s].queue:
        if self.visited[i] == False:
            
            value = self.cost_dict[s,i]
            self.UCS_util(i,copy.deepcopy(self.visited),copy.deepcopy(path),goal,value)


def all_paths(self):
    
    if bool(self.final_dict):
        print("All the paths: ")
        for i in self.final_dict:
            print ("path: ",i,"cost: ",self.final_dict[i])
    else:
        print ("No Path exist between start and goal node")


def optimal_path(self):
    if bool(self.final_dict):
        print ("best path: ",min(self.final_dict, key=self.final_dict.get))
    else:
        print ("No Path exist between start and goal node")
        
    g = Graph()
g.tnode(10)

g.addEdge(A, A, 0); g.addEdge(B, A, 3); g.addEdge(C, H, 16);
g.addEdge(D, J, 16); g.addEdge(E, F, 11); g.addEdge(F, G, 9);
g.addEdge(G, A, 1); g.addEdge(H, F, 13); g.addEdge(I, F, 11);
g.addEdge(J, A, 4); 

g.UCS(0,10)
g.all_paths()
g.optimal_path()
 
###################### 2nd option ###############
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]
    
    def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))
                    
Graph1.edges = "A,B"
Graph1.weight ="3,4"      
              
                    
