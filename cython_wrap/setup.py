from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# WARNING: the library_dirs is fixed to a specific build folder
shapes_extension = Extension(
    name="shapes_cython",
    sources=["shapes_cython.pyx"],
    libraries=["shapes"],
    library_dirs=["../build/"],
    include_dirs=["../src"],
    extra_compile_args=["-std=c++11"]
)

setup(
    name="shapes_cython",
    ext_modules=cythonize([shapes_extension])
)