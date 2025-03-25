# 4. Counting Passengers in a Bus
# A city bus stops at different stations, and passengers board at each stop. The bus conductor
# notes down the number of passengers at each stop for 5 stops. Write a Python program to take
# input for each stop and calculate the total number of passengers at the end.

total_pass = 0
for stops in range(1 ,5) :
    num_pass = int(input("enter number of passengers "))
    total_pass += num_pass
print("total passengers are ", total_pass)