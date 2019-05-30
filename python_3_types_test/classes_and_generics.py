from typing import TypeVar, Generic

############################################################
# TEST Classes
############################################################
class Dog_1:
    name: str;
    age: int;
    def speak(self) -> str:
        pass

class Dog_2:
    name: str;
    age: int;
    def speak(self) -> str:
        pass

def get_words(dog: Dog_1) -> None:
    pass

dog_1 = Dog_1()
dog_2 = Dog_2()

get_words(dog_1)
get_words(dog_2) # expected error: dog_2 is not type Dog_1


##### Learnings:
# * Duck typing is not used in classes


############################################################
# TEST Inheritance
############################################################
class Collie(Dog_1):
    def speak(self) -> str:
        return 'border collie'

def get_words_2(collie: Collie) -> None:
    pass

collie = Collie()
get_words(collie)

get_words_2(dog_1) # expected error: dog_1 is not of type collie
get_words_2(collie)



############################################################
# TEST Generic Functions
############################################################
T = TypeVar('T')

def get_value(value: T) -> T:
    pass

var_1: str = get_value('dog')
var_2: int = get_value(5)
var_3: str = get_value(5) # expected error: int is not assignable to type string

############################################################
# TEST Generic Classes
############################################################

class ClassTest1(Generic[T]):
    def get_value(self, value: T) -> T:
        return value

class_1: ClassTest1[str] = ClassTest1()
class_2: ClassTest1[int] = ClassTest1()
var_4: str = class_1.get_value('dog')
var_5: int = class_2.get_value(5)


class ClassTest2(Generic[T]):
    def __init__(self, value: T):
        pass

    def get_value(self, value: T) -> T:
        return value

class_3 = ClassTest2('dog')
class_4 = ClassTest2(5)
var_6: str = class_3.get_value('dog')
var_7: int = class_4.get_value(5)


##### Learnings:
# * From ClassTest2 and ClassTest1, it is possible to infer the type of the generic class directly from constructor args. But if that cannot be done it must be explicitly defined
