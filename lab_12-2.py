# Author: JD 02/15/2022
# Open the file with append mathod.
my_file = open("my_file.txt","a")
# Adding the lines at the end of the file, starts with an escape character to start with a new line.
my_file.write("\nHaving vedio calls with family members.\n")

my_file.write("Go back home to see my family.")
# Closing the file in the end.
my_file.close()
