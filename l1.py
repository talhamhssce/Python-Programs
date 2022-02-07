#Read a file line by line 


# Open file
mf = open("myfile.txt", "r")
print("File to read: ", mf.name)

# Read all lines in the file
file_content = mf.readlines()
word_count = mf.read().split()
char_str = mf.read()
if len(word_count) <=250 :
    print("pass")

# Print all lines in file
for f in file_content :
    print(f)

# print("Characters are :", len(char_count))
char_count=len(char_str)
print(char_count)
# Close opened file
mf.close()

