def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    # You have to code here!
    def division(x):
        assert type(n) == int, 'Solo puedes ingresar enteros'
        assert n > 0, 'El divisor debe ser mayor a 0'
        assert type(x) == int, 'Solo puedes ingresar enteros'
        return x / n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):

        def setUp(self):
            self.testing = {
                6: [18, 3],
                20: [100, 5],
                3: [54, 18],
                2: [8, 4],
                5: [10, 2],
                2: [6, 3],
            }

        def test_closure_make_division_by(self):
            # Make the closure test here
            for key, value in self.testing.items():
                division_by_n = make_division_by(value[1])
                # print(f'{key}, {value[1}, {value[0]}, {division_by_n}, {division_by_n(value[0])}')
                self.assertEqual(key, division_by_n(value[0]))
                del(division_by_n)
                
        def tearDown(self):
            # Delete the needed values for the tests
            del(self.testing)
            print('Result: ')
            run()
            

    unittest.main()
