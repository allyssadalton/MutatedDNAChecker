#function that asks if you want to print the sequences
#and that asks if you want to repeat the program
s=0

aminoaciddict  = {"UUU" : "Phe", "CUU" : "Leu", "AUU" : "Ile", "GUU" : "Val", "UUC" : "Phe", "CUC" : "Leu", "AUC" : "Ile", "GUC" : "Val", 
"UUA" : "Leu", "CUA" : "Leu", "AUA" : "Ile", "GUA" : "Val", 
"UUG" : "Leu", "CUG" : "Leu", "AUG" : "Met", "GUG" : "Val", 
"UCU" : "Ser", "CCU" : "Pro", "ACU" : "Thr", "GCU" : "Ala", 
"UCC" : "Ser", "CCC" : "Pro", "ACC" : "Thr", "GCC" : "Ala", 
"UCA" : "Ser", "CCA" : "Pro", "ACA" : "Thr", "GCA" : "Ala", 
"UCG" : "Ser", "CCG" : "Pro", "ACG" : "Thr", "GCG" : "Ala", 
"UAU" : "Tyr", "CAU" : "His", "AAU" : "Asn", "GAU" : "Asp", 
"UAC" : "Tyr", "CAC" : "His", "AAC" : "Asn", "GAC" : "Asp", 
"UAA" : "STOP", "CAA" : "Gln", "AAA" : "Lys", "GAA" : "Glu", 
"UAG" : "STOP", "CAG" : "Gln", "AAG" : "Lys", "GAG" : "Glu", 
"UGU" : "Cys", "CGU" : "Arg", "AGU" : "Ser", "GGU" : "Gly", 
"UGC" : "Cys", "CGC" : "Arg", "AGC" : "Ser", "GGC" : "Gly", 
"UGA" : "STOP", "CGA" : "Arg", "AGA" : "Arg", "GGA" : "Gly", 
"UGG" : "Trp", "CGG" : "Arg", "AGG" : "Arg", "GGG" : "Gly" 
} 

global seq1
global seq2
#opens and read files
filename1=input("Enter the file name of the original DNA sequence: ")
filename2=input("Enter the file name of the second/mutated DNA sequence: ")
print("")
file1=open(filename1)
file2=open(filename2)
seq1=file1.read().upper()
seq2=file2.read().upper()

#makes codon chart & first rna lists
amino1=[]
amino2=[]
rna1=[]
rna2=[]

for base in seq1:
    if base == "T":
      rna1 += "A"
    elif base == "A":
      rna1 += "U"
    elif base == "C":
      rna1 += "G"
    elif base == "G":
      rna1 += "C"    
for base in seq2:
    if base == "T":
      rna2 += "A"
    elif base == "A":
      rna2 += "U"
    elif base == "C":
      rna2 += "G"
    elif base == "G":
      rna2 += "C"
      
#makes list for dictionary
rnalist1 = [(rna1[f:f+3]) for f in range(0,len(rna1), 3)]
rnalist2 = [(rna2[h:h+3]) for h in range(0,len(rna2), 3)]
rnalist1=[]
rnalist2=[]
rna1="".join(rna1)
rna2="".join(rna2)
q=0
for q in range(0, len(rna1), 3):
  rnalist1.append("".join(rna1[q:q+3]))
q=0
for q in range(0, len(rna2), 3):
  rnalist2.append("".join(rna2[q:q+3]))
rnastr1=" ".join(rnalist1)      
rnastr2=" ".join(rnalist2)

#checks for mutations
#if there are no differences
if seq1==seq2:
  print("There are no mutations.")
  s+=1
#creates correct index
if len(seq1)==len(seq2) or len(seq1)<len(seq2):
  i=len(seq1)
if len(seq1)>len(seq2):
  i=len(seq2)
while True:
  #runs through entire sequence
  for x in range(i):
    #deletion
    if len(seq2)<len(seq1):
      if seq2[x]!=seq1[x]:
        print(f"The mutation type is deletion. The {seq1[x]} is deleted at place {x+1} in the second sequence.")
        s+=1
        break
      if seq2==seq1[:len(seq1)]:
        print(f"The mutation type is deletion. The {seq1[len(seq1)]} is deleted at place {len(seq1)} in the second sequence.")
        s+=1
        break
      if seq2[x]==seq1[x]:
        continue
    if seq1[x]!=seq2[x]:
      #insertion
      if seq2[x]!=seq1[x-1] and seq2[x]!=seq1[x-2] and seq2[x]!=seq1[x+1]:
        if x==i-1 and len(seq2)==len(seq1):
          None 
        elif len(seq2)>len(seq1): 
          print(f"The mutation type is insertion. {seq2[x]} is inserted at place {x+1} in the second sequence.")
          s+=1
        
      #duplication
      try:
        if seq2[x]==seq1[x-2] and seq2[x+1]==seq1[x-1]:
          print(f"The mutation type is duplication. The pair {seq1[x-2]}{seq1[x-1]} is repeated at place {x+1} and {x+2}." )
        s+=1
      #inversion
        if seq2[x]==seq1[x+1] and seq1[x]==seq2[x+1]:
          print(f'The mutation type is inversion. The pair {seq1[x]}{seq1[x+1]} is inverted at place {x+1} and {x+2}.')
      
      except IndexError:
        if seq1[x]==seq2[x]:
          continue
      
      print("")
      if seq1!=seq2:
        try:
          for y in range(len(rnalist1)):
            amino1.append(aminoaciddict[rnalist1[y]])
            y=0
          for y in range(len(rnalist2)):
            amino2.append(aminoaciddict[rnalist2[y]])

          if amino1==amino2:
            print(f"There is a silent substitution mutation in the amino acids. Amino Acid {seq1[x]} is substituted with {seq2[x]} at place {x+1} in sequence 2.")
            print("")
          elif amino1!=amino2:
            for k in range(len(amino1)):
              if amino1[k]!=amino2[k]:
                  print(f"There is a missense substitution mutation in the amino acids. The mutation is in place {k+1}, and is mutated to {amino2[k]} instead of  {amino1[k]}. Amino Acid {seq1[x]} is substituted with {seq2[x]} at place {x+1} in sequence 2.")
                  print("")
        except KeyError:
          print(f"There is a nonsense substitution mutation in the amino acids. The codon missing is {amino1[y]} in place {y+1}. Amino Acid {seq1[x]} is substituted with {seq2[x]} at place {x+1} in sequence 2.")
          c=1
  print("")
  break 

if s>=1:
  try:
    for y in range(len(rnalist1)):
      amino1.append(aminoaciddict[rnalist1[y]])
      y=0
    for y in range(len(rnalist2)):
      amino2.append(aminoaciddict[rnalist2[y]])
  except KeyError: 
    None 
      
#prints sequence1 & 2 info
print("")
print(f"Sequence 1 DNA: {seq1}")
print(f"Sequence 1 RNA: {rna1}")
print(f"Sequence 1 Amino Acid: {' '.join(rnastr1)}")
print(f"Sequence 1 Codon Chart: {' '.join(amino1)}")
print("")
print(f"Sequence 2 DNA: {seq2}")
print(f"Sequence 2 RNA: {rna2}")
print(f"Sequence 2 Amino Acid: {' '.join(rnastr2)}")
print(f"Sequence 2 Codon Chart: {' '.join(amino2)}")
  
#creates amino acid files
AminoAcid1 = amino1
AminoAcid2 = amino2
textfile1 = open("AminoAcid1.txt","w")
for element in AminoAcid1:
  textfile1.write(element + ",")
textfile1.close()   
textfile2 = open("AminoAcid2.txt","w")
for elements in AminoAcid2:
  textfile2.write(elements + ",")
textfile2.close()    
