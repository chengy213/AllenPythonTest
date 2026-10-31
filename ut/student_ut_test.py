import unittest

from student_test import Student, MY_GENDER


class TestStudent(unittest.TestCase):
    def setUp(self):
        """每个测试方法前执行，重置计数器"""
        Student.count = 0

    def tearDown(self):
        """每个测试方法后执行"""
        pass
    def test_count(self):
        s1 = Student("allen", MY_GENDER.BOY, 35)
        s2 = Student("frank", MY_GENDER.BOY, 30)
        s3 = Student("andy", MY_GENDER.GIRL, 40)
        self.assertEqual(Student.count, 3)
        self.assertEqual(s1._gender, s2._gender)

if __name__ == '__main__':
    unittest.main()