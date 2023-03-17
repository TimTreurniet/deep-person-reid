from Cython.Build import cythonize
import numpy as np
from distutils.extension import Extension
import os


# def numpy_include():
#     try:
#         numpy_include = np.get_include()
#     except AttributeError:
#         numpy_include = np.get_numpy_include()
#     return numpy_include


# ext_modules = [
#     Extension(
#         'torchreid.metrics.rank_cylib.rank_cy',
#         ['torchreid/metrics/rank_cylib/rank_cy.pyx'],
#         include_dirs=[numpy_include()],
#     )
# ]

# def build(setup_kwargs):
#     setup_kwargs.update({
#         'ext_modules': cythonize(ext_modules)
#     })


# See if Cython is installed
try:
    from Cython.Build import cythonize
# Do nothing if Cython is not available
except ImportError:
    # Got to provide this function. Otherwise, poetry will fail
    def build(setup_kwargs):
        pass
# Cython is installed. Compile
else:
    from setuptools import Extension
    from setuptools.dist import Distribution
    from distutils.command.build_ext import build_ext

    # This function will be executed in setup.py:
    def build(setup_kwargs):
        # The file you want to compile
        extensions = [
            "torchreid.metrics.rank_cylib.rank_cy"
        ]

        # gcc arguments hack: enable optimizations
        os.environ['CFLAGS'] = '-O3'

        # Build
        setup_kwargs.update({
            'ext_modules': cythonize(
                extensions,
                language_level=3,
                compiler_directives={'linetrace': True},
            ),
            'cmdclass': {'build_ext': build_ext}
        })
