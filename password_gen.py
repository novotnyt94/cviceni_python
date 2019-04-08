# The dependency on numpy is a bit of an overkill and you would usually want
# to avoid it -- if people only want a password generator, they don't want to
# install numpy for it to work :). Besides, there's random.choice [1] in the
# standard library.
#
# [1] https://docs.python.org/3/library/random.html#random.choice
#
# Unless, of course, you know that numpy gives better randomness. I don't think
# so, but it's possible.

import numpy.random as rand
import string
SPEC_CHARS = ['-','+','_','#','$','%','&','=',';','/','\\']
def password_gen(length=8, spec_chars=4):
    if spec_chars > length:
        raise ValueError("Number of special characters must not be greater than password length");
    #concatenate required number of random chars and special characters
    base_passwd = list(rand.choice(list(string.ascii_letters + string.digits), length-spec_chars, replace=True)) + list(rand.choice(SPEC_CHARS, spec_chars, replace=True))
    #permutate them and transform into string
    return ''.join(rand.permutation(base_passwd))


print(password_gen())
print(password_gen(16,2))            
