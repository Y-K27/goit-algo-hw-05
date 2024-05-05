from typing import Callable
import re 
#Завдання перше
def caching_fibonacci(cache = {}) -> Callable[[int], int]:
    def fibonacci(n)-> int:
        if n<=0 : 
            return 0
        elif n==1 : 
            return 1
        elif n in cache: 
            return cache[n]
        else:
            cache[n] = fibonacci(n-1)+ fibonacci(n-2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(15))

#Завдання друге
def generator_numbers(text: str):
    pattern = r'\d+\.\d+'
    float_string =re.findall(pattern, text)             #знаходомо всі числа типу float в радку        
    for i in float_string:
        yield float(i)                                  #переворюємо всі знвчення сиписку в числа перед поверненням

def sum_profit(tekst, item_of_profit):
    sum = 0.0
    for item in item_of_profit(tekst):                  #підраховуємо дохід
        sum+= item
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")