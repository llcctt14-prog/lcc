"""用独立公式和边界情况核对计算，运行：python -m unittest -v。"""

import unittest

from calculator import future_value


class FutureValueTests(unittest.TestCase):
    def test_compound_without_contributions(self):
        self.assertAlmostEqual(future_value(10000, 0.06, 1), 10616.778118644983)

    def test_contributions_match_annuity_formula(self):
        rate = 0.06 / 12
        growth = (1 + rate) ** 24
        expected = 10000 * growth + 500 * (growth - 1) / rate
        self.assertAlmostEqual(future_value(10000, 0.06, 2, 500), expected)

    def test_end_of_month_contributions(self):
        # 首笔投入计息 11 个月，最后一笔投入不计息。
        expected = sum(100 * 1.01 ** months for months in range(12))
        self.assertAlmostEqual(future_value(0, 0.12, 1, 100), expected)

    def test_zero_rate(self):
        self.assertEqual(future_value(10000, 0, 1, 500), 16000)

    def test_zero_years(self):
        self.assertEqual(future_value(10000, 0.06, 0, 500), 10000)

    def test_negative_rate(self):
        self.assertAlmostEqual(future_value(10000, -0.12, 1), 10000 * 0.99 ** 12)

    def test_invalid_inputs(self):
        cases = [
            (-1, 0.06, 1, 0), (100, 0.06, 1, -1),
            (100, -1, 1, 0), (100, 0.06, -1, 0),
            (100, 0.06, 1.5, 0), (float("nan"), 0.06, 1, 0),
            (100, float("inf"), 1, 0), (100, 0.06, 1, float("inf")),
        ]
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError):
                future_value(*case)

    def test_overflow(self):
        with self.assertRaises(ValueError):
            future_value(1e308, 12, 1)


if __name__ == "__main__":
    unittest.main()
