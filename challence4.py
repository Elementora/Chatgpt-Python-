##########################################################
# Challenge: 3’ün Katlarını "Fizz", 5’in Katlarını "Buzz" Yazan Program
# Normal Fonksiyon ile (def)

def fizzbuzz(lst):
    return ["FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
            "Fizz" if num % 3 == 0 else
            "Buzz" if num % 5 == 0 else
            num for num in lst]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 18, 20, 30]
print(fizzbuzz(numbers))


# Lambda Fonksiyonu ile
def fizzbuzz(lst): return ["Fizzbuzz" if num % 3 == 0 and num % 5 == 0 else
                           "Fizz" if num % 3 == 0 else
                           "Buzz" if num % 5 == 0 else
                           num for num in lst]
