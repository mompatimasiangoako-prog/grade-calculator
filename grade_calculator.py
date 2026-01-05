
Num_Of_subjects = int(input("Enter the number of subjects you take"));
count = 0;
subject = " ";
grade = 0;
subjects = [];
grades = []
average = 0;

while(count != Num_Of_subjects):
    subject = str(input("Enter the name of your subject"));
    grade = int(input("Enter your grade"));
    subjects.append(subject);
    grades.append(grade);
    count = count + 1;

for i in range(len(grades)):
    average =  average + grades[i];
 
average = average / 2;
print("Your average mark is",average);
    
    
    
    

    
    