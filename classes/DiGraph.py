from GraphInterface import GraphInterface
from Edge import Edge
from node import node
from typing import Dict


class DiGraph(GraphInterface):

    def __init__(self):
        self.countEdge = 0
        self.mc = 0
        self.Nodes = {}
        self.Edges = {}


    def v_size(self) -> int:
        return len(self.Nodes)

    def e_size(self) -> int:
        return self.countEdge

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.Nodes:
            ans = {}
            for i, j in self.Edges.items():
                if id1 in j:
                    ans[i] = j[id1]
            return ans
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.Nodes:
            return self.Edges[id1]
        return {}

    def get_mc(self) -> int:
        return self.mc

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        n = node (id=node_id, p=pos)
        self.Nodes[node_id] = n
        self.Edges[node_id] = {}

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.Nodes and id2 in self.Nodes and id2 not in self.Edges[id1]:
            if self.Edges[id1] is None:
                self.Edges[id1] = {}
                self.Edges[id1][id2] = weight
            else:
                self.Edges[id1][id2] = weight
            self.countEdge += 1
            self.mc += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.Nodes:
            size_EdgeOut = self.all_out_edges_of_node(node_id)
            size_EdgeIn = self.all_in_edges_of_node(node_id)
            self.countEdge -= size_EdgeIn
            self.countEdge -= size_EdgeOut
            self.mc += size_EdgeOut + size_EdgeIn
            del (self.Edges[node_id])
            for id in size_EdgeIn.keys():
                self.remove_edge(id,node_id)
            self.Nodes.pop(node_id)
            self.mc+=1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 in self.Nodes and node_id2 in self.Nodes and (node_id1 != node_id2)):
            self.countEdge -= 1
            self.mc += 1
            self.Edges[node_id1].pop(node_id2)
            return True
        return False

    def __repr__(self):
        return "Graph{ vertexs: %s edgeOut: %s edgeIn: %s VertexsNum: %s EdgeNum: %s Mc: %s }" % (
        self.__vertexs, self.__edgesOut, self.__edgesIn, self.v_size(), self.__countEdge, self.__mc)

if __name__ == '__main__':
    graph: DiGraph = DiGraph()
    graph.add_node(1, (2, 3))
    graph.add_node(2, (2, 3))
    graph.add_node(3, (2, 3))
    graph.add_node(4, (2, 3))
    graph.add_node(5, (2, 3))
    graph.add_edge(1, 2, 50)
    graph.add_edge(1, 3, 50)
    graph.add_edge(4, 1, 50)
    print("******************************************")
    print(graph)
    graph.remove_node(1)
    print("******************************************")
    print(graph)
    # graph:DiGraph = DiGraph()
    # graph.add_node(1,(2,3))
    # graph.add_node(1,(2,3))
    # print("******************************************")
    # print(graph)
    # graph.add_edge(1, 2,50)
    # graph.add_edge(2, 1,50)
    # print("******************************************")
    # print(graph)
    # graph.add_node(2,(5,7))
    # graph.add_edge(2, 1,50)
    # graph.add_edge(1, 2,50)
    # print("******************************************")
    # print(graph)


    # graph.remove_edge(2,8)
    # graph.remove_edge(8,2)
    # graph.remove_edge(8,3)
    # print("******************************************")
    # print(graph)
    # graph.remove_edge(1,2)
    # print("******************************************")
    # print(graph)