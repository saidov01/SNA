import json

import click
import networkx as nx
import json

import algo.eigenvector
import algo.greedy
import algo.kclique
import algo.label_propagation
import algo.spectral_clustering
import algo.walktrap
import algo.betweness


def get_graph(file: str):
    if file.endswith(".csv"):
        G = nx.Graph()
        with open(file) as f:
            f.readline()
            for ids in f:
                G.add_edge(*ids.strip().split(","))
    elif file.endswith(".json"):
        with open(file) as f:
            G = nx.from_dict_of_lists(json.loads(f.read(), parse_int=str))
    else:
        raise ValueError("Unsupported file format. Only supports .csv and .json")
    return G


@click.command("greedy")
@click.option("--file", default=".data/twitter.csv")
def greedy(file):
    algo.greedy.run(get_graph(file))


@click.command("eigenvector")
@click.option("--file", default=".data/twitter.csv")
def eigenvector(file):
    algo.eigenvector.run(get_graph(file))


@click.command("kclique")
@click.option("--file", default=".data/twitter.csv")
@click.option("--k", default=5)
@click.option("--small", default=False)
def kclique(file, k, small):
    algo.kclique.run(get_graph(file), k, small)


@click.command("label_propagation")
@click.option("--file", default=".data/twitter.csv")
def label_propagation(file):
    algo.label_propagation.run(get_graph(file))


@click.command("spectral_clustering")
@click.option("--file", default=".data/twitter.csv")
@click.option("--kmax", default=10)
def spectral_clustering(file, kmax):
    algo.spectral_clustering.run(get_graph(file), kmax)


@click.command("walktrap")
@click.option("--file", default=".data/twitter.csv")
def walktrap(file):
    algo.walktrap.run(get_graph(file))


@click.command("betweness")
@click.option("--file", default=".data/twitter.csv")
@click.option("--truncate", default=True)
def betweness(file, truncate):
    algo.betweness.run(get_graph(file), truncate)


@click.group()
def cli():
    pass


cli.add_command(greedy)
cli.add_command(eigenvector)
cli.add_command(kclique)
cli.add_command(label_propagation)
cli.add_command(spectral_clustering)
cli.add_command(walktrap)
cli.add_command(betweness)


if __name__ == "__main__":
    cli()
