#In your CMake configuration, make sure that PYTHON_LIBRARY, PYTHON_INCLUDE_DIR, and CYTHON_EXECUTABLE are all using the same CPython version.

find_package( PythonLibs REQUIRED )


if( CYTHON_EXECUTABLE )
    # customed cmake module downloaded from
    #https://github.com/thewtex/cython-cmake-example/cmake/
    find_package( Cython REQUIRED )
    include( UseCython )

    include_directories("${PROJECT_SOURCE_DIR}/src")

    # If the pyx file is a C++ file, we should specify that here.
    set_source_files_properties("shapes_cython.pyx"
    PROPERTIES CYTHON_IS_CXX TRUE )

    # copy the source folder, because the generated wrapping code using relative path include
    #file(COPY "${PROJECT_SOURCE_DIR}/src/Rectangle.cpp" DESTINATION "${PROJECT_BINARY_DIR}/src/Rectangle.cpp")

    # Multi-file cython modules do not appear to be working at the moment.
    cython_add_module( "${MY_MODULE}_cython"  shapes_cython.pyx 
                                                            )
    #${PROJECT_SOURCE_DIR}/src/Rectangle.cpp 
    link_libraries("${MY_MODULE}_cython" PRIVATE ${MY_SHARED_LIB})
else()
    message("UseCython is not found/usable, run setup.py later")
    if(OFF)
        # the shared_object is not ready to be linked
        execute_process(COMMAND python3 setup.py --dist-dir ${PROJECT_BINARY_DIR} build_ext --inplace
                                WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
                                ERROR_VARIABLE error_var
                                RESULT_VARIABLE ret_var)
            message("rv='${ret_var}'\n error msg = '${error_var}'")
        # copy target to a central place for testing
        file(COPY "*.${PY_EXTENSION}" DESTINATION "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")
    endif()
endif()