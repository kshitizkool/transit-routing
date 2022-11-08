"""
Enter the solution for Q3 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""


def number_of_routes(source_stopid: str, destination_stopid: str) -> int:
    """
    Find the number of routes going from source stop id to destination stop id.

    Args:
        source_stopid (str): Source Stop Id
        destination_stopid (str): Destination Stop Id

    Returns:
        final_count (int): Number of routes going from source to destination.
    """
    final_count = -1
    try:
        file = open("C:/Users/GVS-ASUS/Downloads/anaheim_gtfs.zip", "r")
        line = file.readline()

        while(len(line) == True):    
            l = line.split()
            source_stopid = int(l[0])
            destination_stopid = int(l[1])
            src_node_cost = int(float(l[3]))

            a = Q1_dijkstra(1,933)
            print("THE SHORTEST PATH IS:", a)  

        visited_node = [] 
        initial_node_cost = float('inf')

        for neighbour_node in a:
                if neighbour_node not in visited_node:    

                    visited_node.append[source_stopid] = [destination_stopid]
                    new_node_cost = initial_node_cost + src_node_cost

                    if(initial_node_cost[neighbour_node] > new_node_cost):
                        file[neighbour_node] = new_node_cost    
        return final_count
    except:
        return final_count
