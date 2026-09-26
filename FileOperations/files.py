# Read a Whole File 
with open('requirements.txt','r') as file:
  content=file.read()
  print(content)

# Read a file Line By Line 
with open('requirements.txt','r') as file:
  for line in file:
    # print(line)
    print(line.strip())

# Writing a file (Overwriting)
with open('requirements.txt','w') as file:
 file.write('Hi ra toby \n')
 file.write('I am the new Line  \n')

# Writing a file Without Overwriting 
with open('requirements.txt','a') as file:
  file.write("Append Operation \n ")

lines=["\nI am Lines \n","Demo \n","ra Babu \n"]
#Writing a list of lines to a file
with open('requirements.txt','a') as file:
  file.writelines(lines)