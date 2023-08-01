# Python3 Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 4

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

# Solves all pair shortest path
# via Floyd Warshall Algorithm


def floydWarshall(graph):

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):

                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
    print("Following matrix shows the shortest distances\
between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()


# Driver's code
if __name__ == "__main__":

    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
# Function call
floydWarshall(graph)
# This code is contributed by Mythri J L

# import sys

# # Function to get minimum number of trials
# # needed in worst case with n eggs and k floors


# def eggDrop(n, k):

#     # If there are no floors, then no trials
#     # needed. OR if there is one floor, one
#     # trial needed.
#     if (k == 1 or k == 0):
#         return k

#     # We need k trials for one egg
#     # and k floors
#     if (n == 1):
#         return k

#     min = sys.maxsize

#     # Consider all droppings from 1st
#     # floor to kth floor and return
#     # the minimum of these values plus 1.
#     for x in range(1, k + 1):

#         res = max(eggDrop(n - 1, x - 1),
#                   eggDrop(n, k - x))
#         if (res < min):
#             min = res

#     return min + 1


# # Driver Code
# if __name__ == "__main__":

#     n = 2
#     k = 10
#     print("Minimum number of trials in worst case with",
#           n, "eggs and", k, "floors is", eggDrop(n, k))

# # This code is contributed by ita_c
