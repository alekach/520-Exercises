import bisect
    seen = []
    for num in numbers:
        pos = bisect.bisect_left(seen, num)
        if pos > 0 and abs(num - seen[pos - 1]) < threshold:
            return True
        if pos < len(seen) and abs(seen[pos] - num) < threshold:
            return True
        bisect.insort(seen, num)
    return False