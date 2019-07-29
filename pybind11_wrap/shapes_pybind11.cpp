#include <pybind11/pybind11.h>
#include "../src/Rectangle.h"
#include <string>

namespace py = pybind11;
using namespace shapes;

PYBIND11_MODULE(shapes_pybind11, m) {
    py::class_<Rectangle>(m, "Rectangle")
        .def(py::init<>())
        .def(py::init<int, int, int, int>())
        .def("getArea", &Rectangle::getArea)
        .def("getSize", &Rectangle::getSize)
        .def("getStartPoint", &Rectangle::getStartPoint)
        .def("move", &Rectangle::move)
        .def("__repr__", [](const Rectangle& r)
            {
                return "Rectangle(" + std::to_string(r.getArea()) + ")";
            }
        );
}
