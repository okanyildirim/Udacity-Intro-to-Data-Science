import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:

    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''

    #create input and output file
    inputFile=open(filenames[0],'r')
    outputFile=open(filenames[1],'w')

    #create readers ans writers
    reader=csv.reader(inputFile)
    writer=csv.writer(outputFile)

    for line in reader:
        column0 = line[0]
        column1 = line[1]
        column2 = line[2]
        index=3
        numberOfNewLine=round((len(line)-3)/5)
        for i in range(0,numberOfNewLine):
            newline=[column0,column1,column2]
            for j in range(0,5):
                newline.append(line[index])
                index+=1
            writer.writerow(newline)
            print(newline)
            #newline.clear()

    inputFile.close()
    outputFile.close()
    """
        for name in filenames:
        print(name)
    """


fileNames=["turnstile_110521.txt","updated_turnstile_110521.txt"]
fix_turnstile_data(fileNames)
