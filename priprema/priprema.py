import math
global new_path_list

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, d1 = None, d2 = math.inf):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.p = None
        self.d1 = d1
        self.d2 = d2
        self.list = list()

class InDegrees:
    def __init__(self, d1 = None, in_degrees = None):
        self.d1 = d1
        self.in_degrees = in_degrees

class OutDegrees:
    def __init__(self, d1 = None, out_degrees = None):
        self.d1 = d1
        self.out_degrees = out_degrees


class Edge:
    def __init__(self, source = None, destination = None, weight = None):
        self.source = source;
        self.destination = destination
        self.weight = weight

def MakeGraph():
    vertex_list = list()
    a = Vertex(d1 = 'a')
    b = Vertex(d1 = 'b')
    c = Vertex(d1 = 'c')
    d = Vertex(d1 = 'd')
    e = Vertex(d1 = 'e')
    f = Vertex(d1 = 'f')
    g = Vertex(d1 = 'g')

    a.list.append(Edge(a,b,8))
    a.list.append(Edge(a,c,6))
    
    b.list.append(Edge(b,d,10))

    c.list.append(Edge(c,d,15))
    c.list.append(Edge(c,e,9))

    d.list.append(Edge(d,e,14))
    d.list.append(Edge(d,f,4))

    e.list.append(Edge(e,f,13))
    e.list.append(Edge(e,g,17))

    f.list.append(Edge(f,g,7))
    
    
    vertex_list.append(a)
    vertex_list.append(b)
    vertex_list.append(c)
    vertex_list.append(d)
    vertex_list.append(e)
    vertex_list.append(f)
    vertex_list.append(g)

    return vertex_list


def PrintGraph(vertex_list):
    for i in vertex_list:
        print("-->",i.d1)
        for j in i.list:
            print(">>>>>>",j.destination.d1, "-->",j.weight)    


def GetInDegrees(graph):
    in_degrees_list = list()

    for i in graph:
        k = InDegrees(i.d1, 0)
        in_degrees_list.append(k)

    for i in graph:
        for j in i.list:
            for k in in_degrees_list:
                if j.destination.d1 == k.d1:
                    k.in_degrees += 1
    
    return in_degrees_list

def GetOutDegrees(graph):
    out_degrees_list = list()
    
    for i in graph:
        outs = len(i.list)
        k = OutDegrees(i.d1, outs)
        out_degrees_list.append(k)
        
    return out_degrees_list
    
def initialize_single_source(G,s):
    for v in G:
        v.d2 = math.inf
        v.p = None
    s.d2 = 0

def relax(u, v, w):    
    if v.d2 > u.d2 + w:
        v.d2 = u.d2 + w
        v.p = u

def BellMan_Ford(G,w,s):    
    initialize_single_source(G,s)
    for i in G:
        for j in i.list:
            relax(j.source, j.destination, j.weight)
    for i in G:
        for j in i.list:
            if j.destination.d2 > j.source.d2 + j.weight:
                return False
    return True

def ShortestPath(graph, A, B):
    shortest_path_list = list()
    
    BellMan_Ford(graph, 0, graph[0])
    w = B.d2
    parent = B.p
    shortest_path_list.append(B)

    while parent != A:
        shortest_path_list.append(parent)
        parent = parent.p
    shortest_path_list.append(A)
    shortest_path_list = shortest_path_list[::-1]

    return shortest_path_list,w
    
def UpdateEdge(graph, A, B, weight):
    flag = 0
    for i in A.list:
        if i.destination == B:
            i.weight = weight
            flag = 1
    if flag == 0:
        A.list.append(Edge(A,B,weight))
   
def NewShortestPath():
    global new_path_list
    tmp = list()
    w = 0

    BellMan_Ford(new_path_list, 0, new_path_list[0])
    tmp, w = ShortestPath(new_path_list, new_path_list[0], new_path_list[6])
    for i in tmp:
        print(i.d1)
    print(w)

if __name__ == "__main__":
    global new_path_list

    vertex_list = list()
    out_degrees_list = list()
    in_degrees_list = list()
    shortest_path_list = list()
    new_path_list = list()

    vertex_list = MakeGraph()
    
    PrintGraph(vertex_list)
    
    print("------------------------------------------------\nGetInDegrees\n")
    in_degrees_list = GetInDegrees(vertex_list)
    for i in in_degrees_list:
        print(i.d1, " -> ", i.in_degrees)

    print("------------------------------------------------\nGetOutDegrees\n")
    out_degrees_list = GetOutDegrees(vertex_list)
    for i in out_degrees_list:
        print(i.d1, " -> ", i.out_degrees)

    
    print("------------------------------------------------\nShortestPath\n")
    BellMan_Ford(vertex_list, 0, vertex_list[0])
    shortest_path_list, w = ShortestPath(vertex_list, vertex_list[0], vertex_list[6])
    for i in shortest_path_list:
        print(i.d1)
    print(w)


    print("------------------------------------------------\nUpdateEdge and NewShortestPath\n")
    UpdateEdge(vertex_list, vertex_list[1], vertex_list[2], -6)
    for i in vertex_list:
        new_path_list.append(i)
    NewShortestPath()
    
    

    