import matplotlib.pyplot as plt

def plotTSP(paths, points, num_iters=1):

    """
    path: List of lists with the different orders in which the nodes are visited
    points: coordinates for the different nodes
    num_iters: number of paths that are in the path list
    
    """

    # Unpack the primary TSP path and transform it into a list of ordered 
    # coordinates

    # Obtain the cordinates for each path
    def dist_cost(cordinates):
        x_cordinate = []; y_cordinate = []
        for i in range(len(cordinates)):
            x_cordinate.append(cordinates[i][0])
            y_cordinate.append(cordinates[i][1])
        
        x_y_cord_cost = 0 
        for j in range(len(x_cordinate)):
            if j < len(x_cordinate) - 1:
                x_y_cord_cost += abs((x_cordinate[j] - x_cordinate[j+1]) + (y_cordinate[j] - y_cordinate[j+1]))
            if j + 1 == len(x_cordinate):
                x_y_cord_cost += abs((x_cordinate[j-1] - x_cordinate[j]) + (y_cordinate[j-1] - y_cordinate[j]))

        return (x_y_cord_cost)

    cordinate = {"cost": [], "path": []}
    for i in range(len(paths)):
        current_cordinate = []
        for j in range(len(paths[i])):
            current_cordinate.append(points[j])
        cordinate['cost'].append(dist_cost(current_cordinate))
        cordinate['path'].append(paths[i])

    # Obtain path that has lowest cordinate cost after calculation 
    best_cost = min(cordinate['cost'])
    best_path = cordinate['path'][cordinate['cost'].index(best_cost)]



    # Calculate the cost for each cordinate


    x = []; y = []
    for i in paths[paths.index(best_path)]:
        x.append(points[i][0])
        y.append(points[i][1])
    
    plt.plot(x, y, 'co')
    plt.xlabel("x-cordinate")
    plt.ylabel("y-cordinate")


    # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
    a_scale = float(max(x))/float(50)


 

    # Draw the primary path for the TSP problem
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale, 
            color ='g', length_includes_head=True)
    for i in range(0,len(x)-1):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
                color = 'g', length_includes_head = True)

    #Set axis too slitghtly larger than the set of x and y
    plt.xlim(0, max(x)*1.1)
    plt.ylim(0, max(y)*1.1)
    plt.show()


if __name__ == '__main__':
    # Run an example
    
    # Create a randomn list of coordinates, pack them into a list
    x_cor = [1, 8, 4, 9, 2, 1, 8]
    y_cor = [1, 2, 3, 4, 9, 5, 7]
    points = []
    for i in range(0, len(x_cor)):
        points.append((x_cor[i], y_cor[i]))

    # Create two paths, teh second with two values swapped to simulate a 2-OPT
    # Local Search operation
    path4 = [0, 1, 2, 3, 4, 5, 6]
    path3 = [0, 2, 1, 3, 4, 5, 6]
    path2 = [0, 2, 1, 3, 6, 5, 4]
    path1 = [0, 2, 1, 3, 6, 4, 5]

    # Pack the paths into a list
    paths = [path1, path2, path3, path4]
    
    # Run the function
    plotTSP(paths, points, 4)
