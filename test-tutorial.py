from dask.distributed import Client, progress

# check all good with dask
client = Client(n_workers=4, processes = False)

from dask import delayed

from time import sleep

# define some auxiliary functions - we simulate computational time with the 'sleep' function
def inc(x):
    sleep(1)
    return x + 1

def add(x, y):
    sleep(1)
    return x + y
	
del_x = delayed(inc)(1)
del_y = delayed(inc)(2)
del_z = delayed(add)(del_x, del_y)

# check whether we can plot the graph
del_z.visualize()

_ = del_z.compute()

# check all good with files
data_folder = 'data/'
scores_file_names = data_folder + 'score_group1.txt'

with open(scores_file_name, 'r') as f:
	data = f.read()