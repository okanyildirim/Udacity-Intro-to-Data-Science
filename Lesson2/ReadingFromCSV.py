import pandas as pd

dataFrame=pd.read_csv("../Lesson1/Lesson1Quizs/titanic_data.csv")


print(dataFrame)
print(dataFrame.Fare)
print(dataFrame.describe())

dataFrame["PassengerNo"]=dataFrame["PassengerId"]+dataFrame["Fare"]

print(dataFrame)

dataFrame.to_csv("titanicDataEditedwithPassengerNo.csv")

print("***********************************************")
#import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe and adds a new column
    #called 'nameFull' with a player's full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron',
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv

    #WRITE YOUR CODE HERE
    baseballDataFrame=pd.read_csv(path_to_csv)
    baseballDataFrame["nameFull"]=baseballDataFrame["nameFirst"]+" "+baseballDataFrame["nameLast"]
    baseballDataFrame.to_csv(path_to_new_csv)




if __name__ == "__main__":
    # For local use only
    # If you are running this on your own machine add the path to the
    # Lahman baseball csv and a path for the new csv.
    # The dataset can be downloaded from this website: http://www.seanlahman.com/baseball-archive/statistics
    # We are using the file Master.csv
    path_to_csv = ""
    path_to_new_csv = ""
    add_full_name(path_to_csv, path_to_new_csv)
