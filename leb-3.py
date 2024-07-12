
name = input("Enter Your Name:")
rl = int(input("Enter Your Roll No:"))

a = int(input("Enter C# Marks: "))
b = int(input("Enter OS Marks: "))
c = int(input("Enter Java Marks: "))
d = int(input("Enter SEO Marks: "))
e = int(input("Enter Python Marks:"))

total = a+b+c+d+e
per = total/5

print("\t\t\t--Marksheet---\n ")

print("\t\t\tYour Name:",name)
print("\t\t\tRoll No: ",rl)

print("\n\nSubject \t\t Total Mark \t\t Obtained Mark ")
print("\t\t-----------------------------")
print("\nC# \t\t\t 100 \t\t\t" ,a) 
print("OS \t\t\t 100 \t\t\t" ,b) 
print("Java \t\t\t 100 \t\t\t" ,c) 
print("SEO \t\t\t 100 \t\t\t" ,d)
print("Python \t\t\t 100 \t\t\t",e)
print("\t\t-----------------------------")
print("\nTotal: \t\t\t 500 \t\t\t",total)
print("\t\t-----------------------------")
print("Percentage: \t\t\t\t\t",per)
print("\t\t-----------------------------")


if(per>90 and per<=100):
  print("A grade")
elif(per>80 and per<=90):
  print("B grade")
elif(per>60 and per<=80):
  print("C grade")
elif(per>50 and per<=60):
  print("D grade")
elif(per>0 and per<=50):
  print("pass class")
else:
  print("error")
  
if(a<33 or b<33 or c<33 or d<33 or e<33):
    print("You Fail")

