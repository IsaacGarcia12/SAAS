from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
"""
cline = ClustalwCommandline("clustalw", infile="new.fasta", outfile="new.aln")
print (cline)
stdout, stderr = cline()
print(stdout)

#Con esto leemos el phytlotree
tree = Phylo.read("new.dnd", "newick")
tree.rooted = True

#Imprimimos el Arbol
Phylo.draw(tree)
"""
cline = ClustalwCommandline("clustalw", infile="/home/isaac/Escritorio/SAmin/TT/creacion.fasta", outfile="new.aln")
print (cline)
stdout, stderr = cline()
print(stdout)

#Con esto leemos el phytlotree
tree = Phylo.read("/home/isaac/Escritorio/SAmin/TT/creacion.dnd", "newick")
tree.rooted = True