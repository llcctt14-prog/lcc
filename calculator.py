"""�����붨Ͷ���㣺���������� / 12��ÿ�µ�Ͷ�롣"""

from math import isfinite


def future_value(principal, annual_rate, years, monthly_contribution=0):
    """������ĩ��annual_rate ��С�������� 0.06 ��ʾ 6%��"""
    if not all(isfinite(x) for x in (principal, annual_rate, monthly_contribution)):
        raise ValueError("�������ʺͶ�Ͷ���������������֡�")
    if principal < 0 or monthly_contribution < 0:
        raise ValueError("�����ÿ�¶�Ͷ����Ϊ������")
    if annual_rate <= -1:
        raise ValueError("����ϰҪ�����������ʴ��� -100%��")
    if not isinstance(years, int) or years < 0:
        raise ValueError("���������ǷǸ�������")

    monthly_rate = annual_rate / 12
    months = years * 12
    balance = principal

    for month in range(months):
        # �ȼ��㱾����Ϣ���ټ����µ�Ͷ��Ľ�
        balance = balance * (1 + monthly_rate) + monthly_contribution
        if not isfinite(balance):
            raise ValueError("�����������뽵�ͽ����ʻ�������")

    return balance
