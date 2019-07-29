cmake_minimum_required(VERSION 3.0)
project("python wrap interoperation")

set(MY_PYBIND11_WRAP "shapes_pybind11")
set(MY_SHARED_LIB "shapes")
set(MY_MODULE "shapes")

# can be set to C++14, 17 on a newer class
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(PYBIND11_CPP_STANDARD -std=c++11)

######################################
# options
######################################
option(USE_CYTHON "use cython" ON)
option(USE_SWIG "use swig to generate interface code" OFF)  # error not fixed
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

######################################
# c++ shared library
######################################
#Generate the shared library from the library sources
add_library(${MY_SHARED_LIB} SHARED 
    src/Rectangle.cpp
)

## put all targets in bin
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
## put all libraries in lib
#set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/test)

if(USE_BINDER)
    ######################################
    # binder use a modified pybind11
    ######################################
    add_subdirectory(pybind11_binder)
    #git submodule add https://github.com/RosettaCommons/binder.git
    # it is required build binder inside llvm-tool-extra from source
    #git submodule add https://github.com/RosettaCommons/pybind11.git
    include_directories("pybind11_binder/pybind11/include")

else()
    ######################################
    # pybind11 binder
    ######################################
    add_subdirectory(pybind11_wrap/pybind11)
    include_directories("pybind11_wrap/pybind11/include")

    # this will generate multiple versions of py module
    #set(PYBIND11_PYTHON_VERSION 2.7 3.6)
    pybind11_add_module(${MY_PYBIND11_WRAP} pybind11_wrap/shapes_pybind11.cpp)
    target_link_libraries(${MY_PYBIND11_WRAP} PRIVATE ${MY_SHARED_LIB})
endif()

######################################
# swig build
######################################
if(USE_SWIG)
    FIND_PACKAGE(PythonLibs)
    INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})
    find_package(SWIG REQUIRED)  # cmake 3 has official swig support
    if(OFF)
        include(UseSWIG)
        set(MY_SWIG_INTERFACE "swig_wrap/example.i")
        set_property(SOURCE  ${MY_SWIG_INTERFACE}  PROPERTIES SWIG_FLAGS "-includeall")
        set_property(SOURCE  ${MY_SWIG_INTERFACE}  PROPERTY CPLUSPLUS ON)

        #TYPE <SHARED|MODULE|STATIC|USE_BUILD_SHARED_LIBS>  default to MODULE
        swig_add_library(${MY_MODULE}_swig
                         LANGUAGE python
                         #NO_PROXY
                         OUTPUT_DIR ${PROJECT_BINARY_DIR}
                         OUTFILE_DIR ${PROJECT_BINARY_DIR}/swig
                         SOURCES example.i
                        )
    else()
        INCLUDE(${SWIG_USE_FILE}) # 3.6 or less
        #http://www.swig.org/Doc3.0/SWIGDocumentation.html#Introduction_build_system
        SET_SOURCE_FILES_PROPERTIES(  ${MY_SWIG_INTERFACE}  PROPERTIES CPLUSPLUS ON)
        SET_SOURCE_FILES_PROPERTIES(  ${MY_SWIG_INTERFACE}  PROPERTIES SWIG_FLAGS "-includeall")

        swig_add_module(${MY_MODULE}_swig
                         python
                        ${MY_SWIG_INTERFACE}  
                        )
    endif()
    #target_link_libraries
    swig_link_libraries(${MY_MODULE}_swig ${MY_SHARED_LIB} ${PYTHON_LIBRARIES})
endif()

######################################
# cython build
######################################
#find_package(Cython)  # no such config file
if(USE_CYTHON)
    execute_process(COMMAND "python3 setup.py --dist-dir ${PROJECT_BINARY_DIR} build_ext --inplace" 
        WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}/cython_wrap"
        #OUTPUT_VARIABLE outMessage
        )
    #message(${outMessage})
    # this file match os on Unix-like system, dll on other OSs
    #file(COPY "cython_wrap/*.${PY_EXTENSION}" DESTINATION ${PROJECT_BINARY_DIR})
else()
    message("Cython3 is not found/used")
endif()


######################################
# test
######################################

#file(COPY "${PROJECT_SOURCE_DIR}/test/test_*.py" 
#     DESTINATION ${PROJECT_BINARY_DIR}
#    )

