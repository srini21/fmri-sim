#author : Srinivasan Sivaramachandran
import os,sys,numpy as np

#get the number of ages for the given person
def num_age(curr_dir):
    with open(curr_dir+'/age') as a:
        age_list=np.load(a)
        return age_list

#generates bs as time-series from the b0 and the ages for the given person. Noise added as given using the input argument


def gen_bs(num_ppl,behav_ft,noise_strength):
    print "------------------------"
    print "generating b Time series"
    print "------------------------"
    for i in range(0,num_ppl):
        dir='person'+str(i)
        with open(dir+'/b0') as b0:
            with open(dir+'/F') as F_mat:
                F=np.load(F_mat)
                b_prev=np.load(b0)
                num=num_age(dir)
                for j in range(1,behav_ft):
                    b_curr=np.dot(F,b_prev)+np.random.normal(0,noise_strength)
                    if j in num:
                        temp=b_curr
                        temp=np.append(temp,j)
                        temp=np.append(temp,1)
                        np.save(dir+'/b'+str(j),temp)
                    b_prev=b_curr
    print "Done"


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

