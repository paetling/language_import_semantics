from typing import *

############################################################
# TEST List, Set, Dict, Sequence
############################################################

def function_1(list: List, set: Set, dict: Dict) -> None:
    pass

function_1([], Set([]), {})
function_1((5, 4), Set([]), {'dog': True})
function_1([], Set([]), {}) # expected error: tuple is not type list
function_1(5, Set([]), {'dog': True}) # expected error: 5 is not an array
function_1([], [], {'dog': True}) # expected error: [] is not a set
function_1([], Set([]), []) # expected error: [] is not a dict


def test_sequence(seq: Sequence):
    pass

test_sequence((1,2,3))
test_sequence([1,2,3])
test_sequence({'cat': False}) # expected error: dict is not a sequence


def test_list(list: List[int]):
    pass

test_list([])
test_list([1, 2, 3])
test_list(['string', 'string']) #expected error: string list is not an int list

l1 = []
l1.append('string')
test_list(l1) # expected error: string list is not an int

l2: List[str] = []
l2.append('string')
test_list(l2) # expected error: string list is not an int


def test_dict(dict: Dict[str, int]):
    pass

test_dict({})
test_dict({'cat': 5})
test_dict({'dog': 'the best'}) # expected error: dict[str, str] is not assignable to type dict[str, int]


##### Learnings
# * On line 35, i expected no error. mypy must be doing something smart about assuming l1 is not valid



############################################################
# TEST Callable
############################################################
def test_callable_1(fun: Callable):
    pass

def function_2(value: str) -> str:
    pass

def function_3(value: int) -> int:
    pass

test_callable_1(function_2)
test_callable_1(function_3)
test_callable_1(lambda dog: dog)
test_callable_1(5) # expected error: 5 is not callable

def test_callable_2(fun: Callable[[int], int]):
    pass

test_callable_2(function_2) # expected error: function types do not match
test_callable_2(function_3)



############################################################
# TEST Union
############################################################
def function_4(value: Union[str, int, Callable]):
    pass

function_4(5)
function_4('5')
function_4(function_3)
function_4({'dog': True}) # expected error: dict is not one of the union types
