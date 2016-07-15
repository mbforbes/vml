# coding: utf-8

import numpy as np
from bokeh.plotting import figure, show, output_notebook, ColumnDataSource
from bokeh.palettes import magma, inferno, plasma, viridis
from IPython.core.display import display, HTML


# It's currently 256, but this allows them to expand up to 1024.
ALL_MAGMA = magma(len(set(magma(1024))))


def style():
    '''
    Tweaks notebook styling.
    '''
    # Make paragraph text wrap way sooner.
    display(HTML('<style>p {max-width: 500px !important; }</style>'))

    # Display Bokeh plots to the notebook.
    output_notebook()


# Helper function for color selection.
def get_color(min_val, max_val, n, val):
    '''
    Gets the background and text color for rendering a cell with value val in a
    matrix with n values and min and max values min_val and max_val,
    respectively.

    Args:
        min_val (float) Smallest value in the matrix.
        max_val (float) Largest value in the matrix.
        n (int) Number of values in the matrix.
        val (float|int) Value of cell in question.

    Returns:
        (str, str) The background and text color
    '''
    # The result should be memoized so we don't have to keep computing the full
    # range of values, but oh well. Choose from: magma, inferno, plasma,
    # viridis.
    top = float(max_val - min_val)
    black = magma(2)[0]
    white = 'white'

    # If the matrix is basically all the same value just return black.
    if np.isclose(0.0, top):
        return black, white

    # Compute which color to return.
    idx = int(((val - min_val)/top)*n)
    bg_color = magma(n + 1)[idx]
    text_color = white
    # This is specific to magma. To make the text more readable, change its
    # color to black if we're more than 90% of the way through the magma
    # colors.
    if ALL_MAGMA.index(bg_color) >= 0.9*len(ALL_MAGMA):
        text_color = black
    return bg_color, text_color


# Here's a function to visualize a matrix.
def display_matrix(M, base_size=600):
    '''
    Renders the matrix M as a heatmap.

    Args:
        M (numpy's matrix) Matrix to render.
        base_size (int) Default size (in pixels, I think) of
            larger dimension.
    '''
    # Work with the underlying array.
    m = np.asarray(M)
    n = len(m.flatten())

    # Get value range for color computation.
    min_val = m.min()
    max_val = m.max()

    # Massage data into format for plotting a bunch of rectangles.
    xvals = []
    yvals = []
    vals = []
    colors = []
    text_colors = []
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            datum = m[i][j]

            # Turn the index into plotting coordinates.
            x = j
            y = m.shape[0] - i
            xvals += [x]
            yvals += [y]

            # Change display based on numerical type for
            # cleaner look.
            if type(datum) is np.int64:
                vals += [str(datum)]
            else:
                vals += ['%0.2f' % (datum)]

            # Get the background and text color for the cell.
            bg, txt = get_color(min_val, max_val, n, datum)
            colors += [bg]
            text_colors += [txt]

    # This is the format we stick it in for bokeh plotting.
    source = ColumnDataSource(
        data=dict(
            xvals=xvals,
            yvals=yvals,
            colors=colors,
        )
    )

    # Create a figure and remove tje default plotting crap. (Not all of this
    # may be necessary.)
    p = figure(
        tools='',
    )
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.minor_tick_line_color = None
    p.axis.major_label_text_font_size = '0pt'
    p.axis[0].ticker.num_minor_ticks = 0
    p.toolbar_location = None

    # Shrink size if n_rows != n_cols. Enforce a minimum of 50px so that the
    # values are visible.
    n_rows, n_cols = m.shape[0], m.shape[1]
    rc_ratio = float(n_rows) / n_cols
    w, h = base_size, base_size
    if n_rows > n_cols:
        w = max(50.0 * n_cols, (1.0 / rc_ratio) * base_size)
        h = max(50.0 * n_rows, rc_ratio * w)
    elif n_cols > n_rows:
        h = max(50.0 * n_rows, rc_ratio * base_size)
        w = max(50.0 * n_cols, (1.0 / rc_ratio) * h)
    p.plot_width = int(w)
    p.plot_height = int(h)

    # Plot and display.
    p.rect('xvals', 'yvals', 0.9, 0.9, source=source, color='colors')
    p.text(
        np.array(xvals) - 0.25,
        np.array(yvals) - 0.25,
        vals,
        text_color=text_colors
    )
    show(p)
