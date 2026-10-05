#take marks of 5 subjects and calculate total number and percentage
english = int(input("Enter your marks in English: "))
hindi = int(input("Enter your marks in Hindi: "))
maths = int(input("Enter your marks in Maths: "))
science = int(input("Enter your marks in Science: "))  
udru = int(input("Enter your marks in Urdu: ")) 
total_marks= english + hindi + maths + science + udru
percentage = (total_marks / 500) * 100
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")    
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")    

