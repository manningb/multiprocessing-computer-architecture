iters       = 100
mem_num     = 1000
pro_num     = 20000
max_procs   = 10

line_width  = 2.0
legend_size = 10
fig_name    = 'timing.pdf'
def UseMemory(num):
    test1 = np.zeros([num,num])
    test2 = np.arange(num*num)
    test3 = np.array(test2).reshape([num, num])
    test4 = np.empty(num, dtype=object)
    return 

def UseProcessor(num):
    test1 = np.arange(num)
    test1 = np.cos(test1)
    test1 = np.sqrt(np.fabs(test1))
    test2 = np.zeros(num)
    for i in range(num): test2[i] = test1[i]
    return np.std(test2)

def MemJob(its): 
    for ii in range(its): UseMemory(1000)

def ProJob(its): 
    pro_num = 20000
    for ii in range(iters): UseProcessor(pro_num)
