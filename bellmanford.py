def bellman_ford(graph,vertex,source):
    dist=[float("inf")]*vertex
    dist[source]=0
    for i in range(vertex-1):
        for u,v,weight in graph:
            if dist[u]!=float("inf") and dist[u]+weight<dist[v]:
                dist[v]=dist[u]+weight

    for u,v,weight in graph:
        if dist[u]!=float("inf") and dist[u]+weight<dist[v]:
            print("Graph contains a negative cycle!")
    print("Shortest distance from source to vertex:")
    print(dist)
graph=[
    (0, 1, 1),
    (1, 2, -1),
    (2, 3, -1),
    (3, 1, -1) 
]
vertex=5
src=0
bellman_ford(graph,vertex,src)
