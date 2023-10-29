#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Borrowed from pymzml examples

import os
import sys

import pymzml
from pymzml.plot import Factory


def main(mzml_file):
    """
    Plots a chromatogram for the given mzML file. File is saved as
    'chromatogram_<mzml_file>.html'.

    usage:

        ./plot_chromatogram.py <path_to_mzml_file>

    """
    run = pymzml.run.Reader(mzml_file)
    mzml_basename = os.path.basename(mzml_file)
    pf = Factory()
    pf.new_plot()
    pf.add(run["TIC"].peaks(), color=(0, 0, 0), style="lines", title=mzml_basename)
    pf.save(
        "chromatogram_{0}.html".format(mzml_basename),
        layout={
            "xaxis":{
                "title": "Retention time",
                "ticks": 'outside',
                "ticklen": 2,
                "tickwidth": 0.25,
                "showgrid": False,
                "linecolor": 'black',
            },
            "yaxis": {
                "title": "TIC",
                "ticks": 'outside',
                "ticklen": 2,
                "tickwidth": 0.25,
                "showgrid": False,
                "linecolor": 'black',
            },
            "plot_bgcolor": 'rgba(255, 255, 255, 0)',
            "paper_bgcolor": 'rgba(255, 255, 255, 0)',
        },
    )
    return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(main.__doc__)
        exit()
    mzml_file = sys.argv[1]
    #mzml_file = "../qc/qc/neg/PoolQC161_MX612252_NegLIPIDS_postLongevity_Female2163.mzML"
    main(mzml_file)