import libcplx as lc
import unittest

class Testcplxfunc(unittest.TestCase):

    def test_sumcplx(self):
        # (3+5i) + (-2.6 + 6.8i) = 0.4 + 11.8i
        c1= (3, 5)
        c2= (-2.6, 6.8)
        suma = lc.sumacplx(c1,c2)
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)

if __name__ == '__main__':
    unittest.main()