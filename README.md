# ProjectMTLS
* For final deadline
scripts are present in general scripts folder
PSSM model generates model based on full database and store it in model folder.
PSSM predictor predict topology for one example protein, resulting prediction is stored as text file in ../results folder named predictedPSSM(3 line format)
model is called PSSM_model and it is stored in model folder
other models for no PSSM and also DTC and RFC methods are also present in model folder.
more results from model testing are present in excel file in documents folder named results_excel


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
* 1.03
    * resolved issue with error in shape of predictors - set value of the encoder to 21
    * tested all different kernels and settings of model, seems like linear is best. only improvement found was when tolerance was moved to 0.003 (0.001 default) not big difference tho
    * checked scores for random forest and simple decision tree, they are attached in results

* 2.03 
    * quick update for deadline instruction and make sure my model actualy predicts
* 5.03
    * fighting with bash script to work it finalyy work but take 25 min / prot on my pc, tried using remotely lab pcs didnt work
    * DB into separate fasta files
* 6.03
    * trying to figure out how to make the PSSM parser
* 7.03 
    * figured out I pushed from wrong direction so diary wasnt updated :|
    * Did PSSM from swisprot cuz its fast
    * working on PSSM extractor - how to merge data in windows
    * also make fractions
* 8.03 
    * working on the PSSM
    * ask bout the extraction of additional proteins tmr
    * work on results from today to make graphs for the final report
* 9.03 
    * posted deadline things
* 12.03
    * testing of model running some optimization and statistics for the final report
    * trying to improve the model
    * looking for state of the are for SVC predictors on my task
    * ROC 
* 13.03 
    * continued working on figures to report
    * prepared ROC 
    * started to write the final report
* 14.03 
    * continued working on report
    * almost finished introduction
    * working on extracting additional proteins from PDBTM
    * made my programs look better by changing everything into functions - was a lot of work but it seems like my programs look much better now.
    * need to work on docstrings tho
* 15.03
    * continued work on final report - results part. 
    * still working on confusion matrix and extracting more proteins for testing
* 16.03 
    * almost finished report, if enough time will check PDBTM for aditional proteins
    * gona finish project tmr.
    * g2g sleep tho.
* 17.03
    * some corrections to the report
    * changed structure of files