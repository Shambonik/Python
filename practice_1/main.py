import math


# def e_form(num):
#     return format(num, '.2e')


def f11(x):
    res = (48*x - math.tan(x)+18)**7 - x**4 + ((6*x**7+28*x**8)/(46*x**6+x**2-28))**(1/2) - (math.exp(x)+2*x**8+24)
    return res
    #print('f('+str(x)+') = ' + e_form(res))


def f12(x):
    res = 0
    if(x<112):
        res = 15*x**3 - x**2
    elif(x<156):
        res = (76*x**6+math.exp(x))/55 + 60*x**7
    else:
        res = 38*x**4
    return res
    #print('f(' + str(x) + ') = ' + e_form(res))


def f13(n, m):
    result = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            result+=45*(i+83*j**6-74)
        result+=i**7-math.cos(i)
    return result
    #print('f(' + str(n) + ',' + str(m) + ') = ' + e_form(result))

def f14(n):
    if(n == 0):
        return 6
    return math.tan(f14(n-1))+(1/34)*(f14(n-1)**2)


# def f(n):
#     if(n == 0):
#         return 6
#     return math.tan(f(n-1))+(1/34)*(f(n-1)**2)
#
#
# def f14(n):
#     print('f(' + str(n) + ') = ' + e_form(f(n)))
