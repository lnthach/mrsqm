#!/usr/bin/env python3 -u
# coding: utf-8

__author__ = "Thach Le Nguyen"

from setuptools import Extension, setup
from Cython.Build import cythonize

setup(
    #name = "mrsqm",
    #version = "0.0.1",
    #packages = ["mrsqm"],
    ext_modules = cythonize(Extension(
            name="mrsqm",                                # the extension name
            sources=["src/mrsqm/mrsqm_wrapper.pyx","src/mrsqm/sfa/MFT.cpp","src/mrsqm/sfa/DFT.cpp","src/mrsqm/sfa/SFA.cpp","src/mrsqm/sfa/TimeSeries.cpp"], # the Cython source and
                                                  # additional C++ source files
            #sources=["mrsqm_wrapper.pyx"],
            extra_compile_args=["-Wall", "-Ofast", "-g", "-std=c++11", "-ffast-math"],
            extra_link_args=["-lfftw3", "-lm", "-L/opt/local/lib"],           
            language="c++",                        # generate and compile C++ code

      )),

    install_requires=["numpy"],
      
      
      )
