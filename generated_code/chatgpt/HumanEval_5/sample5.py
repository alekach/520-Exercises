from functools import reduce
    if not numbers:
        return []    
    def reducer(acc: List[int], curr: int) -> List[int]:
        if not acc:
            return [curr]
        return acc + [delimeter, curr]    
    return reduce(reducer, numbers, [])