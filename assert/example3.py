import unittest


def broken_function():
    raise Exception('Это ошибка')


class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            broken_function()

        self.assertTrue('Это ошибка' in str(context.exception))


if __name__ == '__main__':
    unittest.main()