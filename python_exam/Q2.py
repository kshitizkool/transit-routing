"""
Enter the solution for Q2 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""

import heapq
def bidirectional_dij(source: int, destination: int, graph_object) -> int:
    """
    Bi-directional Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1

    try:
        initial_node_value = float('inf')
        dictionary = {}
        for i in dictionary:
            source1 = input("START NODES:")
            destination1 = input("END NODES:")

            dictionary['source1'] = ['destination1']
        print(dictionary)

        adjacency_list = ()
        for i in adjacency_list:
            source2 = input("START NODES:")
            destination2 = input("END NODES:")

            adjacency_list['source2'] = ['destination2']
        print(adjacency_list)

        while(adjacency_list!=0):
            if(source2, destination2 in adjacency_list):
                maximum_value = heappop(source2)
                minimum_value = heappop(destination2)

            if(maximum_value, minimum_value)>=initial_node_value:
                return initial_node_value

        distance = []
        for i in distance:
            source3 = input("START NODES:")
            destination3 = input("END NODES:")

            distance['source3'] = ['destination3']
        print(distance)

        def traversal(self, dist = distance):
            return dist

        def neighbour_nodes(row,column):
            for m,n in (row,column):
                return m, n, dist[row][column] - dist[m][n]

        while(m, n in neighbour_nodes!=0):
            if(dictionary[(m,n)])>maximum_value:
                heappush(source2,(m,n))

            if(dictionary[(m,n)])>maximum_value:
                heappush(destination2,(m,n))

        if(dist_start[(nx,ny)]>=initial_node_value):
            initial_node_value(source1[(m,n)],destination1[(m,n)])
        return shortest_path_distance
    except:
        return shortest_path_distance
