import numpy as np

# cluster centres
def cluster_centre(input_list):
    output_list = np.zeros(shape=(3,2))
    for i in range(0, 6, 2):
        point = np.array([input_list[i], input_list[i+1]])
        output_list[int(i/2)] = point
        
    return output_list

def make_cluster_centres():
    input_list = np.array([])
    for i in range(6):
        coordinate = float(input())
        input_list = np.append(input_list, coordinate)
        
    return cluster_centre(input_list)

