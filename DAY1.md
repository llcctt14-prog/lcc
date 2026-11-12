# 第一天：从运行到自己修改

今天只完成 5 个任务，约 40–50 分钟。起步代码已经提供；重点是能解释和修改核心计算。

## 1. 打开项目并运行（5–10 分钟）

1. 在 VS Code 选择“文件 → 打开文件夹”，打开本项目 `lcc` 文件夹。左侧应能看到 `main.py` 和 `calculator.py`。
2. 选择“终端 → 新建终端”。确认终端当前目录是 `lcc`，而不是它的上一级。
3. 输入 `python --version`。本次搭建环境中 Python 3.13.9 可用，来自 Anaconda，无需重复安装。
4. 输入 `python main.py`。
5. 依次输入 `10000`、`6`、`1`、`500`，每次按回车。期末金额应为 `16,784.56`。

如果以后换电脑，可从 GitHub 仓库页面选择 Code → Download ZIP，解压后打开包含 `main.py` 的文件夹；已经配置 Git 的电脑也可使用：

```powershell
git clone https://github.com/llcctt14-prog/lcc.git
cd lcc
python main.py
```

若 VS Code 的运行按钮选错 Python，按 `Ctrl+Shift+P`，搜索 `Python: Select Interpreter`，选择可用的 Python。若没有此命令，可先使用终端运行，随后安装 Microsoft 发布的 Python 扩展。

## 2. 理解最重要的 4 行（10 分钟）

```python
monthly_rate = annual_rate / 12
balance = principal
for month in range(years * 12):
    balance = balance * (1 + monthly_rate) + monthly_contribution
```

`principal` 是初始本金，`balance` 是每个月更新后的余额。`range(12)` 让循环执行 12 次。`month` 是循环次数的标记，暂时不参与计算。

手算本金 1000 元、名义年利率 12%、每月底投入 100 元：

- 月利率：`0.12 / 12 = 0.01`。
- 第一个月底：`1000 × 1.01 + 100 = 1110`。
- 第二个月底：`1110 × 1.01 + 100 = 1221.10`。

注意：每月投入的 100 元在月底才进入账户，因此本月不产生利息。

## 3. 自己手写函数（10–15 分钟）

在项目中新建 `practice.py`，自己输入以下基础版，不要先照抄输入检查部分：

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

运行 `python practice.py`，应看到 `16784.56`。

这里 `return balance` 在循环结束后执行，把最终金额交给 `result`。如果删掉 return，函数默认返回 None；如果把 return 缩进到循环里面，程序就只计算第一个月。

## 4. 核对并做一次修改（10 分钟）

分别运行 `python main.py`，检查下表。输入利率时不加百分号。

| 本金 | 年利率输入 | 年数 | 每月定投 | 期末金额 | 收益 |
| --- | --- | --- | --- | --- | --- |
| 10000 | 0 | 1 | 500 | 16000.00 | 0.00 |
| 10000 | 6 | 1 | 0 | 10616.78 | 616.78 |
| 10000 | 6 | 1 | 500 | 16784.56 | 784.56 |

再运行 `python -m unittest -v`，应看到 8 项测试通过。今天不要求自己写懂测试文件。

动手修改 `main.py`：在输出收益后增加下面的判断，注意它和其他输出一样处于 try 内部：

```python
if profit > 0:
    print("本次模拟有正收益")
elif profit < 0:
    print("本次模拟为负收益")
else:
    print("本次模拟收益为零")
```

用年利率 `6`、`-6`、`0` 各运行一次，验证三个分支。

## 5. 保存自己的学习记录（5 分钟）

先保存文件，再查看改动。本次准备的本地项目已关联 GitHub；如果你以后使用 Download ZIP 下载，ZIP 不含 Git 历史，需要先用 git clone 获取仓库，再把自己的修改复制过去，才能执行下面的提交步骤。

```powershell
git status
git diff
```

确认改动只有自己刚修改的文件，然后提交：

```powershell
git add main.py practice.py
git commit -m "Practice compound interest and profit conditions"
```

commit 把版本记录到本地，push 才上传到 GitHub。若 Git 提示未配置身份，用你希望显示在提交记录里的名字和 GitHub 隐私邮箱设置本仓库的 `user.name`、`user.email`，再重试；不必改全局配置。网络与登录可用时运行 `git push origin main`。

## 今天的完成标准

- [ ] 能运行 main.py 并得到示例结果。
- [ ] 能解释本金、利率、年数和定投四个参数。
- [ ] 能手算前两个月，并解释先计息后投入。
- [ ] 能解释 return 为什么放在循环外面。
- [ ] 自己写过 practice.py，并验证三个收益判断分支。
- [ ] 本地保存一次自己的 Git 提交。

下一次再学习列表，用它保存每一年的余额。
