from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo

cline = ClustalwCommandline("clustalw", infile="new.fasta", outfile="new.aln")
print (cline)
stdout, stderr = cline()
print(stdout)

tree = Phylo.read("new.dnd", "newick")
tree.rooted = True
#tree.ladderize()
with open('phylo.png', 'w') as phylo:
    phylo.write(Phylo.draw(tree))