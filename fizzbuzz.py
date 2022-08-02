from typing import Union
fizz = "Fizz"
buzz = "Buzz"

def fizzbuzz(num: int) -> Union[str, int]:
    if(num % 3 == 0 and num % 5 == 0):
        return fizz+" "+buzz
    elif(num % 3 == 0):
        return fizz
    elif(num % 5 == 0):
        return buzz
    else:
        return num
