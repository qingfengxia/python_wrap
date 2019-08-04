
/*
tutorial from tutorial on stackoverflow
user contributions licensed under cc by-sa 3.0 with attribution required. 
https://stackoverflow.com/questions/31555161/how-to-compile-create-shared-library-and-import-c-boost-module-in-python


#sudo apt-get install python3-dev libboost-python-dev
g++ -I /usr/include/python2.7 -fpic -c -o orm.o orm.cpp  && g++ -o orm.so -shared orm.o -lboost_python -lpython2.7
g++ -I /usr/include/python3.6 -fpic -c -o boost_wrap.o boost_wrap.cpp  && g++ -o boost_wrap.so -shared boost_wrap.o -lboost_python -lpython3.6

#change python2.7 to python3.6/python3.5m in both line, you should be able to compile on ubuntu 18.04
*/

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-local-typedefs"
#include <boost/python.hpp>
#include <boost/python/raw_function.hpp>
#pragma GCC diagnostic pop

namespace python = boost::python;

class ORM
{
public:
  void foo(){std::cout << "foo" << std::endl;}
};

BOOST_PYTHON_MODULE(orm)
{
python::class_<ORM>("ORM")
    .def("foo", &ORM::foo)
;
}