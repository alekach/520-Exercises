    def helper(index: int, current_max: int) -> List[int]:
        if index == len(numbers):
            return []
        new_max = max(numbers[index], current_max)
        return [new_max] + helper(index + 1, new_max)    
    return helper(0, float('-inf'))