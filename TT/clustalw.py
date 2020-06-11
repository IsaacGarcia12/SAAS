from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo

cline = ClustalwCommandline("clustalw", infile="new.fasta", outfile="new.aln")
print (cline)
stdout, stderr = cline()
print(stdout)

#Con esto leemos el phytlotree
tree = Phylo.read("new.dnd", "newick")
tree.rooted = True
#Con esto lo convertimos a otro tipo de notacion
Phylo.convert('new.dnd', 'newick', 'new.xml', 'phyloxml')
#tree.ladderize()
#Imprimimos el Arbol
Phylo.draw_ascii(tree)