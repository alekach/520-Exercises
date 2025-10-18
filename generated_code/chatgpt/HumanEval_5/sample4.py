    if not numbers:
        return []    
    return [elem for i in range(len(numbers)) 
            for elem in ( (numbers[i], delimeter) if i != len(numbers) - 1 else (numbers[i],) )]