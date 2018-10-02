
class Node(object):
    def __init__(self, value):
        
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, edges = [], nodes = []):
        self.edges = edges
        self.nodes = nodes


    def insert_node(self, new_node_value):
        new_node = Node(new_node_value)
        self.nodes.append(new_node)


    def insert_edge(self, new_edge_value, node_from_val, node_to_val):

        from_found = None
        to_found = None

        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node

            if node_to_val == node.value:
                to_found = node

        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)

        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)

        new_edge = Edge(new_edge_value, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)


    def EdgeList(self):
        a = []
        for edge in self.edges:
            a.append((edge.value, edge.node_from.value, edge.node_to.value))
        return a

    def AdjencyList(self):
        adjlist = [None]*len(self.nodes)

        for edge in self.edges:
            if adjlist[edge.node_from.value]!=None:
                adjlist[edge.node_from.value].append((edge.node_to.value, edge.value))
            else:
                adjlist[edge.node_from.value] = [edge.node_to.value, edge.value]

        return adjlist

    def AdjMatrix(self):
        
            adjmatrix = [[0 for i in range(len(self.nodes)+1)] for j in range(len(self.nodes)+1)]
            for edge in self.edges:
                adjmatrix[edge.node_from.value][edge.node_to.value] = edge.value
            return adjmatrix
            
                          
        

def main():
    graph = Graph()
    graph.insert_edge(10, 1, 2)
    graph.insert_edge(11, 1, 3)
    graph.insert_edge(12, 1, 4)
    graph.insert_edge(13, 3, 4)

    print(graph.EdgeList())
    print(graph.AdjencyList())
    print(graph.AdjMatrix())
    
if __name__ == '__main__':
    main()
        











            
              
            
