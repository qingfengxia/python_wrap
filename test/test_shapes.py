import shapes_pybind11 as pw
import shapes_cython as cw

dir(pw)
dir(cw)

def test_init():
    r1 = pw.Rectangle()
    r2 = pw.Rectangle(0, 0, 2, 4)
    r3 = cw.PyRectangle()
    r4 = cw.PyRectangle(0, 0, 2, 4)


def test_getArea():
    r1 = pw.Rectangle(0, 0, 2, 4)
    r2 = cw.PyRectangle(0, 0, 2, 4)
    assert r1.getArea() == r2.getArea()


def test_getStartPoint():
    r1 = pw.Rectangle(0, 1, 2, 3)
    assert (0, 1) == r1.getStartPoint()

test_getArea()
test_getStartPoint()