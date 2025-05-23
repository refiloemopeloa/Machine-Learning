def make_cluster_centres():
    input_list = []
    for i in range(3):
        x = float(input())
        y = float(input())
        coordinate = [x,y]
        input_list.append(coordinate)
        
    return input_list

# k-means algorithm

def stopping_condition(centre_prev, centre_curr):
    for i in range(len(centre_curr)):
        for j in range(len(centre_curr[i])):
            if abs(centre_curr[i][j] - centre_prev[i][j]) != 0:
                return False
    return True


def euclidean_distance(point_1, point_2):
    distance = 0
    for i in range(len(point_1)):
        distance += pow(point_1[i] - point_2[i], 2)
    return pow(distance,0.5)

def euclidean_list(point, cluster_centres):
    min = float('inf')
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
    x = 0
    y = 0

    for point in points:
        x += point[0]
        y += point[1]
        
    x /= len(points)
    y /= len(points)
    coords = [x,y]
    
    return coords    

def empty_clusters(clusters):
    empty_cluster_list = []
    for i in range(len(clusters)-1,-1,-1):
        if len(clusters[i]) == 0:
            empty_cluster_list.append(i)
        
    return empty_cluster_list

def delete_empty_clusters(clusters, cluster_centres, flag):
    empty_cluster_list = empty_clusters(clusters)
    
    for index in empty_cluster_list:
        clusters.pop(index)
        if not flag:
            cluster_centres.pop(index)
    
    return clusters, cluster_centres
        
def k_means(cluster_centres, data):
    centre_prev = [[0,0],[0,0],[0,0]]
    centre_curr = [[1,1],[1,1],[1,1]]
    clusters = [[],[],[]]
    flag = False
    while not stopping_condition(centre_prev, centre_curr):
        clusters = [[],[],[]]
        centre_prev = cluster_centres.copy()  
        for point in data:
            index = euclidean_list(point, cluster_centres)
            clusters[index].append(point)      
        
        clusters, cluster_centres = delete_empty_clusters(clusters, cluster_centres, flag)
        flag = True
        
        for i in range(len(clusters)):
            cluster = clusters[i]
            cluster_centres[i] = get_avg(cluster)
        centre_curr = cluster_centres.copy()
        
     
    return cluster_centres, clusters

# compute loss

def loss(clusters, cluster_centres):
    error = 0
    for i in range(len(clusters)):
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
    data = [[0.22,0.33],
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
                    [0.44,0.55]]

    cluster_centres = make_cluster_centres()

    cluster_centres, clusters = k_means(cluster_centres, data)

    print(f'{loss(clusters, cluster_centres):.4f}')
    
    return 0

if __name__ == "__main__":
    main()