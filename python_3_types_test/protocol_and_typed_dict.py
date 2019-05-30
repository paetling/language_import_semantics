# see https://www.python.org/dev/peps/pep-0544/ and https://www.python.org/dev/peps/pep-0589/
from typing_extensions import Protocol
from abc import abstractmethod
from typing import Optional, Dict
from mypy_extensions import TypedDict

############################################################
# TEST Protocols
############################################################
class Dog(Protocol):
    name: str
    age: int

    @abstractmethod
    def bark(self, length: int) -> str:
        raise NotImplementedError

class Thunder():
    name = 'thunder'
    age = 18
    def bark(self, length: int) -> str:
        return 'AAAooooOoOoOo'

class NotQuite1():
    name: str
    age: int

class NotQuite2():
    def bark(self, length: int) -> str:
        return 'hey'

def function_1(dog: Dog) -> None:
    pass

thunder = Thunder()
not_quite_1 = NotQuite1()
not_quite_2 = NotQuite2()

function_1(thunder)
function_1(not_quite_1) # expected error: does not have the right method
function_1(not_quite_2) # expected error: does not have right properties
function_1(5) # expected error: just plain the wrong type


############################################################
# TEST TypedDict
############################################################
class BaseDict(TypedDict):
    key_1: int
    key_2: str

class OptionalDict(BaseDict, total=False):
    key_3: str

class CompositionDict(BaseDict):
    key_4: BaseDict


var_1: BaseDict = {"key_1": 5, "key_2": "6"}
var_2: BaseDict = {"key_1": 5, "key_2": 6} # expected error: key_2 has wrong type
var_3: BaseDict = {"key_1": 5 } # missing key_2
var_4: BaseDict = {"key_1": 5, "key_2": "6", "key_4": 7} # expected error: error due to extra key


var_5: OptionalDict = {"key_1": 5, "key_2": "6"}
var_6: OptionalDict = {"key_1": 5, "key_2": "6", "key_3": "7"}
var_7: OptionalDict = {"key_1": 5, "key_2": "6", "key_3": 7} # expected error: optional key does not have right type

var_8: CompositionDict = {"key_4": {"key_1": 5, "key_2": "6"}}

##### Learnings
# * From my experimentation, it does not seem like you can declare properties with type Optional and have mypy work correctly
#   * https://github.com/python/mypy/issues/2632
#   * You instead need to declare a second class which is annoying actually
# * It seems like extra key error from like 62 is due to this: https://github.com/python/mypy/issues/4617. It only happens when statically declaring a type
