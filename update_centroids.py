import numpy as np
import os
import sys


def remove_and_create_centroids():
    if os.path.exists('centroids.npy'):
        os.remove('centroids.npy')

    centroid_list = []
    for line in sys.stdin:
        values = list(map(float, line.strip().split(',')))
        centroid_list.append(values)

    new_centroids = np.array(centroid_list)
    np.save('centroids.npy', new_centroids)


if __name__ == '__main__':
    remove_and_create_centroids()