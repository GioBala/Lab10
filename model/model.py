from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self.get_num_edges()
        self.get_num_nodes()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        #self.G.add_nodes_from(i for i in range(self._nodes))
        rami=[]
        for i in self.get_all_edges():
            if i[2].get("peso",0) >= int(threshold):
                rami.append(i)
        self.G.add_edges_from(rami)
        result=""
        for i in range(len(rami)):
            h1=(DAO.get_hub(rami[i][0]))
            h2=(DAO.get_hub(rami[i][1]))
            p=(rami[i][2].get("peso"))
            # print(h1)
            # print(h2)
            # print(p)
            result= result + f"{i + 1}) [{h1[0]} ({h1[1]}) -> {h2[0]} ({h2[1]})] - guadagno Medio Per Spedizione: € {p} \n"
        #print(result)
        return len(self.G.nodes), len(rami),result


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        self._edges = DAO.get_num_archi()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        self._nodes = DAO.get_num_nodi()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        result=[]
        for i in range(self._nodes):
            for j in range(i,self._nodes):
                result.append((i,j,{"peso":DAO.get_arco(i,j)}))
        return result




