# !/usr/bin/env python3
__author__ = "Shivchander Sudalairaj"
__license__ = "MIT"

import numpy as np
import os
import sys
from scipy.spatial import distance


def get_centroids(filepath):
    # if centroids file exist, load the centroids from it
    if os.path.exists(filepath):
        centroids = np.load(filepath)
        return centroids
    else:
        # create 20 random centroids in the range 1 to 100 and save it in a file
        random_centroids = np.random.randint(1, 100, size=(20, 11))
        np.save(filepath, random_centroids)
        return random_centroids


def mapper(centroids):
    # read lines from terminal
    for line in sys.stdin:
        line = line.strip()
        coords = np.array(list(map(float, line.split(','))))
        distances = {}

        # calculating the distances from the point to all the centroids
        for i, c in enumerate(centroids):
            dist = distance.euclidean(coords, c)
            distances[i] = dist

        # pick the index of centroid with least distance
        centroid_ind = min(distances, key=distances.get)
        # print tab delimited values to the terminal for the reducer
        print(centroid_ind, *coords, sep='\t')


if __name__ == "__main__":
    centroids = get_centroids('centroids.npy')
    mapper(centroids)
