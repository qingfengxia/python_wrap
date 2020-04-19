#
#   copyright Qingfeng Xia 2019
#   CC BY 4.0
#


from distutils.core import setup, Extension
import os

os.system("swig -python -c++ example.i")  # generate example_wrap.cxx
#swig -python -c++ example.i
#the generated wrap code is py2 and py3 compatible

#python3 setup.py build_ext --inplace

linking_shared_object = False
if not linking_shared_object:
    example_module = Extension('_shapes_swig',
        sources=['example_wrap.cxx', '../src/Rectangle.cpp'],  # do not link to shared obj
        include_dirs=["../src"],
        extra_compile_args=["-std=c++11"]
    )
else:
    example_module = Extension('_shapes_swig',
        sources=['example_wrap.cxx'],  # link to shared lib (cpp)
        libraries=["shapes"],
        library_dirs=["../lib/"],
        include_dirs=["../src"],
        extra_compile_args=["-std=c++11"]
    )

setup (name = 'shapes_swig',
   version = '0.1',
   author = "SWIG Docs",
   description = """Simple swig example from docs""",
   ext_modules = [example_module],
   py_modules = ["_shapes_swig"],
)

#you may need to copy files to other place to compare with other wrap methods