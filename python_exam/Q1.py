"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""


def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        graph_object = open("C:/Users/GVS-ASUS/Downloads/TransportationNetworks-master/Chicago-Sketch/ChicagoSketch_flow.tntp", "r")
        line = graph_object.readline()

        while(len(line) == True):    
            l = line.split()
            source = int(l[0])
            destination = int(l[1])
            src_node_cost = int(float(l[3]))

            a = Q1_dijkstra(1,933)
            print("THE SHORTEST PATH IS:", a)  

        visited_node = [] 
        initial_node_cost = float('inf')
        return graph_object
    except:
        return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        for neighbour_node in a:
            if neighbour_node not in visited_node:    
                
                visited_node.append[source] = [destination]
                new_node_cost = initial_node_cost + src_node_cost
                
                if(initial_node_cost[neighbour_node] > new_node_cost):
                    graph_object[neighbour_node] = new_node_cost                              
        return shortest_path_distance
    except:
        return shortest_path_distance
