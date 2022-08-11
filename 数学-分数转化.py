import fractions # 分数运算模块

for s in ['0.5', '1.55553333333333333', '2.4324323425454353', '5e-1']:
    f = fractions.Fraction(s)
    print('{0:>4} = {1}'.format(s, f))