from copy import deepcopy

class Graph:
    def __init__(self):
        self.__nodes = []  # nodes = [nodeId1, nodeId2, ...]
        self.__edges = {}  # edge[edgeId] = (source, destination)
        self.__edgeCosts = {}  # edge[edgeId] = cost of edge
        self.latestGeneratedEdgeId = 0

    def overwriteNodes(self, newNodesList):
        """
        Overwrites the existing list of nodes with a new list provided as an argument
        :param newNodesList: list of nodes to overwrite
        :return:
        """
        self.__nodes = newNodesList
    def overwriteEdges(self, newEdgesList):
        """
        Overwrites the existing dictionary of edges with a new dictionary provided as an argument
        :param newEdgesList: dictionary of edges to overwrite
        :return:
        """
        self.__edges = newEdgesList
    def overwriteEdgeCosts(self, newEdgesCostList):
        """
        Overwrites the existing dictionary of edge costs with a new dictionary provided as an argument
        :param newEdgesCostList: dictionary of edges of costs to overwrite
        :return:
        """
        self.__edgesCosts = newEdgesCostList

    def copyGraph(self):
        """
        Creates a deep copy of the graph object and returns it
        :return: a copy of the graph, type Graph
        """
        newNodesList = deepcopy(self.__nodes)
        newEdgesList = deepcopy(self.__edges)
        newEdgesCostsList = deepcopy(self.__edgesCosts)
        newGraph = Graph()
        newGraph.overwriteNodes(newNodesList)
        newGraph.overwriteEdges(newEdgesList)
        newGraph.overwriteEdgeCosts(newEdgesCostsList)
        return newGraph


    def createNode(self, nodeId):
        """
        Adds a new node to the graph with the specified node ID if it does not already exist
        :param nodeId: node to add to the graph
        :return: True if the node was added, False if already added
        """
        if nodeId not in self.__nodes:
            self.__nodes.append(nodeId)
            return True
        else:
            return False

    def removeNode(self, nodeId):
        """
        Removes the node with the specified ID from the graph, along with any incident edges
        :param nodeId: node to remove from the graph
        :return: True if node was removed, False if not in graph
        """
        if nodeId in self.__nodes:
            for nodeNr in range(len(self.__nodes)):
                if self.__nodes[nodeNr] == nodeId:
                    self.__nodes.pop(nodeNr)
            for edgeId in self.__edges:
                if self.__edges[edgeId][0] == nodeId or self.__edges[edgeId][1] == nodeId:
                    self.__edges.pop(edgeId)
            return True
        else:
            return False


    def checkIfNodeExists(self, nodeId):
        """
        Checks if a node with the specified ID exists in the graph
        :param nodeId: node id to check if in the graph
        :return: True if node is in the graph, False otherwise
        """
        if nodeId not in self.__nodes:
            return False
        return True

    def checkIfExistsEdgeFromNodeToNode(self, node1, node2):
        """
        Checks if an edge exists between two specified nodes
        :param node1: source node
        :param node2: destination node
        :return: the Edge ID if found, -1 if does not exist
        """
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == node1 and self.__edges[edgeId][1] == node2:
                return edgeId
        return -1



    def addEdge(self, source, target, edgeId, cost=0):
        """
        Adds a new edge to the graph with the specified source and target nodes, edge ID, and optionally, cost
        :param source: the source node
        :param target: the destination node
        :param edgeId: the given edge id
        :param cost: the cost of the edge (optional, will be set as 0 if not specified)
        :return: True if edge was added, False if edge from source to destination already exists
        """
        if self.checkIfExistsEdgeFromNodeToNode(source, target) != -1:
            return False
        self.__edges[edgeId] = (source, target)
        self.__edgeCosts[edgeId] = cost
        return True

    def removeEdgeById(self, edgeId):
        """
        Removes the edge with the specified ID from the graph
        :param edgeId: the edge ID
        :return: True if the edge was removed, False if not in graph
        """
        if edgeId not in self.__edges:
            return False
        self.__edges.pop(edgeId)
        self.__edgeCosts.pop(edgeId)
        return True

    def removeEdgeByNodes(self, source, destination):
        """
        Removes the edge between the specified source and destination nodes from the graph
        :param source: the source node
        :param destination: the destination node
        :return: True if the edge was removed, False if not in graph
        """
        edgeId = self.checkIfExistsEdgeFromNodeToNode(source, destination)
        if edgeId == -1:
            return False
        self.__edges.pop(edgeId)
        self.__edgeCosts.pop(edgeId)
        return True


    def setEdgeCost(self, edgeId, cost):
        """
        Sets the cost of the edge with the specified ID to the provided cost value
        :param edgeId: the edge ID
        :param cost: the cost to set
        :return: None
        """
        self.__edgeCosts[edgeId] = cost

    def getNumberOfNodes(self):
        """
        Returns the total number of nodes in the graph
        :return: the total number of nodes
        """
        return len(self.__nodes)

    def getNumberOfEdges(self):
        """
        Returns the total number of edges in the graph
        :return: the total number of edges
        """
        return len(self.__edges)


    def getEdgeEndpoints(self, edgeId):
        """
        Returns a tuple containing the source and destination nodes of the edge with the specified ID.
        :param edgeId: the edge ID
        :return: a tuple (source, destination)
        """
        if edgeId not in self.__edges:
            return None
        return self.__edges[edgeId]

    def hasEdge(self, source, destination):
        """
        Checks if there exists an edge between the specified source and target nodes
        :param source: the source node
        :param destination: the destination node
        :return: the edge ID if found, False otherwise
        """
        if self.checkIfExistsEdgeFromNodeToNode(source, destination) == -1:
            return False
        return self.checkIfExistsEdgeFromNodeToNode(source, destination)

    def getOutDegree(self, source):
        """
        Returns the outer degree of the specified node
        :param source: the node too check for its degree
        :return: the node outer degree
        """
        degree = 0
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == source:
                degree += 1
        return degree

    def getInDegree(self, destination):
        """
        Returns the inner degree of the specified node
        :param destination: the node too check for its degree
        :return: the node inner degree
        """
        degree = 0
        for edgeId in self.__edges:
            if self.__edges[edgeId][1] == destination:
                degree += 1
        return degree

    def getOutEdges(self, source):
        """
        Returns a dictionary containing all outgoing edges from the specified source node, with edge IDs as keys and endpoints as values
        :param source: the node too check for its outgoing edges
        :return: a dictionary of outgoing edges
        """
        outEdges = {}
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == source:
                outEdges[edgeId] = self.__edges[edgeId]
        return outEdges

    def getInEdges(self, destination):
        """
        Returns a dictionary containing all incoming edges to the specified destination node, with edge IDs as keys and endpoints as values
        :param destination: the node too check for its incoming edges
        :return: a dictionary of incoming edges
        """
        inEdges = {}
        for edgeId in self.__edges:
            if self.__edges[edgeId][1] == destination:
                inEdges[edgeId] = self.__edges[edgeId]
        return inEdges


    def getEdgeIdPrice(self, edgeId):
        """
        Returns the cost associated with the edge specified by the given edge ID
        :param edgeId: the edge ID
        :return: the cost of the edge
        """
        return self.__edgeCosts[edgeId]


    def getEdgeNodesPrice(self, source, destination):
        """
        Returns the edge ID and cost associated with the edge between the specified source and destination nodes
        :param source: the source node
        :param destination: the destination node
        :return: the cost of the edge
        """
        edgeId = self.checkIfExistsEdgeFromNodeToNode(source, destination)
        if edgeId == -1:
            return False
        return self.__edges[edgeId]


    def parseNodes(self):
        """
        Generator function that yields each node in the graph
        :return: an iterator with each node in the graph
        """
        for nodeId in self.__nodes:
            yield nodeId

    def parseEdges(self):
        """
        Generator function that yields each edge ID in the graph
        :return: an iterator with each edge in the graph
        """
        for edge in self.__edges:
            yield edge

    def parseOutboundEdges(self, nodeId):
        """
        Generator function that yields each outbound edge ID from the specified node
        :param nodeId: the node ID
        :return: an iterator with each outbound edge for the specified node
        """
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == nodeId:
                yield edgeId

    def parseInboundEdges(self, nodeId):
        """
        Generator function that yields each inbound edge ID to the specified node
        :param nodeId: the node ID
        :return: an iterator with each inbound edge for the specified node
        """
        for edgeId in self.__edges:
            if self.__edges[edgeId][1] == nodeId:
                yield edgeId

