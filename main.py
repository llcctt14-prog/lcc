"""运行方式：python main.py"""

from calculator import future_value


def main():
    print("复利与定投计算器")
    print("规则：月利率 = 名义年利率 / 12，每月底定投。")
    print("固定利率数学练习，不包含费用、税费和市场波动。\n")

    try:
        principal = float(input("初始本金（元）："))
        rate_percent = float(input("假设名义年利率（输入 6 表示 6%）："))
        years = int(input("年数（非负整数）："))
        monthly_contribution = float(input("每月定投（元，不定投请输入 0）："))

        annual_rate = rate_percent / 100
        balance = future_value(principal, annual_rate, years, monthly_contribution)
        total_invested = principal + monthly_contribution * years * 12
        profit = balance - total_invested

        print(f"\n累计投入：{total_invested:,.2f} 元")
        print(f"期末金额：{balance:,.2f} 元")
        print(f"累计收益：{profit:,.2f} 元")
    except (ValueError, OverflowError) as error:
        print(f"输入或计算有误：{error}")
        print("请重新运行，输入普通数字；年数需为整数，6% 请填写 6。")


if __name__ == "__main__":
    main()
