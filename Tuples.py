"""
So if you want your code to run you have to use python 2 version
because the hash function  for a specific immutable gives the same value across all machines

hash() : returns an integer hash value for an object , This integer is used internally by python for fast lookups in dictionaries and sets
1 --> only immutable objects are hashable like int , float, str, tuple  , so lists and dicts and sets are not hashable

Version	Behavior of hash() :

Python 2	Deterministic across runs (same integer every time)
Python 3	Randomized for some types (like strings and tuples) — hash values change across runs for security
"""

# Python 2:
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))

# Python 3:
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

