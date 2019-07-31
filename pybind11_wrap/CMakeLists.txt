######################################
# pybind11 wrap
######################################

#first of all detect system installation, then check local folder,
#find_package(pybind11)
if(pybind11_FOUND)
    message("system wide pybind11 installation found\n")
    # systemwide installation by package manager with header in `/usr/include/`
else()
    if(NOT EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/pybind11/include/")
        message("===============================================================\n"
                "pybind11 not found on system and ${CMAKE_CURRENT_SOURCE_DIR}, run git submodule add\n"
                "===============================================================\n")
        execute_process(COMMAND git submodule add --force https://github.com/pybind/pybind11.git
                    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                    ERROR_VARIABLE error_var
                    RESULT_VARIABLE ret_var)
        message("rv='${ret_var}'\n error msg = '${error_var}'")
        # need build
        
    else()
        message("pybind11 is found in the folder: ${CMAKE_CURRENT_SOURCE_DIR}\n")
    endif()

    add_subdirectory("${CMAKE_CURRENT_SOURCE_DIR}/pybind11")
    SET(pybind11_FOUND TRUE)
endif()


if(pybind11_FOUND)
    # this will generate multiple versions of py module
    #set(PYBIND11_PYTHON_VERSION 2.7 3.6)
    pybind11_add_module(${MY_MODULE}_pybind11 shapes_pybind11.cpp)

    # "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/${MY_SHARED_LIB}"
    target_link_libraries(${MY_MODULE}_pybind11 PRIVATE ${MY_SHARED_LIB})
else()  # compile local download pybind11 lib and extra cmake module
    message("===============================================================\n"
            "pybind11 not found, please install systemwide or clone to this folder\n"
            "===============================================================\n")
endif()
