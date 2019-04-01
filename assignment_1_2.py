def sum_func(*numbers):
    return sum(numbers)

def test_palindrome(string):
    for i in range((len(string)+1)//2):
        if string[i] != string[-i-1]:
            return False
    return True



print(sum_func(1,5,3,-4,-2.5,39.5)) #42
print(test_palindrome("asdfdsa")) #True    
print(test_palindrome("asdffdsa")) #True
print(test_palindrome("asdffsa")) #False
print(test_palindrome("ab")) #False
print(test_palindrome("")) #True
    
            
