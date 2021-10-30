from math import *
# ポアソン分布
def expectPoisson(lamb, k):
    return exp(-lamb) * (lamb ** k) / factorial(k)

def calcLambda(n,p):
    # 期待値
    return n*p

if __name__ == '__main__':
    lamb = calcLambda(40,0.05)
    ans = 0
    for i in range(3):
        ans += expectPoisson(lamb,i)
        print(expectPoisson(lamb,i))
    print(1-ans)
