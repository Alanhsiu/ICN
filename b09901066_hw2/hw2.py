import numpy as np
import sys
import copy
import filecmp

if len(sys.argv) <= 1:
    print('Usage : "python hw2.py p2_test1.txt [Removed Router Number]"')
    sys.exit(2)

inputfile = sys.argv[1]
removed_router_number = -1 if len(sys.argv) < 3 else int(sys.argv[2])-1
if (removed_router_number == -1):
    outputfile = inputfile.replace(".txt", "_GenTable.txt")
else:
    outputfile = inputfile.replace(
        ".txt", "_RmRouter"+sys.argv[2]+".txt")

node = 0  # num of nodes
data = []  # input data


def printResult(source, cost, next, output):

    # reindex the node number
    output.write("Routing table of router {}:".format(source+1))
    output.write('\n')
    for i in range(node):
        output.write(str(cost[i]))
        output.write(' ')
        if next[i] == -1:
            output.write(str(next[i]))
        else:
            output.write(str(next[i]+1))
        output.write('\n')


def dijkstra(e, source, output):  # e is a table record the distance between any two nodes

    # initialize the distance and nextHop
    dist = e[source]
    nextHop = np.ones(node, dtype=int)*(-1)
    nextHop[source] = source

    # early stop for the isolated node
    if np.count_nonzero(dist == -1) != node-1:

        # leftNode: nodes which are not added to final graph yet
        # queue: nodes which are reached but not added to final graph yet
        leftNode = [int(x) for x in range(node)]
        leftNode.remove(source)
        if removed_router_number != -1:
            leftNode.remove(removed_router_number)

        queue = set()
        for i in leftNode:
            if dist[i] != -1:
                queue.add(i)
                nextHop[i] = i
        while queue:

            # find the node with minimum distance from source
            min = np.inf
            u = -1
            for i in queue:
                if dist[i] != -1 and dist[i] < min:
                    min = dist[i]
                    u = i
            # update distance of all left nodes
            if u != -1:
                queue.remove(u)  # u is added to final graph
                leftNode.remove(u)
                for v in leftNode:
                    if e[u][v] != -1 and (dist[v] == -1 or dist[v] > dist[u]+e[u][v]):
                        dist[v] = dist[u]+e[u][v]
                        nextHop[v] = nextHop[u]
                        queue.add(v)

    printResult(source, dist, nextHop, output)


########## read file ##########
with open(inputfile, 'r') as f:
    line = f.readline()
    node = int(line)
    while line:
        line = f.readline()
        eachline = line.split()
        num = [int(x) for x in eachline[0:]]
        n = np.array(num)
        data.append(n)
    if (removed_router_number != -1):
        for i in range(node):
            data[removed_router_number][i] = -1
            data[i][removed_router_number] = -1

########## start to run ##########
output = open(outputfile, "w")
for i in range(node):
    e = copy.deepcopy(data)
    if i != removed_router_number:
        dijkstra(e, i, output)
output.close()

# compare the result with the golden file
if (removed_router_number == -1):
    print(filecmp.cmp(outputfile, inputfile.replace(".txt", "_golden.txt")))
else:
    print(filecmp.cmp(outputfile, inputfile.replace(
        ".txt", "_golden_rm"+sys.argv[2]+".txt").replace("p1", "p2")))
