from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

# Read the sequences from the Phylo file
align = AlignIO.read('Data_MultiSeq.phy','phylip')

calc = DistanceCalculator('identity')

distMatrix = calc.get_distance(align)
print("=====> Distance Matrix <=====")
print(distMatrix)

# Phlyogenetic tree with UPGMA algorithm
treeUPGMA = DistanceTreeConstructor().upgma(distMatrix)
print("\n\n\n=====> Merging Steps <=====")
print(treeUPGMA)

# Draw the Phlyo-tree
Phylo.draw(treeUPGMA)