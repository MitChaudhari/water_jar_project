from collections import deque
import collections
"""
Author: Mitansh Chaudhari, Outline: Prof. Xiaolong Wang
CS-Data Structures and Algorithms 
Date: Nov-28-2022 

The goal of the project is to use the Breadth First Search 
to find the shortest paths from given jar volumes to the 
target. 

"""
class Graph:
    
    class GraphNode:
        def __init__(self, jar1 = 0, jar2 = 0, jar3 = 0, color = "white", pi = None):
            self.jar1 = jar1
            self.jar2 = jar2
            self.jar3 = jar3
            self.color = color
            self.pi = pi

        def __str__(self):
            print("({}, ".format(self.jar1)+ "{}, ".format(self.jar2) + "{})".format(self.jar3)+"\n")
        
            return("Done")

        def __repr__(self):
            return str(self)

    def __init__(self, jl1 = 0, jl2 = 0, jl3 = 0, target = 0):
        self.jl1 = jl1
        self.jl2 = jl2
        self.jl3 = jl3
        self.target = target
        self.V = {}
        for x in range(jl1 + 1):
            for y in range(jl2 + 1):
                for z in range(jl3 + 1):
                    node = Graph.GraphNode(x, y, z, "white", None)
                    self.V[node] = None

    def isFound(self, a: GraphNode) -> bool:
        if a.jar3 == self.target or a.jar2 == self.target or a.jar1 == self.target:
            return True
        else:
            return False
        
    def isAdjacent(self, a: GraphNode, b: GraphNode) -> bool:
        if a.jar1 > 0 and b.jar1 == 0 and a.jar2 == b.jar2 and a.jar3 == b.jar3:
            return True

        elif a.jar2 > 0 and b.jar2 == 0 and a.jar1 == b.jar1 and a.jar3 == b.jar3:
            return True

        elif a.jar3 > 0 and b.jar3 == 0 and a.jar1 == b.jar1 and a.jar2 == b.jar2:
            return True
        
        elif a.jar1 < self.jl1 and b.jar1 == self.jl1 and a.jar2 == b.jar2 and a.jar3 == b.jar3:
            return True

        elif a.jar2 < self.jl2 and b.jar2 == self.jl2 and a.jar1 == b.jar1 and a.jar3 == b.jar3:
            return True

        elif a.jar3 < self.jl3 and b.jar3 == self.jl3 and a.jar1 == b.jar1 and a.jar2 == b.jar2:
            return True
        
        elif a.jar1 > 0 and a.jar2 < self.jl2 and b.jar1 == a.jar1 - min(a.jar1, self.jl2 - a.jar2) and b.jar2 == a.jar2 + min(a.jar1, self.jl2 - a.jar2) and a.jar3 == b.jar3:
            return True
        
        elif a.jar1 > 0 and a.jar3 < self.jl3 and b.jar1 == a.jar1 - min(a.jar1, self.jl3 - a.jar3) and b.jar3 == a.jar3 + min(a.jar1, self.jl3 - a.jar3) and a.jar2 == b.jar2:
            return True

        elif a.jar2 > 0 and a.jar1 < self.jl1 and b.jar2 == a.jar2 - min(a.jar2, self.jl1 - a.jar1) and b.jar1 == a.jar1 + min(a.jar2, self.jl1 - a.jar1) and a.jar3 == b.jar3:
            return True

        elif a.jar2 > 0 and a.jar3 < self.jl3 and b.jar2 == a.jar2 - min(a.jar2, self.jl3 - a.jar3) and b.jar3 == a.jar3 + min(a.jar2, self.jl3 - a.jar3) and a.jar1 == b.jar1:
            return True

        elif a.jar3 > 0 and a.jar1 < self.jl1 and b.jar3 == a.jar3 - min(a.jar3, self.jl1 - a.jar1) and b.jar1 == a.jar1 + min(a.jar3, self.jl1 - a.jar1) and a.jar2 == b.jar2:
            return True

        elif a.jar3 > 0 and a.jar2 < self.jl2 and b.jar3 == a.jar3 - min(a.jar3, self.jl2 - a.jar2) and b.jar2 == a.jar2 + min(a.jar3, self.jl2 - a.jar2) and a.jar1 == b.jar1:
            return True
        else:
            return False

    def BFS(self) -> []:
        queue = deque()
        queue.append(list(self.V.keys())[0])
        while queue:
            u = queue.popleft()
            u.color = "black"
            for val in self.V.keys():
                if self.isAdjacent(u, val) and val.color == "white":
                    val.color = "yellow"
                    val.pi = u 
                    queue.append(val)
                    if self.isFound(val):
                        path = []
                        while val.pi:
                            path.append(val)
                            val = val.pi
                        path.append(val)
                        return path[::-1]
                    
        return "No such series of operations exist, Please try Again."
    
if __name__ == "__main__":
    jar1 = 0
    jar2 = 0 
    jar3 = 0
    target = 0
    print("Lets set the volume for the jars and the target value.\n")
    
    while True:
        try:
            jar1 = int(input("Please enter first jar volume between 1 to 9: "))
            if jar1 < 1 or jar1 > 9:
                raise ValueError 
            break
        except ValueError:
            print("Invalid input...")
    
    while True:
        try:
            jar2 = int(input("Please enter second jar volume between 1 to 9: "))
            if jar2 < 1 or jar2 > 9:
                raise ValueError
            break
        except ValueError:
            print("Invalid input...")
    
    while True:       
        try:
            jar3 = int(input("Please enter third jar volume between 1 to 9: "))
            if jar3 < 1 or jar3 > 9:
                raise ValueError 
            break
        except ValueError:
            print("Invalid input...")
    
    while True:
        max_water = max(jar1, jar2, jar3)       
        try:
            target = int(input("Enter the target value between (1 - {0}) to get a valid output: ".format(max_water)))
            x = str(target).isnumeric()
    
            if x == False:
                raise ValueError
            break         
        except ValueError:
            print("Enter an integer...")
    
    graph = Graph(jar1, jar2, jar3, target )
    print(graph.BFS())
    # graph = Graph(3, 5, 7, 4)
    # print(graph.BFS())
    # graph2 = Graph(1, 2, 1, 2)
    # print(graph2.BFS())
    