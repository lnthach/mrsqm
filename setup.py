#!/usr/bin/env python3 -u
# coding: utf-8

__author__ = "Thach Le Nguyen"

from setuptools import Extension, setup
#from Cython.Build import cythonize
import sys

# setup(
#     #name = "mrsqm",
#     #version = "0.0.1",
#     #packages = ["mrsqm"],
#     ext_modules = cythonize(Extension(
#             name="mrsqm",                                # the extension name
#             sources=["src/mrsqm/mrsqm_wrapper.pyx","src/mrsqm/sfa/MFT.cpp","src/mrsqm/sfa/DFT.cpp","src/mrsqm/sfa/SFA.cpp","src/mrsqm/sfa/TimeSeries.cpp"], # the Cython source and
#                                                   # additional C++ source files
#             #sources=["mrsqm_wrapper.pyx"],
#             extra_compile_args=["-Wall", "-Ofast", "-g", "-std=c++11", "-ffast-math"],
#             extra_link_args=["-lfftw3", "-lm", "-L/opt/local/lib"],           
#             language="c++",                        # generate and compile C++ code

#       )),

#     install_requires=["numpy"],
      
      
#       )

def get_extensions():
  return [Extension(
            name="mrsqm",                                # the extension name
            sources=["src/mrsqm/mrsqm_wrapper.pyx","src/mrsqm/sfa/MFT.cpp","src/mrsqm/sfa/DFT.cpp","src/mrsqm/sfa/SFA.cpp","src/mrsqm/sfa/TimeSeries.cpp"], # the Cython source and
                                                  # additional C++ source files
            #sources=["mrsqm_wrapper.pyx"],
            extra_compile_args=["-Wall", "-Ofast", "-g", "-std=c++11", "-ffast-math"],
            extra_link_args=["-lfftw3", "-lm", "-L/opt/local/lib"],           
            language="c++",                        # generate and compile C++ code

      )]


def setup_package():

    # Figure out whether to add ``*_requires = ['numpy']``.
    build_requires = []
    numpy_requirement = 'numpy>=1.20, <2.0'
    try:
        import numpy
    except ImportError:
        build_requires = [numpy_requirement]

    # we require cython because we need to know which part of the wrapper
    # to build to avoid missing symbols at runtime. But if this script is
    # called without building pyfftw, for example to install the
    # dependencies, then we have to hide the cython dependency.
    try:
        import cython
    except ImportError:
        build_requires.append('cython>=0.29.18, <1.0')

    install_requires = [numpy_requirement]

    # opt_requires = {
    #     'dask': ['numpy>=1.20, <2.0', 'dask[array]>=1.0'],
    #     'scipy': ['scipy>=1.8.0']
    # }

    setup_args = {
        'name': 'mrsqm',
        
        'author': 'Le Nguyen Thach',
        'author_email': 'thach.lenguyen@ucd.ie',
        'description': (
            'A test version for mrsqm.'),
        'url': 'https://github.com/lnthach/mrsqm',
        
        'classifiers': [
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Scientific/Engineering :: Image Processing',
            'Topic :: Scientific/Engineering :: Physics',
            'Topic :: Multimedia :: Sound/Audio :: Analysis'
        ],        
        'python_requires': ">=3.8",
    }

    setup_args['setup_requires'] = build_requires
    setup_args['install_requires'] = install_requires
    # setup_args['extras_require'] = opt_requires

    if len(sys.argv) >= 2 and (
        '--help' in sys.argv[1:] or
        sys.argv[1] in ('--help-commands', 'egg_info', '--version',
                        'clean')):
        # For these actions, NumPy is not required.
        pass
    else:
        #setup_args['packages'] = [
        #    'pyfftw', 'pyfftw.builders', 'pyfftw.interfaces']
        setup_args['ext_modules'] = get_extensions()
        #setup_args['package_data'] = get_package_data()

    # Do a trial run to determine dependencies
    # Not ideal, but distutils, setuptools and cython are hard to work with
    # and several hours of messing around didn't yield a good solution
    # The problem is getting access to either a good compiler object or
    # the compile_time_env before calling setup()
    if sys.argv[1] == "build_ext":
        from Cython.Build import cythonize

        trial_distribution = setup(**setup_args)
        cython_compile_time_env = trial_distribution.get_command_obj("build_ext")
        
        #setup_args["ext_modules"] = cythonize(get_extensions(), compile_time_env=cython_compile_time_env)

        setup_args["ext_modules"] = cythonize(Extension(
            name="mrsqm",                                # the extension name
            sources=["src/mrsqm/mrsqm_wrapper.pyx","src/mrsqm/sfa/MFT.cpp","src/mrsqm/sfa/DFT.cpp","src/mrsqm/sfa/SFA.cpp","src/mrsqm/sfa/TimeSeries.cpp"], # the Cython source and
                                                  # additional C++ source files
            #sources=["mrsqm_wrapper.pyx"],
            extra_compile_args=["-Wall", "-Ofast", "-g", "-std=c++11", "-ffast-math"],
            extra_link_args=["-lfftw3", "-lm", "-L/opt/local/lib"],           
            language="c++",                        # generate and compile C++ code

      ))

    setup(**setup_args)

if __name__ == '__main__':
    setup_package()