print('hello')
from platform import python_version
print("Current Python Version-", python_version())
import Bio
print(f"Biopyton version = {Bio.__version__}")
path ='/home/martin/CourseraPY/'
filename="dna2.fasta"
from Bio import SeqIO
count=0
record_len =[]
for seq_record in SeqIO.parse(filename, "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    record_len.append(len(seq_record.seq))

    count += 1

print(f"total number of seqs in file is = {count}")
print(record_len)
print(min(record_len))
print(max(record_len))

#question 4
#https://stackoverflow.com/questions/49073217/how-to-use-biopython-to-translate-a-series-of-dna-sequences-in-a-fasta-file-and
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
out=[]
for dna_record in SeqIO.parse("dna2.fasta", 'fasta'):
    # use  fwd sequences
    # if len(dna_record)%3==1:
    #     dna_record = dna_record + 'NN'
    # if len(dna_record)%3==2:
    #     dna_record = dna_record + 'N'
    ## print(len(dna_record)%3)
    aa_seqs = dna_record[1:].translate(to_stop=True) 
    # select the longest one
    print(len(dna_record))
    out.append(len(aa_seqs))
print("Answer to question 4:")
print(out)
print (max(out)*3)
#solution may be in https://stackoverflow.com/questions/61212538/finding-the-longest-orf-open-reading-frame-in-reading-frame-2-in-multiple-sequ
