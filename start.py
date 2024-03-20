from random import randint
from graphDomain import Graph



def parseFile(filename, graph):
    """
    Reads data from a file and populates the graph with nodes and edges
    :param filename: the name of the file to read from
    :param graph: the graph to populate
    :return: None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        numberOfVertices,numberOfEdges = lines[0].split(" ")
        lines.pop(0)
        for line in lines:
            nodeId, destination, cost = line.split(" ")
            if not graph.checkIfNodeExists(nodeId):
                graph.createNode(nodeId)
            graph.latestGeneratedEdgeId += 1
            latestGeneratedEdgeId = graph.latestGeneratedEdgeId
            graph.addEdge(nodeId, destination, latestGeneratedEdgeId, cost)


def createRandomGraphFile(filename, numberOfNodes, numberOfEdges):
    """
    Generates a random graph and writes it to a file
    :param filename: the name of the file to write to
    :param numberOfNodes: the number of nodes to create
    :param numberOfEdges: the number of edges to create
    :return: None
    """
    alreadyExistingNodes = []
    addedEdges = 0
    textToWrite = F"{numberOfNodes} {numberOfEdges}\n"
    for nodeId in range(numberOfNodes):
        if nodeId == numberOfNodes - 1:
            numberOfEdgesRemaining = numberOfEdges - addedEdges
        else:
            maximumEdges = 2* ((numberOfEdges - addedEdges) // (numberOfNodes - nodeId + 1))
            numberOfEdgesRemaining = randint(maximumEdges//2 , maximumEdges)
        for edge in range(numberOfEdgesRemaining):
            randomNode = randint(0, numberOfNodes)
            while (nodeId, randomNode) in alreadyExistingNodes:
                randomNode = randint(0, numberOfNodes)
            alreadyExistingNodes.append((nodeId, randomNode))
            randomPrice = randint(0, 200)
            textToWrite += f"{nodeId} {randomNode} {randomPrice}\n"
            addedEdges += 1
    with open(filename, 'w+') as file:
        file.write(textToWrite)



def writeGraphToFile(graph, filename):
    """
    Writes the details of the graph into a file
    :param graph: the graph to write to file
    :param filename: the name of the file to write to
    :return: None
    """
    numberOfNodes = graph.getNumberOfNodes()
    numberOfEdges = graph.getNumberOfEdges()

    textToWrite = F"{numberOfNodes} {numberOfEdges}\n"
    for edge in graph.parseEdges():
        sourceNode, destinationNode = graph.getEdgeEndpoints(edge)
        edgeCost = graph.getEdgeIdPrice(edge)
        textToWrite += f"{sourceNode} {destinationNode} {edgeCost}"
    with open(filename, 'w+') as file:
        file.write(textToWrite)


def displayGraphNodes(graph):
    """
    Prints the number of nodes in the graph and lists each node
    :param graph: the graph
    :return: None
    """
    numberOfNodes = graph.getNumberOfNodes()
    textToPrint = f"Number of nodes: {numberOfNodes}\n\n"
    for node in graph.parseNodes():
        textToPrint += f"Node: {node}\n"
    print(textToPrint)

def displayGraphEdges(graph):
    """
    Prints the number of edges in the graph and details of each edge (id, source and destination) and its cost
    :param graph: the graph
    :return: None
    """
    numberOfEdges = graph.getNumberOfEdges()
    textToPrint = f"Number of edges: {numberOfEdges}\n\n"
    for edge in graph.parseEdges():
        edgeBounds = graph.getEdgeEndpoints(edge)
        cost = graph.getEdgeIdPrice(edge)
        textToPrint += f"Edge {edge}: {edgeBounds}. Cost: {cost}\n"
    print(textToPrint)




# Visual functions

def initialMenu(graph):
    option = int(input(" >> INITIAL MENU <<\nChoose an option:\n1.Read from file\n2.Create random graph\n"))
    if option == 1:
        parseFile("graph1k.txt", graph)
    elif option == 2:
        numberOfNodes = int(input("Insert the number of vertices the generated graph should have: "))
        numberOfEdges = int(input("Insert the number of edges the generated graph should have: "))
        createRandomGraphFile("randomlyGeneratedFile.txt", numberOfNodes, numberOfEdges)
        parseFile("randomlyGeneratedFile.txt", graph)


def printMenu():
    print("\nChoose an option:")
    print("1.Display the nodes")
    print("2.Display the edges")
    print("3.Display the outbound edges for each node")
    print("4.Display the inbound edges for each node")
    print("5.Write the graph inside graph.txt file\n")

def menu(graph):
    while True:
        printMenu()
        option = int(input())
        if option == 1:
            displayGraphNodes(graph)
        elif option == 2:
            displayGraphEdges(graph)
        elif option == 5:
            writeGraphToFile(graph, "graph.txt")

def start():
    graph = Graph()
    initialMenu(graph)
    menu(graph)

start()
