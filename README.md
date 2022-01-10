# OOP_EX4
## Authors:
Noam David-319073235
Gaya Ossi- 208575480
## Explanation:
Our final project is a Pokemon Game concentrating the algorithms from previous assignments. With the help of the algorithm we built in the previous assignments and with the help of the client algorithm and the student code algorithm we basically simulate a Pokemon game where the agents we built try to catch as many Pokemon as possible. When the game ends the customer score is printed in addition to the amount of Pokemon he caught and how long it took him to perform it.

## GraphAlgo methods
###	get_graph(self) -> GraphInterface: This method return the directed graph on which the algorithm works on.
###	load_from_json(self, file_name: str) -> bool: This method loads a graph from an existing JSON file. file_name is directorty path.
###	save_to_json(self, file_name: str) -> bool: This method is used to save the graph to JSON file. file_name is directorty path.
###	shortest_path(self, id1: int, id2: int) -> (float, list): This method returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm in pair (shortest path weight, path).
###	TSP (self, node_lst: List[int]) -> (List[int], float): This method finds the shortest path that visits all the nodes in the list.
###	plot_graph(self) -> None: This method Plots the graph. It means that if the nodes have a position, the nodes will be placed there, Otherwise, they will be placed in a random but elegant manner.

## DiGraph methods
###	v_size(self) -> int: This method return the number of vertices in the graph, in Integer.
###	e_size(self) -> int: This method return the number of edges in the graph, in Integer.
###	get_all_v(self) -> dict: This method return a dictionary of all the nodes in the graph, each node is represented using a pair (node_id, node_data).
###	all_in_edges_of_node(self, id1: int) -> dict: This method return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair (other_node_id, weight).
###	all_out_edges_of_node(self, id1: int) -> dict: This method return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight).
###	get_mc(self) -> int: This method method returns integer representing the current version of graph, each change in the state of the graph should change this number.
###	add_node(self, node_id: int, pos: tuple) -> bool: This method method adds node to graph with node_id as it's key and pos and it's postion, if not given position add node without one.
###	add_edge(self, id1: int, id2: int, weight: float) -> bool: This method method adds an edge from node with key od id1 to node with key of id2 with weight representing the weight of this edge.
###	remove_node(self, node_id: int) -> bool: This method removes a node from the graph. It received the node id we want to remove and returns true if we removed it successfully.
###	Remove_edge(self, node_id1: int, node_id2: int) ->bool: This method removes an edge from the graph. It received two nodes id and returns true if we removed theedge between them it successfully.


