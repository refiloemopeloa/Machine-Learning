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

# k-means algorithm

def stopping_condition(centre_prev, centre_curr):
    return True if (abs(centre_curr - centre_prev).all()==np.array([0,0,0]).all()) else False

def euclidean_distance(point_1, point_2):
    distance = 0
    for i in range(len(point_1)):
        distance += pow(point_1[i] - point_2[i], 2)
    return pow(distance,0.5)

def euclidean_list(point, cluster_centres):
    min = np.iinfo(np.int64).max
    index = 0
    counter = 0
    
    for centre in cluster_centres:
        distance = euclidean_distance(point, centre)
        if (min > distance):
            min = distance 
            index = counter
        counter += 1
        
    return index
    
def get_avg(points):
    coords = np.zeros(shape=(len(points[0])))
    for point in points:
        for i in range(len(point)):
            coords[i] += point[i]
        
    for i in range(len(coords)):
        coords[i] /= len(points)
    
    return coords    
        
def k_means(cluster_centres, data):
    centre_prev = np.array([0,0,0])
    centre_curr = np.array([1,1,1])
    clusters = {
        0:[],
        1:[],
        2:[]    
    }
    
    while not stopping_condition(centre_prev, centre_curr):
        centre_prev =np.copy(cluster_centres)    
        clusters = {
            0:[],
            1:[],
            2:[]    
        }
        for point in data:
            index = euclidean_list(point, cluster_centres)
            clusters[index].append(point)            
            
        counter = 0
        for cluster in clusters.values():
            cluster_centres[counter] = get_avg(cluster)
            counter += 1           
        centre_curr = np.copy(cluster_centres)
    
    return cluster_centres, clusters

# compute loss

def loss(clusters, cluster_centres, k):
    error = 0
    for i in range(k):
        distance_error = 0
        cluster = clusters[i]
        for point in cluster:
            distance_error += pow(euclidean_distance(point, cluster_centres[i]), 2)
        error+=distance_error
    
    return error

def main():
    # number of clusters
    k=3

    # dataset
    data = np.array([[0.22,0.33],
                    [0.45,0.76],
                    [0.73,0.39],
                    [0.25,0.35],
                    [0.51,0.69],
                    [0.69,0.42],
                    [0.41,0.49],
                    [0.15,0.29],
                    [0.81,0.32],
                    [0.50,0.88],
                    [0.23,0.31],
                    [0.77,0.30],
                    [0.56,0.75],
                    [0.11,0.38],
                    [0.81,0.33],
                    [0.59,0.77],
                    [0.10,0.89],
                    [0.55,0.09],
                    [0.75,0.35],
                    [0.44,0.55]])

    cluster_centres = make_cluster_centres()

    cluster_centres, clusters = k_means(cluster_centres, data)

    print(loss(clusters, cluster_centres, k))
    
    return 0

if __name__ == "__main__":
    main()