#!/usr/bin/env python
# coding: utf-8

###
# Tutorial code modified from SDS 262 (https://sparc.science/datasets/262?type=dataset)
# modified to run from relative path to data, and to save output data 
###

# Install pyeCAP in your python environment prior to using this juypter notebook.
# It is available through pyPI with the command 'pip install pyeCAP: https://pypi.org/project/pyeCAP/
# Or through GitHub: https://github.com/ludwig-lab/pyeCAP (includes tutorial on setting up)


import pyeCAP as pyCAP
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import os

directory = r'../dataset/files/primary/sub-1/perf-sub-1-vagus-ecap/' #insert location of folder

data = pyCAP.Ephys(directory, stores=['maco','mico']) #importing ephys data from TDT files
data = data.remove_ch((6,7,11)) #removing unused recording channels
stim_data = pyCAP.Stim(directory)
ecap_unfilt = pyCAP.ECAP(data,stim_data)
stim_data.parameters

print(data.ch_names)
real_ch_names = ['Cuff 1', 'Cuff 2', 'Cuff 3', 'LIFE 1', 'LIFE 2', 'LIFE 3', 'Micro 1', 'Micro 2', 'Micro 3'] #for vagus

#Filtering for ecap (high pass and low pass) and naturally occuring activity (additional mains filter)
data_low = data.filter_iir(Wn = 100, btype='highpass')   #100 default
data_spikes = data_low.filter_powerline(frequencies=[60])   #Default for spikes is 60 Hz, no mains filter for ECAP
data_spikes_all = data_spikes.filter_gaussian(5000, btype='lowpass', order=0, truncate=4.0)    #5000 default
data_ecap_all = data_low.filter_gaussian(5000, btype='lowpass', order=0, truncate=4.0)    #5000 default

ecap_filt = pyCAP.ECAP(data_ecap_all,stim_data)


# ## Plotting individual channels for ECAP


sel = 14   # select form parameter tables above which train to plot
param = (0,sel)

fig, ax = plt.subplots(figsize=(15,5))
for i in [0,2,4]: #add desired channels to plot here
    plt.plot(ecap_filt.time(param)*1e3, ecap_filt.median(param)[i,:]*1e6, label = str(real_ch_names[i]))

plt.xlabel('Time (ms)')
plt.ylabel('Voltage (\u03BCV)')
plt.xlim([1,9]) #1-9 for Abeta, 1-19 for B
plt.ylim([-150,150]) #150 for Abeta, 20 for B
plt.legend(loc='upper right',fontsize=18)
plt.xlabel('Time (ms)', fontsize = 20)
plt.ylabel('Voltage (uV)', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.show()

# ## Saving the filtered data
time_processed = ecap_filt.time(param)*1e3
value_processed = ecap_filt.median(param)[i,:]*1e6
pd.DataFrame({'Time': time_processed, 'Values': value_processed}).to_csv(r'../dataset/outputs/Processed.csv')





