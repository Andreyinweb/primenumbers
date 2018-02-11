"""
Search for prime numbers.
Поиск простых чисел.
"""

from math import sqrt 

class PrimeNumbers():
    """
    A class for finding prime numbers.
    Класс для нахождения простых чисел.
    """
    
    def __init__(self,max_number = 100):
        
        
        self.max_number = max_number
        self.list_data = list()
        self.list_need = list()
 

    def sequenceprimes (self, max_number = 0):
        """
        The function returns a list of prime numbers from 2 to max (by default, max = 100)
        Функция возвращает список простых чисел от 2 до max (по умолчанию max = 100)
        """
        
        if max_number != 0 :
            self.max_number = max_number + 1
        # A list of numbers from 3 to max_number is created, excluding the numbers divisible by 2 and 3.
        # Создается список чисел от 3 до max_number, исключая числа делящиеся на 2 и на 3.
        self.list_data = [ i for i in range(3, self.max_number, 2) if (i % 3 != 0) ]
        # Current divisor
        # Текущий делитель
        number_now = 5
        j = 1
        # Rewrite all dividers from the created list.
        # Перебераем все делители из созданного списка.
        while number_now <= int (sqrt(self.max_number)):
            # Rewrite the list excluding the divisible numbers.
            # Переписываем список исключая делящиеся на делитель числа.
            self.list_data = [ i for i in self.list_data  if (i % number_now != 0)]
            
            self.list_data.insert(j-1, number_now)
            number_now = self.list_data [j]
            j += 1 

        data_list = [] + self.list_data
        # Add to list 2 and 3
        # Добавляем в список 2 и 3
        data_list.insert(0,2)
        data_list.insert(1,3)
        return data_list     

    def rangeprimes(self, min_number = 5, max_number = 0):
        """
        The function returns a range of prime numbers from min to max (default is from 2 to the defined self.max_number in the class)
        Функция возвращает диапазон простых чисел от min до max (по умолчанию  от 2 до определенной в классе self.max_number)
        """
        
        if max_number == 0 :
            return self.sequenceprimes()

        if max_number <= 5 :
            return self.sequenceprimes(5)

        if min_number < 4 : min_number = 3
        if min_number % 2 == 0 : 
            min_num = min_number - 1
        else:
            min_num = min_number
            
        # A list of numbers from min_number to max_number is created, excluding the numbers divisible by 2 and 3.
        # Создается список чисел от min_number до max_number, исключая числа делящиеся на 2 и на 3.
        self.list_need  = [ i for i in range(min_num, max_number + 1, 2) if (i % 3 != 0) ]
        # A list of prime numbers is created to a min_number
        # Создается список простых чисел до min_number
        self.sequenceprimes(min_num) 
        
        for number_now in self.list_data:
            
            if number_now > sqrt(max_number) :
                break
            # Rewrite the list excluding the divisible numbers.
            # Переписываем список исключая делящиеся на делитель числа.
            self.list_need = [ i for i in self.list_need if (i % number_now != 0)]
        
        j = 1
        while number_now <= int (sqrt(max_number)):
            # Rewrite the list excluding the divisible numbers.
            # Переписываем список исключая делящиеся на делитель числа.
            self.list_need = [ i for i in self.list_need  if (i % number_now != 0)]
            
            self.list_need.insert(j-1, number_now)
            number_now = self.list_need [j]
            j += 1
            
        if self.list_need[0] < min_number:
            self.list_need.remove(self.list_need[0])
            
        return self.list_need


    
