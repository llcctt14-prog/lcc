"""复利与定投计算：名义年利率 / 12，每月底投入。"""

from math import isfinite


def future_value(principal, annual_rate, years, monthly_contribution=0):
    """返回期末金额。annual_rate 用小数，例如 0.06 表示 6%。"""
    if not all(isfinite(x) for x in (principal, annual_rate, monthly_contribution)):
        raise ValueError("本金、利率和定投金额必须是有限数字。")
    if principal < 0 or monthly_contribution < 0:
        raise ValueError("本金和每月定投金额不能为负数。")
    if annual_rate <= -1:
        raise ValueError("本练习要求名义年利率大于 -100%。")
    if not isinstance(years, int) or years < 0:
        raise ValueError("年数必须是非负整数。")

    monthly_rate = annual_rate / 12
    months = years * 12
    balance = principal

    for month in range(months):
        # 先计算本月利息，再加入月底投入的金额。
        balance = balance * (1 + monthly_rate) + monthly_contribution
        if not isfinite(balance):
            raise ValueError("计算结果过大，请降低金额、利率或年数。")

    return balance
