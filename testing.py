from Bio import SeqIO
from orffinder import orffinder

sequence = SeqIO.read("sample1.fasta", "fasta")
data = orffinder.getORFs(sequence, minimum_length=90, remove_nested=True)
res = [i for i in data if not (i['sense'] == '-')]
print(res)
