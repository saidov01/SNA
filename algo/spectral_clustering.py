from cdlib import algorithms

from utils import draw


def run(G, kmax):
    result = algorithms.spectral(G, kmax=kmax)
    draw(G, result.communities)
