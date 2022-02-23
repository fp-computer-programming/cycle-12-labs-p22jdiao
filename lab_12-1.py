# Author: JD 02/05/2022
# By using a open() statement, the program will open the file with writing mode.
my_file = open("my_file.txt","w")
# By using a .write() mathod, the program will write the contends needed with an escape character '\n' in the end of each line to go to the next line.
my_file.write("JD 021522\n")
my_file.write("Hello world\n")
my_file.write("Playing soccer and computer games.")
my_file.close()
