import math

class node:


    def __init__(self, id: int, p: tuple = None, **kwargs) -> None:
        self.id = id
        self.tag = 0
        self.weight = math.inf
        self.info = "f"
        self.pos = p
        self.edge_out = 0
        self.edge_in = 0

    def __str__(self) -> str:
        return f"{self.id}:|edges out| {self.edge_out} |edges in| {self.edge_in}"

    def __repr__(self) -> str:
        return f"{self.id}:|edges out| {self.edge_out} |edges in| {self.edge_in}"

    def __eq__(self, o: object) -> bool:
        if not (isinstance(o, node)):
            return False
        return self.id == o.id

    def __lt__(self, other):
        return self.weight < other.weight

    def __hash__(self) -> int:
        return self.id

    def getkey(self) -> int:
        return self.id

    def gettag(self) -> int:
        return self.tag

    def getweight(self) -> float:
        return self.weight

    def getinfo(self) -> str:
        return self.info

    def settag(self, tag: int) -> None:
        self.tag = tag

    def setweight(self, w: float) -> None:
        self.weight = w

    def setinfo(self, info: str) -> None:
        self.info = info

    def getlocation(self) -> tuple:
        return self.pos

    def setlocation(self, pos) -> None:
        self.pos = pos