"""���з�ʽ��python main.py"""

from calculator import future_value


def main():
    print("�����붨Ͷ������")
    print("���������� = ���������� / 12��ÿ�µ׶�Ͷ��")
    print("�̶�������ѧ��ϰ�����������á�˰�Ѻ��г�������\n")

    try:
        principal = float(input("��ʼ����Ԫ����"))
        rate_percent = float(input("�������������ʣ����� 6 ��ʾ 6%����"))
        years = int(input("�������Ǹ���������"))
        monthly_contribution = float(input("ÿ�¶�Ͷ��Ԫ������Ͷ������ 0����"))

        annual_rate = rate_percent / 100
        balance = future_value(principal, annual_rate, years, monthly_contribution)
        total_invested = principal + monthly_contribution * years * 12
        profit = balance - total_invested

        print(f"\n�ۼ�Ͷ�룺{total_invested:,.2f} Ԫ")
        print(f"��ĩ��{balance:,.2f} Ԫ")
        print(f"�ۼ����棺{profit:,.2f} Ԫ")
    except (ValueError, OverflowError) as error:
        print(f"������������{error}")
        print("���������У�������ͨ���֣�������Ϊ������6% ����д 6��")


if __name__ == "__main__":
    main()
