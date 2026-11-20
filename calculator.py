# 简易计算器 v1.0 仅支持加减
a = float(input("请输入第一个数字："))
op = input("输入运算符(+/-)：")
b = float(input("请输入第二个数字："))
if op == "+":
    res = a + b
elif op == "-":
    res = a - b
else:
    res = "当前版本只支持加号、减号"
print("计算结果：", res)