testDB = "D:/projekt/project/datasets/testDB.txt"

def filetodictionary(filename):
    dictionary = {}
    file1 = open(filename, "r")
    file2 = file1.readlines()
    for i, line in enumerate(open(filename, "r")):
        if line.startswith(">") == True:
            dictionary[line.strip(">\n")] = [file2[i + 1].strip("\n"), file2[i + 2].strip("\n")]
    file1.close()
    return dictionary
    
if __name__ == "__main__":
    print(filetodictionary(testDB))
