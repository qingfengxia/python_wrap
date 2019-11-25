
""" sucessfully `pip install cppyy` and built the wheel on window 10 with
vs 2019 build tool, x64, cppyy 1.5.4, conda python 3.7
but failed to update cppyy by `pip install -U cppyy`

`cppyy_generator` does not exist, copy `cppyy_generator.exe` into cppyy_generator

building pre-compiled headers failed on startup, it is fine to run with performance impact
# cmake .. && MSBuild.exe SOLUTION_FILE.vcxproj

#export EXTRA_CLING_ARGS='-mavx' && python

"""

import os
import os.path
import cppyy
#std = cppyy.gbl.std
from cppyy.gbl import std

# which compiler it use? cling?
#print(cppyy.gbl.gInterpreter)
print(cppyy.gbl.gInterpreter.ProcessLine("__cplusplus;"))
#export EXTRA_CLING_ARGS='-O2 -std=c++17'
#windows set to C++14
###################

#cppyy.include()  # header files
#cppyy.load_library()   # shared lib
G=cppyy.gbl
print("std namespace", G.std)
##########################
cppyy.cppdef("""
class MyClass {
public:
    MyClass(int i) : m_data(i) {}
    virtual ~MyClass() {}
    virtual int add_int(int i) { return m_data + i; }
    int m_data;
};""")

from cppyy.gbl import MyClass
m = MyClass(42)
cppyy.cppdef("""
void say_hello(MyClass* m) {
    std::cout << "Hello, the number is: " << m->m_data << std::endl;
}""")

MyClass.say_hello = cppyy.gbl.say_hello
m.say_hello()

m.m_data = 13
m.say_hello()