from graphDomain import Graph



def parseFile(filename, graph):
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


def displayGraphNodes(graph):
    numberOfNodes = graph.getNumberOfNodes()
    textToPrint = f"Number of nodes: {numberOfNodes}\n\n"
    for node in graph.parseVertices():
        textToPrint += f"Node: {node}\n"
    print(textToPrint)

def displayGraphEdges(graph):
    numberOfEdges = graph.getNumberOfEdges()
    textToPrint = f"Number of edges: {numberOfEdges}\n\n"
    for edge in graph.parseAllEdges():
        edgeBounds = graph.getEdgeEndpoints(edge)
        cost = graph.getEdgeIdPrice(edge)
        textToPrint += f"Edge {edge}: {edgeBounds}. Cost: {cost}\n"
    print(textToPrint)


def createRandomGraphFile():
    pass

def initialMenu(graph):
    option = int(input("INITIAL MENU\nChoose an option:\n1.Read from file\n2.Create random graph\n"))
    if option == 1:
        parseFile("graph1k.txt", graph)
    elif option == 2:
        createRandomGraphFile()

def menu(graph):
    while True:
        option = int(input("Choose an option:\n1.Display the nodes\n2.Display the edges\n3.Display the outbound edges for each node\n4.Display the inbound edges for each node\n"))
        if option == 1:
            displayGraphNodes(graph)
        elif option == 2:
            displayGraphEdges(graph)

def start():
    graph = Graph()
    initialMenu(graph)
    menu(graph)

start()

# TODO function that prints to textfile the graph
# TODO random file generator
# TODO specifications
