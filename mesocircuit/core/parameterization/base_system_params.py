"""PyNEST Mesocircuit: System Parameters
----------------------------------------

A dictionary with parameters defining machine configurations.

"""

import multiprocessing as mp


# parameters have to be specified for each machine type individually
sys_dict = {
    # high-performance computing system using the SLURM workload manager
    'hpc': {
        # network simulation
        'network': {
            # partition, on JURECA DC the default is 'dc-cpu'
            'partition': 'dc-cpu',
            # number of compute nodes
            'num_nodes': 4,
            # number of MPI processes per node
            'num_mpi_per_node': 8,
            # number of threads per MPI process
            'local_num_threads': 16,
            # wall clock time
            'wall_clock_time': '00:30:00'},
        # analysis, plotting and analysis_and_plotting all use the same
        # configuration
        'analysis_and_plotting': {
            'partition': 'dc-cpu',
            'num_nodes': 1,
            'num_mpi_per_node': 12,
            'local_num_threads': 1,
            'wall_clock_time': '00:30:00'
        }
    },
    # laptop
    'local': {
        # per default, use as many threads as available (logical cores) for
        # network simulation and as many MPI process as possible for
        # analysis and plotting
        'network': {
            # number of MPI processes
            'num_mpi': 1,
            # number of threads per MPI process
            # if 'auto', the number of threads is set such that the total
            # number of virtual processes equals the number of logical
            # cores
            'local_num_threads': 'auto'},
        'analysis_and_plotting': {
            # '$(nproc)' gives the number of available logical cores
            'num_mpi': mp.cpu_count() // 2  # disable multithreading
        }
    }
}