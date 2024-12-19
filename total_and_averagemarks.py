full_marks=300
std_no=int(input("enter the student number"))
std_name=input("enter the student name")
std_c_marks=int(input("enter c marks"))
std_cplus_marks=int(input("enter c++ marks"))
std_java_marks=int(input("enter java marks"))

print("student number :",std_no)
print("student name : ",std_name)

total_marks=std_c_marks+std_cplus_marks+std_java_marks
print("total marks of student :",total_marks)

avg_marks=total_marks/3
print("average of three subjects",avg_marks)

if(avg_marks>70):
    print("passed")
else:
    print("failed")

if(std_c_marks<40 and std_cplus_marks<40 and std_java_marks<40):
  print( "student failed to pass in a subject")
else:
  if(total_marks>0.9*full_marks):
    print("A grade")
  elif(total_marks>0.8*full_marks):
    print("B grade")
  elif(total_marks>0.7*full_marks):
    print("C grade")
  else:
    print("failed  in exam")
