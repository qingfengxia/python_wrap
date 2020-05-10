%module shapes_swig
%{
// relative include path can cause error in cmake, 
// in that case, add the cpp source folder into include_directories()
#include "Rectangle.h"
%}

// cmake failed because it can not find `tuple`, while python3 setup.py is working
// the following copy and paste can be avoided by %include directive
//%include "Rectangle.h"
// however, if there is some modification to the headers,
//  then you should copy the content and trim it, e.g. remove the function returning `std::tuple`

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
            //std::tuple<scalar, scalar>  getStartPoint() const ;  // cause error
            void move(scalar dx, scalar dy);
    };
}