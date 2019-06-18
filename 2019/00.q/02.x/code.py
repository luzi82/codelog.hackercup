import sys

NNOT={
    '0':'1',
    '1':'0',
    'X':'x',
    'x':'X',
}

def cal(v):
    if v[2] == '|':
        if (v[1] == v[3]): return v[1]
        elif (v[1] == '1') or (v[3] == '1'): return '1'
        elif (v[1] == '0'): return v[3]
        elif (v[3] == '0'): return v[1]
        else: return '1'
    elif v[2] == '&':
        if (v[1] == v[3]): return v[1]
        elif (v[1] == '0') or (v[3] == '0'): return '0'
        elif (v[1] == '1'): return v[3]
        elif (v[3] == '1'): return v[1]
        else: return '0'
    elif v[2] == '^':
        if (v[1] == v[3]): return '0'
        elif (v[1] == '0'): return v[3]
        elif (v[3] == '0'): return v[1]
        elif (v[1] == '1'): return NNOT[v[3]]
        elif (v[3] == '1'): return NNOT[v[1]]
        else: return '1'

def check_cal(v,e):
    assert(cal([3,v[0],v[1],v[2]])==e)

check_cal('0|0','0')
check_cal('0|1','1')
check_cal('0|x','x')
check_cal('0|X','X')
check_cal('1|0','1')
check_cal('1|1','1')
check_cal('1|x','1')
check_cal('1|X','1')
check_cal('x|0','x')
check_cal('x|1','1')
check_cal('x|x','x')
check_cal('x|X','1')
check_cal('X|0','X')
check_cal('X|1','1')
check_cal('X|x','1')
check_cal('X|X','X')

check_cal('0&0','0')
check_cal('0&1','0')
check_cal('0&x','0')
check_cal('0&X','0')
check_cal('1&0','0')
check_cal('1&1','1')
check_cal('1&x','x')
check_cal('1&X','X')
check_cal('x&0','0')
check_cal('x&1','x')
check_cal('x&x','x')
check_cal('x&X','0')
check_cal('X&0','0')
check_cal('X&1','X')
check_cal('X&x','0')
check_cal('X&X','X')

check_cal('0^0','0')
check_cal('0^1','1')
check_cal('0^x','x')
check_cal('0^X','X')
check_cal('1^0','1')
check_cal('1^1','0')
check_cal('1^x','X')
check_cal('1^X','x')
check_cal('x^0','x')
check_cal('x^1','X')
check_cal('x^x','0')
check_cal('x^X','1')
check_cal('X^0','X')
check_cal('X^1','x')
check_cal('X^x','1')
check_cal('X^X','0')

case_count = int(sys.stdin.readline().strip())

ANS={
    '0':0,
    '1':0,
    'x':1,
    'X':1,
}

for case_idx in range(case_count):

    line = sys.stdin.readline().strip()
    
    q = [[1,None]]
    
    for c in line:
        if c == '(':
            q.append([1,None,None,None])
            continue
        if c == ')':
            v = q.pop()
            v = cal(v)
            vv = q[-1]
            vv[vv[0]] = v
            vv[0] += 1
            continue
        vv = q[-1]
        vv[vv[0]] = c
        vv[0] += 1

    ret = q[0][1]
    ret = ANS[ret]
    print('Case #{0}: {1}'.format(case_idx+1, ret))
    