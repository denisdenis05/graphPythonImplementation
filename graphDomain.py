from copy import deepcopy

class Graph:
    def __init__(self):
        self.__nodes = {}  # nodes = {nodeId1: True, nodeId2: True, ...}
        self.__edgeIds = {}  # edge[edgeId] = (source, destination)
        self.__edges = {}  # edge[(source, destination)] = edgeId
        self.__edgeCosts = {}  # edge[edgeId] = cost of edge
        self.__outDegree = {}  # outDegree[edgeId] = degree
        self.__inDegree = {}  # outDegree[edgeId] = degree
        self.latestGeneratedEdgeId = 0
        self.numberOfNodes = 0

    def overwriteNodes(self, newNodesList):
        """
        Overwrites the existing list of nodes with a new list provided as an argument
        :param newNodesList: list of nodes to overwrite
        :return:
        """
        self.__nodes = newNodesList
    def overwriteEdgeIds(self, newEdgesIdsList):
        """
        Overwrites the existing dictionary of edges with a new dictionary provided as an argument
        :param newEdgesList: dictionary of edges to overwrite
        :return:
        """
        self.__edgeIds = newEdgesIdsList
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
        newEdgeIdsList = deepcopy(self.__edgeIds)
        newEdgesList = deepcopy(self.__edges)
        newEdgesCostsList = deepcopy(self.__edgesCosts)
        newGraph = Graph()
        newGraph.overwriteNodes(newNodesList)
        newGraph.overwriteEdgeIds(newEdgeIdsList)
        newGraph.overwriteEdges(newEdgesList)
        newGraph.overwriteEdgeCosts(newEdgesCostsList)
        return newGraph


    def createNode(self, nodeId):
        """
        Adds a new node to the graph with the specified node ID, has no effect if it already exists
        :param nodeId: node to add to the graph
        :return: None
        """
        self.__nodes[nodeId] = True
        if nodeId not in self.__outDegree:
            self.__outDegree[nodeId] = 0
        if nodeId not in self.__inDegree:
            self.__inDegree[nodeId] = 0

    def removeNode(self, nodeId):
        """
        Removes the node with the specified ID from the graph, along with any incident edges
        :param nodeId: node to remove from the graph
        :return: True if node was removed, False if not in graph
        """
        if nodeId in self.__nodes.keys():
            self.__nodes.pop(nodeId)
            edges = list(self.__edgeIds.keys())
            for edgeId in edges:
                edgeEndpoints = self.__edgeIds[edgeId]
                if edgeEndpoints[0] == nodeId or edgeEndpoints[1] == nodeId:
                    self.__edgeIds.pop(edgeId)
                    self.__edges.pop(edgeEndpoints)
            return True
        else:
            return False


    def checkIfNodeExists(self, nodeId):
        """
        Checks if a node with the specified ID exists in the graph
        :param nodeId: node id to check if in the graph
        :return: True if node is in the graph, False otherwise
        """
        if nodeId not in self.__nodes.keys():
            return False
        return True

    def checkIfExistsEdgeFromNodeToNode(self, node1, node2):
        """
        Checks if an edge exists between two specified nodes
        :param node1: source node
        :param node2: destination node
        :return: the Edge ID if found, -1 if does not exist
        """
        edgeEndpoints = (node1, node2)
        if edgeEndpoints in self.__edges:
            return self.__edges[edgeEndpoints]
        return -1


    def addEdge(self, source, target, edgeId, cost=0):
        """
        Adds a new edge to the graph with the specified source and target nodes, edge ID, and optionally, cost
        :param source: the source node
        :param target: the destination node
        :param edgeId: the given edge id
        :param cost: the cost of the edge (optional, will be set as 0 if not specified)
        :return: None
        """
        self.__edgeIds[edgeId] = (source, target)
        self.__edges[(source, target)] = edgeId
        self.__edgeCosts[edgeId] = cost
        if source in self.__inDegree:
            self.__inDegree[source] += 1
        else:
            self.__inDegree[source] = 1
        if target in self.__outDegree:
            self.__outDegree[target] += 1
        else:
            self.__outDegree[target] = 1


    def removeEdgeById(self, edgeId):
        """
        Removes the edge with the specified ID from the graph
        :param edgeId: the edge ID
        :return: True if the edge was removed, False if not in graph
        """
        if edgeId not in self.__edgeIds:
            return False
        edgeEndpoints = self.__edgeIds.pop(edgeId)
        self.__edges.pop(edgeEndpoints)
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
        self.__edgeIds.pop(edgeId)
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

    def getEdgeCost(self, edgeId):
        """
        Gets the cost of the edge with the specified ID to the provided cost value
        :param edgeId: the edge ID
        :param cost: the cost to set
        :return: None
        """
        return self.__edgeCosts[edgeId]

    def getNumberOfNodes(self):
        """
        Returns the total number of nodes in the graph
        :return: the total number of nodes
        """
        return self.numberOfNodes


    def getNumberOfEdges(self):
        """
        Returns the total number of edges in the graph
        :return: the total number of edges
        """
        return len(self.__edgeIds)


    def getEdgeEndpoints(self, edgeId):
        """
        Returns a tuple containing the source and destination nodes of the edge with the specified ID.
        :param edgeId: the edge ID
        :return: a tuple (source, destination)
        """
        if edgeId not in self.__edgeIds:
            return None
        return self.__edgeIds[edgeId]

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
        return self.__outDegree[source]

    def getInDegree(self, destination):
        """
        Returns the inner degree of the specified node
        :param destination: the node too check for its degree
        :return: the node inner degree
        """
        return self.__inDegree[destination]

    def getOutEdges(self, source):
        """
        Returns a dictionary containing all outgoing edges from the specified source node, with edge IDs as keys and endpoints as values
        :param source: the node too check for its outgoing edges
        :return: a dictionary of outgoing edges
        """
        outEdges = {}
        for edgeId in self.__edgeIds:
            if self.__edgeIds[edgeId][0] == source:
                outEdges[edgeId] = self.__edgeIds[edgeId]
        return outEdges

    def getInEdges(self, destination):
        """
        Returns a dictionary containing all incoming edges to the specified destination node, with edge IDs as keys and endpoints as values
        :param destination: the node too check for its incoming edges
        :return: a dictionary of incoming edges
        """
        inEdges = {}
        for edgeId in self.__edgeIds:
            if self.__edgeIds[edgeId][1] == destination:
                inEdges[edgeId] = self.__edgeIds[edgeId]
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
        return self.__edgeIds[edgeId]


    def parseNodes(self):
        """
        Generator function that yields each node in the graph
        :return: an iterator with each node in the graph
        """
        for nodeId in self.__nodes.keys():
            yield nodeId
    def parseEdges(self):
        """
        Generator function that yields each edge ID in the graph
        :return: an iterator with each edge in the graph
        """
        for edge in self.__edgeIds.keys():
            yield edge

    def parseOutboundEdges(self, nodeId):
        """
        Generator function that yields each outbound edge ID from the specified node
        :param nodeId: the node ID
        :return: an iterator with each outbound edge for the specified node
        """
        for edgeId in self.__edgeIds.keys():
            if self.__edgeIds[edgeId][0] == nodeId:
                yield edgeId

    def parseInboundEdges(self, nodeId):
        """
        Generator function that yields each inbound edge ID to the specified node
        :param nodeId: the node ID
        :return: an iterator with each inbound edge for the specified node
        """
        for edgeId in self.__edgeIds.keys():
            if self.__edgeIds[edgeId][1] == nodeId:
                yield edgeId

