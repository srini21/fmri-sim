import os,sys,random,itertools
import numpy as np


min_age=7
max_age=21

#generates num_ppl with sorted num_samples of ages between min_age and max_age; given the dimensions of the behavioral features (d), it generates the F matrix by sampling from the Std Normal Distribution
def gen_ppl(num_ppl,num_samples,behav_ft):
    for i in range(0,num_ppl):
        os.mkdir(os.path.join(os.getcwd(),'person'+str(i)))
    for i in range(0,num_ppl):
        with open('person'+str(i)+'/age', 'w') as a:
            with open('person'+str(i)+'/F','w') as f:
                with open('person'+str(i)+'/b0','w') as b0:
                    age=sorted(random.sample(range(min_age,max_age+1),num_samples))
                    np.savetxt(a,age,delimiter=',')
                    F_person=np.random.randn(behav_ft, behav_ft)
                    np.savetxt(f,F_person,delimiter=',')
                    b_init=np.random.randn(behav_ft,1)
                    np.savetxt(b0,b_init,delimiter=',')


def usage():
    print "num_ppl num_samples behav_ft"
    sys.exit(2)


    

def main():
    if len(sys.argv)<2:
        usage()
    num_ppl=int(sys.argv[1])
    num_samples=int(sys.argv[2])
    behav_ft=int(sys.argv[3])
    gen_ppl(num_ppl, num_samples,behav_ft)
#TODO    gen_b(behav_ft,age)    

if __name__ == '__main__':
    main()
