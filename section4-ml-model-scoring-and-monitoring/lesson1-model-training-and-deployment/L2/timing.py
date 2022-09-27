import os
import timeit
import numpy as np

def ingestion_timing():
    starttime = timeit.default_timer()
    os.system('python3 ingestion.py')
    timing=timeit.default_timer() - starttime
    return timing

def training_timing():
    starttime = timeit.default_timer()
    os.system('python3 training.py')
    timing=timeit.default_timer() - starttime
    return timing


def measure_and_save_timings():
    ingestion_timings=[]
    training_timings=[]
    
    for idx in range(20):
        ingestion_timings.append(ingestion_timing())
        training_timings.append(training_timing())
    
    final_output=[]
    final_output.append(np.mean(ingestion_timings))
    final_output.append(np.std(ingestion_timings))
    final_output.append(np.min(ingestion_timings))
    final_output.append(np.max(ingestion_timings))
    final_output.append(np.mean(training_timings))
    final_output.append(np.std(training_timings))
    final_output.append(np.min(training_timings))
    final_output.append(np.max(training_timings))
    
    return final_output
    

    
print(measure_and_save_timings())