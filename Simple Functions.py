def add(var1, var2):
    return var1+var2


def sub(var1, var2):
    return var1-var2


def mul(var1, var2):
    return var1*var2


def div(var1, var2):
    return var1/var2


def rem(var1, var2):
    return var1 % var2


def pwr(var1, var2):
    return pow(var1, var2)


a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
print('sum of A and B is ', add(a, b))
print('sub of A and B is ', sub(a, b))
print('mul of A and B is ', mul(a, b))
print('div of A and B is ', div(a, b))
print('rem of A and B is ', rem(a, b))
print('pwr of A and B is ', pwr(a, b))
print('I would like to add few more functions')
