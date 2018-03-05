import os

DB = "../datasets/buried_exposed_beta.3line.txt"
#buried_exposed_beta.3line
listofnames =  []
listoffilenames = []
listofsequences = []
for i, line in enumerate(open(DB, "r")):
    if i % 3 == 0:
        listofnames.append(line.strip("\n"))
    if i % 3 == 1:
        listofsequences.append(line.strip("\n"))
    if i % 3 == 0:
        listoffilenames.append(line.strip(">\n"))
DBdir = '../datasets/SingleFastaForPSSM'
os.chdir(DBdir)
for i in range(len(listofnames)):
    with open(listoffilenames[i]+".fasta", "w") as f:
        f.write(listofnames[i])
        f.write(("\n"))
        f.write(listofsequences[i])