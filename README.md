fmri-sim
========

Generating a model with simulated fmri and dti data coupled with behavioral features and age , to be used for predicting disease symptoms in the brain.

Code
=========
generate_abF.py 
---------------

Generates the age, b0, F for the number of individuals as reqd. 

 
USAGE:	python generate_abF.py num_ppl num_samples behav_ft 

num_ppl	      :		      No. of persons for whom the data has to be simulated.
num_samples   :		      No. of samples of age for every person between the range 7 and 21.
behav_ft      :		      No. of behavioral features for every person. 

Current usage: num_ppl =10, num_samples=4, behav_ft=30 

generate_b.py
--------------

Generates a time series of b based on age and F for every person for the age that has been sampled. 

USAGE:	python generate_b.py num_ppl behav_ft noise_strength

noise_strength :	     The amount of noise that has to be added for every iteration in the time series.