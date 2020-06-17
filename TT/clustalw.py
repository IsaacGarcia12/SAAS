from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
import sys
import pylab

cline = ClustalwCommandline("clustalw", infile="/home/isaac/Escritorio/SAmin/TT/creacion.fasta", outfile="new.aln")
print (cline)
stdout, stderr = cline()
print(stdout)
#Con esto leemos el phytlotree
tree = Phylo.read("/home/isaac/Escritorio/SAmin/TT/creacion.dnd", "newick")
tree.rooted = True
#tree = Phylo.read("new.dnd", "newick")
#tree.rooted = True
Phylo.draw(tree, do_show=False) 
pylab.axis('off')
pylab.savefig('tree3.png',format='png', bbox_inches='tight', dpi=300)
