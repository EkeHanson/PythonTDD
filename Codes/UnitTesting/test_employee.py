import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUp')

    @classmethod
    def tearDownClass(cls):
        print('tearDwonClass')

    def setUp(self):
        print('SetUp')
        self.emp_1 = Employee('Ekene-onwon', 'Hanson', 100000)
        self.emp_2 = Employee('Uraka', 'Rowland', 10000)

    def tearDown(self):
        print('tearDown\n')
        pass
    
    def test_email(self):
        print('TestEmail')
        self.emp_1.first = 'Gwung'
        self.emp_2.first = 'Eke'

        self.assertEqual(self.emp_1.email, 'Gwung.Hanson@email.com')
        self.assertEqual(self.emp_2.email, 'Eke.Rowland@email.com')


    def test_fullname(self):
        print('Full Name')
        self.assertEqual(self.emp_1.fullname, 'Hanson, Ekene-onwon')
        self.assertEqual(self.emp_2.fullname, 'Rowland, Uraka')


        self.emp_1.first = 'Hanson'
        self.emp_2.first = 'Rowland'

        self.assertEqual(self.emp_1.fullname, 'Hanson, Hanson')
        self.assertEqual(self.emp_2.fullname, 'Rowland, Rowland')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1 = Employee('Ekene-onwon', 'Abraham', 100000)
        self.emp_2 = Employee('Uraka', 'Rowland', 10000)

        self.assertEqual(self.emp_1.fullname, 'Abraham, Ekene-onwon')
        self.assertEqual(self.emp_2.fullname, 'Rowland, Uraka')


        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 100001)
        self.assertEqual(self.emp_2.pay, 10001)



       


if __name__ == '__main__':
    unittest.main()