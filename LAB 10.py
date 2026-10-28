from itertools import permutations

#Functions to solve TSP 
def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    
    min_cost = float('inf')
    best_path = None
    
    #Generate all possible tours
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start
        
        #visit each city in the permutation
        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city

#main program


n = int(input("enter the number of cities:"))

print("enter the cost matrix:")
graph =[]

for i in range(n):
    row=list(map(int, input().split()))
    graph.append(row)

start=int(input("enter the starting city (0 to {}): ".format(n-1)))

path,cost = travelling_salesman(graph, start)

print("\noptimal path", " -> ".join(map(str,path)))
print("minimum cost:",cost)