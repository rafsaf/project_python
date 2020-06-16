""" Tests for classes file """

import unittest
import datetime

import classes

class Test_Bilans(unittest.TestCase):
    def setUp(self):
        self.today = datetime.datetime.today()
        self.current_date = datetime.date(year=self.today.year, month=self.today.month, day=self.today.day)
    def test_get_another_month_return_correct_moth1(self):
        month_now = classes.Bilans().get_another_month(0).month
        self.assertEqual(month_now, self.current_date.month)


class Test_draw_plot_one_month(unittest.TestCase):

    def test_get_ys_for_plot(self):
        parametr_list = [(1,1)]+[(i, 0) for i in range(2,32)]

        correct_result = [1]*31

        self.assertEqual(correct_result, classes.Draw_plot_one_month().get_ys_for_plot(parametr_list))

if __name__ == '__main__':
    unittest.main()
