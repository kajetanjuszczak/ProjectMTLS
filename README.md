# ProjectMTLS

Diary:
* 20.02
    * Created the function to make dictionary out of dataset.
    * Maybe try not to use the .readlines function
* 21.02
    * Started thinking about what my output should look like, created dictionary relating aminoacid to its number. *think about map function as easier solution.
    * Mostly reading stuff related to pandas, Scikit, SVM which is necessary to finish the parser.
    * Try to use with open to make code shorter(def filetodictionary).
    * My parser is now returning amino acid sequence and state in as list of numbers
* 22.02
    * Created function which returns the dictionary in which for each key there are two lists, one contain arrays - windowsof aa other contain list of states related so that l1[0] is the state of l0[0]
    * Still have to finish convernter
    * merged 2 functions into one for aa and states into numbers
* 23.02
    * Corrected dates in diary, apparently its not january anymore
    * finnished my parser so it now given database is produces matrices of windows and lists of states in a dictionary.
    