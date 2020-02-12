import unittest

def fat(n):
    if(n == 0):
        return 1
    return  n * fat(n - 1)

def pot(base, exp):
    if exp(exp == 0):
        return 1
    return base * pot(base, exp - 1)

class TesteMathMthods(unittest.TestCase):
    def test_pot(self):
        self.assertEqual(1024, pot(2, 10))

unittest.main()