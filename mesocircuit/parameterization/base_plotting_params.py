"""PyNEST Mesocircuit: Plotting Parameters
------------------------------------------

A dictionary with parameters defining the plotting.

"""
import numpy as np

# conversion factor from cm to inch
cm2inch = 1. / 2.54

plot_dict = {

    # rcParams to overwrite the default ones
    'rcParams': {
        # dpi for typical journal printing
        'figure.dpi': 300,
        # line width
        'lines.linewidth': 1.,
        # labels close to ticklabels
        'axes.labelpad': 0.1,
        # handling of .svg fonts:
        # 'path' (embed characters as paths) or 'none'
        'svg.fonttype': 'none',
        # font sizes
        'font.size': 7,
        # margin around lines
        'axes.xmargin': 0.0,
        'axes.ymargin': 0.0,

    },

    # plot format (use '.eps' for final figures)
    # TODO: inkscape etc. for eps conversion not available on JURECA
    'extension': '.pdf',

    # figure width for the J Neurosci (in inch):
    # 1 column, 1.5 columns and 2 columns
    'fig_width_1col': 8.5 * cm2inch,
    'fig_width_15col': 11.6 * cm2inch,
    'fig_width_2col': 17.6 * cm2inch,

    # layer labels
    'layer_labels': np.array(['L2/3', 'L4', 'L5', 'L6']),
    # population labels
    'pop_labels': np.array(['L2/3E', 'L2/3I',
                            'L4E', 'L4I',
                            'L5E', 'L5I',
                            'L6E', 'L6I',
                            'TC']),
    # population colors
    'pop_colors': np.array(['#114477',   # L23E blue
                            '#77AADD',   # L23I
                            '#117744',   # L4E green
                            '#88CCAA',   # L4I
                            '#774411',   # L5E brown
                            '#DDAA77',   # L5I
                            '#771155',   # L6E pompadour
                            '#CC99BB',   # L6I
                            '#696969']),  # TC  dimgrey
    # neuron type colors
    'type_colors': np.array(['#595289',   # E, blue pastel
                             '#AF143C',   # I, red pastel
                             '#696969']),  # other, dimgrey


    # parameters for plot_raster()
    # time intervals for raster plots (in ms)
    'raster_time_interval_short': np.array([600., 800.]),
    'raster_time_interval_long': np.array([500., 1500.]),
    # sample step of raster plot (1 means all neurons are shown).
    # if not a number, but 'auto' is given, a sample step is automatically
    # computed
    'raster_sample_step': 'auto',

    # parameters for plot_statistics_overview()
    # number of bins for distributions
    'distr_num_bins': 30,
    # maximum bin for rate distributions (in Hz), first is at 0
    'distr_max_rate': 28.,
    # maximum bin for LV distributions, first is at 0
    'distr_max_lv': 2.8,
    # maximum bin for CC distributions, symmetrically around 0)
    'distr_max_cc': 0.08,

    # maximum frequency to show for PSDs (in Hz)
    'psd_max_freq': 750,

    # parameters for plot_spatial_snapshots()
    # maximum rate on color bar (in spikes/s)
    'snapshots_max_rate': 50.0

}