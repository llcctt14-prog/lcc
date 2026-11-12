# ��һ�죺�����е��Լ��޸�

����ֻ��� 5 ������Լ 40�C50 ���ӡ��𲽴����Ѿ��ṩ���ص����ܽ��ͺ��޸ĺ��ļ��㡣

## 1. ����Ŀ�����У�5�C10 ���ӣ�

1. �� VS Code ѡ���ļ� �� ���ļ��С����򿪱���Ŀ `lcc` �ļ��С����Ӧ�ܿ��� `main.py` �� `calculator.py`��
2. ѡ���ն� �� �½��նˡ���ȷ���ն˵�ǰĿ¼�� `lcc`��������������һ����
3. ���� `python --version`�����δ������ Python 3.13.9 ���ã����� Anaconda�������ظ���װ��
4. ���� `python main.py`��
5. �������� `10000`��`6`��`1`��`500`��ÿ�ΰ��س�����ĩ���ӦΪ `16,784.56`��

����Ժ󻻵��ԣ��ɴ� GitHub �ֿ�ҳ��ѡ�� Code �� Download ZIP����ѹ��򿪰��� `main.py` ���ļ��У��Ѿ����� Git �ĵ���Ҳ��ʹ�ã�

```powershell
git clone https://github.com/llcctt14-prog/lcc.git
cd lcc
python main.py
```

�� VS Code �����а�ťѡ�� Python���� `Ctrl+Shift+P`������ `Python: Select Interpreter`��ѡ����õ� Python����û�д��������ʹ���ն����У����װ Microsoft ������ Python ��չ��

## 2. ��������Ҫ�� 4 �У�10 ���ӣ�

```python
monthly_rate = annual_rate / 12
balance = principal
for month in range(years * 12):
    balance = balance * (1 + monthly_rate) + monthly_contribution
```

`principal` �ǳ�ʼ����`balance` ��ÿ���¸��º����`range(12)` ��ѭ��ִ�� 12 �Ρ�`month` ��ѭ�������ı�ǣ���ʱ��������㡣

���㱾�� 1000 Ԫ������������ 12%��ÿ�µ�Ͷ�� 100 Ԫ��

- �����ʣ�`0.12 / 12 = 0.01`��
- ��һ���µף�`1000 �� 1.01 + 100 = 1110`��
- �ڶ����µף�`1110 �� 1.01 + 100 = 1221.10`��

ע�⣺ÿ��Ͷ��� 100 Ԫ���µײŽ����˻�����˱��²�������Ϣ��

## 3. �Լ���д������10�C15 ���ӣ�

����Ŀ���½� `practice.py`���Լ��������»����棬��Ҫ���ճ������鲿�֣�

```python
def calculate(principal, annual_rate, years, monthly_contribution):
    monthly_rate = annual_rate / 12
    balance = principal
    for month in range(years * 12):
        balance = balance * (1 + monthly_rate) + monthly_contribution
    return balance


result = calculate(10000, 0.06, 1, 500)
print(round(result, 2))
```

���� `python practice.py`��Ӧ���� `16784.56`��

���� `return balance` ��ѭ��������ִ�У������ս��� `result`�����ɾ�� return������Ĭ�Ϸ��� None������� return ������ѭ�����棬�����ֻ�����һ���¡�

## 4. �˶Բ���һ���޸ģ�10 ���ӣ�

�ֱ����� `python main.py`������±�����������ʱ���Ӱٷֺš�

| ���� | ���������� | ���� | ÿ�¶�Ͷ | ��ĩ��� | ���� |
| --- | --- | --- | --- | --- | --- |
| 10000 | 0 | 1 | 500 | 16000.00 | 0.00 |
| 10000 | 6 | 1 | 0 | 10616.78 | 616.78 |
| 10000 | 6 | 1 | 500 | 16784.56 | 784.56 |

������ `python -m unittest -v`��Ӧ���� 8 �����ͨ�������첻Ҫ���Լ�д�������ļ���

�����޸� `main.py`����������������������жϣ�ע�������������һ������ try �ڲ���

```python
if profit > 0:
    print("����ģ����������")
elif profit < 0:
    print("����ģ��Ϊ������")
else:
    print("����ģ������Ϊ��")
```

�������� `6`��`-6`��`0` ������һ�Σ���֤������֧��

## 5. �����Լ���ѧϰ��¼��5 ���ӣ�

�ȱ����ļ����ٲ鿴�Ķ���

```powershell
git status
git diff
```

ȷ�ϸĶ�ֻ���Լ����޸ĵ��ļ���Ȼ���ύ��

```powershell
git add main.py practice.py
git commit -m "Practice compound interest and profit conditions"
```

commit �Ѱ汾��¼�����أ�push ���ϴ��� GitHub���� Git ��ʾδ�������ݣ�����ϣ����ʾ���ύ��¼������ֺ� GitHub ��˽�������ñ��ֿ�� `user.name`��`user.email`�������ԣ����ظ�ȫ�����á��������¼����ʱ���� `git push origin main`��

## �������ɱ�׼

- [ ] ������ main.py ���õ�ʾ�������
- [ ] �ܽ��ͱ������ʡ������Ͷ�Ͷ�ĸ�������
- [ ] ������ǰ�����£��������ȼ�Ϣ��Ͷ�롣
- [ ] �ܽ��� return Ϊʲô����ѭ�����档
- [ ] �Լ�д�� practice.py������֤���������жϷ�֧��
- [ ] ���ر���һ���Լ��� Git �ύ��

��һ����ѧϰ�б�����������ÿһ�����
