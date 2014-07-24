import os,sys,numpy as np
#TODO instead of getting the num_ppl try to find out from the directory


#get the number of ages for the given person
def num_age(curr_dir):
    with open(curr_dir+'/age') as a:
        age_list=np.loadtxt(a,delimiter=',')
        return age_list

#generates bs as time-series from the b0 and the ages for the given person. Noise added as given using the input argument


def gen_bs(num_ppl,behav_ft,noise_strength):
    for i in range(0,num_ppl):
        dir='person'+str(i)
        with open(dir+'/b0') as b0:
            with open(dir+'/F') as F_mat:
                F=np.loadtxt(F_mat,delimiter=',')
                b_prev=np.loadtxt(b0,delimiter=',')
                num=num_age(dir)
                for j in range(1,behav_ft):
                    b_curr=np.dot(F,b_prev)+np.random.normal(0,noise_strength,behav_ft)
                    if j in num:
                        np.savetxt(dir+'/b'+str(j),b_curr,delimiter=',')
                    b_prev=b_curr


def usage():
    print "num_ppl behav_ft noise_strength"
    sys.exit(2)


def main():
    if len(sys.argv)<2:
        usage()

    num_ppl=int(sys.argv[1])
    behav_ft=int(sys.argv[2])
    noise_strength=int(sys.argv[3])
    gen_bs(num_ppl,behav_ft,noise_strength)

if __name__ == '__main__':
    main()

