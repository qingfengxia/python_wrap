#Generate the shared library from the library sources
add_library(${MY_SHARED_LIB} SHARED 
    Rectangle.cpp
)
#global var CMAKE_LIBRARY_OUTPUT_DIRECTORY has been set in toplevel