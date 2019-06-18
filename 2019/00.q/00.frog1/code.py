import sys

case_count = int(sys.stdin.readline().strip())

for case_idx in range(case_count):
    line = sys.stdin.readline().strip()
    line_len = len(line)
    b_count = 0
    for c in line:
        if c == 'B':
            b_count += 1
    mmin = b_count+2
    mmax = 2*b_count + 1

    #print('Case #{0}: {1} {2}'.format(case_idx+1, mmin, mmax))

    if (line_len >= mmin) and (line_len <= mmax):
        result = 'Y'
    else:
        result = 'N'
        
    print('Case #{0}: {1}'.format(case_idx+1, result))
