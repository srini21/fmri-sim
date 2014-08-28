fmri-sim
========

Generating a model with simulated fmri and dti data coupled with behavioral features and age , to be used for predicting disease symptoms in the brain.

The Samples are generated in a new directory called 'Samples_fMRI'

TODO :
Generate DTI Samples


Writeup
=======
Refer to fmri.pdf in writeup/fmri.pdf


Code
=========

******************************************************************
WARNING! Remember to cleanup before generating data to avoid mess.
******************************************************************
CLEANUP (only if you have generated the data before)
=======

Cleans up all the generated data. 

USAGE sh cleanup.sh
------------------------------------------------------------------


main_script.py 
--------------
USAGE: python main_script.py num_ppl num_samples noise_strength num_nodes topology sub_nodes behav_ft num_scans phenotypes

num_ppl	      :		      No. of persons for whom the data has to be simulated.
num_samples   :		      No. of samples of age for every person between the range 7 and 21.
behav_ft      :		      No. of behavioral features for every person. 
noise_strength:		      Amount of normal noise required to add to the behavioral data time series (use 1)
num_nodes     :		      No. of nodes in the brain under question.
topology      :		      star/ substar (use substar)
sub_node      :		      Size of sub cluster
num_scans     :		      No. of scans for every age.
phenotypes    :		      No. of observed variables.

generate_abF.py 
---------------

Generates the age, b0, F for the number of individuals as reqd. 

 
USAGE:	python generate_abF.py num_ppl num_samples behav_ft 


Current usage: num_ppl =10, num_samples=4, behav_ft=30 

generate_b.py
--------------

Generates a time series of b based on age and F for every person for the age that has been sampled. 

USAGE:	python generate_b.py num_ppl behav_ft noise_strength


generate_graph.py
-----------------

Generates an adjacency matrix 'adj_mat', nodes and edges in the local directory. 

USAGE: python generate_graph.py num_nodes topology substar_count ( if single star, 300 star 0 else 300 substar 5)

generate_W.py
-------------

Generates Wd and Wf in the local directory.

USAGE: python generate_W.py num_nodes behav_ft

generate_samples.py
-------------------

generates fMRI and DTI samples


USAGE: python generate_samples.py num_ppl num_nodes num_scans

generate_Z.py
-------------

generates Z= Thetaf*alpha where alpha is the predictive weight for all theta(a,b)

USAGE: python generate_Z


*************************
Proximal Gradient Descent
*************************

Sincere thanks to Eunho Yang and spams toolkit. 
Computes the weight from the input data using proximal_flat in spams. 

Dependency : Python Sparse Modeling Toolkit - SPAMS

present in directory pgd. 

USAGE : python pgd/pgd.py (from the curr dir)

generate_Z_est.py
-----------------
same as generate_Z but generates estimated Zs using the recomputed weight. 

w_results.py
------------
USAGE : python w_results.py

performs an analysis of the computed weights. 