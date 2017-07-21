#!/usr/bin/env python
# Using your own module

# A) Creating your module: Good news! We are already done with this, it is our code in problem 2!

# B) Import the function plot_quasars from your module
from Problem2_MoreFunctions import Plot_Quasars
# C) Using your module: go ahead an use plot_quasars here.
Plot_Quasars('*', 2, 'dotted', 'pink')
# NOTE: if your module wasn't in the same directory as the directory from which you run the python interpreter, you will have to make sure the directory it is in is on the PYTHONPATH
