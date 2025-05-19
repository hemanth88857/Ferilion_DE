

"""find even and  odd"""

# val = [1,34,54,6,7,88,4,6,46,6,43,3,35,5,66,7,]
#
#
# even = list(filter(lambda x:x%2==0,val))
# odd = list(filter(lambda x:x%2 != 0 ,val))
#
# print(even)
# print(odd)
#
# "2. Filter Strings Starting with a Specific Letter a     "
#
# words = ['Apple', 'Banana', 'Avocado', 'Cherry']
#
# word = list(filter(lambda x:x.endswith("y"),words))
#
# print(word)

"""3. Filter Positive Numbers """

# numbers = [-10, 0, 5, -3, 8]
#
# num = list(filter(lambda x:x>0,numbers))
# print(num)


"""4. Filter Palindromic Strings """

# words = ['radar', 'hello', 'level', 'world']
#
# palin = list(filter(lambda x:x == x[::-1] ,words ))
# print(palin)
#


"""5. Filter Prime Numbers """



def is_prime(num):
    if num < 2:
        return False
    for each in range(2,int(num**0.5)+1):
        if num%each == 0:
            return False
    return True


print(is_prime(2))


number = 10



def pirme_numbers(num):
    numr = []
    for each in range(2,num):

        for i in range(2,int(each**0.5)+1):

            if each%i == 0 :
                break
        else:
            numr.append(each)
    return numr

print(pirme_numbers(10))

nu = 10
prime_numbers = list(filter(
    lambda x: x > 1 and len([i for i in range(2, x) if x % i == 0]) == 0,
    range(2, nu+1)
))

print(prime_numbers)

x = 10
y = 20
print(x+y)