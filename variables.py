# get information
this_is_a_variable = float(input("Please give me a number "))

# do calculation
caluclated_answer = this_is_a_variable + 2

# give output
print(caluclated_answer)


a = "all "
b = "work "
c = "and "
d = "no "
e = "play "
f = "makes "
g = "Jack "
h = "a "
i = "dull "
j = "boy"
print(a + b + c + d + e + f + g + h + i + j)

#print(6 * (1 - 2))   # is a comment for not conduct

#print(bruce + 4)

bruce=6
print(bruce+ 4)

P=1000
n=5
r=0.01
t=10
A=P*(1+r/n)**(n*t)
print(float(A))

a=2+51-24*2
print(a)

current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int

final_answer = final_time_int % 24

print("The time after waiting is: ", final_answer)
