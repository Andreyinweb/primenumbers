# python3 search.py

# Search for prime numbers.
# Простые числа 

from prime_numbers import PrimeNumbers
from time import process_time
print("time =", process_time())


prime_numbers = PrimeNumbers()


print(prime_numbers.sequenceprimes())
print("LEN =", len(prime_numbers.sequenceprimes()))

print("Default:", prime_numbers.rangeprimes())

print(prime_numbers.sequenceprimes(11))

print("from 6 to 13:", prime_numbers.rangeprimes(6,13))

print("------------------------------------------------")

print("from 98 to 280:", prime_numbers.rangeprimes(98,250))

print("------------------------------------------------")

print("time =", process_time())
list_need = prime_numbers.rangeprimes(10000,1000000)
print("time =", process_time())

print("LEN =",str(len(list_need)))
print("list_data [",'1', "]=", list_need[0])
print("list_data [",len(list_need)-2, "]=", list_need[len(list_need)-3])
print("list_data [",len(list_need)-1, "]=", list_need[len(list_need)-2])
print("list_data [",len(list_need), "]=", list_need[len(list_need)-1])





















# from time import process_time
# print("time =", process_time())

# min_number = 4   
# max_number = 100000


# if min_number % 2 == 0: 
#     min_number -= 1

# print("min_number =",min_number)
# print("max_number =",max_number)

# number_now = 5
# number_two = 7
# j = 1
# list_data = [ i for i in range(min_number,max_number,2) if (i % 3 != 0) ]
# print("time under while =", process_time())
# while number_now <= int (sqrt(max_number)):
#     # print("number_now =", number_now)
#     # print("time =", process_time())

#     for i in list_data  :
#         if (i % number_now == 0 or i % number_two == 0):
#              list_data.remove(i)

    
#     list_data.insert(j-1, number_now)
#     list_data.insert(j, number_two)

#     number_now = list_data [j+1]
#     number_two = list_data [j+2]
#     j += 2

 
# if len(list_data) <= 100:    
#     print(list_data)
# print("time =", process_time())

# print("LEN =",str(len(list_data)))
# print("list_data [",len(list_data)-2, "]=", list_data[len(list_data)-3])
# print("list_data [",len(list_data)-1, "]=", list_data[len(list_data)-2])
# print("list_data [",len(list_data), "]=", list_data[len(list_data)-1])
# print("Квадрат ",number_now, " = ", str(number_now*number_now))
  


    
