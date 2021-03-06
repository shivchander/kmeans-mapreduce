import numpy as np
import pandas as pd


def plus_plus(ds, k, random_state=42):
    """
    Centroids generated using kmeans++ algorithm.
    Source: https://stackoverflow.com/questions/5466323/how-could-one-implement-the-k-means-algorithm
    """

    np.random.seed(random_state)
    centroids = [ds[0]]

    for _ in range(1, k):
        dist_sq = np.array([min([np.inner(c - x, c - x) for c in centroids]) for x in ds])
        probs = dist_sq / dist_sq.sum()
        cumulative_probs = probs.cumsum()
        r = np.random.rand()

        for j, p in enumerate(cumulative_probs):
            if r < p:
                i = j
                break

        centroids.append(ds[i])

    return np.array(centroids)


if __name__ == "__main__":
    data = pd.read_csv('data/data.csv')
    centroids = plus_plus(data.values, k=20)
    np.save('centroids.npy', centroids)
