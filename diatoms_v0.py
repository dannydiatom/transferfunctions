import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

def get_data(filename):
# get some data from a csv file
# make sure column headings are commented out with a #

    dataset = pd.read_csv(filename)

    return dataset

# ##########################################

species = get_data('c:\\Users\\bsherrod\\python\\diatoms\\data\\species_data.csv')
env = get_data('c:\\Users\\bsherrod\\python\\diatoms\\data\\diatom_env.csv')

print (list(species))
plt.scatter(env.SWLI, species.LUTMUT)
plt.show()
