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
