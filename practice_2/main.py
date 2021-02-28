
def f21(x):
    if(x[2] == 2000):
        if(x[3] == 'mako'):
            if(x[0] == 2016):
                return 0
            return 1
        elif(x[3] == 'boo'):
            if(x[1] == 'r'):
                return 3
            return 4
        return 2
    elif(x[2] == 1961):
        if(x[1]=='r'):
            if(x[0] == 2016):
                return 5
            return 6
        else:
            if(x[0] == 2016):
                return 7
            return 8
    return 9

def f22(n):
    c = (n&0x3fe00)>>9
    b = (n&0x1f8)<<6
    a = (n&0x7)<<15
    fed = n&0xfffc0000
    return fed|a|b|c

def f23(inp):
    s = set()
    length = 0
    outp = [[], [], []]
    for str in inp:
        s.add(str[0])
        s.add(str[1])
        if(len(s)!= length):
            length = len(s)
            list = str[0].split(':')
            data = list[0].split('/')
            name = str[1].split(' ')
            outp[0].append(list[1].split('@')[1])
            outp[1].append(name[2]+' '+name[0])
            outp[2].append(data[2]+'-'+data[1]+'-'+data[0])
    return outp

