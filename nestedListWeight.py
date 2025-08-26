"""
Traverse the nested structure; track the current depth
For each integer x at depth d, add x * d to the total
Works with either DFS (recursive/stack) or BFS (level order)
"""
"""
Time Complexity: O(N) where N is total NestedInteger elements (integers + lists)
Space Complexity: O(H) for recursion/queue (worst-case depth or width)
"""

from typing import List, Union

class NestedInteger:
    def __init__(self, value: Union[int, List['NestedInteger']]):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = value

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> Union[int, None]:
        return self._integer

    def getList(self) -> Union[List['NestedInteger'], None]:
        return self._list


class nestedListWeight:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(items, depth):
            total = 0
            for ni in items:
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    total += dfs(ni.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)


def build_nested(obj: Union[int, list]) -> NestedInteger:
    if isinstance(obj, int):
        return NestedInteger(obj)
    return NestedInteger([build_nested(x) for x in obj])


if __name__ == "__main__":
    s = nestedListWeight()

    cases = [
        ([[1,1], 2, [1,1]], 10),   
        ([1,[4,[6]]], 27),        
        ([1,2,3], 6),            
        ([[[5]]], 15),           
    ]

    for nested, expected in cases:
        nl = [build_nested(x) for x in nested]
        ans = s.depthSum(nl)
        print(ans)
