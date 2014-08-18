#author : Srinivasan Sivaramachandran
import os,sys
import generate_graph
import generate_W
import generate_abF
import generate_b
import generate_samples
import generate_Z
import concatenate_samples

def usage():
    print "num_ppl num_samples noise_strength num_nodes topology sub_nodes behav_ft num_scans phenotypes"
    sys.exit(2)

def main():
    if len(sys.argv)<2:
        usage()
    
    num_ppl=int(sys.argv[1])
    num_samples=int(sys.argv[2])
    noise_strength=int(sys.argv[3])
    num_nodes=int(sys.argv[4])
    topology=sys.argv[5]
    sub_nodes=int(sys.argv[6])
    behav_ft=int(sys.argv[7])
    num_scans=int(sys.argv[8])
    phenotypes=int(sys.argv[9])
    generate_graph.generate_graph(num_nodes, topology, sub_nodes)
    generate_abF.gen_ppl(num_ppl, num_samples, behav_ft)
    generate_b.gen_bs(num_ppl, behav_ft, noise_strength)
    generate_W.generate_w(num_nodes, behav_ft)
    generate_samples.generate_samplesfmri(num_ppl, num_nodes, num_scans)
    generate_samples.generate_samplesdti(num_ppl, num_nodes, num_scans)
    generate_Z.getThetaAlpha(phenotypes)
    concatenate_samples.concat('fMRI')
    concatenate_samples.concat('dti')
    concatenate_samples.concat_b(num_ppl,num_scans)
    
if __name__ == '__main__':
    main()
