from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._idMap = {}
        self._listSighting = []
        self._listStates = []

        self._grafo = nx.Graph()
        self._nodes = []
        self._edges = []

        self.loadSighting()
        self.loadStates()

    def loadSighting(self):
        self._listSighting = DAO.get_all_sightings()

    def loadStates(self):
        self._listStates = DAO.get_all_states()

    @property
    def listSighting(self):
        return self._listSighting

    @property
    def listStates(self):
        return self._listStates

    def buildGraph(self, s, a):
        self._grafo.clear()
        self._nodes.clear()
        for state in self._listStates:
            if s == state.name:
                S_id = state.id

        for x in self._listSighting:
            if x.state.upper() == S_id and str(x.datetime.year) == a:
                self._nodes.append(x)
        self._grafo.add_nodes_from(self._nodes)

        #edges modo programmatico

        for i in range(0, len(self._nodes) - 1):
            for j in range(i+1, len(self._nodes)):
                if self._nodes[i].shape == self._nodes[j].shape and self._nodes[i].distance_HV(self._nodes[j])<100:
                    self._grafo.add_edge(self._nodes[i],self._nodes[j])
    def get_num_connesse(self):
        return nx.number_connected_components(self._grafo)

    def get_largest_connessa(self):
        conn = list(nx.connected_components(self._grafo))
        conn.sort(key=lambda x: len(x), reverse=True)
        return conn[0]

    def get_nodes(self):
        return self._grafo.nodes()

    def get_edges(self):
        return list(self._grafo.edges(data=True))

    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self._grafo.number_of_edges()

