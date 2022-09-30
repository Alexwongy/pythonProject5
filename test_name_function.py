import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""


    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这种名字吗"""
        formatted_name = get_formatted_name('Janis', 'Joplin') #使用两个实参调用get_formatted_name()
        self.assertEqual(formatted_name, 'Janis Joplin') #unittest类最常用的功能：断言方法，核实得到的结果是否与期望的结果一致


    def test_firt_last_middle_name(self):
        """能够正确地处理三个name地名字吗"""
        formatted_name = get_formatted_name(
            'wolfang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()