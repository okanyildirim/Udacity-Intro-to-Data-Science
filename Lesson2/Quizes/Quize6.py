import csv
def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file. The input files do not have column header
    rows of their own.

    For example, if file_1 has:
    line 1 ...
    line 2 ...

    and another file, file_2 has:
    line 3 ...
    line 4 ...
    line 5 ...

    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
    with open(output_file, 'w')  as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        writer = csv.writer(master_file)
        for filename in filenames:
            inputFile=open(filename,'r')
            inputFile.readline()    #read first line, it is unnecessary
            reader=csv.reader(inputFile)
            writer.writerows(reader)
            """
            for line in reader:
                 print(line)
                 for i in line:
                     if i=="\n":
                         continue
                    master_file.write(i)
                    master_file.write(",")
                 master_file.write("\n")
                 """

        inputFile.close()
        master_file.close()

fileNames=["turnstile_110521.txt","weather_underground.csv"]
create_master_turnstile_file(fileNames,"output.txt")