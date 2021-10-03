def graph_to_table(x,y,z): #x-массив с графом у-массив куда записать таблицу смежности z-костыль
    for i in range(len(x)):
        for j in range(len(x[i])):
            if int(x[i][j])==1:
                z.append(j)
        y.append(list(z))
        z.clear()

def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

n=int(input())
a=[]
table=[]
temp=[]
visited=[]
queue=[]

for i in range(n):
    a.append(input().split())
graph_to_table(a,table,temp)


print(table)
aim=int(input())
bfs(visited,table, aim)