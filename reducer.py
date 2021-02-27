# !/usr/bin/env python3
__author__ = "Shivchander Sudalairaj"
__license__ = "MIT"

import sys
import numpy as np


def reducer():
    current_centroid = None
    sum_arr = np.zeros(11)
    count = 0

    new_centroids = {}

    # input from mapper terminal
    for line in sys.stdin:
        values = list(map(float, line.split('\t')))
        centroid_ind = values[0]
        coords = np.array(values[1:])

        if current_centroid == centroid_ind:
            count += 1
            sum_arr += coords
            new_centroids[centroid_ind] = sum_arr / count
        else:
            if count != 0:
                new_centroids[centroid_ind] = sum_arr/count
                # print(*(sum_arr/count), sep=',')
            current_centroid = centroid_ind
            sum_arr = coords

    # print last cluster's centroid
    if current_centroid == centroid_ind and count != 0:
        # print(*(sum_arr/count), sep=',')
        new_centroids[centroid_ind] = sum_arr / count

    # check if there are 20 centroids, if not create random centroids
    for c_ind in new_centroids:
        print(*new_centroids[c_ind], sep=',')


if __name__ == '__main__':
    reducer()
