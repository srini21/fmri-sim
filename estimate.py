import os,sys,numpy as np
import generate_samples_est
import generate_Z_est
import concatenate_est_samples
def usage():
    print "num_ppl num_nodes num_scans phenotypes"
    sys.exit(2)

def main():
    if len(sys.argv)<2:
        usage()
    num_ppl=int(sys.argv[1])
    num_nodes=int(sys.argv[2])
    num_scans=int(sys.argv[3])
    phenotypes=int(sys.argv[4])
    generate_samples_est.generate_samplesfmri(num_ppl, num_nodes, num_scans)
    generate_samples_est.generate_samplesdti(num_ppl, num_nodes, num_scans)
    generate_Z_est.getThetaAlpha(phenotypes,num_scans)
    concatenate_est_samples.concat('fMRI')
    concatenate_est_samples.concat('dti')
    
    
    
if __name__ == '__main__':
    main()
