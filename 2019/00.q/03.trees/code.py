from collections import deque
import sys


def dfs(n_set, req_list):
    #print('n_set {0}'.format(n_set))
    #print('req_list {0}'.format(req_list))
    for n in n_set:
        # skip when exist n,x,x
        #print('n {0}'.format(n))
        skip = False
        for req in req_list:
            if req[2] == n: continue
            if req[0] == n:
                skip = True
                break
            if req[1] == n:
                skip = True
                break
        if skip: continue
        
        remain_set = set([ i for i in n_set if i != n ])

        n_to_req_list_dict = {}
        for nn in n_set:
            n_to_req_list_dict[nn] = []
        for req in req_list:
            n_to_req_list_dict[req[0]].append(req)
            n_to_req_list_dict[req[1]].append(req)
            n_to_req_list_dict[req[2]].append(req)

        # group set

        child_set_list = []
        req_queue = deque()
        
        while(len(remain_set)>0):
            child_set = set()
            child_set_list.append(child_set)
            nn = min(remain_set)
            child_set.add(nn)
            remain_set.remove(nn)
            for req in n_to_req_list_dict[nn]:req_queue.append(req)
            while(len(req_queue)>0):
                #print('child_set {0}'.format(child_set))
                #print('remain_set {0}'.format(remain_set))
                req = req_queue.popleft()
                #print('req {0}'.format(req))
                if req[2] == n: continue
                for v in req:
                    if v not in remain_set: continue
                    child_set.add(v)
                    remain_set.remove(v)
                    for reqq in n_to_req_list_dict[v]:req_queue.append(reqq)

        # check seperate
        n_to_group_id = {}
        for i in range(len(child_set_list)):
            child_set = child_set_list[i]
            for child in child_set:
                n_to_group_id[child] = i
        #print('n_to_group_id {0}'.format(n_to_group_id))
        
        for req in req_list:
            if req[2] != n: continue
            if req[0] == n: continue
            if req[1] == n: continue
            g0 = n_to_group_id[req[0]]
            g1 = n_to_group_id[req[1]]
            if g0 != g1: continue
            skip = True
            break
            
        if skip: continue
        
        # create req_list_list
        
        req_list_list = [[] for _ in range(len(child_set_list))]
        for req in req_list:
            if n in req: continue
            g0 = n_to_group_id[req[0]]
            req_list_list[g0].append(req)
        
        child_list = []
        for i in range(len(child_set_list)):
            child_set0 = child_set_list[i]
            req_list0 = req_list_list[i]
            child_ret = dfs(child_set0, req_list0)
            if child_ret is None: return None
            child_list.append(child_ret)
        
        return {'v':n,'cl':child_list}
    
    return None

def to_ary(root,N):
    ret = [0]*N
    tto_ary(ret, root)
    return ret

def tto_ary(ary, root):
    if root is None:return
    v = root['v']
    for c in root['cl']:
        assert(ary[c['v']]==0)
        ary[c['v']]=v+1
        tto_ary(ary, c)

def check(root, N, req_list):
    if root is None: return
    ary = to_ary(root,N)
    assert(len(ary)==N)
    zero_cnt = 0
    for v in ary:
        if v != 0: continue
        zero_cnt += 1
    assert(zero_cnt==1)
    for req in req_list:
        assert(check_req_dfs(root, req))

def check_req_dfs(root, req):
    if root is None:
        return False
    v = root['v']
    cl = root['cl']
    if v == req[2]:
        g0 = None
        if v != req[0]:
            for i in range(len(cl)):
                c = cl[i]
                if not exist_dfs(c,req[0]): continue
                g0 = i
            assert(g0 is not None)
        g1 = None
        if v != req[1]:
            for i in range(len(cl)):
                c = cl[i]
                if not exist_dfs(c,req[1]): continue
                g1 = i
            assert(g1 is not None)
        assert(g0!=g1)
        return True
    for c in cl:
        if check_req_dfs(c, req): return True
    return False

def exist_dfs(root,vv):
    if root is None: return False
    v = root['v']
    cl = root['cl']
    if v == vv: return True
    for c in cl:
        if exist_dfs(c,vv): return True
    return False

case_count = int(sys.stdin.readline().strip())

for case_idx in range(case_count):
    
    line_split = sys.stdin.readline().strip().split(' ')
    N = int(line_split[0])
    M = int(line_split[1])
    
    req_list = []
    for _ in range(M):
        line_split = sys.stdin.readline().strip().split(' ')
        req = tuple(int(i)-1 for i in line_split)
        req_list.append(req)
    
    n_set = set(range(N))
    ret = dfs(n_set, req_list)

    check(ret, N, req_list)
    
    if ret is None:
        print('Case #{0}: Impossible'.format(case_idx+1))
    else:
        ret_ary = to_ary(ret,N)
        ret_str = ' '.join(map(str,ret_ary))
        print('Case #{0}: {1}'.format(case_idx+1,ret_str))
