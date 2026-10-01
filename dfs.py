nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


edges = [(0, 29),
 (0, 46),
 (0, 21),
 (0, 14),
 (0, 38),
 (0, 31),
 (1, 41),
 (1, 31),
 (1, 21),
 (1, 17),
 (2, 9),
 (2, 26),
 (2, 5),
 (2, 25),
 (2, 4),
 (3, 18),
 (3, 30),
 (3, 47),
 (4, 28),
 (4, 9),
 (4, 8),
 (5, 44),
 (5, 12),
 (6, 37),
 (6, 10),
 (7, 23),
 (7, 22),
 (7, 39),
 (9, 19),
 (9, 28),
 (9, 27),
 (11, 33),
 (13, 25),
 (13, 38),
 (13, 29),
 (14, 26),
 (14, 28),
 (14, 39),
 (15, 22),
 (15, 31),
 (15, 19),
 (15, 41),
 (16, 46),
 (16, 26),
 (16, 38),
 (16, 27),
 (17, 40),
 (17, 29),
 (18, 45),
 (18, 42),
 (18, 35),
 (18, 33),
 (18, 47),
 (20, 36),
 (20, 49),
 (20, 42),
 (22, 26),
 (22, 34),
 (23, 31),
 (23, 32),
 (23, 40),
 (24, 31),
 (24, 44),
 (25, 38),
 (26, 31),
 (27, 32),
 (29, 48),
 (29, 41),
 (30, 47),
 (30, 37),
 (33, 36),
 (33, 49),
 (34, 48),
 (35, 45),
 (36, 45),
 (37, 49),
 (37, 45),
 (37, 47),
 (38, 41),
 (40, 48),
 (41, 44),
 (42, 49),
 (43, 48),
 (45, 47)]

graph = {} #creamos diccionario para la lista de adyacencia

for node in nodes:
    graph[node] = [] # lo llenamos de todos los nodos posibles

for u, v in edges: #para cada vertice lo metemos en su nodo correspondiente
    graph[u].append(v) #como es un grafo no dirigido debemos de meter para cada nodo a que otro nodo va
    graph[v].append(u) #si no se hace asi estariamos creando una arista dirigida

visited = set() #creamos set para los visited que no se repitan
components = [] # creamos lista donde vamos a contener los nodos de cada conjunto

def dfs(node,graph,visited,component): #dfs que recibe el nodo inicial, el graph y las listas
    
    visited.add(node) #visited en general
    component.add(node) #visited para cada conjunto

    for n in graph[node]: #buscamos las aristas de cada nodo
        if n not in visited: # si no estan visitadas
            dfs(n,graph,visited,component) #buscamos los hijos de ese nodo



for node in nodes:#for para revisar que todos los nodos esten visitados

    if node not in visited: #si no se han visitado debemos de hacerles DFS
        component = set() #se crea un nuevo set con los nodos visitados
        dfs(node, graph, visited, component) #se hace dfs con ese nodo nuevo
        components.append(component) #se agrega el component a la lista de components

print("Componentes:", len(components)) #2
print("Visitados:", len(visited)) #50
print(components)
#[{0, 1, 2, 4, 5, 7, 8, 9, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 38, 39, 40, 41, 43, 44, 46, 48}, 
# {33, 35, 3, 36, 37, 6, 10, 11, 42, 45,47, 49, 18, 20, 30}]