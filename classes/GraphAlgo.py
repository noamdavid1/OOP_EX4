from typing import List
import Js as Js
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from classes.DiGraph import DiGraph
import json
import math
from queue import PriorityQueue
import random
import matplotlib.pyplot as plt
from typing import Dict

class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph = DiGraph()):
        self.__g: DiGraph = graph


    def init_graph(self, g: GraphInterface) -> None:
        """
        Init the graph on which this set of algorithms operates on.
        :param g:the graph
        :return:None
        """
        self.__g = g

    def get_graph(self) -> GraphInterface:
        return self.__g

    def load_from_json(self, file_name: str) -> bool:
        try:
            new_graph = DiGraph()
            with open(file_name, 'r') as reader:
                json_graph = Js.load(reader)
                reader.close()
                edges = json_graph["Edges"]
                nodes = json_graph["Nodes"]
                for x in nodes:
                    pos = None
                    if 'pos' in x:
                        posString = x["pos"].split(",")
                        pos = (float(posString[0]), float(posString[1]),
                               float(posString[2]))
                    new_graph.add_node(int(x["id"]),
                                       pos)
                for x in edges:
                    new_graph.add_edge(int(x["src"]), int(x["dest"]), float(x["w"]))
                self.__g = new_graph
                return True
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
       pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        all_vertex = self.__g.get_all_v()
        #validation
        if id1 not in all_vertex or id2 not in all_vertex:
            return math.inf, []
        if id1 is id2:
            return 0, list(id1)

        #init all vertexs
        self.__init_all_vertex()

        queue = PriorityQueue()
        src:Vertex = all_vertex.get(id1)
        src.w = 0
        queue.put(src)

        while not queue.empty():
            #v = queue.get()[1]
            v:Vertex = queue.get()
            for edge in self.__g.all_out_edges_of_node(v.get_id()).values():
                u = all_vertex.get(edge.get_dest())
                dist = edge.get_w() + v.w
                if dist < u.w:
                    u.w = dist
                    u.info = v.get_id()
                    queue.put(u)

        dest: Vertex = all_vertex.get(id2)
        if dest.w is math.inf:
            return math.inf, []

        path = []
        path.append(dest.get_id())
        str = dest.info
        while str != "":
            node:Vertex = all_vertex.get(int(str))
            path.insert(0, node.get_id())
            str = node.info
        return dest.w,path

    def __init_all_vertex(self):
        for v in self.__g.get_all_v().values():
            v: Vertex = v
            v.info = ""
            v.tag = 0
            v.w = math.inf

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        path = []  # the list that represents the path
        dist = 0  # the number that represents the all path distance
        if len(node_lst) > 0:
            path.append(node_lst[0])
            src_node = node_lst[0]
            for n in node_lst[1:]:
                cal = self.shortest_path(src_node, n)
                dist += cal[0]
                route = cal[1]
                src_node = n
                for v in route[1:]:
                    path.append(v)

        return path, dist

    def centerPoint(self) -> (int, float):
        vertexs: Dict[int, Vertex] = dict()
        j = 0
        for i in self.__g.get_all_v():
            Min_Center = self.shortest_path(vertexs[i].getId(), vertexs[j].getId())
            if Min_Center > self.shortest_path(vertexs[i + 1], vertexs[j + 1]):
                Min_Center = self.shortest_path(vertexs[i + 1], vertexs[j + 1])
            j += 1
        return Min_Center

    def plot_graph(self) -> None:
        all_nodes = self.graph.get_all_v()
        x = []
        y = []
        for i in all_nodes.values():
            if i.getPos() is None:
                random_x = random.uniform(0, 100)
                random_y = random.uniform(0, 100)
                i.setPos((random_x, random_y, 0.0))
                x.append(random_x)
                y.append(random_y)
            else:
                x.append(i.getPos()[0])
                y.append(i.getPos()[1])

        n = [j for j in all_nodes.keys()]
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        for p, txt in enumerate(n):
            ax.annotate(n[p], (x[p], y[p]))
        plt.plot(x, y, "black")
        for i in all_nodes.keys():
            for j in self.graph.all_out_edges_of_node(i):
                x1_coordinate = all_nodes.get(i).getPos()[0]
                y1_coordinate = all_nodes.get(i).getPos()[1]
                x2_coordinate = all_nodes.get(j).getPos()[0]
                y2_coordinate = all_nodes.get(j).getPos()[1]
                plt.arrow(x1_coordinate, y1_coordinate, (x2_coordinate - x1_coordinate),
                          (y2_coordinate - y1_coordinate), length_includes_head=True, width=0.00001,
                          head_width=0.00032, color='black')
        plt.ylabel("y")
        plt.title("Ex3")
        plt.xlabel("x")
        plt.title("My DiGraph")
        plt.show()
