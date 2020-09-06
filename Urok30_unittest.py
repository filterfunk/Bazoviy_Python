import unittest
from Urok30_Testirovanie import full_name


class NameTestCase(unittest.TestCase):
    '''Тесты для full_name'''

    def test_first_last_nane(self):
        '''Имена вида - Иванов Иван'''
        format_name = full_name('Иванов', 'Иван')
        self.assertEqual(format_name, 'Иванов Иван')

    def test_last_middle(self):
        '''Имена вида - Иванов Иван Иванович'''
        format_name = full_name('Иванов', 'Иван', 'Иванович')
        self.assertEqual(format_name, 'Иванов Иван Иванович')


if __name__ == "__name__":
    unittest.main()
