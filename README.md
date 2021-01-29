# Join-CSV
This project joins two csv files

# Input
File_1.csv from equipment 1 <br/>
File_2.csv from equipment 2 <br/>
Both files need to be joined on Time stamp

# Possible Anomolies 
Both system times may have some offset wrt each other. This needs to be corrected taking one of these as base file, We will take file_1 as the base file.

# Output
Output file is a csv file containing one time stamp and all collumns of file 1 and corresponding rows of file 2.

# Date formats <br/>
 A few possible cases <br/>
 2019-05-28 22:12:58 --->  %Y-%m-%d %H:%M:%S <br/>
 28/05/2019 22:12:58 --->  %d/%m/%Y %H:%M:%S <br/>
 28-Jan-21 01:48:39:417 --->  %d-%b-%y %H:%M:%S:%f <br/>
 28-January-21 01:48:39:417 --->  %d-%B-%y %H:%M:%S:%f <br/>

# Joining dataframes/csv
Let file1 (left) and file2 (right) be the two files to be joined on key/column Timestamp.<br/>
## Full Outer join 
Joined file will have all rows of file1 and file2, NAN is filled in places where no record exists.<br/>
## Inner Join 
Joined file will only the records corresponding to Timestamp which matches in both files.<br/>
## Right Join 
Joined file will all the records of file2 and only the rows of file1 whose Timestamp matches with file2. If no match then NaN is filled.<br/>
## Left Join 
Joined file will all the records of file1 and only the rows of file2 whose Timestamp matches with file1. If no match then NaN is filled.<br/>
