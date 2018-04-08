from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()
if rank == 0:
   data = [x+1 for x in range(size)]
   print 'we will be scattering:',data
else:
   data = None

data = comm.scatter(data, root=1)

print name,' rank',rank,'has data:',data,'trnf',data**rank

newData = comm.gather(data,root=1)

if rank == 0:
   print 'master:',newData


