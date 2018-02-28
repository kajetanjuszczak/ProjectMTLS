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
* 24.02
    * working on dictionaries made me realy frustrated, changed to lists and frustration is gone
    * tried using map function for changing states and aa into numbers, it worked just fine 
* 26.02
    * consolidated all functions into one program
    * did backup all in one script where windows for different proteins are stored separately, merged them in my script
    * established system where user can input the fold of kFold validation 
    * introduced Kfold validation of my set
    * my script now prints out the average accuracy after k fold cross validation of my dataset
* 28.02
    * my model creating script works. 
    * best accuracy for window 19 for accuracies see documents folder
    * predictor predicts, only problem is its getting errors in one of aminoacids is not present in given sequence cause it change the shape of the array making it not suitable for model
    * I should work on the abovementioned problem
    * next step analysis of the results, false positives false negatives etc. 