#
#   copyright Qingfeng Xia 2019
#   CC BY 4.0
#

cmake_minimum_required(VERSION 3.0)
project("python wrap interoperation")

# name shared by subdirectories cmakelists.txt
set(MY_PYBIND11_WRAP "shapes_pybind11")
set(MY_SHARED_LIB "shapes")
set(MY_MODULE "shapes")

# can be set to C++14, 17 on a newer std
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(PYBIND11_CPP_STANDARD -std=c++11)

#extra cmake module provided by this repo
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} 
    "${CMAKE_CURRENT_SOURCE_DIR}/cMake" 
    )

######################################
# options
######################################
option(USE_CYTHON "use cython" ON)
option(USE_PYBIND11 "use pybind11" ON)
option(USE_SWIG "use swig to generate interface code" ON)  # error not fixed
option(USE_BINDER "use binder to generate pybind11 wrap code" OFF)


find_package(PythonInterp REQUIRED)
message(STATUS "Found Python: ${PYTHON_EXECUTABLE} (found version \"${PYTHON_VERSION_STRING}\")")

# cross OS setup
IF(WIN32)
   # windows
   SET(PY_EXTENSION "dll")
ELSE()
   SET(PY_EXTENSION "so")
ENDIF()

## put all targets in bin
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
## put all libraries in lib
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)

link_directories(${CMAKE_LIBRARY_OUTPUT_DIRECTORY})

######################################
# c++ shared library to be wrapped
######################################
add_subdirectory("src")

if(USE_BINDER)
    ######################################
    # binder use a modified pybind11
    ######################################
    add_subdirectory(pybind11_binder)
endif()

if(USE_PYBIND11)
    ######################################
    # pybind11 wrap
    ######################################
    add_subdirectory("pybind11_wrap")
endif()

######################################
# swig build
# camke and setup.py are both provided in subdir
######################################
if(USE_SWIG)
    add_subdirectory("swig_wrap")
endif()

######################################
# cython build
# camke and setup.py are both provided in subdir
######################################
if(USE_CYTHON)
    add_subdirectory("cython_wrap")
endif()


######################################
# test
######################################

#file(COPY "${PROJECT_SOURCE_DIR}/test/test_*.py" 
#     DESTINATION ${PROJECT_BINARY_DIR}
#    )

