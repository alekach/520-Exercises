    import itertools
    return list(itertools.accumulate(numbers, max)) if numbers else []