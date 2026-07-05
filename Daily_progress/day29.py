# Python  frozenset

'''A Frozenset is simply an immutable Set.




List      → Mutable ✅
Tuple     → Immutable 🔒

Set       → Mutable ✅
Frozenset → Immutable 🔒

'''




kpop = frozenset({"list1", "list2", "list3"})

print(kpop)






'''
A frozenset is an immutable version of a set. It does not allow adding, removing, or updating elements. However, it supports non-mutating methods like union(), intersection(), and difference(), which return a new frozenset instead of modifying the original.
'''