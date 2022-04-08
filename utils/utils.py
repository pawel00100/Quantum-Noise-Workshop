import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram


def draw_ciurcuits(circuit):
    if (isinstance(circuit, list)):
        n = len(circuit)
        # rows = int(math.sqrt(n))
        # cols = math.ceil(n / rows)
        # fig, axs = plt.subplots(rows, cols)
        fig, axs = plt.subplots(n)
        fig.set_size_inches(10, 3 * n)

        for i, c in enumerate(circuit):
            c.draw('mpl', ax=axs[i])

        plt.show()
    else:
        circuit[0].draw('mpl')


def plot_histograms(counts, bar_labels=True):
    if (isinstance(counts, list)):
        n = len(counts)
        # rows = int(math.sqrt(n))
        # cols = math.ceil(n / rows)
        # fig, axs = plt.subplots(rows, cols)
        fig, axs = plt.subplots(n)
        fig.set_size_inches(10, 3 * n)

        for i, c in enumerate(counts):
            plot_histogram(c, bar_labels=bar_labels, ax=axs[i])

        plt.show()
    else:
        plot_histogram(counts, bar_labels=bar_labels)