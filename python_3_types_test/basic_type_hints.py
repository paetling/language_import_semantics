from typing import Any

############################################################
# TEST INPUT CHECKING
############################################################
def input_test_1(yes: bool, value_1: int, value_2: float, value_3: str) -> None:
    print(yes, value_1, value_2, value_3)

input_test_1(1, 1, 2, 'dog') # expected error: input has incompatible type
input_test_1(True, 1.0, 2, 'dog') # expected error: input has incompatible type
input_test_1(False, 'string', 2, 'dog') # expected error: input has incompatible type
input_test_1(True, 1, 2.0, 1) # expected error: input has incompatible type

x = 'cat'
y = 10
z: Any = 'cat'
input_test_1(True, x, x, 'x') # expected error: input has incompatible type
x = 10
input_test_1(True, x, x, 'x') # expected error: input has incompatible type
input_test_1(y, y, y, y) # expected error: input has incompatible type
input_test_1(z, z, z, z)

def input_test_2(yes, value_1: int) -> None:
    pass

input_test_2(5, 5)
input_test_2(5, '5') # expected error: incompatible type
input_test_2('5', 5)


##### Learnings:
# * booleans are accepted as number
# * on line 16 when we reassign x, it is still being treated as a string on line 17


############################################################
# TEST RETURN VALUES
############################################################
def return_test_1(value: bool) -> None:
    return value # expected error: no return value expected

def return_test_2(value: str) -> int:
    return value # expected error: incompatible return value

def return_test_3(value: str) -> str:
    return value

def return_test_4(value: str):
    return value

str_1 = 5
str_1 = return_test_1(True) # expected error: can't assign to None
str_1 = return_test_2('dog')
str_1 = return_test_3('dog') # expected error: string not assignable to in
str_1 = return_test_4('dog')

str_2: Any = 5
str_2 = None
str_2 = return_test_1(True) # expected error: cannot assign None to any
str_2 = return_test_2('dog')
str_2 = return_test_3('dog')
str_2 = return_test_4('dog')

##### Learnings:
# * line 59, you cannot assign None to an any variable



############################################################
# TEST TYPE ALIASES
############################################################
Url = str
def alias_input(url: Url) -> None:
    pass

alias_input('dog')
alias_input(5)
