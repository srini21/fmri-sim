import os,sys,random
import numpy as np


min_age=7
max_age=21


def gen_ppl(num_ppl,num_samples,behav_ft):#generates num_ppl with sorted num_samples of ages between min_age and max_age; given the dimensions of the behavioral features (d), it generates the F matrix by sampling from the Std Normal Distribution
    for i in range(0,num_ppl):
        with open('person%i' %i, 'w') as a:
            with open('F%i' %i,'w') as f:
                age=sorted(random.sample(range(min_age,max_age+1),num_samples))
                print>>a,age
                F_person=np.random.randn(behav_ft, behav_ft)
                print>>f,F_person
            
def gen_b():
        

def usage():
    print "num_ppl num_samples behav_ft"
    sys.exit(2)


    

def main():
    if len(sys.argv)<3:
        usage()
    num_ppl=int(sys.argv[1])
    num_samples=int(sys.argv[2])
    behav_ft=int(sys.argv[3])
    gen_ppl(num_ppl, num_samples,behav_ft)
#TODO    gen_b(behav_ft,age)    

if __name__ == '__main__':
    main()
