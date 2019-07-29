comparison and interopereation of different c++11 class python wrapping methods, like swig, pybind11, binder, cython, cppyy, etc, with CMake integration setup.

## Introduction

+ demo and comparison of diff methods
+ build systems: cmake,  python setup.py
+ interoperation of compiled module 


## tools to wrap python code

Wrapping binary library is possible, if header files are available.

For C code/lib interfacing
+  C-API:`#include <python.h>` <https://docs.python.org/3/extending/extending.html>
+ `ctypes`  foreign function library/module from the python standard lib, to wrap binary C library. see [cytpes official doc](https://docs.python.org/3/library/ctypes.html)
+ [cffi](): an easier approach than ctypes, but support only C

+ cppyy: Automatic Python-C++ bindings, based on `cling`,  need a c++17 compiler
+ `PyCXX`: C++ version for C-API: `<python.h>`

+  `swig`: wrap C/C++ to several languages like Java, and interpreting lanugages like python, etc.

+ [boost.python](): part of boost lib, it avoid lots of boiler-plate code by c++ template technology
+ `pybind11`: similar but with more features than boost.python
+ binder, can generate pybind11 wrapping code automatically

+ `cython3`: write c++ module in python grammar, it is possible to wrap existing shared binary library given header files.
+ pyrex:

+ wrapping tools for/as a part of some large scale libraries: Qt, GTK, VTK, etc.


>Disclaimer: This is very subjective.

## code organisation

+ `src` : c++ header and source files
+ `*_wrap`: wrap code and setup.py
+ one cmakelists.txt

### environment

This repo focuses on Python3, as 2.7.x has reached the end-of-life in Jan 2020.

Ubuntu 16.04 and 18.04

C++11 is the base line

the example C++ code is adapted from cython official document: 
<http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html>

### Installation

1. manual wrap:
Install `python.h` from package `python3-dev`on Linux ( example for Ubuntu):
`sudo apt-get install -y python3-dev python3-numpy cmake g++`
https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/c++-wrapping.html

1. cython3
Install `cython3` by `sudo apt-get install -y cython3 ` 
<http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html>


2. `pybind11` has been integrated into this repo, there is no need to install

`git submodule add https://github.com/pybind/pybind11.git`

3. boost.python:

4. swig:
try install the latest swig for better c++11 support `sudo apt-get install -y swig3` 

```bash
#this is not OS nor python version portable command to build the py module
swig -c++ -python example.i
c++ -fPIC -c example_wrap.cxx  -I/usr/include/python3.5 -std=c++11
c++ -shared -std=c++11 example_wrap.o -lshapes -L../build -o shape_swig.so
```

python setup.py can also build module, `once example_wrap.cxx` has been generated
https://www.tutorialspoint.com/wrapping-c-cplusplus-for-python-using-swig

CMake has official support to SWIG `swig_add_library`
<https://cmake.org/cmake/help/v3.12/module/UseSWIG.html#command:swig_link_libraries>
<http://www.swig.org/Doc3.0/SWIGDocumentation.html#Introduction_build_system>

5. cppyy:
installation is a little complicated, it is recommended to install into conda virtualenv


6. SIP/shiboken2 for Qt:

### testing

1. `cython` seems incorporate the target so into python so,  because cpp is include

   todo: binary

2. while pybind11 link to it. `ldd this_python.so`

3. testing the mixed, then polymorphal code should be done

   https://cppyy.readthedocs.io/en/latest/classes.html

### Extra readings



[wrap binary C libriary using Cython](https://medium.com/@shamir.stav_83310/making-your-c-library-callable-from-python-by-wrapping-it-with-cython-b09db35012a3)

[swig]()