t1 = 98
t2 = 94
t3 = 41
t4 = 95
t5 = 11
sum = t1+t2+t3+t4+t5
avg = sum / 5
print(avg)
# actvity 2
Amount =int(input("please enter your amount"))
note_100 = Amount//100
note_50 = (Amount%100)//50
note_10 = ((Amount%100)%50)//10
print("notes of 100",note_100)
print("notes of 50",note_50)
print("notes of 10",note_10)
print("Enter marks obtaines in 3 subjects")
math = int(input("math: "))
science = int(input("science: "))
social = int(input("social: "))
sum = math+science+social
per= (sum/300)*100
print("the percentage obtained by the student")
print(end="percentage mark = ")
print(per)