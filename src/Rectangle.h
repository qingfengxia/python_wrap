#ifndef RECTANGLE_H
#define RECTANGLE_H

#include <tuple>

//extern C export

namespace shapes {
    typedef int scalar;
    class Rectangle {
        public:
            scalar x0, y0, x1, y1;  // cython wrap code stop var to be private
            Rectangle();
            Rectangle(scalar x0, scalar y0, scalar x1, scalar y1);
            ~Rectangle();
            scalar getArea() const;
            void getSize(scalar* width, scalar* height) const;
            std::tuple<scalar, scalar>  getStartPoint() const ;
            void move(scalar dx, scalar dy);
    };
}

#endif