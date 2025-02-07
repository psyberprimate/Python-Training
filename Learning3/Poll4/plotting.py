import matplotlib.pyplot as plt
import os


def find_file(target_file: str):
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for name in files:
            if name == target_file:
                return os.path.abspath(root)


def create_pie_chart(options: list[tuple]):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1, 1, 1)
    ax.pie([option[1] for option in options],
           labels=[option[0].text for option in options],
           autopct="%1.1f%%",
           wedgeprops={"edgecolor": "black",
                       'linewidth': 2,
                       'antialiased': True},
           labeldistance=1.2,
           textprops={'size': 'smaller'})
    return fig


def create_bar_plot(options: list[tuple], save_fig: bool):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(range(len([option for option in options])),
           [option[1] for option in options])

    plt.xticks(rotation=30, ha="right")
    ax.set_xticks(range(len([option for option in options])))
    ax.set_xticklabels([option[0].text for option in options])
    ax.set_xlabel("Poll options")
    ax.set_ylabel("Poll votes")

    if save_fig:
        fig.savefig(os.path.join(find_file(target_file="plotting.py"),
                                 "bar_plot.png"),
                    bbox_inches="tight")
    return fig
