import networkx as nx,os,sys,math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


def usage():
    print "num_nodes topology substar_count. if single star, 300 star 0 else 300 substar 5"
    sys.exit(2)

def generate_graph(num_nodes, topology, substar_count):
    print "---------------------"
    print "generating the graph"
    print "---------------------"
    nodes=range(0,num_nodes)
    G=nx.Graph()
    G.add_nodes_from(nodes)
    
    if(topology=='star'):
        for node in range(0,num_nodes-1):
            G.add_edge(node,num_nodes-1)        
    elif(topology=='substar'):
        if(substar_count==0):
            print "0 substars not possible"
            sys.exit(2)
        subhead=range(substar_count-1,num_nodes,substar_count)
        for a,b in zip(subhead,subhead[1:]):
            G.add_edge(a,b)
        for node in range(0,num_nodes):
            if(node!=int(math.ceil(node/substar_count)*substar_count)+(substar_count-1)):
                G.add_edge(node, int(math.ceil(node/substar_count)*substar_count)+(substar_count-1))
    #Adding self weight
    for a in range(0,num_nodes):
        G.add_edge(a,a)
    np.save(open('nodes','w'),G.nodes())
    np.save(open('edges','w'),G.edges())
    np.save(open('adj_mat','w'),nx.to_numpy_matrix(G))
    nx.draw(G)
    plt.savefig('graphRep.png')
    print "Done"

def main():
    if len(sys.argv)<2:
        usage()
    
    num_nodes=int(sys.argv[1])
    topology=sys.argv[2]
    substar_count=int(sys.argv[3])
    generate_graph(num_nodes,topology, substar_count)
    
if __name__ == '__main__':
    main()
