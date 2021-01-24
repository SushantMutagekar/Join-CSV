# Join-CSV
This project joins two csv files

# Input
File_1.csv from equipment 1
File_2.csv from equipment 2
Both files need to be joined on Time stamp

#Possible Anomolies 
Both system times may have some offset wrt each other. This needs to be corrected taking one of these as base file, We will take file_1 as the base file.

#Output
Output file is a csv file containing one time stamp and all collumns of file 1 and corresponding rows of file 2.
