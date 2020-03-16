# 
# Multiprocessing in Python: An example
# 

from time import sleep, time
from multiprocessing import Pool

def wait(t):
    from datetime import datetime
    from time import sleep
    
    t_start = datetime.now()
    sleep(t)
    t_end = datetime.now()
    print('Time for execution: {} sec.'.format(
            str((t_end-t_start).total_seconds())))

# Without Parallelization:
# -------------------------

wait(3)
# >> Time for execution: 3.003093 sec.

# With Parallelization:
# -------------------------

T_START = time()
with Pool(10) as p:
    print(p.map(wait, [3]*10))
T_END = time()
print('Total time for execution: {} sec.'.format(
        str(T_END-T_START)))
# Time for execution: 3.000477 sec.
# Time for execution: 3.000673 sec.
# Time for execution: 3.003045 sec.
# Time for execution: 3.002303 sec.
# Time for execution: 3.002679 sec.
# Time for execution: 3.00307 sec.
# Time for execution: 3.003296 sec.
# Time for execution: 3.003047 sec.
# Time for execution: 3.00304 sec.
# Time for execution: 3.002988 sec.
# [None, None, None, None, None, None, None, None, None, None]
# Total time for execution: 3.1463358402252197 sec.
