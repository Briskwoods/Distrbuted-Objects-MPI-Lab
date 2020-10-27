from mpi4py import MPI
from TrapezoidalRule import f  

comm = MPI.COMM_WORLD
no_of_processes = comm.Get_size()
rank = comm.Get_rank()

x = 0.0  
y = 10.0  
n = 5  
h = (y - x) / n  
s = 0.0

total = 0  

if rank != 0:
    if rank == 1:
        s += f(x) 
        message = s
        comm.send(message, dest=0)
    elif rank == 2:
        for i in range(1, int(n)):
            s += 2 * f(x + i * h)  
        message = s
        comm.send(message, dest=0)
    elif rank == 3:
        s += f(y)  
        message = s * (h / 2.0)  
        comm.send(message, dest=0)

else:
    for procid in range(1, no_of_processes):
        message = comm.recv(source=procid)
        total += message
        print('Area from process', procid, ':', message)

if total > 0:
    print('Total area', ':', total, "square units")


"use 'mpiexec -np 4 python MPITrapezoidalRule.py' to run on Windows."