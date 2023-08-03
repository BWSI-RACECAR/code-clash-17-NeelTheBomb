class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

class Solution:
    
    def spath_algo(self, graph, start_node):
            #type graph: String Dictionary
            #type start_node: 
            #return type: int
            
            #TODO: Write code below to return an int with the solution to the prompt.
            start = graph[start_node]
            print(start)
            print(graph)

            pass

def main():
    tc1 = Solution()
    in_graph = {}
    nodes = input().split(",")
    nodes[len(nodes) - 1] = nodes[len(nodes) - 1].strip()
    for i in range (0, len(nodes) - 1):
        in_graph[nodes[i]] = {}
        edges = input().split(",")
        edges[len(edges) - 1] = edges[len(edges) - 1].strip()
        weights = input().split(" ")
        for j in range (0, len(edges)):
            in_graph[nodes[i]][edges[j]] = int(weights[j])

    graph = Graph(nodes, in_graph)
    _, shortest_path = tc1.spath_algo(graph, "Start")
    print(shortest_path["Finish"])

if __name__ == "__main__":
    main()
