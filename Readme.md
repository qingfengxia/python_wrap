

# python wrap

Demonstration, comparison and inter-operation of different c++11 class python wrapping methods, like swig, pybind11, boost-python, cython, cppyy, etc, with CMake and python `setuptools` integration example.

Demonstration of mixed C++ and Python debugging will come soon.

Some other similar comparison: <https://iscinumpy.gitlab.io/post/tools-to-bind-to-python/>

## Feature

+ demonstrate and comparr of different language binding methods
+ demonstrate how to build wrap code and link shared object, instead of compile all from sources
+ build systems: `cmake`,  python `setup.py`
+ support C++11  with options setup in cmake and setup.py
+ investigate the inter-operation of compiled modules from different methods
+ illustration of supporting `numpy.ndarray`
+ introduce the approach of automated binding code generating
+ mixed debugging: debug C++ wrapping code when called in Python


## Tools to wrap python code

### The list of wrapping tools

Wrapping binary library is possible, if header files are available.

**For C code/lib interfacing**
+ directly use Python C-API: `#include <python.h>` 

+ `ctypes`  foreign function library/module from the python standard lib, to interface binary C library in python. see [cytpes official doc](https://docs.python.org/3/library/ctypes.html)

+ [cffi](): an easier and automatic approach, but support only C


** Using C++ template to simplify wrapping**

- [boost.python](https://www.boost.org/doc/libs/1_70_0/libs/python/doc/html/index.html): part of boost lib, it avoid lots of boiler-plate code by c++ template technology
- [`pybind11`](https://github.com/pybind/pybind11): similar but with more features than boost.python
- [PyCXX](http://cxx.sourceforge.net/): long existent C++ version for C-API: `<python.h>`

**Automatic binding generation**

- [cppyy](https://cppyy.readthedocs.io/en/latest/): LLVM JIT solution without writing any wrap code, based on `cling`, still in heavy-development.
- `numba`: generous automatic binding generation without user interference, but limited to math and numpy API, i.e. it can not easily link/use with third-party API.
- [PyBindGen](https://pythonhosted.org/PyBindGen/index.html): similar with cppyy, using GCC to parse C++ header and  generate wrapping code.
- `binder`,  a tool can generate pybind11 wrapping code automatically
-  `boost.python` wrapping code generation: <https://github.com/personalrobotics/chimera>

Wrap C++ code in C, as the bridge to other scripting language like python, javascript. FFI can be used to automatic wrap C API into the target languages.

+ google tensorflow is a good example: <https://github.com/tensorflow/tensorflow>. 

+ swig has a not completed branch to generate C code for C++ code, <https://stackoverflow.com/questions/4547163/c-to-c-wrapper-using-swig-for-fltk>
  
  <https://github.com/swig/swig/tree/gsoc2012-c>
  
+ `libclang` may help to generate C interface to C++ code.

Dedicated wrapping tools mainly targeting on the specific project, but can be used in other projects

+ Qt5: https://wiki.qt.io/Qt_for_Python/Shiboken
+ GTK3 : see [architecture of object introspectin](https://wiki.gnome.org/Projects/GObjectIntrospection/Architecture), it is based on libFFI.so and typelib (API info)
+ VTK, etc. 

Other solutions

+ [cppyy](https://cppyy.readthedocs.io/en/latest/): LLVM JIT solution without writing wrap code, based on `cling`, still in heavy-development

+ [swig](http://www.swig.org): wrap C/C++ to several languages like Java, and interpreting lanugages like python, etc.

+ [cython3](<http://docs.cython.org/): write c++ module in python grammar, it is possible to wrap existing shared binary library given header files.

+ [pyrex](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/): discontinued, superseded by Cython

+ [py++](): automatically extract cpp method and parameter types using gcc-xml and generate the wrapping code

  Py++ uses GCC C++ compiler to parse C++ source files and allows you to expose C++ code to Python in quick and elegant way using the Boost.Python library.

  It uses the following steps to do so:

   - source code is passed to GCC-XML
   - GCC-XML passes it to GCC C++ compiler
   - GCC-XML generates an XML description of a C++ program from GCC's internal
     representation.
   - Py++ uses pygccxml package to read GCC-XML generated file.

**Auto Translate python code into C++ for performance**
There are some python tools that can compile computation expensive function into C module for better performance.

+ numba
+ dask

>Disclaimer: This short description to each tool is very subjective, and for no means it is a complete list. the following suggestion is highly subjective



### Tools to ease the compiling process

+ [cppimport]()  import wrapping cpp source code as normal python module
+ CMake support for: SWIG, CPPYY, pybind11
+ python `setup.py` and `build_ext()`

### Subjective suggestion

For a small project with several header files, pybind11 is recommended to write pythonic interface in a manageable way.

For a project with tens of headers, writing configuration file to control binder for code generation is recommended which can automatically generate boilerplate wrapping code,  <https://github.com/RosettaCommons/binder>.
<https://cppbinder.readthedocs.io/en/latest/basics.html>

If the project has no dependency on binary library, but C++ STL. It is recommended to try `cppyy` to generate the interface without writing extra interfacing code. Currently, installation and project integration is a bit difficult.

For large project like <https://github.com/LaughlinResearch/pyOCCT>,  project specific fork of binder, see <https://github.com/LaughlinResearch/pyOCCT_binder> is used with the specific pyOCCT project.

## Repo organization

+ `src` : c++ header and source files

  the example C++ code is adapted from Cython official document with extra c++11 feature: 
  <http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html>

+ `*_wrap`: has wrap code, `setup.py` and `CMakeLists.txt`

+ Cmake is setup for each wrap methods, with top level and subfolder `CMakelists.txt`.   Python `setup.py` may be also provided in case you do not use cmake build system. 

+ submodule

  `git submodule add https://github.com/pybind/pybind11.git`

### Environment

Tested by python3 on Ubuntu 18.04 and python2 on Ubuntu 16.04. This repo focuses on Python3, as 2.7.x has reached the end-of-life in Jan 2020.

C++11 compiler is the minimum requirement, in the future, C++17 and C++20 can be added.

In order to work with cmake, DO NOT USE relative include path in cython "*.pxd" and swig `*.i` files. Setup include directories in `setup.py` or cmakelists.txt instead!

On windows, by default all symbols are not exported, so *.lib will not be created, so in the toplevel cmakelists.txt

```cmake
SET(WINDOWS_EXPORT_ALL_SYMBOLS ON)
```

This line is added to  pyd target can be linked by  visual c++.

### Limitations
swig has error "can not find tuple" (C++11 std::tuple class) on cmake,
swig has error can not find if built by setup.py on Ubuntu 16.04 

SWIG and Cython generated wrap code is py2 and py3 compatible, dep on which python intepretor to run setup script

## Installation and compiling extension module

### manual wrap:
Install `python.h` from package `python3-dev`on Linux ( example for Ubuntu):

`sudo apt-get install -y python3-dev python3-numpy cmake g++`

Manually wrapping needs a lots of boiler plate code, but it is worth of reading <https://docs.python.org/3/extending/extending.html> to understand the process of wrapping.



### cython3
Install `cython3` by `sudo apt-get install -y cython3 ` 
<http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html>

Cython cmake supported is provided by: https://github.com/thewtex/cython-cmake-example

### pybind11

Cmake will detect system wide installation, 
`sudo apt-get install python3-pybind11 pybind11-dev`
if not installed to system wide, detect a downloaded repo to this folder. If both are not found, CMake will prompt to install:

`git submodule add https://github.com/pybind/pybind11.git`

pybind11 also support `setup.py` and `cppimport`. Example `setup.py` can be adapted from: https://github.com/pybind/python_example/blob/master/setup.py

### pybind11-binder  (written in C++)

`binder` is a tool to generate pybind11 wrapping code automatically, but it still require user configuration.  It is based on LLVM and Clang, written in C++.

source code: <https://github.com/RosettaCommons/binder>

documentation: <https://cppbinder.readthedocs.io/en/latest/>

### pybind11 binder written in python

pyocct:  using his own binding generator, based on python-clangp, LGPL, OCCT 7.4 

 https://github.com/LaughlinResearch/pyOCCT  

macro and class template needs special treatment.

```c++
template <typename TheItemType>

void bind_NCollection_Sequence(py::module &mod, std::string const &name, py::module_local const &local){

py::class_<NCollection_Sequence<TheItemType>, NCollection_BaseSequence> cls_NCollection_Sequence(mod, name.c_str(), "Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n", local);
    //...
```

### `boost.python`:

`sudo apt-get install libboost-python-dev` it may still built against python2. 

There is also a tool to generate wrapping code automatically, ?



### swig:
try install the latest swig for better c++11 support `sudo apt-get install -y swig3` 

```bash
# first of all, build the c++ shared library
g++ -fPIC -shared -c ../src/Rectangle.cpp -std=c++11 -o ../lib/libshapes.so
```

 `setup.py` can also build module independent of python version, once `example_wrap.cxx` (works for python 2 and python 3) has been generated by `swig -python -c++ example.i`:

```bash
swig -python -c++ example.i
python3 setup.py build_ext --inplace
```

```bash
# generate wrapping code for python 2 and python3
swig -c++ -python example.i
#this is not OS nor python version portable command to build the py module
# to demonstrate how python module are built by `python3 setup.py build_ext --inplace`
c++ -fPIC -c example_wrap.cxx  -I/usr/include/python3.6m -std=c++11
c++ -shared -std=c++11 example_wrap.o -lshapes -L../build -o ../lib/shape_swig.so
```

If `libshapes.so` has not been install to shared library loadable location, such as  LD_LIBRARY_PATH on Linux,  there will be error: `cannot open shared object file: libshapes.so`  . The error can be avoided by not linking to `libshapes.so`

```bash
c++ -fPIC example_wrap.cxx ../src/Rectangle.cpp  -I/usr/include/python3.6m -I../src -std=c++11 -shared  -o ../lib/shape_swig.so
# shape_swig.so is a python module, but it is wrapping of low level C API
# but swig_shape.py higher level python module is generate by setup.py
```

https://www.tutorialspoint.com/wrapping-c-cplusplus-for-python-using-swig

CMake has official support to SWIG `swig_add_library`
<https://cmake.org/cmake/help/v3.12/module/UseSWIG.html#command:swig_link_libraries>
<http://www.swig.org/Doc3.0/SWIGDocumentation.html#Introduction_build_system>

### cppyy:
`cppyy` is  based on cling JIT intepreter, there is not compiling needed. see `test_cppyy.py`. Meanwhile, it is possible to generate importable python binding like other tools.   

Here is an example cmake integration in `cppyy_wrap` folder, based on

> cppyy-knn: An example of cppyy-generated bindings for a simple knn  implementation. 

 https://github.com/camillescott/cppyy-knn
when following this repo Readme, you need append  ` -c conda-forge` to find packages.  To create conda env. 

My experience, there is still some little work to make it more pythonic, fortunately, example can be found in this [cppyy-knn repo]( https://github.com/camillescott/cppyy-knn)

 http://www.camillescott.org/2019/04/11/cmake-cppyy/

installation to system wide python is possible (tested on Ubuntu 18.04), it is recommended to install into conda virtualenv on linux

set extra envvar by export `EXTRA_CLING_ARGS`, e.g.
`export EXTRA_CLING_ARGS='-O2 -std=c++17' && python`

#### pip on windows

successfully `pip install cppyy` and built the wheel on window 10 with

+ visual studio 2019 build tool (Visual C++ compiler version 14.2)

- windows 10 x64
- cppyy 1.5.4
- Conda python 3.7.3 (64bit) [MSC v.1915 64 bit (AMD64)]

Building pre-compiled headers failed on startup for cppyy 1.5.x, it seems fix in verion 1.6.x. However, it is fine to run test with performance impact

> Fatal in <UnknownClass::GetListOfGlobals>: fInterpreter not initialized
> aborting

On windows 10, only C++14 is supported, while on Linux, C++17 is supported by cppyy. check out by:

```print(cppyy.gbl.gInterpreter.ProcessLine("__cplusplus;"))```

### SIP of PyQt5 or shiboken2 for PySide2:

todo:

https://blog.qt.io/blog/2018/05/31/write-python-bindings/

## testing

### local test

1. `cython` seems incorporate the target shared object into python so,  because source is include

   todo: binary

2. while pybind11 link to shared object, checked by `ldd this_python.so`

3. testing the mixed, then polymorphic code should be done

   https://cppyy.readthedocs.io/en/latest/classes.html

### CI matrix

https://github.com/pybind/pybind11/blob/master/.travis.yml



## numpy array and Eigen Matrix interface

### pybind11 

#### STL vector and python buffer protocol

pybind11 has built-in support for   passing value of `std::vector<T>`. To pass reference, there are two ways, make it opaque, or more generic buffer protocol by `py::buffer_info`.

#### pybind11 for numpy array

and numpy.array as `py::array` or restricted scallar type by `py::array_t<double>`. `py::array_t<T>` class, defiend in  `#include <pybind11/numpy.h>`,  will be automatically map into `numpy.array`.  New data type for `py::array_t<T>` can be crated by `PYBIND11_NUMPY_DTYPE(struct_name, field1, ...)`.  For performance reason, index checking can be disabled by using `auto r = x.mutable_unchecked<3>()` where `x` is of type `py::array_t<T>`

see more   <https://pybind11.readthedocs.io/en/stable/advanced/pycpp/numpy.html>

#### pybind11 for Eigen

> [Eigen](http://eigen.tuxfamily.org/) is C++ header-based library for dense and sparse linear algebra. Due to its popularity and widespread adoption, pybind11 provides transparent conversion and limited mapping support between Eigen and Scientific Python linear algebra data types.

Official document has example to wrap `Eigen::MatrixXd` for numpy

#### xtensor

- `xtensor` is a C++14 library for multi-dimensional arrays enabling numpy-style broadcasting and lazy computing.

  https://xtensor.readthedocs.io/en/latest/

- `xtensor-python` header-only lib enables inplace use of numpy arrays in C++ with all the benefits from `xtensor`

https://github.com/xtensor-stack/xtensor-python

### cppyy

`cppyy.LowLevelView` is used to convert `void*` buffer address back to numpy array `numpy.frombuffer()`, see example

see <https://cppyy.readthedocs.io/en/latest/lowlevel.html#numpy-casts>

passing numpy array to C++ , is surprisely hard. here is code tested to work

`void* compressBlock(const unsigned char* im, std::vector<unsigned int> shape)`

```python
    buf = im.tobytes()  # bytes type and content is fine

    #pbuf = im.ctypes.data_as(ctypes.c_ubyte* len(buf))
    # TypeError: cast() argument 2 must be a pointer type, not c_ubyte_Array_4096
    
    #pbuf = ctypes.create_string_buffer(len(buf), buf) # only for unicode string type

    # ctypes.POINTER(ctypes.c_ubyte)  is for byte** output parameter,
    #pbuf = im.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte*len(buf))) #  error!
    pbuf = array.array('B', buf)  # correct
    
    # from_buffer(buf)  TypeError: underlying buffer is not writable
    #pbuf = (ctypes.c_ubyte * len(buf)).from_buffer_copy(buf)  # correctly
    pbuf = ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte * len(buf)))[0]  # correctly

    print("type of pbuf ", type(pbuf))
    print("content of pbuf: ", pbuf[:16])

    h, w = im.shape[0]//block_size, im.shape[1]//block_size
    arr = cppyy.gbl.compressBlock(pbuf, im.shape) # .reshape((h*w,))
```



## Compatibility and ABI

### Mixing different wrapping is possible 

On the python level, is it possible to use C-exnteions modules wrapped by different methods. 

FreeCAD project has a mixed approaches of:

+ swig

+ PyCXX,  C++ wrapper of C-API in header `#include <Python.h>`

+ pybind11 may be used by some extension

  It is all about ABI compatibility. 

  + C or C++ runtime ABI tends to be more stable on Linux, 

  + Compiler like gcc has the compatible ABI since G++ 5.x.  

  + Python 3.8 and 3.7 has different ABI, although C-API is compatible (only adding new API),  there is subset API is ABI stable since 3.2, see <https://docs.python.org/3/c-api/stable.html>

    

  Hint: compiling FreeCAD from source,  using the same compiler as used to compile python, should work

### Passing C++ object around 

see discussion on Cppyy documentation section:

https://cppyy.readthedocs.io/en/latest/lowlevel.html#capsules

> It is not possible to pass proxies from cppyy through function arguments of another binder/wrapper (and vice versa, with the exception of `ctypes`, see below), because each will use a different internal representation, including for type checking and extracting the C++ object address. However, all Python binders are able to rebind (just like `bind_object` above for cppyy) the result of at least one of the following:
>
> - **ll.addressof**: Takes a cppyy bound C++ object and returns its address as an integer value. Takes an optional `byref` parameter and if set to true, returns a pointer to the address instead.
> - **ll.as_capsule**: Takes a cppyy bound C++ object and returns its address as a PyCapsule object. Takes an optional `byref` parameter and if set to true, returns a pointer to the address instead.
> - **ll.as_cobject**: Takes a cppyy bound C++ object and returns its address as a PyCObject object for Python2 and a PyCapsule object for Python3. Takes an optional `byref` parameter and if set to true, returns a pointer to the address instead.
> - **as_ctypes**: Takes a cppyy bound C++ object and returns its address as a `ctypes.c_void_p` object. Takes an optional `byref` parameter and if set to true, returns a pointer to the address instead.

### Different C++ compilers can compile module 

`pybind11` wrapper cpp file can be compiled by both "mingw32-x64 v8.1" and "Visual C++ compiler version 14.2" .   Python itself has compiled by one kind of compiler, usually is the platform default, such as VS studio on Windows. 

Python 3.8 has unified release and debug compiling ABI. 

Tested: Anaconda python3.7 (64bit), which has the rumtime`vcruntime140`. 



## Extra readings

https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/c++-wrapping.html

[wrap binary C libriary using Cython](https://medium.com/@shamir.stav_83310/making-your-c-library-callable-from-python-by-wrapping-it-with-cython-b09db35012a3)



## License (CC BY 4.0)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

In short: 
 **Share** — copy and redistribute the material in any medium or format 

 **Adapt** — remix, transform, and build upon the material  for any purpose, even commercially. 

**Attribution** — You must give [appropriate credit](https://creativecommons.org/licenses/by/4.0/#), provide a link to the license, and [indicate if changes were made](https://creativecommons.org/licenses/by/4.0/#). You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

see license file in this repo

**Note**:  This CC BY 4.0 does not cover code from other projects:
Cython cmake file from: https://github.com/thewtex/cython-cmake-example
`boost_wrap\boost_python.cpp` which comes from stackoverflow pages, it is covered `cc by-sa 3.0`
