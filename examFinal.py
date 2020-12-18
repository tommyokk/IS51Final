



"""
We are trying to show the the number of grades, the average grade,
and the percentage of grades that are above the average with
our code
Open the file "Final.txt" to get the grades. Copy and paste information.
Average the grades by sum of grades / # of grades.
If the grade is above average, += 1

"""

"""
Open Final.txt infile
grades = line infile
clse infile
avg = sum(grades) / number(grades)

for grade in grades:
    if grade is above avg
    add 1
print("Number of grades:" , number of grades)
print("Average grade:" sum of grades / number of grades)
print("Percentage of grades above average: % above average) 


"""

## Analyze the grades on a final exam.
infile = open("Final.txt", 'r')
grades = [line.rstrip()for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0    # number of grades above average
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average:  {0:2f}%")
format(100 * num / len(grades))