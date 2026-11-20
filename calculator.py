# 简易计算器 v2.0 支持加减乘除
a = float(input("请输入第一个数字："))
op = input("输入运算符(+ - * /)：")
b = float(input("请输入第二个数字："))
if op == "+":
    res = a + b
elif op == "-":
    res = a - b
elif op == "*":
    res = a * b
elif op == "/":
    if b == 0:
        res = "错误：除数不能为0！"
    else:
        res = a / b
else:
    res = "运算符输入错误，仅支持 + - * /"
print("计算结果：", res)
