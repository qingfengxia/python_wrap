#
#   copyright Qingfeng Xia 2019
#   CC BY 4.0
#

#Generate the shared library from the library sources
add_library(${MY_SHARED_LIB} SHARED 
    Rectangle.cpp
)
#global var CMAKE_LIBRARY_OUTPUT_DIRECTORY has been set in toplevel