cmake_minimum_required(VERSION 3.10)

project(cppyy_example LANGUAGES CXX)

#FindLibClang.cmake
#if(WIN32)
#find_library(LibClang_LIBRARY libclang.dll
#    PATH_SUFFIXES $ENV{CONDA_PREFIX}/Library/bin
#)
#endif()


#conda install -c conda-forge LibClang
#python wrap of clang, you need to install libclang first
#pip install clang  # python binding clang6
#install llvm6 from official and add to user PATH


execute_process(COMMAND cling-config --cmake OUTPUT_VARIABLE CPPYY_MODULE_PATH OUTPUT_STRIP_TRAILING_WHITESPACE)
# Make sure this is set to something like:
# ~/.local/lib/python2.7/site-packages/cpyy_backend/cmake
#D:\Software\Anaconda3\Lib\site-packages\cppyy_backend\cmake

message("CPPYY_MODULE_PATH: " ${CPPYY_MODULE_PATH})
list(INSERT CMAKE_MODULE_PATH 0 ${CPPYY_MODULE_PATH})

find_package(Cppyy)  #

set(SOURCES ../src/Rectangle.cpp)
set(HEADERS ../src/Rectangle.h)

# It seems like this library has to be shared...
add_library(cppyy_example SHARED ${SOURCES})
# Note this is a necessary compile flag for cppyy bindings to work.
set_target_properties(cppyy_example PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_include_directories(cppyy_example PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

#windows only has c++14 support
cppyy_add_bindings(
   "cppyy_example" "0.0.1" "Joel" "joel@joel.com"
   LANGUAGE_STANDARD "14"
   GENERATE_OPTIONS "-D__PIC__;-Wno-macro-redefined"
   INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
   LINK_LIBRARIES cppyy_example
   H_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
   H_FILES ${HEADERS})
