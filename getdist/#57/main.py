import os
import sys
import pickle

import numpy as np
import matplotlib.pyplot as plt

from getdist import MCSamples, plots

import matplotlib
matplotlib.use('QT5Agg')


def load_samples(directory, filename="samples"):
    with open(
        "{}/{}.pickle".format(directory, filename),
        "rb"
    ) as f:
        samples = pickle.load(f)

    if not isinstance(samples, MCSamples):
        raise ValueError("...")

    return samples


def triangle_plot(list_of_obj, **kwargs):

    if isinstance(list_of_obj, list):
        pass

    plotter = plots.get_subplot_plotter(
        width_inch=12,
    )

    # NOTE:
    plotter.settings.num_plot_contours = 2

    plotter.triangle_plot(
        list_of_obj,
        legend_labels=kwargs["legend_labels"],
        line_args=kwargs["line_args"],
        contour_args=kwargs["contour_args"],
        markers=kwargs["markers"],
        legend_loc='upper right',
        legend_kwargs={"fontsize":20}
    )


if __name__ == "__main__":



    list_of_obj = []
    for i, filename_suffix in enumerate([
        "dataset_0",
        "dataset_1",
        "dataset_2",
        "dataset_3",
    ]):
        samples = load_samples(
            directory="./", filename="samples_{}".format(filename_suffix)
        )
        list_of_obj.append(samples)


    triangle_plot_kwargs = {
        "legend_labels":[
            r"$M_{sub} = 0.0$",
            r"$M_{sub} = 10^{8}$",
            r"$M_{sub} = 10^{9}$",
            r"$M_{sub} = 10^{10}$"
        ],
        "line_args":[
            {'lw':2, 'ls':'-', 'color':"#008000"},
            {'lw':2, 'ls':'-', 'color':"#0000FF"},
            {'lw':2, 'ls':'-', 'color':"#FF0000"},
            {'lw':2, 'ls':'-', 'color':"#808080"},
        ],
        "contour_args":[
            {'lw':2, 'ls':'-', 'color':"#008000", 'filled':True},
            {'lw':2, 'ls':':', 'color':"#0000FF", 'filled':True},
            {'lw':2, 'ls':':', 'color':"#FF0000", 'filled':True},
            {'lw':2, 'ls':':', 'color':"#808080", 'filled':True},
        ],
        "markers":{
            'x0':0.0,
            'x1':0.0,
            'x2':120.0,
            'x3':0.75,
            'x4':1.0,
            'x5':0.05,
            'x6':120.0,
        }
    }

    triangle_plot(
        list_of_obj=list_of_obj,
        **triangle_plot_kwargs
    )

    plt.show()
