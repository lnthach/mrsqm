#!/usr/bin/env python3 -u
# coding: utf-8

__author__ = "Thach Le Nguyen"

from setuptools import Extension, setup
from Cython.Build import cythonize

setup(
    name = "pysfa",
    version = "0.0.1",
    #packages = ["mrsqm"],
    ext_modules = cythonize(Extension(
           name="pysfa",                                # the extension name
           sources=["pysfa.pyx","MFT.cpp","DFT.cpp","SFA.cpp","TimeSeries.cpp"], # the Cython source and
                                                  # additional C++ source files
           #extra_compile_args=["-Wall -Ofast -g -fopenmp -std=c++11 -mfpmath=both -ffast-math"],
           extra_compile_args=["-Wall", "-Ofast", "-g", "-std=c++11", "-mfpmath=both", "-ffast-math"],
           extra_link_args=["-lfftw3", "-lm", "-L/opt/local/lib"],
           language="c++",                        # generate and compile C++ code

      )))

