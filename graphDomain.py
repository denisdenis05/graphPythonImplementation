from copy import deepcopy

class Graph:
    def __init__(self):
        self.__nodes = []  # nodes = [nodeId1, nodeId2, ...]
        self.__edges = {}  # edge[edgeId] = (source, destination)
        self.__edgeCosts = {}  # edge[edgeId] = cost of edge
        self.latestGeneratedEdgeId = 0

    def overwriteNodes(self, newNodesList):
        self.__nodes = newNodesList
    def overwriteEdges(self, newEdgesList):
        self.__edges = newEdgesList
    def overwriteEdgeCosts(self, newEdgesCostList):
        self.__edgesCosts = newEdgesCostList

    def copyGraph(self):
        newNodesList = deepcopy(self.__nodes)
        newEdgesList = deepcopy(self.__edges)
        newEdgesCostsList = deepcopy(self.__edgesCosts)
        newGraph = Graph()
        newGraph.overwriteNodes(newNodesList)
        newGraph.overwriteEdges(newEdgesList)
        newGraph.overwriteEdgeCosts(newEdgesCostsList)
        return newGraph


    def createNode(self, nodeId):
        if nodeId not in self.__nodes:
            self.__nodes.append(nodeId)
            return True
        else:
            return False

    def removeNode(self, nodeId):
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
        if nodeId not in self.__nodes:
            return False
        return True

    def checkIfExistsEdgeFromNodeToNode(self, node1, node2):
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == node1 and self.__edges[edgeId][1] == node2:
                return edgeId
        return -1



    def addEdge(self, source, target, edgeId, cost=0):
        if self.checkIfExistsEdgeFromNodeToNode(source, target) != -1:
            return False
        self.__edges[edgeId] = (source, target)
        self.__edgeCosts[edgeId] = cost
        return True

    def removeEdgeById(self, edgeId):
        if edgeId not in self.__edges:
            return False
        self.__edges.pop(edgeId)
        self.__edgeCosts.pop(edgeId)
        return True

    def removeEdgeByNodes(self, source, destination):
        edgeId = self.checkIfExistsEdgeFromNodeToNode(source, destination)
        if edgeId == -1:
            return False
        self.__edges.pop(edgeId)
        self.__edgeCosts.pop(edgeId)
        return True


    def setEdgeCost(self, edgeId, cost):
        self.__edgeCosts[edgeId] = cost

    def getNodes(self):
        return self.__nodes

    def getNumberOfNodes(self):
        return len(self.__nodes)

    def getNumberOfEdges(self):
        return len(self.__edges)

    def getAllEdges(self):
        return list(self.__edges)

    def getEdgeEndpoints(self, edgeId):
        if edgeId not in self.__edges:
            return None
        return self.__edges[edgeId]

    def hasEdge(self, source, target):
        if self.checkIfExistsEdgeFromNodeToNode(source, target) == -1:
            return False
        return self.checkIfExistsEdgeFromNodeToNode(source, target)

    def getOutDegree(self, source):
        degree = 0
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == source:
                degree += 1
        return degree

    def getInDegree(self, destination):
        degree = 0
        for edgeId in self.__edges:
            if self.__edges[edgeId][1] == destination:
                degree += 1
        return degree

    def getOutEdges(self, source):
        outEdges = {}
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == source:
                outEdges[edgeId] = self.__edges[edgeId]
        return outEdges

    def getInEdges(self, destination):
        inEdges = {}
        for edgeId in self.__edges:
            if self.__edges[edgeId][1] == destination:
                inEdges[edgeId] = self.__edges[edgeId]
        return inEdges


    def getEdgeIdPrice(self, edgeId):
        return self.__edgeCosts[edgeId]


    def getEdgeNodesPrice(self, source, destination):
        edgeId = self.checkIfExistsEdgeFromNodeToNode(source, destination)
        if edgeId == -1:
            return False
        return self.__edges[edgeId]


    def parseVertices(self):
        for nodeId in self.__nodes:
            yield nodeId

    def parseAllEdges(self):
        for edge in self.__edges:
            yield edge

    def parseOutboundEdges(self, nodeId):
        for edgeId in self.__edges:
            if self.__edges[edgeId][0] == nodeId:
                yield edgeId

    def parseInboundEdges(self, nodeId):
        for edgeId in self.__edges:
            if self.__edges[edgeId][1] == nodeId:
                yield edgeId

