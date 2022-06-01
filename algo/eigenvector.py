from cdlib import algorithms

from utils import draw


def run(G):
    result = algorithms.eigenvector(G)
    draw(G, result.communities)
