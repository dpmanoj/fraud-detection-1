
class Graph(object):

    def __init__(self, structure=None):

        if structure is None:
            structure = dict()

        self.__structure = structure

    def add_vertex(self, v):
        self.__structure[v] = list()

    def add_edge(self, e):
        self.__structure[e[0]].append(e[1])
        self.add_vertex(e[1])
        self.__structure[e[1]].append(e[0])

    def get_all_vertex(self):
        return self.__structure.keys()

    def is_connected(self, e):
        e1 = self.__structure.get(e[0])
        e2 = self.__structure.get(e[1])

        if e[0] in e2 and e[1] in e1:
            return True

        return False

    def same_network(self, e):
        return self.is_connected(e)

    def __str__(self):
        return str(self.__structure)
