from random import randint
from graphDomain import Graph



def parseFile(filename, graph):
    """
    Reads data from a file and populates the graph with nodes and edges
    :param filename: the name of the file to read from
    :param graph: the graph to populate
    :return: None
    """
    print("Loading...\n")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            numberOfVertices,numberOfEdges = lines[0].split(" ")
            numberOfEdges = int(numberOfEdges)
            numberOfVertices = int(numberOfVertices)
            lines.pop(0)
            edgesParsed = 0

            for line in lines:
                if numberOfEdges != 0 and ((edgesParsed * 100) / numberOfEdges) % 10 == 0:
                    print(f"Progress: {(edgesParsed * 100) // numberOfEdges}%")
                nodeId, destination, cost = line.split(" ")
                nodeId = int(nodeId)
                destination = int(destination)
                cost = int(cost)
                graph.createNode(nodeId)
                graph.latestGeneratedEdgeId += 1
                edgesParsed += 1
                latestGeneratedEdgeId = graph.latestGeneratedEdgeId
                graph.addEdge(nodeId, destination, latestGeneratedEdgeId, cost)
            print(f"Progress: 100%")
    except:
        print("Cannot parse the file. Verify the file.")


def createRandomGraphFile(filename, numberOfNodes, numberOfEdges):
    """
    Generates a random graph and writes it to a file
    :param filename: the name of the file to write to
    :param numberOfNodes: the number of nodes to create
    :param numberOfEdges: the number of edges to create
    :return: None
    """
    print("Loading...\n")

    if (numberOfNodes*numberOfNodes < numberOfEdges):
        with open(filename, 'w+') as file:
            file.write(f"Invalid size. A graph with {numberOfNodes} nodes can have maximum {numberOfNodes*numberOfNodes} edges.")
        return

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
            randomNode = randint(0, numberOfNodes+1)
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
    print("Loading...\n")

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
    print("Loading...\n")

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
    print("Loading...\n")

    numberOfEdges = graph.getNumberOfEdges()
    textToPrint = f"Number of edges: {numberOfEdges}\n\n"
    for edge in graph.parseEdges():
        edgeBounds = graph.getEdgeEndpoints(edge)
        cost = graph.getEdgeIdPrice(edge)
        textToPrint += f"Edge {edge}: {edgeBounds}. Cost: {cost}\n"
    print(textToPrint)


def displayAllOutboundEdges(graph):
    """
    Prints the number of edges in the graph and each node with its outbound edges
    :param graph: the graph
    :return: None
    """
    print("Loading...\n")

    numberOfNodes = graph.getNumberOfNodes()
    textToPrint = f"Number of nodes: {numberOfNodes}\n\n"
    for node in graph.parseNodes():
        textToPrint += f"Node: {node}: "
        for outboundEdge in graph.parseOutboundEdges(node):
            edgeEndpoints = graph.getEdgeEndpoints(outboundEdge)
            textToPrint += f"{outboundEdge}{edgeEndpoints} "
        textToPrint += "\n"
    print(textToPrint)

def displayAllInboundEdges(graph):
    """
    Prints the number of edges in the graph and each node with its inbound edges
    :param graph: the graph
    :return: None
    """
    print("Loading...\n")

    numberOfNodes = graph.getNumberOfNodes()
    textToPrint = f"Number of nodes: {numberOfNodes}\n\n"
    for node in graph.parseNodes():
        textToPrint += f"Node: {node}: "
        for outboundEdge in graph.parseInboundEdges(node):
            edgeEndpoints = graph.getEdgeEndpoints(outboundEdge)
            textToPrint += f"{outboundEdge}{edgeEndpoints} "
        textToPrint += "\n"
    print(textToPrint)


# Visual functions

def initialMenu(graph, readFromFile, randomlyGeneratedFile):
    option = int(input(" >> INITIAL MENU <<\nChoose an option:\n1.Read from file\n2.Create random graph\n"))
    if option == 1:
        parseFile(readFromFile, graph)
    elif option == 2:
        numberOfNodes = int(input("Insert the number of vertices the generated graph should have: "))
        numberOfEdges = int(input("Insert the number of edges the generated graph should have: "))
        createRandomGraphFile(randomlyGeneratedFile, numberOfNodes, numberOfEdges)
        parseFile(randomlyGeneratedFile, graph)

def modifyMenu(graph):
    printModifyMenu()
    option = int(input())
    if option == 1:
        nodeId = int(input("Insert the node id: "))
        graph.createNode(nodeId)
    elif option == 2:
        nodeId = int(input("Insert the node id: "))
        graph.removeNode(nodeId)
    elif option == 3:
        edgeId = int(input("Insert the edge id: "))
        while edgeId <= graph.latestGeneratedEdgeId:
            edgeId = int(input("!! Edge already generated. Insert another previously unused edge id: "))
        sourceNode = int(input("Insert the source node: "))
        destinationNode = int(input("Insert the destination node: "))
        cost = int(input("Insert the edge cost: "))
        graph.addEdge(sourceNode, destinationNode, edgeId, cost)
    elif option == 4:
        edgeId = int(input("Insert the edge id: "))
        graph.removeEdgeById(edgeId)
    elif option == 5:
        edgeId = int(input("Insert the edge id: "))
        cost = int(input("Insert the new edge cost: "))
        graph.setEdgeCost(edgeId, cost)


def printModifyMenu():
    print("\n>> Choose an option:")
    print("1.Add a node to the graph")
    print("2.Delete a node from the graph")
    print("3.Add an edge to the graph")
    print("4.Delete an edge from the graph")
    print("5.Update the cost of an edge")

def printMenu():
    print("\nChoose an option:")
    print("1.Display the nodes")
    print("2.Display the edges")
    print("3.Display the outbound edges for each node")
    print("4.Display the inbound edges for each node")
    print("5.Write the graph inside graph.txt file")
    print("6.Modify the graph\n")

def menu(graph):
    while True:
        printMenu()
        option = int(input())
        if option == 1:
            displayGraphNodes(graph)
        elif option == 2:
            displayGraphEdges(graph)
        elif option == 3:
            displayAllOutboundEdges(graph)
        elif option == 4:
            displayAllInboundEdges(graph)
        elif option == 5:
            writeGraphToFile(graph, "graph.txt")
        elif option == 6:
            modifyMenu(graph)

def start():
    graph = Graph()
    readFromFile = "graph1m.txt"
    randomlyGeneratedFile = "randomlyGeneratedFile.txt"
    initialMenu(graph, readFromFile, randomlyGeneratedFile)
    menu(graph)

start()
